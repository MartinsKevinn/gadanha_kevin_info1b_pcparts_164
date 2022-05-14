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
from APP_PCPART.motherboard.gestion_motherboard_wtf_forms import FormWTFAjouterMotherboard
from APP_PCPART.motherboard.gestion_motherboard_wtf_forms import FormWTFDeleteMotherboard
from APP_PCPART.motherboard.gestion_motherboard_wtf_forms import FormWTFUpdateMotherboard

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /motherboard_afficher
    
    Test : ex : http://127.0.0.1:5005/motherboard_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_motherboard_sel = 0 >> tous les motherboard.
                id_motherboard_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/motherboard_afficher/<string:order_by>/<int:id_motherboard_sel>", methods=['GET', 'POST'])
def motherboard_afficher(order_by, id_motherboard_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_motherboard_sel == 0:
                    strsql_motherboard_afficher = """SELECT id_motherboard, motherboard_brand, motherboard_model FROM t_motherboard ORDER BY id_motherboard ASC"""
                    mc_afficher.execute(strsql_motherboard_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_motherboard"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_motherboard_selected_dictionnaire = {"value_id_motherboard_selected": id_motherboard_sel}
                    strsql_motherboard_afficher = """SELECT id_motherboard, motherboard_brand, motherboard_model FROM t_motherboard WHERE id_motherboard = %(value_id_motherboard_selected)s"""

                    mc_afficher.execute(strsql_motherboard_afficher, valeur_id_motherboard_selected_dictionnaire)
                else:
                    strsql_motherboard_afficher = """SELECT id_motherboard, motherboard_brand, motherboard_model FROM t_motherboard ORDER BY id_motherboard DESC"""

                    mc_afficher.execute(strsql_motherboard_afficher)

                data_motherboard = mc_afficher.fetchall()

                print("data_motherboard ", data_motherboard, " Type : ", type(data_motherboard))

                # Différencier les messages si la table est vide.
                if not data_motherboard and id_motherboard_sel == 0:
                    flash("""La table "t_motherboard" est vide. !!""", "warning")
                elif not data_motherboard and id_motherboard_sel > 0:
                    # Si l'utilisateur change l'id_motherboard dans l'URL et que le genre n'existe pas,
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_motherboard" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données motherboard affichés !!", "success")

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
    
    But : Ajouter un genre pour une motherboard
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "motherboard/motherboard_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/motherboard_ajouter", methods=['GET', 'POST'])
def motherboard_ajouter_wtf():
    form = FormWTFAjouterMotherboard()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_motherboard_wtf = form.nom_motherboard_wtf.data
                name_motherboard = name_motherboard_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_motherboard_brand": name_motherboard}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_motherboard = """INSERT INTO t_motherboard (id_motherboard,motherboard_brand) VALUES (NULL,%(value_motherboard_brand)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_motherboard, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('motherboard_afficher', order_by='DESC', id_motherboard_sel=0))

        except Exception as Exception_motherboard_ajouter_wtf:
            raise ExceptionMotherboardAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{motherboard_ajouter_wtf.__name__} ; "
                                            f"{Exception_motherboard_ajouter_wtf}")

    return render_template("motherboard/motherboard_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "motherboard" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "motherboard_afficher.html"
    
    Remarque :  Dans le champ "nom_motherboard_update_wtf" du formulaire "motherboard/motherboard_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genre_update", methods=['GET', 'POST'])
