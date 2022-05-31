"""
    Fichier : gestion_gpu_gpumanufacturer_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les gpu et les gpumanufacturer.
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_PCPART.database.database_tools import DBconnection
from APP_PCPART.erreurs.exceptions import *

"""
    Nom : gpu_gpumanufacturer_afficher
    Auteur : OM 2021.05.01
    Définition d'une "route" /gpu_gpumanufacturer_afficher
    
    But : Afficher les gpu avec les gpumanufacturer associés pour chaque gpu.
    
    Paramètres : id_gpu_manufacturer_sel = 0 >> tous les gpu.
                 id_gpu_manufacturer_sel = "n" affiche le gpu dont l'id est "n"
                 
"""


@app.route("/gpu_gpumanufacturer_afficher/<int:id_gpu_sel>", methods=['GET', 'POST'])
def gpu_gpumanufacturer_afficher(id_gpu_sel):
    print(" gpu_gpumanufacturer_afficher id_gpu_sel ", id_gpu_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_gpumanufacturer_gpu_afficher_data = """SELECT id_gpu, GPU_Brand, GPU_Name, GPU_Codename, GPU_Bus, GPU_Memory, GPU_Clock, Memory_Clock, GPU_TDP, GPU_Released,
                                                            GROUP_CONCAT(GPU_Manufacturer) as GpumanufacturerGpu FROM t_gpumanufacturer_produce_gpu
                                                            RIGHT JOIN t_gpu ON t_gpu.id_gpu = t_gpumanufacturer_produce_gpu.fk_gpu
                                                            LEFT JOIN t_gpumanufacturer ON t_gpumanufacturer.id_gpumanufacturer = t_gpumanufacturer_produce_gpu.fk_gpumanufacturer
                                                            GROUP BY id_gpu"""
                if id_gpu_sel == 0:
                    # le paramètre 0 permet d'afficher tous les gpu
                    # Sinon le paramètre représente la valeur de l'id du gpu
                    mc_afficher.execute(strsql_gpumanufacturer_gpu_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du gpu sélectionné avec un nom de variable
                    valeur_id_gpu_selected_dictionnaire = {"value_id_gpu_selected": id_gpu_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_gpumanufacturer_gpu_afficher_data += """ HAVING id_gpu= %(value_id_gpu_selected)s"""

                    mc_afficher.execute(strsql_gpumanufacturer_gpu_afficher_data, valeur_id_gpu_selected_dictionnaire)

                # Récupère les données de la requête.
                data_gpumanufacturer_gpu_afficher = mc_afficher.fetchall()
                print("data_gpumanufacturer ", data_gpumanufacturer_gpu_afficher, " Type : ",
                      type(data_gpumanufacturer_gpu_afficher))

                # Différencier les messages.
                if not data_gpumanufacturer_gpu_afficher and id_gpu_sel == 0:
                    flash("""Table "t_gpu" is empty !""", "warning")
                elif not data_gpumanufacturer_gpu_afficher and id_gpu_sel > 0:
                    # Si l'utilisateur change l'id_gpu dans l'URL et qu'il ne correspond à aucun gpu
                    flash(f"Searched gpu {id_gpu_sel} doesn't exist !!", "warning")
                else:
                    flash(f"Data gpus and Manufacturers shown !!", "success")

        except Exception as Exception_gpu_gpumanufacturer_afficher:
            raise ExceptiongpugpumanufacturerAfficher(
                f"fichier : {Path(__file__).name}  ;  {gpu_gpumanufacturer_afficher.__name__} ;"
                f"{Exception_gpu_gpumanufacturer_afficher}")

    print("gpu_gpumanufacturer_afficher  ", data_gpumanufacturer_gpu_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("gpu_gpumanufacturer/gpu_gpumanufacturer_afficher.html",
                           data=data_gpumanufacturer_gpu_afficher)


"""
    nom: edit_gpumanufacturer_gpu_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les gpumanufacturer du gpu sélectionné par le bouton "MODIFIER" de "gpu_gpumanufacturer_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les gpumanufacturer contenus dans la "t_gpumanufacturer".
    2) Les gpumanufacturer attribués au gpu selectionné.
    3) Les gpumanufacturer non-attribués au gpu sélectionné.

    On signale les erreurs importantes

