from pydantic import BaseModel, validator
from model_musique import ModelMusique

class ModelMagasin(BaseModel):
    def __init__(self):
      self.__type_musique: str
      self.__vinyle_musiques_disponibles : "ModelMusique"= []
      self.__dvd_musiques_disponibles : "ModelMusique" = []

# dispose de methodes pour acceder à ces informations et ajouter/retirer des titre aux listes
    @classmethod
    def getTypeMusique(self):
        return self.__type_musique
    @classmethod
    def getVinyleMusiquesDisponibles(self):
        return self.__vinyle_musiques_disponibles
    @classmethod
    def getDvdMusiquesDisponibles(self):
        return self.__dvd_musiques_disponibles
    
    @classmethod
    def addDvdMusique(self, dvdMusique):
        self.__dvd_musiques_disponibles.append(dvdMusique)

    @classmethod
    def deleteDvdMusique(self, dvdMusique):
        self.__dvd_musiques_disponibles.remove(dvdMusique)
        
    @classmethod
    def addVinyleMusique(self, vinyleMusique):
        self.__vinyle_musiques_disponibles.append(vinyleMusique)

    @classmethod
    def removeVinyleMusique(self, vinyleMusique):
        self.__vinyle_musiques_disponibles.remove(vinyleMusique)
    
        
    @validator("self.__type_musique")
    def control_type_musique(cls, value):
        if value not in range("POP", "RAP", "RNB") :
          raise ValueError("champs type musique incorrect")
        return value
    
    