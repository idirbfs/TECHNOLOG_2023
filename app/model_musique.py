from pydantic import BaseModel, validator

class ModelMusique(BaseModel):
    titre: str
    artiste : str
    immatriculation : str #JH/250/POP/1234


# dispose de methodes pour acceder à ces informations et ajouter/retirer des titre aux listes
    
  # verifier titre
    @validator("titre")
    def control_titre(cls, value):
      
      if value.len() == 0:
          raise ValueError("le titre doit contenir qlq chose")
      return value
    
  # verifier artiste
    @validator("artiste")
    #l'artiste ne doit contenir que des lettres
    def control_artiste(cls, value):
      if value.len() == 0 or value.isalpha() == False:
          raise ValueError("l'artiste ne doit contenir que des lettres")
      return value
    
  # verifier les initials d'un artist
    @validator("immatriculation")
    def control_initiales_artiste(cls, value):
        initials_artist = value[0:2]
        if not initials_artist.isalpha():
            raise ValueError("champs initials d'artiste est incorrect")
        return value
    
    # verifier 1er slash
    @validator("immatriculation")
    def control_slash1(cls, value):
        slash1 = value[2]
        if not slash1 == "/":
            raise ValueError("Le 3 eme caractere du code de rayon doit etre un slash \"/\".")
        return value
    # verifier la duree d'un titre (numeric entre 1 et 5 minutes)

    @validator("immatriculation")
    def control_duree(cls, value):
       duree = value[3:6]
       if (duree.isnumeric() == False or duree < 1*60 or duree > 5*60):
          raise ValueError("champs duree incorrect")
       return value
    # verifier 2eme slash
    @validator("immatriculation")
    def control_slash2(cls, value):
        slash2 = value[6]
        if not slash2 == "/":
            raise ValueError("Le 7 eme caractere du code de rayon doit etre un slash \"/\".")
        return value
    
    # verifier le type de musique RAP POP RNB
    @validator("immatriculation")
    def control_type_musique(cls, value):
       type_musique = value[7:10]
       if type_musique not in range("POP", "RAP", "RNB") :
          raise ValueError("champs type musique incorrect")
       return value
    
    # verifier 3eme slash
    @validator("immatriculation")
    def control_slash3(cls, value):
        slash3 = value[10]
        if not slash3 == "/":
            raise ValueError("Le 3 eme caractere du code de rayon doit etre un slash \"/\".")
        return value
      
    # verifier identifiant qui ne contien pas de 6
    @validator("immatriculation")
    def control_identifiant(cls, value):
       id = value[11:]
       if id.find("6") != -1 :
          raise ValueError("champs identifiant incorrect")
       return value

    