from fastapi import FastAPI, HTTPException
from model_magasin import ModelMagasin
from db import database

app = FastAPI()


@app.get("/magasins")
def fetch_magasins():
    db = database()
    magasins = db.warehouse.find()
    res = []
    for magasin in magasins:
        data = {
            "type_musique": magasin["type_musique"],
            "vinyle_musiques_disponibles": magasin["vinyle_musiques_disponibles"],
            "dvd_musiques_disponibles": magasin["dvd_musiques_disponibles"],
        }
        res.append(data)
    return res

#post magasin
@app.post("/magasins")
def create_magasin(magasin: ModelMagasin):
    db = database()
    db.warehouse.insert_one(magasin.dict())
    return magasin.dict()


