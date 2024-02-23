import os
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import shutil

def extract_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find(class_='Titre-NoteFaq').get_text(strip=True) if soup.find(class_='Titre-NoteFaq') else 'N/A'
    creation_date = soup.select_one('.cartouche_commun:contains("Créé le")').get_text(strip=True) if soup.select_one('.cartouche_commun:contains("Créé le")') else 'N/A'
    update_date = soup.find(class_='entete_date').get_text(strip=True) if soup.find(class_='entete_date') else 'N/A'
    description = soup.find(class_='Descriptif').get_text(strip=True) if soup.find(class_='Descriptif') else 'N/A'
    manip_simple = soup.find(class_='manip_simple').get_text(strip=True) if soup.find(class_='manip_simple') else 'N/A'
    manip_avance = soup.find(class_='manip_avance').get_text(strip=True) if soup.find(class_='manip_avance') else 'N/A'
    ticket_jira = soup.select_one('.corrige:contains("Ticket Jira")').get_text(strip=True) if soup.select_one('.corrige:contains("Ticket Jira")') else 'N/A'

    return title, creation_date, update_date, description, manip_simple, manip_avance, ticket_jira

def move_processed_files(input_directory, processed_directory, excel_file_name):
    date_today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination = os.path.join(processed_directory, date_today)

    if not os.path.exists(destination):
        os.makedirs(destination)

    for folder in os.listdir(input_directory):
        shutil.move(os.path.join(input_directory, folder), destination)

    # Copier le fichier Excel dans le dossier de traitement
    shutil.copy(excel_file_name, destination)

def main():
    input_directory = 'input'
    output_directory = 'output'
    processed_directory = 'processedFAQ'
    excel_file_name = 'output.xlsx'
    data = []

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file in ['_ASSIST.HTM', '_PRINCIPAL.HTM']:
                # Extraire le numéro du dossier
                folder_number = root.split('N')[-1]  # Modification ici
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='iso-8859-1') as f:
                    html_content = f.read()
                    info = extract_info(html_content)
                    data.append([folder_number, file] + list(info))  # Utiliser folder_number ici

    df = pd.DataFrame(data, columns=['Dossier', 'Fichier', 'Titre', 'Date de création', 'Date de mise à jour', 'Description', 'Manipulations simples', 'Manipulations avancées', 'Ticket JIRA'])
    os.makedirs(output_directory, exist_ok=True)
    df.to_excel(f'{output_directory}/{excel_file_name}', index=False)

    move_processed_files(input_directory, processed_directory, f'{output_directory}/{excel_file_name}')

if __name__ == "__main__":
    main()