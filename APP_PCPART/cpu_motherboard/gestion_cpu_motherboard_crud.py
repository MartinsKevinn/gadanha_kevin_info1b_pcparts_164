"""
    Fichier : gestion_cpu_motherboard_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les films et les motherboard.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_PCPART.database.database_tools import DBconnection
from APP_PCPART.erreurs.exceptions import *

"""
    Nom : cpu_motherboard_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /cpu_motherboard_afficher
    
    But : Afficher les films avec les motherboard associés pour chaque film.
    
    Paramètres : id_motherboard_sel = 0 >> tous les films.
                 id_motherboard_sel = "n" affiche le film dont l'id est "n"
                 
"""


@app.route("/cpu_motherboard_afficher/<int:id_cpu_sel>", methods=['GET', 'POST'])
def cpu_motherboard_afficher(id_cpu_sel):
    print(" cpu_motherboard_afficher id_cpu_sel ", id_cpu_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_motherboard_cpu_afficher_data = """SELECT id_cpu, CPU_Name, CPU_Codename, CPU_Cores, CPU_Clock, CPU_Socket,
                                                            GROUP_CONCAT(motherboard_brand, motherboard_model) as MotherboardCPU FROM t_cpu_compatible_motherboard
                                                            RIGHT JOIN t_cpu ON t_cpu.id_cpu = t_cpu_compatible_motherboard.fk_cpu
                                                            LEFT JOIN t_motherboard ON t_motherboard.id_motherboard = t_cpu_compatible_motherboard.fk_motherboard
                                                            GROUP BY id_cpu"""
                if id_cpu_sel == 0:
                    # le paramètre 0 permet d'afficher tous les films
                    # Sinon le paramètre représente la valeur de l'id du film
                    mc_afficher.execute(strsql_motherboard_cpu_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    valeur_id_cpu_selected_dictionnaire = {"value_id_cpu_selected": id_cpu_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_motherboard_cpu_afficher_data += """ HAVING id_cpu= %(value_id_cpu_selected)s"""

                    mc_afficher.execute(strsql_motherboard_cpu_afficher_data, valeur_id_cpu_selected_dictionnaire)

                # Récupère les données de la requête.
                data_motherboard_cpu_afficher = mc_afficher.fetchall()
                print("data_motherboard ", data_motherboard_cpu_afficher, " Type : ", type(data_motherboard_cpu_afficher))

                # Différencier les messages.
                if not data_motherboard_cpu_afficher and id_cpu_sel == 0:
                    flash("""La table "t_cpu" est vide. !""", "warning")
                elif not data_motherboard_cpu_afficher and id_cpu_sel > 0:
                    # Si l'utilisateur change l'id_cpu dans l'URL et qu'il ne correspond à aucun film
                    flash(f"Le film {id_cpu_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données films et motherboard affichés !!", "success")

        except Exception as Exception_cpu_motherboard_afficher:
            raise ExceptionCpuMotherboardAfficher(f"fichier : {Path(__file__).name}  ;  {cpu_motherboard_afficher.__name__} ;"
                                               f"{Exception_cpu_motherboard_afficher}")

    print("cpu_motherboard_afficher  ", data_motherboard_cpu_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("cpu_motherboard/cpu_motherboard_afficher.html", data=data_motherboard_cpu_afficher)


"""
    nom: edit_cpu_compatible_motherboard_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les motherboard du film sélectionné par le bouton "MODIFIER" de "cpu_motherboard_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les motherboard contenus dans la "t_motherboard".
    2) Les motherboard attribués au film selectionné.
    3) Les motherboard non-attribués au film sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_cpu_compatible_motherboard_selected", methods=['GET', 'POST'])
