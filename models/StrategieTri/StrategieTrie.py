from abc import ABC, abstractmethod

class StrategieTrie(ABC):

    @abstractmethod
    def afficher_produits(self, produits) -> list[dict]:
        pass

