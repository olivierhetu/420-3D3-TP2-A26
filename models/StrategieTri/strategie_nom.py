from StrategieTrie import StrategieTrie


class strategie_nom(StrategieTrie):
    
    def afficher_produits(self, produits) -> list[dict]:
        produits = sorted(produits, key=lambda p: p.nom.lower())
        return produits