"""


@app.route("/edit_gpumanufacturer_gpu_selected", methods=['GET', 'POST'])
def edit_gpumanufacturer_gpu_selected():
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_id_gpu_manufacturer_afficher = """SELECT id_gpumanufacturer, GPU_Manufacturer FROM t_gpumanufacturer ORDER BY id_gpumanufacturer ASC"""
                mc_afficher.execute(strsql_id_gpu_manufacturer_afficher)
            data_gpumanufacturer_all = mc_afficher.fetchall()
            print("dans edit_gpumanufacturer_gpu_selected ---> data_gpumanufacturer_all", data_gpumanufacturer_all)

            # Récupère la valeur de "id_gpu" du formulaire html "gpu_gpumanufacturer_afficher.html"
            # l'utilisateur clique sur le bouton "Edit" et on récupère la valeur de "id_gpu"
            # grâce à la variable "id_gpu_gpumanufacturer_edit_html" dans le fichier "gpu_gpumanufacturer_afficher.html"
            # href="{{ url_for('edit_gpumanufacturer_gpu_selected', id_gpu_gpumanufacturer_edit_html=row.id_gpu) }}"
            id_gpu_gpumanufacturer_edit = request.values['id_gpu_gpumanufacturer_edit_html']

            # Mémorise l'id du gpu dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_gpu_gpumanufacturer_edit'] = id_gpu_gpumanufacturer_edit

            # Constitution d'un dictionnaire pour associer l'id du gpu sélectionné avec un nom de variable
            valeur_id_gpu_selected_dictionnaire = {"value_id_gpu_selected": id_gpu_gpumanufacturer_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction gpumanufacturer_gpu_afficher_data
            # 1) Sélection du gpu choisi
            # 2) Sélection des gpumanufacturer "déjà" attribués pour le gpu.
            # 3) Sélection des gpumanufacturer "pas encore" attribués pour le gpu choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "gpumanufacturer_gpu_afficher_data"
            data_gpumanufacturer_gpu_selected, data_gpumanufacturer_gpu_non_attribues, data_gpumanufacturer_gpu_attribues = \
                gpumanufacturer_gpu_afficher_data(valeur_id_gpu_selected_dictionnaire)

            print(data_gpumanufacturer_gpu_selected)
            lst_data_gpu_selected = [item['id_gpu'] for item in data_gpumanufacturer_gpu_selected]
            print("lst_data_gpu_selected  ", lst_data_gpu_selected,
                  type(lst_data_gpu_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les gpumanufacturer qui ne sont pas encore sélectionnés.
            lst_data_gpumanufacturer_gpu_non_attribues = [item['id_gpumanufacturer'] for item in
                                                          data_gpumanufacturer_gpu_non_attribues]
            session['session_lst_data_gpumanufacturer_gpu_non_attribues'] = lst_data_gpumanufacturer_gpu_non_attribues
            print("lst_data_gpumanufacturer_gpu_non_attribues  ", lst_data_gpumanufacturer_gpu_non_attribues,
                  type(lst_data_gpumanufacturer_gpu_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les gpumanufacturer qui sont déjà sélectionnés.
            lst_data_gpumanufacturer_gpu_old_attribues = [item['id_gpumanufacturer'] for item in
                                                          data_gpumanufacturer_gpu_attribues]
            session['session_lst_data_gpumanufacturer_gpu_old_attribues'] = lst_data_gpumanufacturer_gpu_old_attribues
            print("lst_data_gpumanufacturer_gpu_old_attribues  ", lst_data_gpumanufacturer_gpu_old_attribues,
                  type(lst_data_gpumanufacturer_gpu_old_attribues))

            print(" data data_gpumanufacturer_gpu_selected", data_gpumanufacturer_gpu_selected, "type ",
                  type(data_gpumanufacturer_gpu_selected))
            print(" data data_gpumanufacturer_gpu_non_attribues ", data_gpumanufacturer_gpu_non_attribues, "type ",
                  type(data_gpumanufacturer_gpu_non_attribues))
            print(" data_gpumanufacturer_gpu_attribues ", data_gpumanufacturer_gpu_attribues, "type ",
                  type(data_gpumanufacturer_gpu_attribues))

            # Extrait les valeurs contenues dans la table "t_gpumanufacturer", colonne "GPU_Manufacturer"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_gpumanufacturer
            lst_data_gpumanufacturer_gpu_non_attribues = [item['GPU_Manufacturer'] for item in
                                                          data_gpumanufacturer_gpu_non_attribues]
            print("lst_all_gpumanufacturer gf_edit_gpumanufacturer_gpu_selected ",
                  lst_data_gpumanufacturer_gpu_non_attribues,
                  type(lst_data_gpumanufacturer_gpu_non_attribues))

        except Exception as Exception_edit_gpumanufacturer_gpu_selected:
            raise ExceptionEditgpumanufacturergpuSelected(f"fichier : {Path(__file__).name}  ;  "
                                                          f"{edit_gpumanufacturer_gpu_selected.__name__} ; "
                                                          f"{Exception_edit_gpumanufacturer_gpu_selected}")

    return render_template("gpu_gpumanufacturer/gpu_gpumanufacturer_modifier_tags_dropbox.html",
                           data_gpumanufacturer=data_gpumanufacturer_all,
                           data_gpu_selected=data_gpumanufacturer_gpu_selected,
                           data_gpumanufacturer_attribues=data_gpumanufacturer_gpu_attribues,
                           data_gpumanufacturer_non_attribues=data_gpumanufacturer_gpu_non_attribues)


"""
    nom: update_gpumanufacturer_gpu_selected

    Récupère la liste de tous les gpumanufacturer du gpu sélectionné par le bouton "MODIFIER" de "gpu_gpumanufacturer_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les gpumanufacturer contenus dans la "t_gpumanufacturer".
    2) Les gpumanufacturer attribués au gpu selectionné.
    3) Les gpumanufacturer non-attribués au gpu sélectionné.

    On signale les erreurs importantes
