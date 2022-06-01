"""Gestion des "routes" FLASK et des données pour les ram.
Fichier : gestion_ram_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_PCPART.database.database_tools import DBconnection
from APP_PCPART.erreurs.exceptions import *
from APP_PCPART.ram.gestion_ram_wtf_forms import *

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /ram_afficher
    
    Test : ex : http://127.0.0.1:5005/ram_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_ram_sel = 0 >> tous les ram.
                id_ram_sel = "n" affiche la ram dont l'id est "n"
"""


@app.route("/ram_afficher/<string:order_by>/<int:id_ram_sel>", methods=['GET', 'POST'])
def ram_afficher(order_by, id_ram_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_ram_sel == 0:
                    strsql_ram_afficher = """SELECT id_ram, ram_brand, ram_name, ram_capacity, ram_timings FROM t_ram ORDER BY id_ram ASC"""
                    mc_afficher.execute(strsql_ram_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_ram"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id de la ram sélectionné avec un nom de variable
                    valeur_id_ram_selected_dictionnaire = {"value_id_ram_selected": id_ram_sel}
                    strsql_ram_afficher = """SELECT id_ram, ram_brand, ram_name, ram_capacity, ram_timings FROM t_ram WHERE id_ram = %(value_id_ram_selected)s"""

                    mc_afficher.execute(strsql_ram_afficher, valeur_id_ram_selected_dictionnaire)
                else:
                    strsql_ram_afficher = """SELECT id_ram, ram_brand, ram_name, ram_capacity, ram_timings FROM t_ram ORDER BY id_ram DESC"""

                    mc_afficher.execute(strsql_ram_afficher)

                data_ram = mc_afficher.fetchall()

                print("data_ram ", data_ram, " Type : ", type(data_ram))

                # Différencier les messages si la table is empty
                if not data_ram and id_ram_sel == 0:
                    flash("""Table "t_ram" is empty !!""", "warning")
                elif not data_ram and id_ram_sel > 0:
                    # Si l'utilisateur change l'id_ram dans l'URL et que la ram n'existe pas,
                    flash(f"La ram demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_ram" is empty
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Data ram shown !!", "success")

        except Exception as Exception_ram_afficher:
            raise ExceptionRamAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{ram_afficher.__name__} ; "
                                          f"{Exception_ram_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("ram/ram_afficher.html", data=data_ram)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /ram_ajouter
    
    Test : ex : http://127.0.0.1:5005/ram_ajouter
    
    Paramètres : sans
    
    But : Ajouter une brand pour une ram
    
    Remarque :  Dans le champ "brand_ram_html" du formulaire "ram/ram_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/ram_ajouter", methods=['GET', 'POST'])
def ram_ajouter_wtf():
    form = FormWTFAjouterRam()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                brand_ram = form.brand_ram_wtf.data
                name_ram = form.name_ram_wtf.data
                capacity_ram = form.capacity_ram_wtf.data
                timings_ram = form.timings_ram_wtf.data
                valeurs_insertion_dictionnaire = {"value_ram_brand": brand_ram,
                                                  "value_ram_name": name_ram,
                                                  "value_ram_capacity": capacity_ram,
                                                  "value_ram_timings": timings_ram
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_ram = """INSERT INTO t_ram (id_ram,ram_brand,ram_name,ram_capacity,ram_timings) VALUES (NULL,%(value_ram_brand)s,%(value_ram_name)s,%(value_ram_capacity)s,%(value_ram_timings)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_ram, valeurs_insertion_dictionnaire)

                flash(f"Data inserted !!", "success")
                print(f"Data inserted !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('ram_afficher', order_by='DESC', id_ram_sel=0))

        except Exception as Exception_ram_ajouter_wtf:
            raise ExceptionRamAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                         f"{ram_ajouter_wtf.__name__} ; "
                                         f"{Exception_ram_ajouter_wtf}")

    return render_template("ram/ram_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /ram_update
    
    Test : ex cliquer sur le menu "ram" puis cliquer sur le bouton "EDIT" d'un "ram"
    
    Paramètres : sans
    
    But : Editer(update) un ram qui a été sélectionné dans le formulaire "ram_afficher.html"
    
    Remarque :  Dans le champ "brand_ram_update_wtf" du formulaire "ram/ram_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/ram_update", methods=['GET', 'POST'])
def ram_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_ram"
    id_ram_update = request.values['id_ram_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateRam()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "ram_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            ram_brand_update = form_update.brand_ram_update_wtf.data
            name_ram_update = form_update.name_ram_update_wtf.data
            capacity_ram_update = form_update.capacity_ram_update_wtf.data
            timings_ram_update = form_update.timings_ram_update_wtf.data

            valeur_update_dictionnaire = {"value_id_ram": id_ram_update,
                                          "value_ram_brand": ram_brand_update,
                                          "value_ram_name": name_ram_update,
                                          "value_ram_capacity": capacity_ram_update,
                                          "value_ram_timings": timings_ram_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_ram_brand = """UPDATE t_ram SET ram_brand = %(value_ram_brand)s, 
            ram_name = %(value_ram_name)s, ram_capacity = %(value_ram_capacity)s, ram_timings = %(value_ram_timings)s WHERE id_ram = %(value_id_ram)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_ram_brand, valeur_update_dictionnaire)

            flash(f"Data updated !!", "success")
            print(f"Data updated !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_ram_update"
            return redirect(url_for('ram_afficher', order_by="ASC", id_ram_sel=id_ram_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_ram" et "ram_brand" de la "t_ram"
            str_sql_id_ram = "SELECT id_ram, ram_brand, ram_name, ram_capacity, ram_timings FROM t_ram " \
                               "WHERE id_ram = %(value_id_ram)s"

            valeur_select_dictionnaire = {"value_id_ram": id_ram_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_ram, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom ram" pour l'UPDATE
            data_nom_ram = mybd_conn.fetchone()
            print("data_nom_ram ", data_nom_ram, " type ", type(data_nom_ram), " ram_brand ",
                  data_nom_ram["ram_brand"])

            # Show la valeur sélectionnée dans les champs du formulaire "ram_update_wtf.html"
            form_update.brand_ram_update_wtf.data = data_nom_ram["ram_brand"]
            form_update.name_ram_update_wtf.data = data_nom_ram["ram_name"]
            form_update.capacity_ram_update_wtf.data = data_nom_ram["ram_capacity"]
            form_update.timings_ram_update_wtf.data = data_nom_ram["ram_timings"]

    except Exception as Exception_ram_update_wtf:
        raise ExceptionRamUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                    f"{ram_update_wtf.__name__} ; "
                                    f"{Exception_ram_update_wtf}")

    return render_template("ram/ram_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /ram_delete
    
    Test : ex. cliquer sur le menu "ram" puis cliquer sur le bouton "DELETE" d'un "ram"
    
    Paramètres : sans
    
    But : Effacer(delete) une ram qui a été sélectionnée dans le formulaire "ram_afficher.html"
    
    Remarque :  Dans le champ "brand_ram_delete_wtf" du formulaire "ram/ram_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/ram_delete", methods=['GET', 'POST'])
def ram_delete_wtf():
    data_ramgen_attribue_ram_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_ram"
    id_ram_delete = request.values['id_ram_btn_delete_html']

    # Objet formulaire pour effacer la ram sélectionné.
    form_delete = FormWTFDeleteRam()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("ram_afficher", order_by="ASC", id_ram_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "ram/ram_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_ramgen_attribue_ram_delete = session['data_ramgen_attribue_ram_delete']
                print("data_ramgen_attribue_ram_delete ", data_ramgen_attribue_ram_delete)

                flash(f"Permanently delete the ram kit!!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer ram" qui va irrémédiablement EFFACER le ram
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_ram": id_ram_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_ramgen_ram = """DELETE FROM t_ram_is_ramgen WHERE fk_ram = %(value_id_ram)s"""
                str_sql_delete_idram = """DELETE FROM t_ram WHERE id_ram = %(value_id_ram)s"""
                # Manière brutale d'effacer d'abord la "fk_ram", même si elle n'existe pas dans la "t_ram_is_ramgen"
                # Ensuite on peut effacer la ram vu qu'il n'est plus "lié" (INNODB) dans la "t_ram_is_ramgen"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_ramgen_ram, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idram, valeur_delete_dictionnaire)

                flash(f"Ram permanently erased !!", "success")
                print(f"Ram permanently erased !!")

                # afficher les données
                return redirect(url_for('ram_afficher', order_by="ASC", id_ram_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_ram": id_ram_delete}
            print(id_ram_delete, type(id_ram_delete))

            # Requête qui affiche tous les ram_is_ramgen qui ont la ram que l'utilisateur veut effacer
            str_sql_ram_ramgen_delete = """SELECT id_ramgen, ram_generation, id_ram, ram_brand, ram_name, ram_capacity, ram_timings FROM t_ram_is_ramgen 
                                            INNER JOIN t_ramgen ON t_ram_is_ramgen.fk_ramgen = t_ramgen.id_ramgen
                                            INNER JOIN t_ram ON t_ram_is_ramgen.fk_ram = t_ram.id_ram
                                            WHERE fk_ram = %(value_id_ram)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_ram_ramgen_delete, valeur_select_dictionnaire)
                data_ramgen_attribue_ram_delete = mydb_conn.fetchall()
                print("data_ramgen_attribue_ram_delete...", data_ramgen_attribue_ram_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "ram/ram_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_ramgen_attribue_ram_delete'] = data_ramgen_attribue_ram_delete

                # Opération sur la BD pour récupérer "id_ram" et "ram_brand" de la "t_ram"
                str_sql_id_ram = "SELECT id_ram, ram_brand, ram_name, ram_capacity, ram_timings FROM t_ram WHERE id_ram = %(value_id_ram)s"

                mydb_conn.execute(str_sql_id_ram, valeur_select_dictionnaire)
                data_nom_ram = mydb_conn.fetchone()
                print("data_nom_ram ", data_nom_ram, " type ", type(data_nom_ram), " ram ",
                      data_nom_ram["ram_brand"])

                mydb_conn.execute(str_sql_id_ram, valeur_select_dictionnaire)
                data_nom_ram = mydb_conn.fetchone()
                print("data_nom_ram ", data_nom_ram, " type ", type(data_nom_ram), " ram ",
                      data_nom_ram["ram_name"])

            # Show la valeur sélectionnée dans le champ du formulaire "ram_delete_wtf.html"
            form_delete.brand_ram_delete_wtf.data = data_nom_ram["ram_brand"]
            form_delete.name_ram_delete_wtf.data = data_nom_ram["ram_name"]

            # Le bouton pour l'action "DELETE" dans le form. "ram_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_ram_delete_wtf:
        raise ExceptionRamDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                    f"{ram_delete_wtf.__name__} ; "
                                    f"{Exception_ram_delete_wtf}")

    return render_template("ram/ram_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_ramgen_associes=data_ramgen_attribue_ram_delete)
