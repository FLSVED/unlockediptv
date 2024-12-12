

## Description

Secure IPTV Application est une application web sécurisée pour gérer des abonnements IPTV. Elle permet de se connecter à des serveurs IPTV, de gérer des abonnements, de lire des flux en direct et de la vidéo à la demande (VOD), tout en garantissant une expérience utilisateur optimisée et sécurisée.

## Fonctionnalités

- Connexion sécurisée aux serveurs IPTV via différents modes (Xtream, MAC Portal, Stalker Portal)
- Gestion des abonnements avec vérification de leur légitimité
- Mise en cache des contenus pour améliorer les performances
- Adaptation dynamique de la qualité des flux selon les conditions réseau
- Gestion des sessions utilisateurs avec JWT
- Possibilité de mettre en favori des chaînes et VOD
- Application responsive et compatible avec plusieurs appareils

## Prérequis

- Python 3.8+
- PostgreSQL pour la base de données

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/iptv-app.git
   cd iptv-app
   ```

2. **Créer un environnement virtuel :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données :**

   Créez une base de données PostgreSQL et mettez à jour la configuration de la connexion dans `app/config.py`.

5. **Lancer les migrations :**

   ```bash
   alembic upgrade head
   ```

6. **Démarrer l'application :**

   ```bash
   uvicorn app.main:app --reload
   ```

## Utilisation

- Accédez à l'application via un navigateur web à l'adresse `http://localhost:8000`.
- Les API sont documentées via Swagger et accessibles à `http://localhost:8000/docs`.

## Structure du projet

```
iptv-app/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── config.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── ...
│
├── requirements.txt
└── README.md
```

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre un pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs

- **FLSVED** - Développeur principal
- **Autres Contributeurs** - Voir la liste des contributeurs qui ont participé à ce projet.
