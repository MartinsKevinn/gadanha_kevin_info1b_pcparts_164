"""
    Fichier : gestion_user_config_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les user et les config.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_CONFIG_164.database.database_tools import DBconnection
from APP_CONFIG_164.erreurs.exceptions import *

"""
    Nom : user_config_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /user_config_afficher
    
    But : Afficher les users avec les config associés pour chaque user.
    
    Paramètres : id_config_sel = 0 >> tous les users.
                 id_config_sel = "n" affiche le user dont l'id est "n"
                 
"""


@app.route("/user_config_afficher/<int:id_user_sel>", methods=['GET', 'POST'])
def user_config_afficher(id_user_sel):
    print(" user_config_afficher id_user_sel ", id_user_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_config_user_afficher_data = """SELECT id_user, user_firstname, user_lastname, user_birthdate,
                                                            GROUP_CONCAT("ID Config : ", id_config, ", ", "Config use case : ", config_use_case, ", ", "Config rating : ", config_rating, "/5") as UserConfig FROM t_user_created_config
                                                            RIGHT JOIN t_user ON t_user.id_user = t_user_created_config.fk_user
                                                            LEFT JOIN t_config ON t_config.id_config = t_user_created_config.fk_config
                                                            GROUP BY id_user"""
                if id_user_sel == 0:
                    # le paramètre 0 permet d'afficher tous les users
                    # Sinon le paramètre représente la valeur de l'id du user
                    mc_afficher.execute(strsql_config_user_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du user sélectionné avec un nom de variable
                    valeur_id_user_selected_dictionnaire = {"value_id_user_selected": id_user_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_config_user_afficher_data += """ HAVING id_user= %(value_id_user_selected)s"""

                    mc_afficher.execute(strsql_config_user_afficher_data, valeur_id_user_selected_dictionnaire)

                # Récupère les données de la requête.
                data_config_user_afficher = mc_afficher.fetchall()
                print("data_config ", data_config_user_afficher, " Type : ", type(data_config_user_afficher))

                # Différencier les messages.
                if not data_config_user_afficher and id_user_sel == 0:
                    flash("""La table "t_user" est vide. !""", "warning")
                elif not data_config_user_afficher and id_user_sel > 0:
                    # Si l'utilisateur change l'id_user dans l'URL et qu'il ne correspond à aucun user
                    flash(f"L'utilisateur {id_user_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données utilisateurs et config affichés !!", "success")

        except Exception as Exception_user_config_afficher:
            raise ExceptionUserConfigAfficher(f"fichier : {Path(__file__).name}  ;  {user_config_afficher.__name__} ;"
                                              f"{Exception_user_config_afficher}")

    print("user_config_afficher  ", data_config_user_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("user_config/user_config_afficher.html", data=data_config_user_afficher)


"""
    nom: edit_config_user_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les config du user sélectionné par le bouton "MODIFIER" de "user_config_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les config contenus dans la "t_config".
    2) Les config attribués au user selectionné.
    3) Les config non-attribués au user sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_config_user_selected", methods=['GET', 'POST'])
