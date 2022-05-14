"""
    Fichier : gestion_cpu_cpumanufacturer_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les cpu et les cpumanufacturer.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_CONFIG_164.database.database_tools import DBconnection
from APP_CONFIG_164.erreurs.exceptions import *

"""
    Nom : cpu_cpumanufacturer_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /cpu_cpumanufacturer_afficher
    
    But : Afficher les cpu avec les cpumanufacturer associés pour chaque cpu.
    
    Paramètres : id_cpu_manufacturer_sel = 0 >> tous les cpu.
                 id_cpu_manufacturer_sel = "n" affiche le cpu dont l'id est "n"
                 
"""


@app.route("/cpu_cpumanufacturer_afficher/<int:id_cpu_sel>", methods=['GET', 'POST'])
def cpu_cpumanufacturer_afficher(id_cpu_sel):
    print(" cpu_cpumanufacturer_afficher id_cpu_sel ", id_cpu_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_cpumanufacturer_cpu_afficher_data = """SELECT id_cpu, CPU_Name, CPU_Codename, CPU_Cores, CPU_Clock, CPU_Socket,
                                                            GROUP_CONCAT(CPU_Manufacturer) as CpumanufacturerCpu FROM t_cpumanufacturer_produce_cpu
                                                            RIGHT JOIN t_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
                                                            LEFT JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
                                                            GROUP BY id_cpu"""
                if id_cpu_sel == 0:
                    # le paramètre 0 permet d'afficher tous les cpu
                    # Sinon le paramètre représente la valeur de l'id du cpu
                    mc_afficher.execute(strsql_cpumanufacturer_cpu_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du cpu sélectionné avec un nom de variable
                    valeur_id_cpu_selected_dictionnaire = {"value_id_cpu_selected": id_cpu_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_cpumanufacturer_cpu_afficher_data += """ HAVING id_cpu= %(value_id_cpu_selected)s"""

                    mc_afficher.execute(strsql_cpumanufacturer_cpu_afficher_data, valeur_id_cpu_selected_dictionnaire)

                # Récupère les données de la requête.
                data_cpumanufacturer_cpu_afficher = mc_afficher.fetchall()
                print("data_cpumanufacturer ", data_cpumanufacturer_cpu_afficher, " Type : ",
                      type(data_cpumanufacturer_cpu_afficher))

                # Différencier les messages.
                if not data_cpumanufacturer_cpu_afficher and id_cpu_sel == 0:
                    flash("""La table "t_cpu" est vide. !""", "warning")
                elif not data_cpumanufacturer_cpu_afficher and id_cpu_sel > 0:
                    # Si l'utilisateur change l'id_cpu dans l'URL et qu'il ne correspond à aucun cpu
                    flash(f"Le cpu {id_cpu_sel} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données cpu et cpumanufacturer affichés !!", "success")

        except Exception as Exception_cpu_cpumanufacturer_afficher:
            raise ExceptionCpuCpumanufacturerAfficher(
                f"fichier : {Path(__file__).name}  ;  {cpu_cpumanufacturer_afficher.__name__} ;"
                f"{Exception_cpu_cpumanufacturer_afficher}")

    print("cpu_cpumanufacturer_afficher  ", data_cpumanufacturer_cpu_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("cpu_cpumanufacturer/cpu_cpumanufacturer_afficher.html",
                           data=data_cpumanufacturer_cpu_afficher)


"""
    nom: edit_cpumanufacturer_cpu_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les cpumanufacturer du cpu sélectionné par le bouton "MODIFIER" de "cpu_cpumanufacturer_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les cpumanufacturer contenus dans la "t_cpumanufacturer".
    2) Les cpumanufacturer attribués au cpu selectionné.
    3) Les cpumanufacturer non-attribués au cpu sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_cpumanufacturer_cpu_selected", methods=['GET', 'POST'])
