from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration de la base de données MySQL
DATABASE_URL = "mysql+mysqlconnector://root:password@mysql:3306/clientdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Modèle Client pour la base de données
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    orders = Column(Integer)

# Créer les tables dans la base de données
Base.metadata.create_all(bind=engine)

# Schéma Pydantic pour la validation des données
class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    orders: int

app = FastAPI()

# Endpoint pour ajouter un client
@app.post("/clients/")
async def create_client(client: ClientCreate):
    db = SessionLocal()
    db_client = Client(
        first_name=client.first_name,
        last_name=client.last_name,
        email=client.email,
        orders=client.orders
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    db.close()
    return {"id": db_client.id}

# Endpoint pour accéder à un client
@app.get("/clients/{client_id}")
async def get_client(client_id: int):
    db = SessionLocal()
    client = db.query(Client).filter(Client.id == client_id).first()
    db.close()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Endpoint pour modifier un client
@app.put("/clients/{client_id}")
async def update_client(client_id: int, client: ClientCreate):
    db = SessionLocal()
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db_client.first_name = client.first_name
    db_client.last_name = client.last_name
    db_client.email = client.email
    db_client.orders = client.orders
    db.commit()
    db.refresh(db_client)
    db.close()
    return {"message": "Client updated"}

# Endpoint pour supprimer un client
@app.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    db = SessionLocal()
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    db.close()
    return {"message": "Client deleted"}
