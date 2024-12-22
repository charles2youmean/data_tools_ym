import importlib
import re

def check_imports(file_path):
    """
    Analyse les imports d'un fichier Python et vérifie leur disponibilité.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file :
            code = file.read()
        
        # Rechercher les importations dans le code
        imports = re.findall(r'^\s*(?:import|from)\s+([\w\.]+)', code, re.MULTILINE)
        imports = list(set(imports))  # Supprime les doublons

        print(f"Bibliothèques détectées : {imports}\n")

        # Vérifier si chaque bibliothèque est installée
        missing_modules = []
        for module in imports:
            try:
                importlib.import_module(module.split(".")[0])
                print(f"YY {module} est installé")
            except ImportError:
                print(f"NN {module} n'est pas installé")
                missing_modules.append(module)

        if missing_modules:
            print("\nBibliothèques manquantes :")
            for module in missing_modules:
                print(f"- {module}")
        else:
            print("\nToutes les bibliothèques nécessaires sont installées !")
    
    except FileNotFoundError:
        print(f"Erreur : Fichier '{file_path}' introuvable.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# Remplacez 'app.py' par le chemin vers votre fichier Python
check_imports("data_tools_ym_app.py")