def motherboard_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_motherboard"
    id_genre_update = request.values['id_genre_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateMotherboard()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "motherboard_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_genre_update = form_update.nom_motherboard_update_wtf.data
            name_genre_update = name_genre_update.lower()
            date_genre_essai = form_update.date_motherboard_wtf_essai.data

            valeur_update_dictionnaire = {"value_id_genre": id_genre_update,
                                          "value_name_genre": name_genre_update,
                                          "value_date_genre_essai": date_genre_essai
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulegenre = """UPDATE t_motherboard SET motherboard_brand = %(value_name_genre)s, 
            motherboard_model = %(value_date_genre_essai)s WHERE id_motherboard = %(value_id_genre)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('motherboard_afficher', order_by="ASC", id_motherboard_sel=id_genre_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_motherboard" et "motherboard_brand" de la "t_motherboard"
            str_sql_id_motherboard = "SELECT id_motherboard, motherboard_brand, motherboard_model FROM t_motherboard " \
                               "WHERE id_motherboard = %(value_id_genre)s"
            valeur_select_dictionnaire = {"value_id_genre": id_genre_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_motherboard, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_motherboard = mybd_conn.fetchone()
            print("data_nom_motherboard ", data_nom_motherboard, " type ", type(data_nom_motherboard), " genre ",
                  data_nom_motherboard["motherboard_brand"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "motherboard_update_wtf.html"
            form_update.nom_motherboard_update_wtf.data = data_nom_motherboard["motherboard_brand"]
            form_update.date_motherboard_wtf_essai.data = data_nom_motherboard["motherboard_model"]

    except Exception as Exception_genre_update_wtf:
        raise ExceptionMotherboardUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{motherboard_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    return render_template("motherboard/motherboard_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "motherboard" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "motherboard_afficher.html"
    
    Remarque :  Dans le champ "nom_motherboard_delete_wtf" du formulaire "motherboard/motherboard_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/genre_delete", methods=['GET', 'POST'])
def motherboard_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_motherboard"
    id_genre_delete = request.values['id_genre_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeleteMotherboard()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("motherboard_afficher", order_by="ASC", id_motherboard_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "motherboard/motherboard_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
                print("data_films_attribue_genre_delete ", data_films_attribue_genre_delete)

                flash(f"Effacer le genre de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_genre = """DELETE FROM t_cpu_compatible_motherboard WHERE fk_motherboard = %(value_id_genre)s"""
                str_sql_delete_idgenre = """DELETE FROM t_motherboard WHERE id_motherboard = %(value_id_genre)s"""
                # Manière brutale d'effacer d'abord la "fk_motherboard", même si elle n'existe pas dans la "t_cpu_compatible_motherboard"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_cpu_compatible_motherboard"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_genre, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idgenre, valeur_delete_dictionnaire)

                flash(f"Genre définitivement effacé !!", "success")
                print(f"Genre définitivement effacé !!")

                # afficher les données
                return redirect(url_for('motherboard_afficher', order_by="ASC", id_motherboard_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_genre": id_genre_delete}
            print(id_genre_delete, type(id_genre_delete))

            # Requête qui affiche tous les cpu_motherboard qui ont le genre que l'utilisateur veut effacer
            str_sql_genres_films_delete = """SELECT id_cpu_compatible_motherboard, CPU_Name, id_motherboard, motherboard_brand FROM t_cpu_compatible_motherboard 
                                            INNER JOIN t_cpu ON t_cpu_compatible_motherboard.fk_cpu = t_cpu.id_cpu
                                            INNER JOIN t_motherboard ON t_cpu_compatible_motherboard.fk_motherboard = t_motherboard.id_motherboard
                                            WHERE fk_motherboard = %(value_id_genre)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_films_attribue_genre_delete = mydb_conn.fetchall()
                print("data_films_attribue_genre_delete...", data_films_attribue_genre_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "motherboard/motherboard_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

                # Opération sur la BD pour récupérer "id_motherboard" et "motherboard_brand" de la "t_motherboard"
                str_sql_id_motherboard = "SELECT id_motherboard, motherboard_brand FROM t_motherboard WHERE id_motherboard = %(value_id_genre)s"

                mydb_conn.execute(str_sql_id_motherboard, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_motherboard = mydb_conn.fetchone()
                print("data_nom_motherboard ", data_nom_motherboard, " type ", type(data_nom_motherboard), " genre ",
                      data_nom_motherboard["motherboard_brand"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "motherboard_delete_wtf.html"
            form_delete.nom_motherboard_delete_wtf.data = data_nom_motherboard["motherboard_brand"]

            # Le bouton pour l'action "DELETE" dans le form. "motherboard_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_motherboard_delete_wtf:
        raise ExceptionMotherboardDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{motherboard_delete_wtf.__name__} ; "
                                      f"{Exception_motherboard_delete_wtf}")

    return render_template("motherboard/motherboard_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_genre_delete)