def edit_cpumanufacturer_cpu_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_id_cpu_manufacturer_afficher = """SELECT id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer ORDER BY id_cpu_manufacturer ASC"""
                mc_afficher.execute(strsql_id_cpu_manufacturer_afficher)
            data_cpumanufacturer_all = mc_afficher.fetchall()
            print("dans edit_cpumanufacturer_cpu_selected ---> data_cpumanufacturer_all", data_cpumanufacturer_all)

            # Récupère la valeur de "id_cpu" du formulaire html "cpu_cpumanufacturer_afficher.html"
            # l'utilisateur clique sur le bouton "Modifier" et on récupère la valeur de "id_cpu"
            # grâce à la variable "id_cpu_cpumanufacturer_edit_html" dans le fichier "cpu_cpumanufacturer_afficher.html"
            # href="{{ url_for('edit_cpumanufacturer_cpu_selected', id_cpu_cpumanufacturer_edit_html=row.id_cpu) }}"
            id_cpu_cpumanufacturer_edit = request.values['id_cpu_cpumanufacturer_edit_html']

            # Mémorise l'id du cpu dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_cpu_cpumanufacturer_edit'] = id_cpu_cpumanufacturer_edit

            # Constitution d'un dictionnaire pour associer l'id du cpu sélectionné avec un nom de variable
            valeur_id_cpu_selected_dictionnaire = {"value_id_cpu_selected": id_cpu_cpumanufacturer_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction cpumanufacturer_cpu_afficher_data
            # 1) Sélection du cpu choisi
            # 2) Sélection des cpumanufacturer "déjà" attribués pour le cpu.
            # 3) Sélection des cpumanufacturer "pas encore" attribués pour le cpu choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "cpumanufacturer_cpu_afficher_data"
            data_cpumanufacturer_cpu_selected, data_cpumanufacturer_cpu_non_attribues, data_cpumanufacturer_cpu_attribues = \
                cpumanufacturer_cpu_afficher_data(valeur_id_cpu_selected_dictionnaire)

            print(data_cpumanufacturer_cpu_selected)
            lst_data_cpu_selected = [item['id_cpu'] for item in data_cpumanufacturer_cpu_selected]
            print("lst_data_cpu_selected  ", lst_data_cpu_selected,
                  type(lst_data_cpu_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les cpumanufacturer qui ne sont pas encore sélectionnés.
            lst_data_cpumanufacturer_cpu_non_attribues = [item['id_cpu_manufacturer'] for item in
                                                          data_cpumanufacturer_cpu_non_attribues]
            session['session_lst_data_cpumanufacturer_cpu_non_attribues'] = lst_data_cpumanufacturer_cpu_non_attribues
            print("lst_data_cpumanufacturer_cpu_non_attribues  ", lst_data_cpumanufacturer_cpu_non_attribues,
                  type(lst_data_cpumanufacturer_cpu_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les cpumanufacturer qui sont déjà sélectionnés.
            lst_data_cpumanufacturer_cpu_old_attribues = [item['id_cpu_manufacturer'] for item in
                                                          data_cpumanufacturer_cpu_attribues]
            session['session_lst_data_cpumanufacturer_cpu_old_attribues'] = lst_data_cpumanufacturer_cpu_old_attribues
            print("lst_data_cpumanufacturer_cpu_old_attribues  ", lst_data_cpumanufacturer_cpu_old_attribues,
                  type(lst_data_cpumanufacturer_cpu_old_attribues))

            print(" data data_cpumanufacturer_cpu_selected", data_cpumanufacturer_cpu_selected, "type ",
                  type(data_cpumanufacturer_cpu_selected))
            print(" data data_cpumanufacturer_cpu_non_attribues ", data_cpumanufacturer_cpu_non_attribues, "type ",
                  type(data_cpumanufacturer_cpu_non_attribues))
            print(" data_cpumanufacturer_cpu_attribues ", data_cpumanufacturer_cpu_attribues, "type ",
                  type(data_cpumanufacturer_cpu_attribues))

            # Extrait les valeurs contenues dans la table "t_cpumanufacturer", colonne "CPU_Manufacturer"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_cpu_manufacturer
            lst_data_cpumanufacturer_cpu_non_attribues = [item['CPU_Manufacturer'] for item in
                                                          data_cpumanufacturer_cpu_non_attribues]
            print("lst_all_cpumanufacturer gf_edit_cpumanufacturer_cpu_selected ",
                  lst_data_cpumanufacturer_cpu_non_attribues,
                  type(lst_data_cpumanufacturer_cpu_non_attribues))

        except Exception as Exception_edit_cpumanufacturer_cpu_selected:
            raise ExceptionEditCpumanufacturerCpuSelected(f"fichier : {Path(__file__).name}  ;  "
                                                          f"{edit_cpumanufacturer_cpu_selected.__name__} ; "
                                                          f"{Exception_edit_cpumanufacturer_cpu_selected}")

    return render_template("cpu_cpumanufacturer/cpu_cpumanufacturer_modifier_tags_dropbox.html",
                           data_cpumanufacturer=data_cpumanufacturer_all,
                           data_cpu_selected=data_cpumanufacturer_cpu_selected,
                           data_cpumanufacturer_attribues=data_cpumanufacturer_cpu_attribues,
                           data_cpumanufacturer_non_attribues=data_cpumanufacturer_cpu_non_attribues)


"""
    nom: update_cpumanufacturer_cpu_selected

    Récupère la liste de tous les cpumanufacturer du cpu sélectionné par le bouton "MODIFIER" de "cpu_cpumanufacturer_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les cpumanufacturer contenus dans la "t_cpumanufacturer".
    2) Les cpumanufacturer attribués au cpu selectionné.
    3) Les cpumanufacturer non-attribués au cpu sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_cpumanufacturer_cpu_selected", methods=['GET', 'POST'])
def update_cpumanufacturer_cpu_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du cpu sélectionné
            id_cpu_selected = session['session_id_cpu_cpumanufacturer_edit']
            print("session['session_id_cpu_cpumanufacturer_edit'] ", session['session_id_cpu_cpumanufacturer_edit'])

            # Récupère la liste des cpumanufacturer qui ne sont pas associés au cpu sélectionné.
            old_lst_data_cpumanufacturer_cpu_non_attribues = session[
                'session_lst_data_cpumanufacturer_cpu_non_attribues']
            print("old_lst_data_cpumanufacturer_cpu_non_attribues ", old_lst_data_cpumanufacturer_cpu_non_attribues)

            # Récupère la liste des cpumanufacturer qui sont associés au cpu sélectionné.
            old_lst_data_cpumanufacturer_cpu_attribues = session['session_lst_data_cpumanufacturer_cpu_old_attribues']
            print("old_lst_data_cpumanufacturer_cpu_old_attribues ", old_lst_data_cpumanufacturer_cpu_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme cpumanufacturer dans le composant "tags-selector-tagselect"
            # dans le fichier "cpumanufacturer_cpu_modifier_tags_dropbox.html"
            new_lst_str_cpumanufacturer_cpu = request.form.getlist('name_select_tags')
            print("new_lst_str_cpumanufacturer_cpu ", new_lst_str_cpumanufacturer_cpu)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_cpumanufacturer_cpu_old = list(map(int, new_lst_str_cpumanufacturer_cpu))
            print("new_lst_cpumanufacturer_cpu ", new_lst_int_cpumanufacturer_cpu_old,
                  "type new_lst_cpumanufacturer_cpu ",
                  type(new_lst_int_cpumanufacturer_cpu_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_cpu_manufacturer" qui doivent être effacés de la table intermédiaire "t_cpumanufacturer_produce_cpu".
            lst_diff_cpumanufacturer_delete_b = list(set(old_lst_data_cpumanufacturer_cpu_attribues) -
                                                     set(new_lst_int_cpumanufacturer_cpu_old))
            print("lst_diff_cpumanufacturer_delete_b ", lst_diff_cpumanufacturer_delete_b)

            # Une liste de "id_cpu_manufacturer" qui doivent être ajoutés à la "t_cpumanufacturer_produce_cpu"
            lst_diff_cpumanufacturer_insert_a = list(
                set(new_lst_int_cpumanufacturer_cpu_old) - set(old_lst_data_cpumanufacturer_cpu_attribues))
            print("lst_diff_cpumanufacturer_insert_a ", lst_diff_cpumanufacturer_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_cpu"/"id_cpu" et "fk_cpumanufacturer"/"id_cpu_manufacturer" dans la "t_cpumanufacturer_produce_cpu"
            strsql_insert_cpumanufacturer_cpu = """INSERT INTO t_cpumanufacturer_produce_cpu (id_cpumanufacturer_produce_cpu, fk_cpumanufacturer, fk_cpu)
                                                    VALUES (NULL, %(value_fk_cpumanufacturer)s, %(value_fk_cpu)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_cpu" et "id_cpu_manufacturer" dans la "t_cpumanufacturer_produce_cpu"
            strsql_delete_cpumanufacturer_cpu = """DELETE FROM t_cpumanufacturer_produce_cpu WHERE fk_cpumanufacturer = %(value_fk_cpumanufacturer)s AND fk_cpu = %(value_fk_cpu)s"""

            with DBconnection() as mconn_bd:
                # Pour le cpu sélectionné, parcourir la liste des cpumanufacturer à INSÉRER dans la "t_cpumanufacturer_produce_cpu".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_cpumanufacturer_ins in lst_diff_cpumanufacturer_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du cpu sélectionné avec un nom de variable
                    # et "id_cpumanufacturer_ins" (l'id du manufacturer dans la liste) associé à une variable.
                    valeurs_cpu_sel_cpumanufacturer_sel_dictionnaire = {"value_fk_cpu": id_cpu_selected,
                                                                        "value_fk_cpumanufacturer": id_cpumanufacturer_ins}

                    mconn_bd.execute(strsql_insert_cpumanufacturer_cpu,
                                     valeurs_cpu_sel_cpumanufacturer_sel_dictionnaire)

                # Pour le cpu sélectionné, parcourir la liste des cpumanufacturer à EFFACER dans la "t_cpumanufacturer_produce_cpu".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_cpumanufacturer_del in lst_diff_cpumanufacturer_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du cpu sélectionné avec un nom de variable
                    # et "id_cpumanufacturer_del" (l'id du manufacturer dans la liste) associé à une variable.
                    valeurs_cpu_sel_cpumanufacturer_sel_dictionnaire = {"value_fk_cpu": id_cpu_selected,
                                                                        "value_fk_cpumanufacturer": id_cpumanufacturer_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_cpumanufacturer_cpu,
                                     valeurs_cpu_sel_cpumanufacturer_sel_dictionnaire)

        except Exception as Exception_update_cpumanufacturer_cpu_selected:
            raise ExceptionUpdateCpumanufacturerCpuSelected(f"fichier : {Path(__file__).name}  ;  "
                                                            f"{update_cpumanufacturer_cpu_selected.__name__} ; "
                                                            f"{Exception_update_cpumanufacturer_cpu_selected}")

    # Après cette mise à jour de la table intermédiaire "t_cpumanufacturer_produce_cpu",
    # on affiche les cpu et le(urs) manufacturer(s) associé(s).
    return redirect(url_for('cpu_cpumanufacturer_afficher', id_cpu_sel=id_cpu_selected))


"""
    nom: cpumanufacturer_cpu_afficher_data

    Récupère la liste de tous les cpumanufacturer du cpu sélectionné par le bouton "MODIFIER" de "cpu_cpumanufacturer_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des cpumanufacturer, ainsi l'utilisateur voit les cpumanufacturer à disposition

    On signale les erreurs importantes
"""


def cpumanufacturer_cpu_afficher_data(valeur_id_cpu_selected_dict):
    print("valeur_id_cpu_selected_dict...", valeur_id_cpu_selected_dict)
    try:

        strsql_cpu_selected = """SELECT id_cpu, CPU_Name, CPU_Codename, CPU_Cores, CPU_Clock, CPU_Socket, GROUP_CONCAT(id_cpu_manufacturer) as CpumanufacturerCpu FROM t_cpumanufacturer_produce_cpu
                                        INNER JOIN t_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
                                        INNER JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
                                        WHERE id_cpu = %(value_id_cpu_selected)s"""

        strsql_cpumanufacturer_cpu_non_attribues = """SELECT id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer WHERE id_cpu_manufacturer not in(SELECT id_cpu_manufacturer as idCpumanufacturerCpu FROM t_cpumanufacturer_produce_cpu
                                                    INNER JOIN t_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
                                                    INNER JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
                                                    WHERE id_cpu = %(value_id_cpu_selected)s)"""

        strsql_cpumanufacturer_cpu_attribues = """SELECT id_cpu, id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer_produce_cpu
                                            INNER JOIN t_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
                                            INNER JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
                                            WHERE id_cpu = %(value_id_cpu_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_cpumanufacturer_cpu_non_attribues, valeur_id_cpu_selected_dict)
            # Récupère les données de la requête.
            data_cpumanufacturer_cpu_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("cpumanufacturer_cpu_afficher_data ----> data_cpumanufacturer_cpu_non_attribues ",
                  data_cpumanufacturer_cpu_non_attribues,
                  " Type : ",
                  type(data_cpumanufacturer_cpu_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_cpu_selected, valeur_id_cpu_selected_dict)
            # Récupère les données de la requête.
            data_cpu_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_cpu_selected  ", data_cpu_selected, " Type : ", type(data_cpu_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_cpumanufacturer_cpu_attribues, valeur_id_cpu_selected_dict)
            # Récupère les données de la requête.
            data_cpumanufacturer_cpu_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_cpumanufacturer_cpu_attribues ", data_cpumanufacturer_cpu_attribues, " Type : ",
                  type(data_cpumanufacturer_cpu_attribues))

            # Retourne les données des "SELECT"
            return data_cpu_selected, data_cpumanufacturer_cpu_non_attribues, data_cpumanufacturer_cpu_attribues

    except Exception as Exception_cpumanufacturer_cpu_afficher_data:
        raise ExceptionCpumanufacturerCpuAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                                      f"{cpumanufacturer_cpu_afficher_data.__name__} ; "
                                                      f"{Exception_cpumanufacturer_cpu_afficher_data}")
