from StrategieAffichage import StrategieAffichage

class detaille(StrategieAffichage):

    def affichage(resultat : list, produits : list[dict]):
        for p in produits:
            resultat.append({
                                "id": id,
                                "nom": p.nom,
                                "prix_total": p.prix_total(),
                                "image_url": p.image_url,
                                "est_bundle": p.est_bundle(),
                            })
            return resultat