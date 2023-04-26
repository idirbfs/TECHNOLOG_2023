from fastapi import FastAPI, HTTPException
from model_egg import ModelEgg
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