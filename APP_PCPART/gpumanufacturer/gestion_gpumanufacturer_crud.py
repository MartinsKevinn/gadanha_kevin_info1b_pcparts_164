"""Gestion des "routes" FLASK et des données pour les gpumanufacturer.
Fichier : gestion_gpumanufacturer_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_PCPART import app
from APP_PCPART.database.database_tools import DBconnection
from APP_PCPART.erreurs.exceptions import *
from APP_PCPART.gpumanufacturer.gestion_gpumanufacturer_wtf_forms import *

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /gpumanufacturer_afficher
    
    Test : ex : http://127.0.0.1:5005/gpumanufacturer_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_gpu_manufacturer_sel = 0 >> tous les gpumanufacturer.
                id_gpu_manufacturer_sel = "n" affiche le manufacturer dont l'id est "n"
"""


@app.route("/gpumanufacturer_afficher/<string:order_by>/<int:id_gpu_manufacturer_sel>", methods=['GET', 'POST'])
def gpumanufacturer_afficher(order_by, id_gpu_manufacturer_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_gpu_manufacturer_sel == 0:
                    strsql_id_gpu_manufacturer_afficher = """SELECT id_gpu_manufacturer, gpu_Manufacturer FROM t_gpumanufacturer ORDER BY id_gpu_manufacturer ASC"""
                    mc_afficher.execute(strsql_id_gpu_manufacturer_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_gpumanufacturer"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du manufacturer sélectionné avec un nom de variable
                    valeur_id_gpu_manufacturer_selected_dictionnaire = {
                        "value_id_gpu_manufacturer_selected": id_gpu_manufacturer_sel}
                    strsql_id_gpu_manufacturer_afficher = """SELECT id_gpu_manufacturer, gpu_Manufacturer  FROM t_gpumanufacturer WHERE id_gpu_manufacturer = %(value_id_gpu_manufacturer_selected)s"""

                    mc_afficher.execute(strsql_id_gpu_manufacturer_afficher,
                                        valeur_id_gpu_manufacturer_selected_dictionnaire)
                else:
                    strsql_id_gpu_manufacturer_afficher = """SELECT id_gpu_manufacturer, gpu_Manufacturer FROM t_gpumanufacturer ORDER BY id_gpu_manufacturer DESC"""

                    mc_afficher.execute(strsql_id_gpu_manufacturer_afficher)

                data_gpumanufacturer = mc_afficher.fetchall()

                print("data_gpumanufacturer ", data_gpumanufacturer, " Type : ", type(data_gpumanufacturer))

                # Différencier les messages si la table is empty
                if not data_gpumanufacturer and id_gpu_manufacturer_sel == 0:
                    flash("""Table "t_gpumanufacturer" is empty !!""", "warning")
                elif not data_gpumanufacturer and id_gpu_manufacturer_sel > 0:
                    # Si l'utilisateur change l'id_gpu_manufacturer dans l'URL et que le manufacturer n'existe pas,
                    flash(f"Le manufacturer demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_gpumanufacturer" is empty
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Data gpu Manufacturers shown !!", "success")

        except Exception as Exception_gpumanufacturer_afficher:
            raise ExceptiongpumanufacturerAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{gpumanufacturer_afficher.__name__} ; "
                                          f"{Exception_gpumanufacturer_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("gpumanufacturer/gpumanufacturer_afficher.html", data=data_gpumanufacturer)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /gpumanufacturer_ajouter
    
    Test : ex : http://127.0.0.1:5005/gpumanufacturer_ajouter
    
    Paramètres : sans
    
    But : Ajouter un manufacturer pour un gpu
    
    Remarque :  Dans le champ "name_gpumanufacturer_html" du formulaire "gpumanufacturer/gpumanufacturer_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/gpumanufacturer_ajouter", methods=['GET', 'POST'])
def gpumanufacturer_ajouter_wtf():
    form = FormWTFAjoutergpumanufacturer()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_gpumanufacturer = form.nom_gpumanufacturer_wtf.data
                valeurs_insertion_dictionnaire = {"value_gpu_Manufacturer": name_gpumanufacturer}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_gpumanufacturer = """INSERT INTO t_gpumanufacturer (id_gpu_manufacturer,gpu_Manufacturer) VALUES (NULL,%(value_gpu_Manufacturer)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_gpumanufacturer, valeurs_insertion_dictionnaire)

                flash(f"Data inserted !!", "success")
                print(f"Data inserted !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('gpumanufacturer_afficher', order_by='DESC', id_gpu_manufacturer_sel=0))

        except Exception as Exception_gpumanufacturer_ajouter_wtf:
            raise ExceptiongpumanufacturerAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                                     f"{gpumanufacturer_ajouter_wtf.__name__} ; "
                                                     f"{Exception_gpumanufacturer_ajouter_wtf}")

    return render_template("gpumanufacturer/gpumanufacturer_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /gpumanufacturer_update
    
    Test : ex cliquer sur le menu "gpumanufacturer" puis cliquer sur le bouton "EDIT" d'un "manufacturer"
    
    Paramètres : sans
    
    But : Editer(update) un manufacturer qui a été sélectionné dans le formulaire "gpumanufacturer_afficher.html"
    
    Remarque :  Dans le champ "nom_gpumanufacturer_update_wtf" du formulaire "gpumanufacturer/gpumanufacturer_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/gpumanufacturer_update", methods=['GET', 'POST'])
def gpumanufacturer_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_gpu_manufacturer"
    id_gpu_manufacturer_update = request.values['id_gpu_manufacturer_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdategpumanufacturer()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "gpumanufacturer_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_gpumanufacturer_update = form_update.nom_gpumanufacturer_update_wtf.data

            valeur_update_dictionnaire = {"value_id_gpu_manufacturer": id_gpu_manufacturer_update,
                                          "value_name_gpumanufacturer": name_gpumanufacturer_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_gpu_Manufacturer = """UPDATE t_gpumanufacturer SET gpu_Manufacturer = %(value_name_gpumanufacturer)s WHERE id_gpu_manufacturer = %(value_id_gpu_manufacturer)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_gpu_Manufacturer, valeur_update_dictionnaire)

            flash(f"Data updated !!", "success")
            print(f"Data updated !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_gpu_manufacturer_update"
            return redirect(
                url_for('gpumanufacturer_afficher', order_by="ASC", id_gpu_manufacturer_sel=id_gpu_manufacturer_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_gpu_manufacturer" et "gpu_Manufacturer" de la "t_gpumanufacturer"
            str_sql_id_gpu_manufacturer = "SELECT id_gpu_manufacturer, gpu_Manufacturer FROM t_gpumanufacturer " \
                               "WHERE id_gpu_manufacturer = %(value_id_gpu_manufacturer)s"
            valeur_select_dictionnaire = {"value_id_gpu_manufacturer": id_gpu_manufacturer_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_gpu_manufacturer, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom manufacturer" pour l'UPDATE
            data_nom_gpumanufacturer = mybd_conn.fetchone()
            print("data_nom_gpumanufacturer ", data_nom_gpumanufacturer, " type ", type(data_nom_gpumanufacturer), " manufacturer ",
                  data_nom_gpumanufacturer["gpu_Manufacturer"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "gpumanufacturer_update_wtf.html"
            form_update.nom_gpumanufacturer_update_wtf.data = data_nom_gpumanufacturer["gpu_Manufacturer"]

    except Exception as Exception_gpumanufacturer_update_wtf:
        raise ExceptiongpumanufacturerUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{gpumanufacturer_update_wtf.__name__} ; "
                                      f"{Exception_gpumanufacturer_update_wtf}")

    return render_template("gpumanufacturer/gpumanufacturer_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /gpumanufacturer_delete
    
    Test : ex. cliquer sur le menu "gpumanufacturer" puis cliquer sur le bouton "DELETE" d'un "manufacturer"
    
    Paramètres : sans
    
    But : Effacer(delete) un manufacturer qui a été sélectionné dans le formulaire "gpumanufacturer_afficher.html"
    
    Remarque :  Dans le champ "nom_gpumanufacturer_delete_wtf" du formulaire "gpumanufacturer/gpumanufacturer_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/gpumanufacturer_delete", methods=['GET', 'POST'])
def gpumanufacturer_delete_wtf():
    data_gpu_attribue_gpumanufacturer_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_gpu_manufacturer"
    id_gpu_manufacturer_delete = request.values['id_gpu_manufacturer_btn_delete_html']

    # Objet formulaire pour effacer le manufacturer sélectionné.
    form_delete = FormWTFDeletegpumanufacturer()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("gpumanufacturer_afficher", order_by="ASC", id_gpu_manufacturer_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "gpumanufacturer/gpumanufacturer_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_gpu_attribue_gpumanufacturer_delete = session['data_gpu_attribue_gpumanufacturer_delete']
                print("data_gpu_attribue_gpumanufacturer_delete ", data_gpu_attribue_gpumanufacturer_delete)

                flash(f"Delete permanently the manufacturer !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer manufacturer" qui va irrémédiablement EFFACER le manufacturer
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_gpu_manufacturer": id_gpu_manufacturer_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_gpu_gpumanufacturer = """DELETE FROM t_gpumanufacturer_produce_gpu WHERE fk_gpumanufacturer = %(value_id_gpu_manufacturer)s"""
                str_sql_delete_idgpumanufacturer = """DELETE FROM t_gpumanufacturer WHERE id_gpu_manufacturer = %(value_id_gpu_manufacturer)s"""
                # Manière brutale d'effacer d'abord la "fk_gpumanufacturer", même si elle n'existe pas dans la "t_gpumanufacturer_produce_gpu"
                # Ensuite on peut effacer le manufacturer vu qu'il n'est plus "lié" (INNODB) dans la "t_gpumanufacturer_produce_gpu"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_gpu_gpumanufacturer, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idgpumanufacturer, valeur_delete_dictionnaire)

                flash(f"Manufacturer permanently erased !!", "success")
                print(f"Manufacturer permanently erased !!")

                # afficher les données
                return redirect(url_for('gpumanufacturer_afficher', order_by="ASC", id_gpu_manufacturer_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_gpu_manufacturer": id_gpu_manufacturer_delete}
            print(id_gpu_manufacturer_delete, type(id_gpu_manufacturer_delete))

            # Requête qui affiche tous les gpu_gpumanufacturer qui ont le manufacturer que l'utilisateur veut effacer
            str_sql_gpumanufacturer_gpu_delete = """SELECT id_gpu, gpu_Name, id_gpu_manufacturer, gpu_Manufacturer FROM t_gpumanufacturer_produce_gpu 
                                            INNER JOIN t_gpu ON t_gpumanufacturer_produce_gpu.fk_gpu = t_gpu.id_gpu
                                            INNER JOIN t_gpumanufacturer ON t_gpumanufacturer_produce_gpu.fk_gpumanufacturer = t_gpumanufacturer.id_gpu_manufacturer
                                            WHERE fk_gpumanufacturer = %(value_id_gpu_manufacturer)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_gpumanufacturer_gpu_delete, valeur_select_dictionnaire)
                data_gpu_attribue_gpumanufacturer_delete = mydb_conn.fetchall()
                print("data_gpu_attribue_gpumanufacturer_delete...", data_gpu_attribue_gpumanufacturer_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "gpumanufacturer/gpumanufacturer_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_gpu_attribue_gpumanufacturer_delete'] = data_gpu_attribue_gpumanufacturer_delete

                # Opération sur la BD pour récupérer "id_gpu_manufacturer" et "gpu_Manufacturer" de la "t_gpumanufacturer"
                str_sql_id_gpu_manufacturer = "SELECT id_gpu_manufacturer, gpu_Manufacturer FROM t_gpumanufacturer WHERE id_gpu_manufacturer = %(value_id_gpu_manufacturer)s"

                mydb_conn.execute(str_sql_id_gpu_manufacturer, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom manufacturer" pour l'action DELETE
                data_nom_gpumanufacturer = mydb_conn.fetchone()
                print("data_nom_gpumanufacturer ", data_nom_gpumanufacturer, " type ", type(data_nom_gpumanufacturer), " manufacturer ",
                      data_nom_gpumanufacturer["gpu_Manufacturer"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "gpumanufacturer_delete_wtf.html"
            form_delete.nom_gpumanufacturer_delete_wtf.data = data_nom_gpumanufacturer["gpu_Manufacturer"]

            # Le bouton pour l'action "DELETE" dans le form. "gpumanufacturer_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_gpumanufacturer_delete_wtf:
        raise ExceptiongpumanufacturerDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{gpumanufacturer_delete_wtf.__name__} ; "
                                      f"{Exception_gpumanufacturer_delete_wtf}")

    return render_template("gpumanufacturer/gpumanufacturer_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_gpu_associes=data_gpu_attribue_gpumanufacturer_delete)
