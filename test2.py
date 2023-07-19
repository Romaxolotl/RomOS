import os
import sys
import requests

def get_current_version():
    return "01/01/2000"  # Remplacez ceci par la version actuelle de votre script

def get_latest_version(repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('tag_name')
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la récupération de la dernière version : {e}")
        return None

def download_and_replace_script(download_url):
    response = requests.get(download_url)
    response.raise_for_status()

    with open('test.py', 'wb') as f:
        f.write(response.content)

    # Ajoutez ici le code pour sauvegarder l'ancien script (facultatif)
    # Puis, remplacez l'ancien script par la mise à jour.
    os.replace('test.py', sys.argv[0])

if __name__ == "__main__":
    # Mettez à jour ces valeurs avec les informations de votre référentiel GitHub
    repo_owner = "Romaxolotl"
    repo_name = "RomOS"

    current_version = get_current_version()
    latest_version = get_latest_version(repo_owner, repo_name)

    if latest_version and latest_version != current_version:
        print(f'Une nouvelle version ({latest_version}) est disponible !')
        print(f'Vous utilisez actuellement la version {current_version}.')
        download_url = f'https://github.com/{repo_owner}/{repo_name}/releases/latest/download/mon_script_maj.py'
        download_and_replace_script(download_url)
        print("Le script a été mis à jour avec succès.")
    else:
        print(f'Vous utilisez déjà la dernière version ({current_version}).')
V = "2"
