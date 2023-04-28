Utilisez les bases de Python-pour l'analyse de marché

Etape et Explication de extraction des données de site "Book to Scrape"

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

Etape 2 - Installation de l'IDE Pycharm :
- Accédez au site Web de PyCharm : https://www.jetbrains.com/pycharm/download/
- Cliquez sur le bouton "Télécharger" pour l'édition communautaire.
- Sélectionnez la version appropriée pour votre système d'exploitation (Windows dans ce cas).
- Une fois le téléchargement terminé, localisez le fichier dans votre dossier Téléchargements et double-cliquez dessus pour exécuter le programme d'installation.
- Suivez les invites du programme d'installation, en choisissant les options par défaut, sauf si vous avez une préférence spécifique.
- Lorsque vous y êtes invité, choisissez d'installer le "Script de lancement" et de créer des icônes sur le bureau.
- Choisissez les options souhaitées, comme l'emplacement et le type d'installation.
- Cliquez sur "Installer" pour commencer le processus d'installation.
- Attendez la fin du processus d'installation.

Une fois l'installation terminée, vous pouvez lancer PyCharm depuis le menu Démarrer ou en double-cliquant sur l'icône du bureau. Vous pouvez ensuite allez sur le dossier pdf que je vous envoie avec l'url qui vous dirigera vers mon repository de mon gitHub pour récupéré les dossiers qui contient le code d'extraction de donnée

Etape 3 - Lancement du dossier d'extraction des données
- Dirigez-vous vers le lien github que je vous ai envoyé (https://github.com/Cameron-HUCK/P2_Utilisez_les_bases-de-Python-pour-l-analyse-de-march_Huck_Cameron)
- Ensuite télécharger le dossier, si vous ne l'avez pas deja.
- Ouvrir le dossier sur Pycharm. Et vous aurez tous le dossier sur le coté gauche
- Ouvrez le terminal (qui se situe en bas) et accédez au répertoire racine de votre projet existant. qui se nomme "Utilisez_les_bases-de-Python-pour-l-analyse-de-march_Huck_Cameron"
- Créez un nouvel environnement virtuel en exécutant la commande python -m venv env(remplacez "env" par le nom que vous souhaitez donner à votre environnement virtuel).
- Activez l'environnement virtuel en exécutant la commande env\Scripts\activate.bat(Windows) ou source env/bin/activate(Linux/Mac).
- Une fois l'environnement virtuel activé, installez toutes les dépendances dont votre projet a besoin en exécutant la commande pip install -r requirements.txt
- Vous pouvez maintenant exécuter votre code d'application en exécutant la commande appropriée pour votre projet spécifique. Donc double-cliquez sur "data_exctraction_from_books.py" et cliquer sur l'icone play (Run) Pour exécuter le code.
- Si tout se passe bien, vous aurez 3 fichiers CSV nommés par rapport au type de donnée extraite et vous pourrez les afficher comme un tableau sur excel.
- Ouvrez excel sur une page vierge et allez sur "Donnée", ensuite "Obtenir des données", "A partir d'un fichier CSV".
- Et voilà votre tableau avec les données actuelles du site Book to scape.