def edit_cpu_compatible_motherboard_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_motherboard_afficher = """SELECT id_motherboard, motherboard_brand FROM t_motherboard ORDER BY id_motherboard ASC"""
                mc_afficher.execute(strsql_motherboard_afficher)
            data_motherboard_all = mc_afficher.fetchall()
            print("dans edit_cpu_compatible_motherboard_selected ---> data_motherboard_all", data_motherboard_all)

            # Récupère la valeur de "id_cpu" du formulaire html "cpu_motherboard_afficher.html"
            # l'utilisateur clique sur le bouton "Modifier" et on récupère la valeur de "id_cpu"
            # grâce à la variable "id_cpu_motherboard_edit_html" dans le fichier "cpu_motherboard_afficher.html"
            # href="{{ url_for('edit_cpu_compatible_motherboard_selected', id_cpu_motherboard_edit_html=row.id_cpu) }}"
            id_cpu_motherboard_edit = request.values['id_cpu_motherboard_edit_html']

            # Mémorise l'id du film dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_cpu_motherboard_edit'] = id_cpu_motherboard_edit

            # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
            valeur_id_cpu_selected_dictionnaire = {"value_id_cpu_selected": id_cpu_motherboard_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction motherboard_cpu_afficher_data
            # 1) Sélection du film choisi
            # 2) Sélection des motherboard "déjà" attribués pour le film.
            # 3) Sélection des motherboard "pas encore" attribués pour le film choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "motherboard_cpu_afficher_data"
            data_motherboard_cpu_selected, data_motherboard_cpu_non_attribues, data_motherboard_cpu_attribues = \
                motherboard_cpu_afficher_data(valeur_id_cpu_selected_dictionnaire)

            print(data_motherboard_cpu_selected)
            lst_data_cpu_selected = [item['id_cpu'] for item in data_motherboard_cpu_selected]
            print("lst_data_cpu_selected  ", lst_data_cpu_selected,
                  type(lst_data_cpu_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les motherboard qui ne sont pas encore sélectionnés.
            lst_data_motherboard_cpu_non_attribues = [item['id_motherboard'] for item in data_motherboard_cpu_non_attribues]
            session['session_lst_data_motherboard_cpu_non_attribues'] = lst_data_motherboard_cpu_non_attribues
            print("lst_data_motherboard_cpu_non_attribues  ", lst_data_motherboard_cpu_non_attribues,
                  type(lst_data_motherboard_cpu_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les motherboard qui sont déjà sélectionnés.
            lst_data_motherboard_cpu_old_attribues = [item['id_motherboard'] for item in data_motherboard_cpu_attribues]
            session['session_lst_data_motherboard_cpu_old_attribues'] = lst_data_motherboard_cpu_old_attribues
            print("lst_data_motherboard_cpu_old_attribues  ", lst_data_motherboard_cpu_old_attribues,
                  type(lst_data_motherboard_cpu_old_attribues))

            print(" data data_motherboard_cpu_selected", data_motherboard_cpu_selected, "type ", type(data_motherboard_cpu_selected))
            print(" data data_motherboard_cpu_non_attribues ", data_motherboard_cpu_non_attribues, "type ",
                  type(data_motherboard_cpu_non_attribues))
            print(" data_motherboard_cpu_attribues ", data_motherboard_cpu_attribues, "type ",
                  type(data_motherboard_cpu_attribues))

            # Extrait les valeurs contenues dans la table "t_genres", colonne "motherboard_brand"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_motherboard
            lst_data_motherboard_cpu_non_attribues = [item['motherboard_brand'] for item in data_motherboard_cpu_non_attribues]
            print("lst_all_motherboard gf_edit_cpu_compatible_motherboard_selected ", lst_data_motherboard_cpu_non_attribues,
                  type(lst_data_motherboard_cpu_non_attribues))

        except Exception as Exception_edit_cpu_compatible_motherboard_selected:
            raise ExceptionEditMotherboardCpuSelected(f"fichier : {Path(__file__).name}  ;  "
                                                 f"{edit_cpu_compatible_motherboard_selected.__name__} ; "
                                                 f"{Exception_edit_cpu_compatible_motherboard_selected}")

    return render_template("cpu_motherboard/cpu_motherboard_modifier_tags_dropbox.html",
                           data_motherboard=data_motherboard_all,
                           data_cpu_selected=data_motherboard_cpu_selected,
                           data_motherboard_attribues=data_motherboard_cpu_attribues,
                           data_motherboard_non_attribues=data_motherboard_cpu_non_attribues)


"""
    nom: update_motherboard_cpu_selected

    Récupère la liste de tous les motherboard du film sélectionné par le bouton "MODIFIER" de "cpu_motherboard_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les motherboard contenus dans la "t_motherboard".
    2) Les motherboard attribués au film selectionné.
    3) Les motherboard non-attribués au film sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_motherboard_cpu_selected", methods=['GET', 'POST'])
def update_motherboard_cpu_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du film sélectionné
            id_cpu_selected = session['session_id_cpu_motherboard_edit']
            print("session['session_id_cpu_motherboard_edit'] ", session['session_id_cpu_motherboard_edit'])

            # Récupère la liste des motherboard qui ne sont pas associés au film sélectionné.
            old_lst_data_motherboard_cpu_non_attribues = session['session_lst_data_motherboard_cpu_non_attribues']
            print("old_lst_data_motherboard_cpu_non_attribues ", old_lst_data_motherboard_cpu_non_attribues)

            # Récupère la liste des motherboard qui sont associés au film sélectionné.
            old_lst_data_motherboard_cpu_attribues = session['session_lst_data_motherboard_cpu_old_attribues']
            print("old_lst_data_motherboard_cpu_old_attribues ", old_lst_data_motherboard_cpu_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme motherboard dans le composant "tags-selector-tagselect"
            # dans le fichier "genres_films_modifier_tags_dropbox.html"
            new_lst_str_motherboard_cpu = request.form.getlist('name_select_tags')
            print("new_lst_str_motherboard_cpu ", new_lst_str_motherboard_cpu)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_cpu_compatible_motherboard_old = list(map(int, new_lst_str_motherboard_cpu))
            print("new_lst_cpu_compatible_motherboard ", new_lst_int_cpu_compatible_motherboard_old, "type new_lst_cpu_compatible_motherboard ",
                  type(new_lst_int_cpu_compatible_motherboard_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_motherboard" qui doivent être effacés de la table intermédiaire "t_cpu_compatible_motherboard".
            lst_diff_motherboard_delete_b = list(set(old_lst_data_motherboard_cpu_attribues) -
                                            set(new_lst_int_cpu_compatible_motherboard_old))
            print("lst_diff_motherboard_delete_b ", lst_diff_motherboard_delete_b)

            # Une liste de "id_motherboard" qui doivent être ajoutés à la "t_cpu_compatible_motherboard"
            lst_diff_motherboard_insert_a = list(
                set(new_lst_int_cpu_compatible_motherboard_old) - set(old_lst_data_motherboard_cpu_attribues))
            print("lst_diff_motherboard_insert_a ", lst_diff_motherboard_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_cpu"/"id_cpu" et "fk_motherboard"/"id_motherboard" dans la "t_cpu_compatible_motherboard"
            strsql_insert_cpu_compatible_motherboard = """INSERT INTO t_cpu_compatible_motherboard (id_cpu_compatible_motherboard, fk_motherboard, fk_cpu)
                                                    VALUES (NULL, %(value_fk_motherboard)s, %(value_fk_cpu)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_cpu" et "id_motherboard" dans la "t_cpu_compatible_motherboard"
            strsql_delete_motherboard_cpu = """DELETE FROM t_cpu_compatible_motherboard WHERE fk_motherboard = %(value_fk_motherboard)s AND fk_cpu = %(value_fk_cpu)s"""

            with DBconnection() as mconn_bd:
                # Pour le film sélectionné, parcourir la liste des motherboard à INSÉRER dans la "t_cpu_compatible_motherboard".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_motherboard_ins in lst_diff_motherboard_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_motherboard_ins" (l'id du genre dans la liste) associé à une variable.
                    valeurs_cpu_sel_motherboard_sel_dictionnaire = {"value_fk_cpu": id_cpu_selected,
                                                               "value_fk_motherboard": id_motherboard_ins}

                    mconn_bd.execute(strsql_insert_cpu_compatible_motherboard, valeurs_cpu_sel_motherboard_sel_dictionnaire)

                # Pour le film sélectionné, parcourir la liste des motherboard à EFFACER dans la "t_cpu_compatible_motherboard".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_motherboard_del in lst_diff_motherboard_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
                    # et "id_motherboard_del" (l'id du genre dans la liste) associé à une variable.
                    valeurs_cpu_sel_motherboard_sel_dictionnaire = {"value_fk_cpu": id_cpu_selected,
                                                               "value_fk_motherboard": id_motherboard_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_motherboard_cpu, valeurs_cpu_sel_motherboard_sel_dictionnaire)

        except Exception as Exception_update_motherboard_cpu_selected:
            raise ExceptionUpdateMotherboardCpuSelected(f"fichier : {Path(__file__).name}  ;  "
                                                   f"{update_motherboard_cpu_selected.__name__} ; "
                                                   f"{Exception_update_motherboard_cpu_selected}")

    # Après cette mise à jour de la table intermédiaire "t_cpu_compatible_motherboard",
    # on affiche les films et le(urs) genre(s) associé(s).
    return redirect(url_for('cpu_motherboard_afficher', id_cpu_sel=id_cpu_selected))


"""
    nom: motherboard_cpu_afficher_data

    Récupère la liste de tous les motherboard du film sélectionné par le bouton "MODIFIER" de "cpu_motherboard_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des motherboard, ainsi l'utilisateur voit les motherboard à disposition

    On signale les erreurs importantes
"""


def motherboard_cpu_afficher_data(valeur_id_cpu_selected_dict):
    print("valeur_id_cpu_selected_dict...", valeur_id_cpu_selected_dict)
    try:

        strsql_cpu_selected = """SELECT id_cpu, CPU_Name, CPU_Codename, CPU_Cores, CPU_Clock, CPU_Socket, GROUP_CONCAT(id_motherboard) as MotherboardCPU FROM t_cpu_compatible_motherboard
                                        INNER JOIN t_cpu ON t_cpu.id_cpu = t_cpu_compatible_motherboard.fk_cpu
                                        INNER JOIN t_motherboard ON t_motherboard.id_motherboard = t_cpu_compatible_motherboard.fk_motherboard
                                        WHERE id_cpu = %(value_id_cpu_selected)s"""

        strsql_motherboard_cpu_non_attribues = """SELECT id_motherboard, motherboard_brand FROM t_motherboard WHERE id_motherboard not in(SELECT id_motherboard as idMotherboardCPU FROM t_cpu_compatible_motherboard
                                                    INNER JOIN t_cpu ON t_cpu.id_cpu = t_cpu_compatible_motherboard.fk_cpu
                                                    INNER JOIN t_motherboard ON t_motherboard.id_motherboard = t_cpu_compatible_motherboard.fk_motherboard
                                                    WHERE id_cpu = %(value_id_cpu_selected)s)"""

        strsql_motherboard_cpu_attribues = """SELECT id_cpu, id_motherboard, motherboard_brand FROM t_cpu_compatible_motherboard
                                            INNER JOIN t_cpu ON t_cpu.id_cpu = t_cpu_compatible_motherboard.fk_cpu
                                            INNER JOIN t_motherboard ON t_motherboard.id_motherboard = t_cpu_compatible_motherboard.fk_motherboard
                                            WHERE id_cpu = %(value_id_cpu_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_motherboard_cpu_non_attribues, valeur_id_cpu_selected_dict)
            # Récupère les données de la requête.
            data_motherboard_cpu_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("motherboard_cpu_afficher_data ----> data_motherboard_cpu_non_attribues ", data_motherboard_cpu_non_attribues,
                  " Type : ",
                  type(data_motherboard_cpu_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_cpu_selected, valeur_id_cpu_selected_dict)
            # Récupère les données de la requête.
            data_cpu_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_cpu_selected  ", data_cpu_selected, " Type : ", type(data_cpu_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_motherboard_cpu_attribues, valeur_id_cpu_selected_dict)
            # Récupère les données de la requête.
            data_motherboard_cpu_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_motherboard_cpu_attribues ", data_motherboard_cpu_attribues, " Type : ",
                  type(data_motherboard_cpu_attribues))

            # Retourne les données des "SELECT"
            return data_cpu_selected, data_motherboard_cpu_non_attribues, data_motherboard_cpu_attribues

    except Exception as Exception_motherboard_cpu_afficher_data:
        raise ExceptionMotherboardCPUAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                               f"{motherboard_cpu_afficher_data.__name__} ; "
                                               f"{Exception_motherboard_cpu_afficher_data}")
