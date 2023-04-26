from pydantic import BaseModel, validator

class ModelMusique(BaseModel):
    titre: str
    artiste = str
    immatriculation = str #JH/250/POP/1234

# dispose de methodes pour acceder à ces informations et ajouter/retirer des titre aux listes
    
    
        
    @validator("codeRayon")
    def control_annee(cls, value):
        annee = value[10:]
        if not annee.isnumeric():
            raise ValueError("Les 4 derniers caractères doivent etre des chiffres.")
        return value
    
    # verifier que l'annee n'est pas sup a 2022

    