def edit_config_user_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_config_afficher = """SELECT id_config, config_use_case FROM t_config ORDER BY id_config ASC"""
                mc_afficher.execute(strsql_config_afficher)
            data_config_all = mc_afficher.fetchall()
            print("dans edit_config_user_selected ---> data_config_all", data_config_all)

            # Récupère la valeur de "id_user" du formulaire html "user_config_afficher.html"
            # l'utilisateur clique sur le bouton "Modifier" et on récupère la valeur de "id_user"
            # grâce à la variable "id_user_config_edit_html" dans le fichier "user_config_afficher.html"
            # href="{{ url_for('edit_config_user_selected', id_user_config_edit_html=row.id_user) }}"
            id_user_config_edit = request.values['id_user_config_edit_html']

            # Mémorise l'id du user dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_user_config_edit'] = id_user_config_edit

            # Constitution d'un dictionnaire pour associer l'id du user sélectionné avec un nom de variable
            valeur_id_user_selected_dictionnaire = {"value_id_user_selected": id_user_config_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction config_user_afficher_data
            # 1) Sélection du user choisi
            # 2) Sélection des config "déjà" attribués pour le user.
            # 3) Sélection des config "pas encore" attribués pour le user choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "config_user_afficher_data"
            data_config_user_selected, data_config_user_non_attribues, data_config_user_attribues = \
                config_user_afficher_data(valeur_id_user_selected_dictionnaire)

            print(data_config_user_selected)
            lst_data_user_selected = [item['id_user'] for item in data_config_user_selected]
            print("lst_data_user_selected  ", lst_data_user_selected,
                  type(lst_data_user_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les config qui ne sont pas encore sélectionnés.
            lst_data_config_user_non_attribues = [item['id_config'] for item in data_config_user_non_attribues]
            session['session_lst_data_config_user_non_attribues'] = lst_data_config_user_non_attribues
            print("lst_data_config_user_non_attribues  ", lst_data_config_user_non_attribues,
                  type(lst_data_config_user_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les config qui sont déjà sélectionnés.
            lst_data_config_user_old_attribues = [item['id_config'] for item in data_config_user_attribues]
            session['session_lst_data_config_user_old_attribues'] = lst_data_config_user_old_attribues
            print("lst_data_config_user_old_attribues  ", lst_data_config_user_old_attribues,
                  type(lst_data_config_user_old_attribues))

            print(" data data_config_user_selected", data_config_user_selected, "type ",
                  type(data_config_user_selected))
            print(" data data_config_user_non_attribues ", data_config_user_non_attribues, "type ",
                  type(data_config_user_non_attribues))
            print(" data_config_user_attribues ", data_config_user_attribues, "type ",
                  type(data_config_user_attribues))

            # Extrait les valeurs contenues dans la table "t_config", colonne "config_use_case"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_config
            lst_data_config_user_non_attribues = [item['config_use_case'] for item in data_config_user_non_attribues]
            print("lst_all_config gf_edit_config_user_selected ", lst_data_config_user_non_attribues,
                  type(lst_data_config_user_non_attribues))

        except Exception as Exception_edit_config_user_selected:
            raise ExceptionEditConfigUserSelected(f"fichier : {Path(__file__).name}  ;  "
                                                  f"{edit_config_user_selected.__name__} ; "
                                                  f"{Exception_edit_config_user_selected}")

    return render_template("user_config/user_config_modifier_tags_dropbox.html",
                           data_config=data_config_all,
                           data_user_selected=data_config_user_selected,
                           data_config_attribues=data_config_user_attribues,
                           data_config_non_attribues=data_config_user_non_attribues)


"""
    nom: update_config_user_selected

    Récupère la liste de tous les config du user sélectionné par le bouton "MODIFIER" de "user_config_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les config contenus dans la "t_config".
    2) Les config attribués au user selectionné.
    3) Les config non-attribués au user sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_config_user_selected", methods=['GET', 'POST'])
def update_config_user_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du user sélectionné
            id_user_selected = session['session_id_user_config_edit']
            print("session['session_id_user_config_edit'] ", session['session_id_user_config_edit'])

            # Récupère la liste des config qui ne sont pas associés au user sélectionné.
            old_lst_data_config_user_non_attribues = session['session_lst_data_config_user_non_attribues']
            print("old_lst_data_config_user_non_attribues ", old_lst_data_config_user_non_attribues)

            # Récupère la liste des config qui sont associés au user sélectionné.
            old_lst_data_config_user_attribues = session['session_lst_data_config_user_old_attribues']
            print("old_lst_data_config_user_old_attribues ", old_lst_data_config_user_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme config dans le composant "tags-selector-tagselect"
            # dans le fichier "config_user_modifier_tags_dropbox.html"
            new_lst_str_config_user = request.form.getlist('name_select_tags')
            print("new_lst_str_config_user ", new_lst_str_config_user)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_config_user_old = list(map(int, new_lst_str_config_user))
            print("new_lst_config_user ", new_lst_int_config_user_old, "type new_lst_config_user ",
                  type(new_lst_int_config_user_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_config" qui doivent être effacés de la table intermédiaire "t_user_created_config".
            lst_diff_config_delete_b = list(set(old_lst_data_config_user_attribues) -
                                            set(new_lst_int_config_user_old))
            print("lst_diff_config_delete_b ", lst_diff_config_delete_b)

            # Une liste de "id_config" qui doivent être ajoutés à la "t_user_created_config"
            lst_diff_config_insert_a = list(
                set(new_lst_int_config_user_old) - set(old_lst_data_config_user_attribues))
            print("lst_diff_config_insert_a ", lst_diff_config_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_user"/"id_user" et "fk_config"/"id_config" dans la "t_user_created_config"
            strsql_insert_config_user = """INSERT INTO t_user_created_config (id_user_created_config, fk_config, fk_user)
                                                    VALUES (NULL, %(value_fk_config)s, %(value_fk_user)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_user" et "id_config" dans la "t_user_created_config"
            strsql_delete_config_user = """DELETE FROM t_user_created_config WHERE fk_config = %(value_fk_config)s AND fk_user = %(value_fk_user)s"""

            with DBconnection() as mconn_bd:
                # Pour le user sélectionné, parcourir la liste des config à INSÉRER dans la "t_user_created_config".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_config_ins in lst_diff_config_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du user sélectionné avec un nom de variable
                    # et "id_config_ins" (l'id de la config dans la liste) associé à une variable.
                    valeurs_user_sel_config_sel_dictionnaire = {"value_fk_user": id_user_selected,
                                                                "value_fk_config": id_config_ins}

                    mconn_bd.execute(strsql_insert_config_user, valeurs_user_sel_config_sel_dictionnaire)

                # Pour l'utilisateur sélectionné, parcourir la liste des config à EFFACER dans la "t_user_created_config".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_config_del in lst_diff_config_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id de l'utilisateur sélectionné avec un nom de variable
                    # et "id_config_del" (l'id de la config dans la liste) associé à une variable.
                    valeurs_user_sel_config_sel_dictionnaire = {"value_fk_user": id_user_selected,
                                                                "value_fk_config": id_config_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_config_user, valeurs_user_sel_config_sel_dictionnaire)

        except Exception as Exception_update_config_user_selected:
            raise ExceptionUpdateConfigUserSelected(f"fichier : {Path(__file__).name}  ;  "
                                                   f"{update_config_user_selected.__name__} ; "
                                                   f"{Exception_update_config_user_selected}")

    # Après cette mise à jour de la table intermédiaire "t_user_created_config",
    # on affiche les utilisateurs et la(les) config(s) associé(s).
    return redirect(url_for('user_config_afficher', id_user_sel=id_user_selected))


"""
    nom: config_user_afficher_data

    Récupère la liste de tous les config du user sélectionné par le bouton "MODIFIER" de "user_config_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des config, ainsi l'utilisateur voit les config à disposition

    On signale les erreurs importantes
"""


def config_user_afficher_data(valeur_id_user_selected_dict):
    print("valeur_id_user_selected_dict...", valeur_id_user_selected_dict)
    try:

        strsql_user_selected = """SELECT id_user, user_firstname, user_lastname, user_birthdate, GROUP_CONCAT(id_config) as UserConfig FROM t_user_created_config
                                        INNER JOIN t_user ON t_user.id_user = t_user_created_config.fk_user
                                        INNER JOIN t_config ON t_config.id_config = t_user_created_config.fk_config
                                        WHERE id_user = %(value_id_user_selected)s"""

        strsql_config_user_non_attribues = """SELECT id_config, config_use_case FROM t_config WHERE id_config not in(SELECT id_config as idConfigUser FROM t_user_created_config
                                                    INNER JOIN t_user ON t_user.id_user = t_user_created_config.fk_user
                                                    INNER JOIN t_config ON t_config.id_config = t_user_created_config.fk_config
                                                    WHERE id_user = %(value_id_user_selected)s)"""

        strsql_config_user_attribues = """SELECT id_user, id_config, config_use_case FROM t_user_created_config
                                            INNER JOIN t_user ON t_user.id_user = t_user_created_config.fk_user
                                            INNER JOIN t_config ON t_config.id_config = t_user_created_config.fk_config
                                            WHERE id_user = %(value_id_user_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_config_user_non_attribues, valeur_id_user_selected_dict)
            # Récupère les données de la requête.
            data_config_user_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("config_user_afficher_data ----> data_config_user_non_attribues ", data_config_user_non_attribues,
                  " Type : ",
                  type(data_config_user_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_user_selected, valeur_id_user_selected_dict)
            # Récupère les données de la requête.
            data_user_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_user_selected  ", data_user_selected, " Type : ", type(data_user_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_config_user_attribues, valeur_id_user_selected_dict)
            # Récupère les données de la requête.
            data_config_user_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_config_user_attribues ", data_config_user_attribues, " Type : ",
                  type(data_config_user_attribues))

            # Retourne les données des "SELECT"
            return data_user_selected, data_config_user_non_attribues, data_config_user_attribues

    except Exception as Exception_config_user_afficher_data:
        raise ExceptionConfigUserAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                               f"{config_user_afficher_data.__name__} ; "
                                               f"{Exception_config_user_afficher_data}")
