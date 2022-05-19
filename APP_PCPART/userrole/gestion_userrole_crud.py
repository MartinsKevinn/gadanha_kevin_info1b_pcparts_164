"""Gestion des "routes" FLASK et des données pour les userrole.
Fichier : gestion_userrole_crud.py
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
from APP_PCPART.userrole.gestion_userrole_wtf_forms import *

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /userrole_afficher
    
    Test : ex : http://127.0.0.1:5005/userrole_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_userrole_sel = 0 >> tous les userrole.
                id_userrole_sel = "n" affiche le role dont l'id est "n"
"""


@app.route("/userrole_afficher/<string:order_by>/<int:id_userrole_sel>", methods=['GET', 'POST'])
def userrole_afficher(order_by, id_userrole_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_userrole_sel == 0:
                    strsql_userrole_afficher = """SELECT id_userrole, userrole FROM t_userrole ORDER BY id_userrole ASC"""
                    mc_afficher.execute(strsql_userrole_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_userrole"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du userrole sélectionné avec un nom de variable
                    valeur_id_userrole_selected_dictionnaire = {"value_id_userrole_selected": id_userrole_sel}
                    strsql_userrole_afficher = """SELECT id_userrole, userrole FROM t_userrole WHERE id_userrole = %(value_id_userrole_selected)s"""

                    mc_afficher.execute(strsql_userrole_afficher, valeur_id_userrole_selected_dictionnaire)
                else:
                    strsql_userrole_afficher = """SELECT id_userrole, userrole FROM t_userrole ORDER BY id_userrole DESC"""

                    mc_afficher.execute(strsql_userrole_afficher)

                data_userrole = mc_afficher.fetchall()

                print("data_userrole ", data_userrole, " Type : ", type(data_userrole))

                # Différencier les messages si la table est vide.
                if not data_userrole and id_userrole_sel == 0:
                    flash("""La table "t_role" est vide. !!""", "warning")
                elif not data_userrole and id_userrole_sel > 0:
                    # Si l'utilisateur change l'id_userrole dans l'URL et que le userrole n'existe pas,
                    flash(f"Le role demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_userrole" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données roles affichés !!", "success")

        except Exception as Exception_userrole_afficher:
            raise ExceptionUserroleAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{userrole_afficher.__name__} ; "
                                          f"{Exception_userrole_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("userrole/userrole_afficher.html", data=data_userrole)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /userrole_ajouter
    
    Test : ex : http://127.0.0.1:5005/userrole_ajouter
    
    Paramètres : sans
    
    But : Ajouter un role pour un utilisateur
    
    Remarque :  Dans le champ "name_userrole_html" du formulaire "userrole/userrole_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/userrole_ajouter", methods=['GET', 'POST'])
def userrole_ajouter_wtf():
    form = FormWTFAjouterUserrole()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_userrole = form.nom_userrole_wtf.data
                valeurs_insertion_dictionnaire = {"value_userrole": name_userrole}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_userrole = """INSERT INTO t_userrole (id_userrole,userrole) VALUES (NULL,%(value_userrole)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_userrole, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('userrole_afficher', order_by='DESC', id_userrole_sel=0))

        except Exception as Exception_userrole_ajouter_wtf:
            raise ExceptionUserroleAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{userrole_ajouter_wtf.__name__} ; "
                                            f"{Exception_userrole_ajouter_wtf}")

    return render_template("userrole/userrole_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /userrole_update
    
    Test : ex cliquer sur le menu "userrole" puis cliquer sur le bouton "EDIT" d'un "userrole"
    
    Paramètres : sans
    
    But : Editer(update) un role qui a été sélectionné dans le formulaire "userrole_afficher.html"
    
    Remarque :  Dans le champ "nom_userrole_update_wtf" du formulaire "userrole/userrole_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/userrole_update", methods=['GET', 'POST'])
def userrole_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_userrole"
    id_userrole_update = request.values['id_userrole_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateUserrole()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "userrole_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_userrole_update = form_update.nom_userrole_update_wtf.data

            valeur_update_dictionnaire = {"value_id_userrole": id_userrole_update,
                                          "value_name_userrole": name_userrole_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_userrole = """UPDATE t_userrole SET userrole = %(value_name_userrole)s
                                                        WHERE id_userrole = %(value_id_userrole)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_userrole, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_userrole_update"
            return redirect(url_for('userrole_afficher', order_by="ASC", id_userrole_sel=id_userrole_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_userrole" et "userrole" de la "t_userrole"
            str_sql_id_userrole = "SELECT id_userrole, userrole FROM t_userrole " \
                               "WHERE id_userrole = %(value_id_userrole)s"
            valeur_select_dictionnaire = {"value_id_userrole": id_userrole_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_userrole, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom role" pour l'UPDATE
            data_nom_userrole = mybd_conn.fetchone()
            print("data_nom_userrole ", data_nom_userrole, " type ", type(data_nom_userrole), " userrole ",
                  data_nom_userrole["userrole"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "userrole_update_wtf.html"
            form_update.nom_userrole_update_wtf.data = data_nom_userrole["userrole"]


    except Exception as Exception_userrole_update_wtf:
        raise ExceptionUserroleUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{userrole_update_wtf.__name__} ; "
                                      f"{Exception_userrole_update_wtf}")

    return render_template("userrole/userrole_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /userrole_delete
    
    Test : ex. cliquer sur le menu "userrole" puis cliquer sur le bouton "DELETE" d'un "role"
    
    Paramètres : sans
    
    But : Effacer(delete) un role qui a été sélectionné dans le formulaire "userrole_afficher.html"
    
    Remarque :  Dans le champ "nom_userrole_delete_wtf" du formulaire "userrole/userrole_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/userrole_delete", methods=['GET', 'POST'])
def userrole_delete_wtf():
    data_user_attribue_userrole_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_userrole"
    id_userrole_delete = request.values['id_userrole_btn_delete_html']

    # Objet formulaire pour effacer le role sélectionné.
    form_delete_userrole = FormWTFDeleteUserrole()
    try:
        print(" on submit ", form_delete_userrole.validate_on_submit())
        if request.method == "POST" and form_delete_userrole.validate_on_submit():

            if form_delete_userrole.submit_btn_annuler.data:
                return redirect(url_for("userrole_afficher", order_by="DESC", id_userrole_sel=0))

            if form_delete_userrole.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "userrole/userrole_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_user_attribue_userrole_delete = session['data_user_attribue_userrole_delete']
                print("data_user_attribue_userrole_delete ", data_user_attribue_userrole_delete)

                flash(f"Effacer le role de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer role" qui va irrémédiablement EFFACER le role
                btn_submit_del = True

            if form_delete_userrole.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_userrole": id_userrole_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_user_userrole = """DELETE FROM t_user_has_userrole WHERE fk_userrole = %(value_id_userrole)s"""
                str_sql_delete_iduserrole = """DELETE FROM t_userrole WHERE id_userrole = %(value_id_userrole)s"""
                # Manière brutale d'effacer d'abord la "fk_userrole", même si elle n'existe pas dans la "t_user_has_userrole"
                # Ensuite on peut effacer le role vu qu'il n'est plus "lié" (INNODB) dans la "t_user_has_userrole"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_user_userrole, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_iduserrole, valeur_delete_dictionnaire)

                flash(f"Role définitivement effacé !!", "success")
                print(f"Role définitivement effacé !!")

                # afficher les données
                return redirect(url_for('userrole_afficher', order_by="ASC", id_userrole_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_userrole": id_userrole_delete}
            print(id_userrole_delete, type(id_userrole_delete))

            # Requête qui affiche tous les user_userrole qui ont le role que l'utilisateur veut effacer
            str_sql_user_userrole_delete = """SELECT id_user, user_firstname, user_lastname, id_userrole, userrole FROM t_user_has_userrole
                                            LEFT JOIN t_user ON t_user_has_userrole.fk_user = t_user.id_user
                                            LEFT JOIN t_userrole ON t_user_has_userrole.fk_userrole = t_userrole.id_userrole
                                            WHERE fk_userrole = %(value_id_userrole)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_user_userrole_delete, valeur_select_dictionnaire)
                data_user_attribue_userrole_delete = mydb_conn.fetchall()
                print("data_user_attribue_userrole_delete...", data_user_attribue_userrole_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "userrole/userrole_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_user_attribue_userrole_delete'] = data_user_attribue_userrole_delete

                # Opération sur la BD pour récupérer "id_userrole" et "userrole" de la "t_userrole"
                str_sql_id_userrole = "SELECT id_userrole, userrole FROM t_userrole WHERE id_userrole = %(value_id_userrole)s"

                mydb_conn.execute(str_sql_id_userrole, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom userrole" pour l'action DELETE
                data_nom_userrole = mydb_conn.fetchone()
                print("data_nom_userrole ", data_nom_userrole, " type ", type(data_nom_userrole), " role ",
                      data_nom_userrole["userrole"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "userrole_delete_wtf.html"
            form_delete_userrole.nom_userrole_delete_wtf.data = data_nom_userrole["userrole"]

            # Le bouton pour l'action "DELETE" dans le form. "userrole_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_userrole_delete_wtf:
        raise ExceptionUserroleDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{userrole_delete_wtf.__name__} ; "
                                      f"{Exception_userrole_delete_wtf}")

    return render_template("userrole/userrole_delete_wtf.html",
                           form_delete_userrole=form_delete_userrole,
                           btn_submit_del=btn_submit_del,
                           data_user_associes=data_user_attribue_userrole_delete)
