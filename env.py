import os
import subprocess

def main():
    # Lire la valeur de la variable d'environnement
    env_type = os.environ.get("TYPE_ENV", "MEDI")  # "MEDI" est la valeur par défaut

    # Sélectionner le script à exécuter en fonction de la valeur
    if env_type == "MEDI":
        script_to_run = "scripts/script_medi.py"
    elif env_type == "AUXI":
        script_to_run = "scripts/script_auxi.py"
    else:
        raise ValueError("Type d'environnement non supporté")

    # Exécuter le script sélectionné
    subprocess.run(["python", script_to_run])

if __name__ == "__main__":
    main()