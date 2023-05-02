Utilisez les bases de Python-pour l'analyse de marché

Etape et Explication de l'extraction des données de site "Book to Scrape"

Etape 1 - Installation de Python : 
- Allez sur le site Python : https://www.python.org/
- Cliquez sur le lien "Téléchargements" en haut de la page.
- Faites défiler jusqu'à la section "Python Releases for Windows".
- Recherchez la dernière version de Python compatible avec le système d'exploitation de votre ordinateur. Par exemple, si vous avez une version 64 bits de Windows, vous souhaiterez télécharger la version 64 bits de Python.
- Cliquez sur le lien de la version appropriée de Python pour commencer le téléchargement.
- Une fois le téléchargement terminé, localisez le fichier dans votre dossier. Téléchargements et double-cliquez dessus pour exécuter le programme d'installation.
- Suivez les invites du programme d'installation, en vous assurant de sélectionner "Ajouter Python à PATH" afin de pouvoir utiliser Python à partir de la ligne de commande.
- Choisissez les options souhaitées, comme l'emplacement et le type d'installation.
- Cliquez sur "Installer" pour commencer le processus d'installation.
- Attendez que le processus d'installation soit terminé.
- Une fois l'installation terminée, vous pouvez ouvrir l'invite de commande ou le terminal et taper "python" pour démarrer l'interpréteur Python. Vous pouvez également utiliser un IDE tel que PyCharm pour écrire et exécuter du code Python.


Une fois l'installation terminée, vous pouvez ensuite aller sur le dossier pdf que je vous envoie avec l'url qui vous dirigera vers mon repository de mon gitHub pour récupéré les dossiers qui contient le code d'extraction de donnée

Etape 2 - Lancement du dossier d'extraction des données
- Dirigez-vous vers le lien github que je vous ai envoyé (https://github.com/Cameron-HUCK/P2_Utilisez_les_bases-de-Python-pour-l-analyse-de-march_Huck_Cameron)
- Ensuite télécharger le dossier, si vous ne l'avez pas deja.
- Ouvrez votre programme de terminal. Cela peut généralement être trouvé en recherchant "Terminal" sur votre ordinateur.
- Accédez au répertoire où se trouve le fichier .py. Vous pouvez le faire en utilisant la commande "cd", suivie du chemin du répertoire. Par exemple, si votre fichier se trouve dans le dossier "Documents", vous pouvez taper "cd Documents" dans le terminal.
- Une fois dans le répertoire, installez toutes les dépendances dont votre projet a besoin en exécutant la commande pip install -r requirements.txt. Le package "OS" devrait être djà installer, si ce n'est pas le cas, installer le en tapant cette commande dans le terminal "pip install os-sys"
- Une fois téléchargé vous pouvez ouvrir le fichier dans le terminal avec cette commande "python data_extraction_from_books.py" dans le terminal.
- Si tout se passe bien, cela va générer 3 fichiers CSV nommés par rapport au type de donnée extraite et vous pourrez les afficher comme un tableau sur excel.
- Ouvrez excel sur une page vierge et allez sur "Donnée", ensuite "Obtenir des données", "A partir d'un fichier CSV".
- Et voilà votre tableau avec les données actuelles du site Book to scape.