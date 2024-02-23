
# FAQtoEXCEL

  

## Installer Python

Installer python via : https://www.python.org/downloads/

Ajouter la variable au PATH.

  

## Installer les dépendances

Ouvrir terminal et exécuter :

  

pip install beautifulsoup4

pip install pandas

pip install lxml

pip install openpyxl

  

## Fonctionnement

  

Récupérez vos dossiers FAQ au format N[number].

Mettez vos dossiers dans le dossier `input`

  

### Définir l'environnement

  

Ouvrez le fichier `env.py` et définissez le contexte :

  

#### Pour les FAQs MEDI :

    env_type = os.environ.get("TYPE_ENV", "MEDI")

  

#### Pour les FAQs AUXI :

    env_type = os.environ.get("TYPE_ENV", "AUXI")

  
  

### Lancer le script :

Ouvre un terminal et naviguez dans votre dossier FAQtoEXCEL :

Lancez le script :

    py .\env.py

Récupérez le contenu dans le dossier `output`, au format EXCEL.
Chaque execution de script génère un dossier à la date et l'heure de l'execution.

Le dossier comprend :

 - Toutes les FAQs qui ont été traitées 
 - La sortie Excel de cette
   execution


Deux exemples sont actuellement prêt à être migrés. Lancez simplement le script après installation pour voir le résultat : 

    py .\env.py
  

## Mise en garde

Aucun fichier Excel généré au préalable ne doit être ouvert / en cours de modification (sauf si vous l'avez déplacé)