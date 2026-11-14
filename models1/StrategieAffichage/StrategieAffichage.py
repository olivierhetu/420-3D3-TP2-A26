from abc import ABC, abstractmethod

class StrategieAffichage(ABC):

     @abstractmethod
     def afficher(produits : list)   -> list[dict]:
          pass









