# Marche à suivre pour l'installation et la mise en service du serveur avec la base de données et la page web !
1. Il faut télécharger le dossier du projet :
   * Appuyer sur le bouton vert "Code" sur la page github du projet.
   * Appuyer sur "Download ZIP" ou "Télécharger ZIP".
   * Une fenêtre de l'explorateur de fichier s'ouvre, choisissez ou vous souhaitez télécharger le projet, il est préférable de le mettre à un endroit où vous pouvez le retrouver facilement, par exemple à la racine du disque "C:".
   * Maintenant il faut faire clique droit sur le dossier que vous venez de télécharger, puis appuyer sur extraire ici pour l'unzip.
   * Vous pouvez changer le nom du dossier par celui qui vous convient, souvenez vous du nom il va être utile pour la suite.
   * Supprimez le dossier .zip !
   
3. Il faut installer un serveur MySql :
   * UWAMP : sur le site de "UWAMP", lire "Prerequisites IMPORTANT!!" (vous devez installer une ou plusieurs des distributions Visual C++).
   * UWAMP : installer la version "EXE" (Choisir : Télécharger Exe/Install) est préférable à la version "PORTABLE".
   * Quand la fenêtre d'installation s'ouvre, choisissez où vous souhaitez installer le serveur MySQL, par exemple à la racine du disque "C:".
   * UWAMP : accepter les 2 alertes de sécurité d'accès aux réseaux (apache et MySql).
   * MAC : MAMP ou https://www.codeur.com/tuto/creation-de-site-internet/version-mysql/
   * Contrôler que tout fonctionne bien. Ouvrir "UWAMP". Cliquer sur le bouton "PhpMyAdmin". Utilisateur : root ; Mot de passe : root
   * Si vous le souhaitez vous pouvez changer le mot de passe et le nom d'utilisateur pour la sécurité !

4. Il faut installer Python :
   * ATTENTION : Cocher la case pour que le "PATH" intègre le programme Python.
   * Une fois la "case à cocher" du PATH cochée, il faut choisir d'installer.
   * Un peu avant la fin du processus d'intallation, cliquer sur "disabled length limit" et cliquer sur "CLOSE".
   * Le test de Python se fait après avec le programme "PyCharm".

5. Il faut installer "PyCharm" (community edition) :
   * Lors de l'installation, il faut cocher toutes les options ASSOCIATIONS, ADD PATH, etc.
   * Ouvrir "PyCharm" pour la première fois pour le configurer. Cliquez sur le bouton "Open".
   * Naviguez jusqu'à la racine du disque "C:" avec l'explorateur de fichier qui s'est ouvert, puis sélectionnez le projet que vous avez téléchargé et auquel vous avez changé le nom au début de la marche à suivre.

# Une fois les installations effectuées on peut passer à la mise en service !
6. Démarrez le serveur MySql :
   * Ouvrir UWAMP avec le fichier "UwAmp.exe" qui se trouve dans le dossier UWAMP que vous avez téléchargé plus tôt, probablement à la racine du disque "C:".

7. Dans "PyCharm", importer la BD à partir du fichier DUMP :
    * Ouvrir le fichier "database/1_ImportationDumpSql.py".
    * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10).
    * En cas d'erreurs : ouvrir le fichier ".env" à la racine du projet, contrôler les indications de connexion pour la bd.
      * Par exemple le compte utilisateur si vous avez modifié son nom ou mot de passe.  
      
8. Démarrez le microframework FLASK
    * Dans le répertoire racine du projet sur PyCharm, cliquez avec le bouton droit sur le fichier "run_mon_app.py" et choisir "run 'run_mon_app'" avec le petit triangle vert à côté.

9. Vous pouvez maintenant ouvrir le site :
   * Appuyez sur le lien bleu "http://127.0.0.1:5577" qui apparait au bas de la fenêtre de PyCharm.

