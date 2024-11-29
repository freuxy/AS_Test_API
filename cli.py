import argparse
import requests

# Définir l'URL de base de votre API FastAPI
BASE_URL = "http://127.0.0.1:8000"


def get_parents(id: str):
    """Fonction pour interroger le point de terminaison FastAPI pour les relations d'entité"""
    response = requests.get(f"{BASE_URL}/?id={id}")

    if response.status_code == 200:
        print("Succès!")
        print(response.json())
    else:
        print(f"Erreur : {response.status_code}")
        print(response.json())


def main():
    """Analyser les arguments de la ligne de commande et interroger l'API"""
    # Configurer l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Interroger le service FastAPI pour les relations d'entité.")
    parser.add_argument('id', type=str, help="L'ID de l'entité à interroger (ex : http://entity/CST/OCCLUS%20CAROTID)")

    # Analyser les arguments
    args = parser.parse_args()

    # Appeler la fonction pour obtenir les relations d'entité
    get_parents(args.id)


if __name__ == "__main__":
    main()
