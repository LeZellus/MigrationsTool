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

Ouvre un terminal et naviguez dans votre dossier FAQtoEXCEL.

Lancez le script : 

    py .\FAQtoEXCEL.py
    
Récupérez le contenu dans le dossier `output`, au format EXCEL.

## Mise en garde
Aucun fichier Excel généré au préalable ne doit être ouvert / en cours de modification (sauf si vous l'avez déplacé)