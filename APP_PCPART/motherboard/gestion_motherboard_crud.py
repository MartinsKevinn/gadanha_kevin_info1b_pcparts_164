"""Gestion des "routes" FLASK et des données pour les motherboard.
Fichier : gestion_motherboard_crud.py
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
from APP_PCPART.motherboard.gestion_motherboard_wtf_forms import *

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /motherboard_afficher
    
    Test : ex : http://127.0.0.1:5005/motherboard_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_motherboard_sel = 0 >> tous les motherboard.
                id_motherboard_sel = "n" affiche la motherboard dont l'id est "n"
"""


@app.route("/motherboard_afficher/<string:order_by>/<int:id_motherboard_sel>", methods=['GET', 'POST'])
def motherboard_afficher(order_by, id_motherboard_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_motherboard_sel == 0:
                    strsql_motherboard_afficher = """SELECT id_motherboard, motherboard_brand, motherboard_model, motherboard_release_year FROM t_motherboard ORDER BY id_motherboard ASC"""
                    mc_afficher.execute(strsql_motherboard_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_motherboard"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id de la motherboard sélectionné avec un nom de variable
                    valeur_id_motherboard_selected_dictionnaire = {"value_id_motherboard_selected": id_motherboard_sel}
                    strsql_motherboard_afficher = """SELECT id_motherboard, motherboard_brand, motherboard_model, motherboard_release_year FROM t_motherboard WHERE id_motherboard = %(value_id_motherboard_selected)s"""

                    mc_afficher.execute(strsql_motherboard_afficher, valeur_id_motherboard_selected_dictionnaire)
                else:
                    strsql_motherboard_afficher = """SELECT id_motherboard, motherboard_brand, motherboard_model, motherboard_release_year FROM t_motherboard ORDER BY id_motherboard DESC"""

                    mc_afficher.execute(strsql_motherboard_afficher)

                data_motherboard = mc_afficher.fetchall()

                print("data_motherboard ", data_motherboard, " Type : ", type(data_motherboard))

                # Différencier les messages si la table is empty
                if not data_motherboard and id_motherboard_sel == 0:
                    flash("""Table "t_motherboard" is empty !!""", "warning")
                elif not data_motherboard and id_motherboard_sel > 0:
                    # Si l'utilisateur change l'id_motherboard dans l'URL et que la motherboard n'existe pas,
                    flash(f"The requested motherboard does not exist !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_motherboard" is empty
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Data motherboard shown !!", "success")

        except Exception as Exception_motherboard_afficher:
            raise ExceptionMotherboardAfficher(f"fichier : {Path(__file__).name}  ;  "
                                               f"{motherboard_afficher.__name__} ; "
                                               f"{Exception_motherboard_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("motherboard/motherboard_afficher.html", data=data_motherboard)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /motherboard_ajouter
    
    Test : ex : http://127.0.0.1:5005/motherboard_ajouter
    
    Paramètres : sans
    
    But : Ajouter une brand pour une motherboard
    
    Remarque :  Dans le champ "name_motherboard_html" du formulaire "motherboard/motherboard_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/motherboard_ajouter", methods=['GET', 'POST'])
def motherboard_ajouter_wtf():
    form_add_motherboard = FormWTFAjouterMotherboard()
    if request.method == "POST":
        try:
            if form_add_motherboard.validate_on_submit():
                name_motherboard = form_add_motherboard.nom_motherboard_wtf.data
                model_motherboard = form_add_motherboard.model_motherboard_wtf.data
                release_year_motherboard = form_add_motherboard.release_year_motherboard_wtf.data
                valeurs_insertion_dictionnaire = {"value_motherboard_brand": name_motherboard,
                                                  "value_motherboard_model": model_motherboard,
                                                  "value_motherboard_release": release_year_motherboard
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_motherboard = """INSERT INTO t_motherboard (id_motherboard,motherboard_brand,motherboard_model,motherboard_release_year) VALUES (NULL,%(value_motherboard_brand)s,%(value_motherboard_model)s,%(value_motherboard_release)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_motherboard, valeurs_insertion_dictionnaire)

                flash(f"Data inserted !!", "success")
                print(f"Data inserted !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('motherboard_afficher', order_by='DESC', id_motherboard_sel=0))

        except Exception as Exception_motherboard_ajouter_wtf:
            raise ExceptionMotherboardAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                                 f"{motherboard_ajouter_wtf.__name__} ; "
                                                 f"{Exception_motherboard_ajouter_wtf}")

    return render_template("motherboard/motherboard_ajouter_wtf.html", form_add_motherboard=form_add_motherboard)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /motherboard_update
    
    Test : ex cliquer sur le menu "motherboard" puis cliquer sur le bouton "EDIT" d'un "motherboard"
    
    Paramètres : sans
    
    But : Editer(update) un motherboard qui a été sélectionné dans le formulaire "motherboard_afficher.html"
    
    Remarque :  Dans le champ "nom_motherboard_update_wtf" du formulaire "motherboard/motherboard_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/motherboard_update", methods=['GET', 'POST'])
def motherboard_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_motherboard"
    id_motherboard_update = request.values['id_motherboard_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateMotherboard()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "motherboard_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            motherboard_brand_update = form_update.nom_motherboard_update_wtf.data
            model_motherboard_update = form_update.model_motherboard_update_wtf.data
            release_year_motherboard_update = form_update.release_year_motherboard_update_wtf.data

            valeur_update_dictionnaire = {"value_id_motherboard": id_motherboard_update,
                                          "value_motherboard_brand": motherboard_brand_update,
                                          "value_motherboard_model": model_motherboard_update,
                                          "value_motherboard_release_year": release_year_motherboard_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_motherboard_brand = """UPDATE t_motherboard SET motherboard_brand = %(value_motherboard_brand)s, 
            motherboard_model = %(value_motherboard_model)s, motherboard_release_year = %(value_motherboard_release_year)s WHERE id_motherboard = %(value_id_motherboard)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_motherboard_brand, valeur_update_dictionnaire)

            flash(f"Data updated !!", "success")
            print(f"Data updated !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_motherboard_update"
            return redirect(url_for('motherboard_afficher', order_by="ASC", id_motherboard_sel=id_motherboard_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_motherboard" et "motherboard_brand" de la "t_motherboard"
            str_sql_id_motherboard = "SELECT id_motherboard, motherboard_brand, motherboard_model, motherboard_release_year FROM t_motherboard " \
                                     "WHERE id_motherboard = %(value_id_motherboard)s"

            valeur_select_dictionnaire = {"value_id_motherboard": id_motherboard_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_motherboard, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom motherboard" pour l'UPDATE
            data_nom_motherboard = mybd_conn.fetchone()
            print("data_nom_motherboard ", data_nom_motherboard, " type ", type(data_nom_motherboard),
                  " motherboard_brand ",
                  data_nom_motherboard["motherboard_brand"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "motherboard_update_wtf.html"
            form_update.nom_motherboard_update_wtf.data = data_nom_motherboard["motherboard_brand"]
            form_update.model_motherboard_update_wtf.data = data_nom_motherboard["motherboard_model"]
            form_update.release_year_motherboard_update_wtf.data = data_nom_motherboard["motherboard_release_year"]

    except Exception as Exception_motherboard_update_wtf:
        raise ExceptionMotherboardUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{motherboard_update_wtf.__name__} ; "
                                            f"{Exception_motherboard_update_wtf}")

    return render_template("motherboard/motherboard_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /motherboard_delete
    
    Test : ex. cliquer sur le menu "motherboard" puis cliquer sur le bouton "DELETE" d'un "motherboard"
    
    Paramètres : sans
    
    But : Effacer(delete) une motherboard qui a été sélectionnée dans le formulaire "motherboard_afficher.html"
    
    Remarque :  Dans le champ "nom_motherboard_delete_wtf" du formulaire "motherboard/motherboard_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/motherboard_delete", methods=['GET', 'POST'])
def motherboard_delete_wtf():
    data_cpu_attribue_motherboard_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_motherboard"
    id_motherboard_delete = request.values['id_motherboard_btn_delete_html']

    # Objet formulaire pour effacer la motherboard sélectionné.
    form_delete = FormWTFDeleteMotherboard()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("motherboard_afficher", order_by="ASC", id_motherboard_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "motherboard/motherboard_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_cpu_attribue_motherboard_delete = session['data_cpu_attribue_motherboard_delete']
                print("data_cpu_attribue_motherboard_delete ", data_cpu_attribue_motherboard_delete)

                flash(f"Permanently delete the motherboard!!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer motherboard" qui va irrémédiablement EFFACER le motherboard
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_motherboard": id_motherboard_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_cpu_motherboard = """DELETE FROM t_cpu_compatible_motherboard WHERE fk_motherboard = %(value_id_motherboard)s"""
                str_sql_delete_idmotherboard = """DELETE FROM t_motherboard WHERE id_motherboard = %(value_id_motherboard)s"""
                # Manière brutale d'effacer d'abord la "fk_motherboard", même si elle n'existe pas dans la "t_cpu_compatible_motherboard"
                # Ensuite on peut effacer la motherboard vu qu'il n'est plus "lié" (INNODB) dans la "t_cpu_compatible_motherboard"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_cpu_motherboard, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idmotherboard, valeur_delete_dictionnaire)

                flash(f"Motherboard permanently erased !!", "success")
                print(f"Motherboard permanently erased !!")

                # afficher les données
                return redirect(url_for('motherboard_afficher', order_by="ASC", id_motherboard_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_motherboard": id_motherboard_delete}
            print(id_motherboard_delete, type(id_motherboard_delete))

            # Requête qui affiche tous les cpu_motherboard qui ont la motherboard que l'utilisateur veut effacer
            str_sql_motherboard_cpu_delete = """SELECT id_cpu, CPU_Name, CPU_Codename, id_motherboard, motherboard_brand, motherboard_model FROM t_cpu_compatible_motherboard 
                                            INNER JOIN t_cpu ON t_cpu_compatible_motherboard.fk_cpu = t_cpu.id_cpu
                                            INNER JOIN t_motherboard ON t_cpu_compatible_motherboard.fk_motherboard = t_motherboard.id_motherboard
                                            WHERE fk_motherboard = %(value_id_motherboard)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_motherboard_cpu_delete, valeur_select_dictionnaire)
                data_cpu_attribue_motherboard_delete = mydb_conn.fetchall()
                print("data_cpu_attribue_motherboard_delete...", data_cpu_attribue_motherboard_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "motherboard/motherboard_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_cpu_attribue_motherboard_delete'] = data_cpu_attribue_motherboard_delete

                # Opération sur la BD pour récupérer "id_motherboard" et "motherboard_brand" de la "t_motherboard"
                str_sql_id_motherboard = "SELECT id_motherboard, motherboard_brand, motherboard_model FROM t_motherboard WHERE id_motherboard = %(value_id_motherboard)s"

                mydb_conn.execute(str_sql_id_motherboard, valeur_select_dictionnaire)
                data_nom_motherboard = mydb_conn.fetchone()
                print("data_nom_motherboard ", data_nom_motherboard, " type ", type(data_nom_motherboard),
                      " motherboard ",
                      data_nom_motherboard["motherboard_brand"])

                mydb_conn.execute(str_sql_id_motherboard, valeur_select_dictionnaire)
                data_nom_motherboard = mydb_conn.fetchone()
                print("data_nom_motherboard ", data_nom_motherboard, " type ", type(data_nom_motherboard),
                      " motherboard ",
                      data_nom_motherboard["motherboard_model"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "motherboard_delete_wtf.html"
            form_delete.nom_motherboard_delete_wtf.data = data_nom_motherboard["motherboard_brand"]
            form_delete.model_motherboard_delete_wtf.data = data_nom_motherboard["motherboard_model"]

            # Le bouton pour l'action "DELETE" dans le form. "motherboard_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_motherboard_delete_wtf:
        raise ExceptionMotherboardDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{motherboard_delete_wtf.__name__} ; "
                                            f"{Exception_motherboard_delete_wtf}")

    return render_template("motherboard/motherboard_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_cpu_associes=data_cpu_attribue_motherboard_delete)
