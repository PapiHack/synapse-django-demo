# Django SynApp

Application en django construite lors d'une démo du club synapse.

## Installation

- Créez un environnement virtuel avec la commande : `python3 -m venv <nom_de_votre_env>`

- Puis placez vous y : `. <nom_de_votre_env>/bin/activate` ou `source <nom_de_votre_env>/bin/activate`

- Placez-vous au niveau du projet et installez les dépendances via : `pip install -r requirements.txt`

- Puis placez-vous au niveau du repertoire `synapp` et appliquez les migrations : `./manage.py makemigrations` puis faites un `./manage.py migrate`

- Démarrez le serveur de l'application avec : `./manage.py runserver`

- Rdv à l'adresse `http://localhost:8000/blog/home`

## Screenshot

![screenshot](./screenshots/app.png)
