"""
    Fichier : gestion_user_userrole_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les user et les userrole.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_PCPART.database.database_tools import DBconnection
from APP_PCPART.erreurs.exceptions import *

"""
    Nom : user_userrole_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /user_userrole_afficher
    
    But : Afficher les users avec les roles associés pour chaque user.
    
    Paramètres : id_userrole_sel = 0 >> tous les users.
                 id_userrole_sel = "n" affiche le user dont l'id est "n"
                 
"""


@app.route("/user_userrole_afficher/<int:id_user_sel>", methods=['GET', 'POST'])
def user_userrole_afficher(id_user_sel):
    print(" user_userrole_afficher id_user_sel ", id_user_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_userrole_user_afficher_data = """SELECT id_user, user_firstname, user_lastname, user_birthdate, user_photo,
                                                            GROUP_CONCAT(" ", userrole) as userrole FROM t_user
                                                            LEFT JOIN t_user_has_userrole ON t_user.id_user = t_user_has_userrole.fk_user
                                                            LEFT JOIN t_userrole ON t_userrole.id_userrole = t_user_has_userrole.fk_userrole
                                                            GROUP BY id_user"""
                if id_user_sel == 0:
                    # le paramètre 0 permet d'afficher tous les users
                    # Sinon le paramètre représente la valeur de l'id du user
                    mc_afficher.execute(strsql_userrole_user_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du user sélectionné avec un nom de variable
                    valeur_id_user_selected_dictionnaire = {"value_id_user_selected": id_user_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_userrole_user_afficher_data += """ HAVING id_user= %(value_id_user_selected)s"""

                    mc_afficher.execute(strsql_userrole_user_afficher_data, valeur_id_user_selected_dictionnaire)

                # Récupère les données de la requête.
                data_userrole_user_afficher = mc_afficher.fetchall()
                print("data_userrole ", data_userrole_user_afficher, " Type : ", type(data_userrole_user_afficher))

                # Différencier les messages.
                if not data_userrole_user_afficher and id_user_sel == 0:
                    flash("""Table "t_user" is empty !""", "warning")
                elif not data_userrole_user_afficher and id_user_sel > 0:
                    # Si l'utilisateur change l'id_user dans l'URL et qu'il ne correspond à aucun user
                    flash(f"L'utilisateur {id_user_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Data users and roles shown !!", "success")

        except Exception as Exception_user_userrole_afficher:
            raise ExceptionUserUserroleAfficher(f"fichier : {Path(__file__).name}  ;  {user_userrole_afficher.__name__} ;"
                                               f"{Exception_user_userrole_afficher}")

    print("user_userrole_afficher  ", data_userrole_user_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("user_userrole/user_userrole_afficher.html", data=data_userrole_user_afficher)


"""
    nom: edit_userrole_user_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les userrole du user sélectionné par le bouton "MODIFIER" de "user_userrole_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les userrole contenus dans la "t_userrole".
    2) Les userrole attribués au user selectionné.
    3) Les userrole non-attribués au user sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_userrole_user_selected", methods=['GET', 'POST'])
