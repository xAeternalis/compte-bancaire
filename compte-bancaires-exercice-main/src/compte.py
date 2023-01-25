import uuid
from abc import ABC
#from exceptions import *


class Compte(ABC):
    """
        Abstract class Compte
    """
    def __init__(self, nomProprietaire, solde = 0, **kwargs):
        self.nomProprietaire = nomProprietaire
        self.solde = solde
        self.numero_compte = ""

    def retrait(self, montant=0):
        self.solde -= montant
        return self.solde

    def versement(self, montant=0):
        self.solde += montant
        return self.solde

    def solde(self): # pragma: no cover
        return self.solde

    def __repr__(self):
        return ""

class CompteCourant(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        self.autorisation_decouvert = 0
        self.pourcentage_agios = 0.1
        super().__init__(nomProprietaire, **kwargs)

    def retrait(self, montant = 0):
        try:
            if montant < 0:
                print("Le montant du retrait est négatif ou égal à 0, mettez une valeur valide")
            elif montant > self.solde:
                print("Le montant du retrait est supérieur à votre solde")
        except ValueError:
            print("Le montant entré n'est pas accepté pour un retrait")
        else:
            if self.solde < 0:
                print(f"Votre solde avant retrait : {self.solde}")
                print(f"Votre opération est de retirer {montant} à votre solde de {self.solde}")
                self.appliquer_agios(float(montant))
            else:
                print(f"Votre solde avant retrait : {self.solde}")
                print(f"Votre opération est de retirer {montant} à votre solde de {self.solde}")
                self.solde -= montant
                print(f"Votre solde après retrait : {self.solde}")
                return self.solde

    def versement(self, montant=0):
        try:
            if montant <= 0:
                print("Le montant de versement ne peux pas être négatif")
        except ValueError:
            print("Le montant de versement ne peux pas être négatif")
        else:
            print(f"Votre solde avant versement : {self.solde}")
            print(f"Votre opération est de verser {montant} à votre solde de {self.solde}")
            self.solde += montant
            print(f"Votre solde après versement : {self.solde}")
            return self.solde

    def solde(self):
        return self.solde

    def appliquer_agios(self, montant):
        self.solde = self.solde - montant * (1 + self.pourcentage_agios)
        return self.solde

class CompteEpargne(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        self.pourcentage_interets = 0.04
        super().__init__(nomProprietaire, **kwargs)


    def retrait(self, montant = 0):
        try:
            if montant < 0:
                print("Le montant du retrait est négatif ou égal à 0, mettez une valeur valide")
            elif montant > self.solde:
                print("Le montant du retrait est supérieur à votre solde")
        except ValueError:
            print("Le montant entré n'est pas accepté pour un retrait")
        else:
            print(f"Votre solde avant retrait : {self.solde}")
            print(f"Votre opération est de retirer {montant} à votre solde de {self.solde}")
            self.solde -= montant
            print(f"Votre solde après retrait : {self.solde}")
            return self.solde

    def versement(self, montant=0):
        try:
            if montant <= 0:
                print("Le montant est inférieur ou égal à 0, mettez une valeur valide")
        except ValueError:
            print("Le montant est inférieur ou égal à 0, mettez une valeur valide")
        else:
            print(f"Votre solde avant versement : {self.solde}")
            print(f"Votre opération est de verser {montant} à votre solde de {self.solde}")
            self.appliquer_interets(float(montant))
            print(f"Votre solde après versement : {self.solde}")
        return self.solde

    def appliquer_interets(self, montant):
        self.solde = self.solde + montant * (1 + self.pourcentage_interets)
        return self.solde