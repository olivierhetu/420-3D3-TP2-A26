from StrategieTrie import StrategieTrie


class strategie_prix(StrategieTrie):
    
    def afficher_produits(self, produits) -> list[dict]:
        produits = sorted(produits, key=lambda p: p.prix_total())
        return produits