"""


@app.route("/update_gpumanufacturer_gpu_selected", methods=['GET', 'POST'])
def update_gpumanufacturer_gpu_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du gpu sélectionné
            id_gpu_selected = session['session_id_gpu_gpumanufacturer_edit']
            print("session['session_id_gpu_gpumanufacturer_edit'] ", session['session_id_gpu_gpumanufacturer_edit'])

            # Récupère la liste des gpumanufacturer qui ne sont pas associés au gpu sélectionné.
            old_lst_data_gpumanufacturer_gpu_non_attribues = session[
                'session_lst_data_gpumanufacturer_gpu_non_attribues']
            print("old_lst_data_gpumanufacturer_gpu_non_attribues ", old_lst_data_gpumanufacturer_gpu_non_attribues)

            # Récupère la liste des gpumanufacturer qui sont associés au gpu sélectionné.
            old_lst_data_gpumanufacturer_gpu_attribues = session['session_lst_data_gpumanufacturer_gpu_old_attribues']
            print("old_lst_data_gpumanufacturer_gpu_old_attribues ", old_lst_data_gpumanufacturer_gpu_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme gpumanufacturer dans le composant "tags-selector-tagselect"
            # dans le fichier "gpumanufacturer_gpu_modifier_tags_dropbox.html"
            new_lst_str_gpumanufacturer_gpu = request.form.getlist('name_select_tags')
            print("new_lst_str_gpumanufacturer_gpu ", new_lst_str_gpumanufacturer_gpu)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_gpumanufacturer_gpu_old = list(map(int, new_lst_str_gpumanufacturer_gpu))
            print("new_lst_gpumanufacturer_gpu ", new_lst_int_gpumanufacturer_gpu_old,
                  "type new_lst_gpumanufacturer_gpu ",
                  type(new_lst_int_gpumanufacturer_gpu_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_gpumanufacturer" qui doivent être effacés de la table intermédiaire "t_gpumanufacturer_produce_gpu".
            lst_diff_gpumanufacturer_delete_b = list(set(old_lst_data_gpumanufacturer_gpu_attribues) -
                                                     set(new_lst_int_gpumanufacturer_gpu_old))
            print("lst_diff_gpumanufacturer_delete_b ", lst_diff_gpumanufacturer_delete_b)

            # Une liste de "id_gpumanufacturer" qui doivent être ajoutés à la "t_gpumanufacturer_produce_gpu"
            lst_diff_gpumanufacturer_insert_a = list(
                set(new_lst_int_gpumanufacturer_gpu_old) - set(old_lst_data_gpumanufacturer_gpu_attribues))
            print("lst_diff_gpumanufacturer_insert_a ", lst_diff_gpumanufacturer_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_gpu"/"id_gpu" et "fk_gpumanufacturer"/"id_gpumanufacturer" dans la "t_gpumanufacturer_produce_gpu"
            strsql_insert_gpumanufacturer_gpu = """INSERT INTO t_gpumanufacturer_produce_gpu (id_gpumanufacturer_produce_gpu, fk_gpumanufacturer, fk_gpu)
                                                    VALUES (NULL, %(value_fk_gpumanufacturer)s, %(value_fk_gpu)s)"""

            # SQL pour effacer une (des) association(s) existantes entre "id_gpu" et "id_gpumanufacturer" dans la "t_gpumanufacturer_produce_gpu"
            strsql_delete_gpumanufacturer_gpu = """DELETE FROM t_gpumanufacturer_produce_gpu WHERE fk_gpumanufacturer = %(value_fk_gpumanufacturer)s AND fk_gpu = %(value_fk_gpu)s"""

            with DBconnection() as mconn_bd:
                # Pour le gpu sélectionné, parcourir la liste des gpumanufacturer à INSÉRER dans la "t_gpumanufacturer_produce_gpu".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_gpumanufacturer_ins in lst_diff_gpumanufacturer_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du gpu sélectionné avec un nom de variable
                    # et "id_gpumanufacturer_ins" (l'id du manufacturer dans la liste) associé à une variable.
                    valeurs_gpu_sel_gpumanufacturer_sel_dictionnaire = {"value_fk_gpu": id_gpu_selected,
                                                                        "value_fk_gpumanufacturer": id_gpumanufacturer_ins}

                    mconn_bd.execute(strsql_insert_gpumanufacturer_gpu,
                                     valeurs_gpu_sel_gpumanufacturer_sel_dictionnaire)

                # Pour le gpu sélectionné, parcourir la liste des gpumanufacturer à EFFACER dans la "t_gpumanufacturer_produce_gpu".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_gpumanufacturer_del in lst_diff_gpumanufacturer_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du gpu sélectionné avec un nom de variable
                    # et "id_gpumanufacturer_del" (l'id du manufacturer dans la liste) associé à une variable.
                    valeurs_gpu_sel_gpumanufacturer_sel_dictionnaire = {"value_fk_gpu": id_gpu_selected,
                                                                        "value_fk_gpumanufacturer": id_gpumanufacturer_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "execute" dans la classe "DBconnection"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "DBconnection"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.execute(strsql_delete_gpumanufacturer_gpu,
                                     valeurs_gpu_sel_gpumanufacturer_sel_dictionnaire)

        except Exception as Exception_update_gpumanufacturer_gpu_selected:
            raise ExceptionUpdategpumanufacturergpuSelected(f"fichier : {Path(__file__).name}  ;  "
                                                            f"{update_gpumanufacturer_gpu_selected.__name__} ; "
                                                            f"{Exception_update_gpumanufacturer_gpu_selected}")

    # Après cette mise à jour de la table intermédiaire "t_gpumanufacturer_produce_gpu",
    # on affiche les gpu et le(urs) manufacturer(s) associé(s).
    return redirect(url_for('gpu_gpumanufacturer_afficher', id_gpu_sel=id_gpu_selected))


"""
    nom: gpumanufacturer_gpu_afficher_data

    Récupère la liste de tous les gpumanufacturer du gpu sélectionné par le bouton "MODIFIER" de "gpu_gpumanufacturer_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des gpumanufacturer, ainsi l'utilisateur voit les gpumanufacturer à disposition

    On signale les erreurs importantes