def edit_userrole_user_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_userrole_afficher = """SELECT id_userrole, userrole FROM t_userrole ORDER BY id_userrole ASC"""
                mc_afficher.execute(strsql_userrole_afficher)
            data_userrole_all = mc_afficher.fetchall()
            print("dans edit_userrole_user_selected ---> data_userrole_all", data_userrole_all)

            # Récupère la valeur de "id_user" du formulaire html "user_userrole_afficher.html"
            # l'utilisateur clique sur le bouton "Edit" et on récupère la valeur de "id_user"
            # grâce à la variable "id_user_userrole_edit_html" dans le fichier "user_userrole_afficher.html"
            # href="{{ url_for('edit_userrole_user_selected', id_user_userrole_edit_html=row.id_user) }}"
            id_user_userrole_edit = request.values['id_user_userrole_edit_html']

            # Mémorise l'id du user dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_user_userrole_edit'] = id_user_userrole_edit

            # Constitution d'un dictionnaire pour associer l'id du user sélectionné avec un nom de variable
            valeur_id_user_selected_dictionnaire = {"value_id_user_selected": id_user_userrole_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction userrole_user_afficher_data
            # 1) Sélection du user choisi
            # 2) Sélection des userrole "déjà" attribués pour le user.
            # 3) Sélection des userrole "pas encore" attribués pour le user choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "userrole_user_afficher_data"
            data_userrole_user_selected, data_userrole_user_non_attribues, data_userrole_user_attribues = \
                userrole_user_afficher_data(valeur_id_user_selected_dictionnaire)

            print(data_userrole_user_selected)
            lst_data_user_selected = [item['id_user'] for item in data_userrole_user_selected]
            print("lst_data_user_selected  ", lst_data_user_selected,
                  type(lst_data_user_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les userrole qui ne sont pas encore sélectionnés.
            lst_data_userrole_user_non_attribues = [item['id_userrole'] for item in data_userrole_user_non_attribues]
            session['session_lst_data_userrole_user_non_attribues'] = lst_data_userrole_user_non_attribues
            print("lst_data_userrole_user_non_attribues  ", lst_data_userrole_user_non_attribues,
                  type(lst_data_userrole_user_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les userrole qui sont déjà sélectionnés.
            lst_data_userrole_user_old_attribues = [item['id_userrole'] for item in data_userrole_user_attribues]
            session['session_lst_data_userrole_user_old_attribues'] = lst_data_userrole_user_old_attribues
            print("lst_data_userrole_user_old_attribues  ", lst_data_userrole_user_old_attribues,
                  type(lst_data_userrole_user_old_attribues))

            print(" data data_userrole_user_selected", data_userrole_user_selected, "type ", type(data_userrole_user_selected))
            print(" data data_userrole_user_non_attribues ", data_userrole_user_non_attribues, "type ",
                  type(data_userrole_user_non_attribues))
            print(" data_userrole_user_attribues ", data_userrole_user_attribues, "type ",
                  type(data_userrole_user_attribues))

            # Extrait les valeurs contenues dans la table "t_userrole", colonne "userrole"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_userrole
            lst_data_userrole_user_non_attribues = [item['userrole'] for item in data_userrole_user_non_attribues]
            print("lst_all_userrole gf_edit_userrole_user_selected ", lst_data_userrole_user_non_attribues,
                  type(lst_data_userrole_user_non_attribues))

        except Exception as Exception_edit_userrole_user_selected:
            raise ExceptionEditUserroleUserSelected(f"fichier : {Path(__file__).name}  ;  "
                                                 f"{edit_userrole_user_selected.__name__} ; "
                                                 f"{Exception_edit_userrole_user_selected}")

    return render_template("user_userrole/user_userrole_modifier_tags_dropbox.html",
                           data_userrole=data_userrole_all,
                           data_user_selected=data_userrole_user_selected,
                           data_userrole_attribues=data_userrole_user_attribues,
                           data_userrole_non_attribues=data_userrole_user_non_attribues)


"""
    nom: update_userrole_user_selected

    Récupère la liste de tous les userrole du user sélectionné par le bouton "MODIFIER" de "user_userrole_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les userrole contenus dans la "t_userrole".
    2) Les userrole attribués au user selectionné.
    3) Les userrole non-attribués au user sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_userrole_user_selected", methods=['GET', 'POST'])
def update_userrole_user_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du user sélectionné
            id_user_selected = session['session_id_user_userrole_edit']
            print("session['session_id_user_userrole_edit'] ", session['session_id_user_userrole_edit'])

            # Récupère la liste des userrole qui ne sont pas associés au user sélectionné.
            old_lst_data_userrole_user_non_attribues = session['session_lst_data_userrole_user_non_attribues']
            print("old_lst_data_userrole_user_non_attribues ", old_lst_data_userrole_user_non_attribues)

            # Récupère la liste des userrole qui sont associés au user sélectionné.
            old_lst_data_userrole_user_attribues = session['session_lst_data_userrole_user_old_attribues']
            print("old_lst_data_userrole_user_old_attribues ", old_lst_data_userrole_user_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme userrole dans le composant "tags-selector-tagselect"
            # dans le fichier "userrole_user_modifier_tags_dropbox.html"
            new_lst_str_userrole_user = request.form.getlist('name_select_tags')
            print("new_lst_str_userrole_user ", new_lst_str_userrole_user)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_userrole_user_old = list(map(int, new_lst_str_userrole_user))
            print("new_lst_userrole_user ", new_lst_int_userrole_user_old, "type new_lst_userrole_user ",
                  type(new_lst_int_userrole_user_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_userrole" qui doivent être effacés de la table intermédiaire "t_userrole_user".
            lst_diff_userrole_delete_b = list(set(old_lst_data_userrole_user_attribues) -
                                              set(new_lst_int_userrole_user_old))
            print("lst_diff_userrole_delete_b ", lst_diff_userrole_delete_b)

            # Une liste de "id_userrole" qui doivent être ajoutés à la "t_userrole_user"
            lst_diff_userrole_insert_a = list(
                set(new_lst_int_userrole_user_old) - set(old_lst_data_userrole_user_attribues))
            print("lst_diff_userrole_insert_a ", lst_diff_userrole_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_user"/"id_user" et "fk_userrole"/"id_userrole" dans la "t_user_has_userrole"
            strsql_insert_userrole_user = """INSERT INTO t_user_has_userrole (id_user_has_userrole, fk_userrole, fk_user)
                                                    VALUES (NULL, %(value_fk_userrole)s, %(value_fk_user)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_user" et "id_userrole" dans la "t_userrole_user"
            strsql_delete_userrole_user = """DELETE FROM t_user_has_userrole WHERE fk_userrole = %(value_fk_userrole)s AND fk_user = %(value_fk_user)s"""

            with DBconnection() as mconn_bd:
                # Pour le user sélectionné, parcourir la liste des userrole à INSÉRER dans la "t_userrole_user".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_userrole_ins in lst_diff_userrole_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du user sélectionné avec un nom de variable
                    # et "id_userrole_ins" (l'id du role dans la liste) associé à une variable.
                    valeurs_user_sel_userrole_sel_dictionnaire = {"value_fk_user": id_user_selected,
                                                                  "value_fk_userrole": id_userrole_ins}

                    mconn_bd.execute(strsql_insert_userrole_user, valeurs_user_sel_userrole_sel_dictionnaire)

                # Pour le user sélectionné, parcourir la liste des userrole à EFFACER dans la "t_userrole_user".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_userrole_del in lst_diff_userrole_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du user sélectionné avec un nom de variable
                    # et "id_userrole_del" (l'id du userrole dans la liste) associé à une variable.
                    valeurs_user_sel_userrole_sel_dictionnaire = {"value_fk_user": id_user_selected,
                                                                  "value_fk_userrole": id_userrole_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_userrole_user, valeurs_user_sel_userrole_sel_dictionnaire)

        except Exception as Exception_update_userrole_user_selected:
            raise ExceptionUpdateUserroleUserSelected(f"fichier : {Path(__file__).name}  ;  "
                                                   f"{update_userrole_user_selected.__name__} ; "
                                                   f"{Exception_update_userrole_user_selected}")

    # Après cette mise à jour de la table intermédiaire "t_userrole_user",
    # on affiche les users et le(urs) role(s) associé(s).
    return redirect(url_for('user_userrole_afficher', id_user_sel=id_user_selected))


"""
    nom: userrole_user_afficher_data

    Récupère la liste de tous les userrole du user sélectionné par le bouton "MODIFIER" de "user_userrole_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des userrole, ainsi l'utilisateur voit les userrole à disposition

    On signale les erreurs importantes
"""


def userrole_user_afficher_data(valeur_id_user_selected_dict):
    print("valeur_id_user_selected_dict...", valeur_id_user_selected_dict)
    try:

        strsql_user_selected = """SELECT id_user, user_firstname, user_lastname, user_birthdate, user_photo, GROUP_CONCAT(userrole) as Userrole FROM t_user_has_userrole
                                        LEFT JOIN t_user ON t_user.id_user = t_user_has_userrole.fk_user
                                        LEFT JOIN t_userrole ON t_userrole.id_userrole = t_user_has_userrole.fk_userrole
                                        WHERE id_user = %(value_id_user_selected)s"""

        strsql_userrole_user_non_attribues = """SELECT id_userrole, userrole FROM t_userrole WHERE id_userrole not in(SELECT id_userrole as iduserroleUser FROM t_user_has_userrole
                                                    INNER JOIN t_user ON t_user.id_user = t_user_has_userrole.fk_user
                                                    INNER JOIN t_userrole ON t_userrole.id_userrole = t_user_has_userrole.fk_userrole
                                                    WHERE id_user = %(value_id_user_selected)s)"""

        strsql_userrole_user_attribues = """SELECT id_user, id_userrole, userrole FROM t_user_has_userrole
                                            LEFT JOIN t_user ON t_user.id_user = t_user_has_userrole.fk_user
                                            LEFT JOIN t_userrole ON t_userrole.id_userrole = t_user_has_userrole.fk_userrole
                                            WHERE id_user= %(value_id_user_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_userrole_user_non_attribues, valeur_id_user_selected_dict)
            # Récupère les données de la requête.
            data_userrole_user_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("userrole_user_afficher_data ----> data_userrole_user_non_attribues ", data_userrole_user_non_attribues,
                  " Type : ",
                  type(data_userrole_user_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_user_selected, valeur_id_user_selected_dict)
            # Récupère les données de la requête.
            data_user_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_user_selected  ", data_user_selected, " Type : ", type(data_user_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_userrole_user_attribues, valeur_id_user_selected_dict)
            # Récupère les données de la requête.
            data_userrole_user_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_userrole_user_attribues ", data_userrole_user_attribues, " Type : ",
                  type(data_userrole_user_attribues))

            # Retourne les données des "SELECT"
            return data_user_selected, data_userrole_user_non_attribues, data_userrole_user_attribues

    except Exception as Exception_userrole_user_afficher_data:
        raise ExceptionUserroleUserAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                                f"{userrole_user_afficher_data.__name__} ; "
                                                f"{Exception_userrole_user_afficher_data}")
