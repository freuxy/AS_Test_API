# Utiliser une image de base officielle pour Python
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port que FastAPI va utiliser
EXPOSE 8000

# Démarrer l'application avec Uvicorn quand le conteneur est lancé
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
