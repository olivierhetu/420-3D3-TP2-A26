import json
from models import ProduitNumerique, Bundle
from StrategieTri import StrategieTrie


class Catalogue:

    def __init__(self, chemin_json: str):
        self._produits: dict[int, ProduitNumerique | Bundle] = {}
        self._charger(chemin_json)

    def _charger(self, chemin: str) -> None:
        with open(chemin, encoding="utf-8") as f:
            donnees = json.load(f)

        for d in donnees:
            if d["type"] == "produit":
                produit = ProduitNumerique(
                    id=d["id"],
                    nom=d["nom"],
                    description=d["description"],
                    prix=d["prix"],
                    nb_ventes=d["nb_ventes"],
                    image_url=d["image_url"]
                )
            else:
                produit = Bundle(
                    id=d["id"],
                    nom=d["nom"],
                    description=d["description"],
                    prix=d["prix"],
                    nb_ventes=d["nb_ventes"],
                    image_url=d["image_url"],
                    rabais=d.get("rabais", 0.0)
                )
            self._produits[produit.id] = produit

        for d in donnees:
            if d["type"] == "bundle":
                bundle = self._produits[d["id"]]
                for enfant_id in d.get("enfants", []):
                    bundle.ajouter(self._produits[enfant_id])

    def tous(self) -> list:
        return list(self._produits.values())

    def obtenir(self, id: int):
        return self._produits.get(id)

    def afficher_produits(self, tri: StrategieTrie , affichage: str) -> list[dict]:
        produits = self.tous()
        tri.afficher_produits(produits)

        # Affichage
        resultat = []
        for p in produits:
            if affichage == "compact":
                resultat.append({
                    "id": p.id,
                    "nom": p.nom,
                    "prix_total": p.prix_total(),
                    "image_url": p.image_url,
                    "est_bundle": p.est_bundle(),
                })
            elif affichage == "detaille":
                donnees = {
                    "id": p.id,
                    "nom": p.nom,
                    "prix_total": p.prix_total(),
                    "image_url": p.image_url,
                    "description": p.description,
                    "nb_ventes": p.nb_ventes,
                    "est_bundle": p.est_bundle(),
                }
                if p.est_bundle():
                    donnees["nb_items"] = p.nb_items()
                resultat.append(donnees)

        return resultat
