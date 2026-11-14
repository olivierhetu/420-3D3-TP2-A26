from abc import ABC, abstractmethod

class StrategieAffichage(ABC):

     @abstractmethod
     def affichage(produits : list)   -> list[dict]:
          pass