"""


def gpumanufacturer_gpu_afficher_data(valeur_id_gpu_selected_dict):
    print("valeur_id_gpu_selected_dict...", valeur_id_gpu_selected_dict)
    try:

        strsql_gpu_selected = """SELECT id_gpu, GPU_Brand, GPU_Name, GPU_Codename, GPU_Bus, GPU_Memory, GPU_Clock, Memory_Clock, GPU_TDP, GPU_Released, GROUP_CONCAT(id_gpumanufacturer) as GpumanufacturerGpu FROM t_gpumanufacturer_produce_gpu
                                        INNER JOIN t_gpu ON t_gpu.id_gpu = t_gpumanufacturer_produce_gpu.fk_gpu
                                        INNER JOIN t_gpumanufacturer ON t_gpumanufacturer.id_gpumanufacturer = t_gpumanufacturer_produce_gpu.fk_gpumanufacturer
                                        WHERE id_gpu = %(value_id_gpu_selected)s"""

        strsql_gpumanufacturer_gpu_non_attribues = """SELECT id_gpumanufacturer, GPU_Manufacturer FROM t_gpumanufacturer WHERE id_gpumanufacturer not in(SELECT id_gpumanufacturer as idgpumanufacturergpu FROM t_gpumanufacturer_produce_gpu
                                                    INNER JOIN t_gpu ON t_gpu.id_gpu = t_gpumanufacturer_produce_gpu.fk_gpu
                                                    INNER JOIN t_gpumanufacturer ON t_gpumanufacturer.id_gpumanufacturer = t_gpumanufacturer_produce_gpu.fk_gpumanufacturer
                                                    WHERE id_gpu = %(value_id_gpu_selected)s)"""

        strsql_gpumanufacturer_gpu_attribues = """SELECT id_gpu, id_gpumanufacturer, GPU_Manufacturer FROM t_gpumanufacturer_produce_gpu
                                            INNER JOIN t_gpu ON t_gpu.id_gpu = t_gpumanufacturer_produce_gpu.fk_gpu
                                            INNER JOIN t_gpumanufacturer ON t_gpumanufacturer.id_gpumanufacturer = t_gpumanufacturer_produce_gpu.fk_gpumanufacturer
                                            WHERE id_gpu = %(value_id_gpu_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with DBconnection() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_gpumanufacturer_gpu_non_attribues, valeur_id_gpu_selected_dict)
            # Récupère les données de la requête.
            data_gpumanufacturer_gpu_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("gpumanufacturer_gpu_afficher_data ----> data_gpumanufacturer_gpu_non_attribues ",
                  data_gpumanufacturer_gpu_non_attribues,
                  " Type : ",
                  type(data_gpumanufacturer_gpu_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_gpu_selected, valeur_id_gpu_selected_dict)
            # Récupère les données de la requête.
            data_gpu_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_gpu_selected  ", data_gpu_selected, " Type : ", type(data_gpu_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_gpumanufacturer_gpu_attribues, valeur_id_gpu_selected_dict)
            # Récupère les données de la requête.
            data_gpumanufacturer_gpu_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_gpumanufacturer_gpu_attribues ", data_gpumanufacturer_gpu_attribues, " Type : ",
                  type(data_gpumanufacturer_gpu_attribues))

            # Retourne les données des "SELECT"
            return data_gpu_selected, data_gpumanufacturer_gpu_non_attribues, data_gpumanufacturer_gpu_attribues

    except Exception as Exception_gpumanufacturer_gpu_afficher_data:
        raise ExceptiongpumanufacturergpuAfficherData(f"fichier : {Path(__file__).name}  ;  "
                                                      f"{gpumanufacturer_gpu_afficher_data.__name__} ; "
                                                      f"{Exception_gpumanufacturer_gpu_afficher_data}")
