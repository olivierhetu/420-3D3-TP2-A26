from StrategieTrie import StrategieTrie


class strategie_populaire(StrategieTrie):
    
    def afficher_produits(self, produits) -> list[dict]:
        produits = sorted(produits, key=lambda p: p.nb_ventes, reverse=True)
        return produits