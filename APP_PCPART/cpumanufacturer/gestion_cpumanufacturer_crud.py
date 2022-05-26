"""Gestion des "routes" FLASK et des données pour les cpumanufacturer.
Fichier : gestion_cpumanufacturer_crud.py
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
from APP_PCPART.cpumanufacturer.gestion_cpumanufacturer_wtf_forms import *

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /cpumanufacturer_afficher
    
    Test : ex : http://127.0.0.1:5005/cpumanufacturer_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_cpu_manufacturer_sel = 0 >> tous les cpumanufacturer.
                id_cpu_manufacturer_sel = "n" affiche le manufacturer dont l'id est "n"
"""


@app.route("/cpumanufacturer_afficher/<string:order_by>/<int:id_cpu_manufacturer_sel>", methods=['GET', 'POST'])
def cpumanufacturer_afficher(order_by, id_cpu_manufacturer_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_cpu_manufacturer_sel == 0:
                    strsql_id_cpu_manufacturer_afficher = """SELECT id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer ORDER BY id_cpu_manufacturer ASC"""
                    mc_afficher.execute(strsql_id_cpu_manufacturer_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_cpumanufacturer"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du manufacturer sélectionné avec un nom de variable
                    valeur_id_cpu_manufacturer_selected_dictionnaire = {
                        "value_id_cpu_manufacturer_selected": id_cpu_manufacturer_sel}
                    strsql_id_cpu_manufacturer_afficher = """SELECT id_cpu_manufacturer, CPU_Manufacturer  FROM t_cpumanufacturer WHERE id_cpu_manufacturer = %(value_id_cpu_manufacturer_selected)s"""

                    mc_afficher.execute(strsql_id_cpu_manufacturer_afficher,
                                        valeur_id_cpu_manufacturer_selected_dictionnaire)
                else:
                    strsql_id_cpu_manufacturer_afficher = """SELECT id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer ORDER BY id_cpu_manufacturer DESC"""

                    mc_afficher.execute(strsql_id_cpu_manufacturer_afficher)

                data_cpumanufacturer = mc_afficher.fetchall()

                print("data_cpumanufacturer ", data_cpumanufacturer, " Type : ", type(data_cpumanufacturer))

                # Différencier les messages si la table est vide.
                if not data_cpumanufacturer and id_cpu_manufacturer_sel == 0:
                    flash("""La table "t_cpumanufacturer" est vide. !!""", "warning")
                elif not data_cpumanufacturer and id_cpu_manufacturer_sel > 0:
                    # Si l'utilisateur change l'id_cpu_manufacturer dans l'URL et que le manufacturer n'existe pas,
                    flash(f"Le manufacturer demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_cpumanufacturer" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Data CPU Manufacturers shown !!", "success")

        except Exception as Exception_cpumanufacturer_afficher:
            raise ExceptionCpumanufacturerAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{cpumanufacturer_afficher.__name__} ; "
                                          f"{Exception_cpumanufacturer_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("cpumanufacturer/cpumanufacturer_afficher.html", data=data_cpumanufacturer)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /cpumanufacturer_ajouter
    
    Test : ex : http://127.0.0.1:5005/cpumanufacturer_ajouter
    
    Paramètres : sans
    
    But : Ajouter un manufacturer pour un cpu
    
    Remarque :  Dans le champ "name_cpumanufacturer_html" du formulaire "cpumanufacturer/cpumanufacturer_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/cpumanufacturer_ajouter", methods=['GET', 'POST'])
def cpumanufacturer_ajouter_wtf():
    form = FormWTFAjouterCpumanufacturer()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_cpumanufacturer = form.nom_cpumanufacturer_wtf.data
                valeurs_insertion_dictionnaire = {"value_CPU_Manufacturer": name_cpumanufacturer}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_cpumanufacturer = """INSERT INTO t_cpumanufacturer (id_cpu_manufacturer,CPU_Manufacturer) VALUES (NULL,%(value_CPU_Manufacturer)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_cpumanufacturer, valeurs_insertion_dictionnaire)

                flash(f"Data inserted !!", "success")
                print(f"Data inserted !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('cpumanufacturer_afficher', order_by='DESC', id_cpu_manufacturer_sel=0))

        except Exception as Exception_cpumanufacturer_ajouter_wtf:
            raise ExceptionCpumanufacturerAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                                     f"{cpumanufacturer_ajouter_wtf.__name__} ; "
                                                     f"{Exception_cpumanufacturer_ajouter_wtf}")

    return render_template("cpumanufacturer/cpumanufacturer_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /cpumanufacturer_update
    
    Test : ex cliquer sur le menu "cpumanufacturer" puis cliquer sur le bouton "EDIT" d'un "manufacturer"
    
    Paramètres : sans
    
    But : Editer(update) un manufacturer qui a été sélectionné dans le formulaire "cpumanufacturer_afficher.html"
    
    Remarque :  Dans le champ "nom_cpumanufacturer_update_wtf" du formulaire "cpumanufacturer/cpumanufacturer_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/cpumanufacturer_update", methods=['GET', 'POST'])
def cpumanufacturer_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_cpu_manufacturer"
    id_cpu_manufacturer_update = request.values['id_cpu_manufacturer_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateCpumanufacturer()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "cpumanufacturer_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_cpumanufacturer_update = form_update.nom_cpumanufacturer_update_wtf.data

            valeur_update_dictionnaire = {"value_id_cpu_manufacturer": id_cpu_manufacturer_update,
                                          "value_name_cpumanufacturer": name_cpumanufacturer_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_CPU_Manufacturer = """UPDATE t_cpumanufacturer SET CPU_Manufacturer = %(value_name_cpumanufacturer)s WHERE id_cpu_manufacturer = %(value_id_cpu_manufacturer)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_CPU_Manufacturer, valeur_update_dictionnaire)

            flash(f"Data updated !!", "success")
            print(f"Data updated !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_cpu_manufacturer_update"
            return redirect(
                url_for('cpumanufacturer_afficher', order_by="ASC", id_cpu_manufacturer_sel=id_cpu_manufacturer_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_cpu_manufacturer" et "CPU_Manufacturer" de la "t_cpumanufacturer"
            str_sql_id_cpu_manufacturer = "SELECT id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer " \
                               "WHERE id_cpu_manufacturer = %(value_id_cpu_manufacturer)s"
            valeur_select_dictionnaire = {"value_id_cpu_manufacturer": id_cpu_manufacturer_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_cpu_manufacturer, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom manufacturer" pour l'UPDATE
            data_nom_cpumanufacturer = mybd_conn.fetchone()
            print("data_nom_cpumanufacturer ", data_nom_cpumanufacturer, " type ", type(data_nom_cpumanufacturer), " manufacturer ",
                  data_nom_cpumanufacturer["CPU_Manufacturer"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "cpumanufacturer_update_wtf.html"
            form_update.nom_cpumanufacturer_update_wtf.data = data_nom_cpumanufacturer["CPU_Manufacturer"]

    except Exception as Exception_cpumanufacturer_update_wtf:
        raise ExceptionCpumanufacturerUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{cpumanufacturer_update_wtf.__name__} ; "
                                      f"{Exception_cpumanufacturer_update_wtf}")

    return render_template("cpumanufacturer/cpumanufacturer_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /cpumanufacturer_delete
    
    Test : ex. cliquer sur le menu "cpumanufacturer" puis cliquer sur le bouton "DELETE" d'un "manufacturer"
    
    Paramètres : sans
    
    But : Effacer(delete) un manufacturer qui a été sélectionné dans le formulaire "cpumanufacturer_afficher.html"
    
    Remarque :  Dans le champ "nom_cpumanufacturer_delete_wtf" du formulaire "cpumanufacturer/cpumanufacturer_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/cpumanufacturer_delete", methods=['GET', 'POST'])
def cpumanufacturer_delete_wtf():
    data_cpu_attribue_cpumanufacturer_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_cpu_manufacturer"
    id_cpu_manufacturer_delete = request.values['id_cpu_manufacturer_btn_delete_html']

    # Objet formulaire pour effacer le manufacturer sélectionné.
    form_delete = FormWTFDeleteCpumanufacturer()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("cpumanufacturer_afficher", order_by="ASC", id_cpu_manufacturer_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "cpumanufacturer/cpumanufacturer_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_cpu_attribue_cpumanufacturer_delete = session['data_cpu_attribue_cpumanufacturer_delete']
                print("data_cpu_attribue_cpumanufacturer_delete ", data_cpu_attribue_cpumanufacturer_delete)

                flash(f"Delete permanently the manufacturer !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer manufacturer" qui va irrémédiablement EFFACER le manufacturer
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_cpu_manufacturer": id_cpu_manufacturer_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_cpu_cpumanufacturer = """DELETE FROM t_cpumanufacturer_produce_cpu WHERE fk_cpumanufacturer = %(value_id_cpu_manufacturer)s"""
                str_sql_delete_idcpumanufacturer = """DELETE FROM t_cpumanufacturer WHERE id_cpu_manufacturer = %(value_id_cpu_manufacturer)s"""
                # Manière brutale d'effacer d'abord la "fk_cpumanufacturer", même si elle n'existe pas dans la "t_cpumanufacturer_produce_cpu"
                # Ensuite on peut effacer le manufacturer vu qu'il n'est plus "lié" (INNODB) dans la "t_cpumanufacturer_produce_cpu"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_cpu_cpumanufacturer, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idcpumanufacturer, valeur_delete_dictionnaire)

                flash(f"Manufacturer permanently erased !!", "success")
                print(f"Manufacturer permanently erased !!")

                # afficher les données
                return redirect(url_for('cpumanufacturer_afficher', order_by="ASC", id_cpu_manufacturer_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_cpu_manufacturer": id_cpu_manufacturer_delete}
            print(id_cpu_manufacturer_delete, type(id_cpu_manufacturer_delete))

            # Requête qui affiche tous les cpu_cpumanufacturer qui ont le manufacturer que l'utilisateur veut effacer
            str_sql_cpumanufacturer_cpu_delete = """SELECT id_cpu, CPU_Name, id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer_produce_cpu 
                                            INNER JOIN t_cpu ON t_cpumanufacturer_produce_cpu.fk_cpu = t_cpu.id_cpu
                                            INNER JOIN t_cpumanufacturer ON t_cpumanufacturer_produce_cpu.fk_cpumanufacturer = t_cpumanufacturer.id_cpu_manufacturer
                                            WHERE fk_cpumanufacturer = %(value_id_cpu_manufacturer)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_cpumanufacturer_cpu_delete, valeur_select_dictionnaire)
                data_cpu_attribue_cpumanufacturer_delete = mydb_conn.fetchall()
                print("data_cpu_attribue_cpumanufacturer_delete...", data_cpu_attribue_cpumanufacturer_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "cpumanufacturer/cpumanufacturer_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_cpu_attribue_cpumanufacturer_delete'] = data_cpu_attribue_cpumanufacturer_delete

                # Opération sur la BD pour récupérer "id_cpu_manufacturer" et "CPU_Manufacturer" de la "t_cpumanufacturer"
                str_sql_id_cpu_manufacturer = "SELECT id_cpu_manufacturer, CPU_Manufacturer FROM t_cpumanufacturer WHERE id_cpu_manufacturer = %(value_id_cpu_manufacturer)s"

                mydb_conn.execute(str_sql_id_cpu_manufacturer, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom manufacturer" pour l'action DELETE
                data_nom_cpumanufacturer = mydb_conn.fetchone()
                print("data_nom_cpumanufacturer ", data_nom_cpumanufacturer, " type ", type(data_nom_cpumanufacturer), " manufacturer ",
                      data_nom_cpumanufacturer["CPU_Manufacturer"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "cpumanufacturer_delete_wtf.html"
            form_delete.nom_cpumanufacturer_delete_wtf.data = data_nom_cpumanufacturer["CPU_Manufacturer"]

            # Le bouton pour l'action "DELETE" dans le form. "cpumanufacturer_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_cpumanufacturer_delete_wtf:
        raise ExceptionCpumanufacturerDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{cpumanufacturer_delete_wtf.__name__} ; "
                                      f"{Exception_cpumanufacturer_delete_wtf}")

    return render_template("cpumanufacturer/cpumanufacturer_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_cpu_associes=data_cpu_attribue_cpumanufacturer_delete)
