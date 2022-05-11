"""Gestion des "routes" FLASK et des données pour les users.
Fichier : gestion_user_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_USER_164.database.database_tools import DBconnection
from APP_USER_164.erreurs.exceptions import *
from APP_USER_164.user.gestion_user_wtf_forms import FormWTFUpdateUser, FormWTFAddUser, FormWTFDeleteUser

"""Ajouter un utilisateur grâce au formulaire "user_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /user_add

Test : exemple: cliquer sur le menu "Utilisateurs/Roles" puis cliquer sur le bouton "ADD" d'un "utilisateur"

Paramètres : sans


Remarque :  Dans le champ "user_firstname_update_wtf" du formulaire "user/user_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/user_add", methods=['GET', 'POST'])
def user_add_wtf():
    # Objet formulaire pour AJOUTER un user
    form_add_user = FormWTFAddUser()
    if request.method == "POST":
        try:
            if form_add_user.validate_on_submit():
                user_firstname_add = form_add_user.user_firstname_add_wtf.data
                user_lastname_add = form_add_user.user_lastname_add_wtf.data
                user_birthdate_add = form_add_user.user_birthdate_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_user_firstname": user_firstname_add,
                                                  "value_user_lastname": user_lastname_add,
                                                  "value_user_birthdate": user_birthdate_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_user = """INSERT INTO t_user (id_user, user_firstname, user_lastname, user_birthdate) 
                VALUES (NULL,%(value_user_firstname)s,%(value_user_lastname)s,%(value_user_birthdate)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_user, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau user (id_user_sel=0 => afficher tous les user)
                return redirect(url_for('user_userrole_afficher', id_user_sel=0))

        except Exception as Exception_userrole_ajouter_wtf:
            raise ExceptionUserroleAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{user_add_wtf.__name__} ; "
                                            f"{Exception_userrole_ajouter_wtf}")

    return render_template("user/user_add_wtf.html", form_add_user=form_add_user)


"""Editer(update) un utilisateur qui a été sélectionné dans le formulaire "user_userrole_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /user_update

Test : exemple: cliquer sur le menu "Utilisateurs/Roles" puis cliquer sur le bouton "EDIT" d'un "utilisateur"

Paramètres : sans

But : Editer(update) un userrole qui a été sélectionné dans le formulaire "userrole_afficher.html"

Remarque :  Dans le champ "user_firstname_update_wtf" du formulaire "user/user_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/user_update", methods=['GET', 'POST'])
def user_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_user"
    id_user_update = request.values['id_user_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_user = FormWTFUpdateUser()
    try:
        print(" on submit ", form_update_user.validate_on_submit())
        if form_update_user.validate_on_submit():
            # Récupèrer la valeur du champ depuis "userrole_update_wtf.html" après avoir cliqué sur "SUBMIT".
            user_firstname_update = form_update_user.user_firstname_update_wtf.data
            user_lastname_update = form_update_user.user_lastname_update_wtf.data
            user_birthdate_update = form_update_user.user_birthdate_update_wtf.data

            valeur_update_dictionnaire = {"value_id_user": id_user_update,
                                          "value_user_firstname": user_firstname_update,
                                          "value_user_lastname": user_lastname_update,
                                          "value_user_birthdate": user_birthdate_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_user = """UPDATE t_user SET user_firstname = %(value_user_firstname)s,
                                                        user_lastname = %(value_user_lastname)s,
                                                        user_birthdate = %(value_user_birthdate)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_user, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le user modifié, "ASC" et l'"id_user_update"
            return redirect(url_for('user_userrole_afficher', id_user_sel=id_user_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer les données de la "t_user"

            # str_sql_id_user = "SELECT id_user, user_firstname, user_lastname, user_birthdate FROM t_user WHERE id_user = %(value_id_user)s, user_firstname = %(value_user_firstname)s, user_lastname = %(value_user_lastname)s, user_birthdate = %(value_user_birthdate)s"

            # str_sql_id_user = "SELECT id_user FROM t_user WHERE id_user = %(value_id_user)s"
            str_sql_id_user = "SELECT id_user, user_firstname, user_lastname, user_birthdate FROM t_user WHERE id_user = %(value_id_user)s"

            valeur_select_dictionnaire = {"value_id_user": id_user_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_user, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom userrole" pour l'UPDATE
            data_user = mybd_conn.fetchone()
            print("data_user ", data_user, " type ", type(data_user), " userrole ",
                  data_user["id_user"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "user_update_wtf.html"
            form_update_user.user_firstname_update_wtf.data = data_user["user_firstname"]
            form_update_user.user_lastname_update_wtf.data = data_user["user_lastname"]
            form_update_user.user_birthdate_update_wtf.data = data_user["user_birthdate"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" user lastname  ", data_user["user_lastname"], "  type ", type(data_user["user_lastname"]))
            form_update_user.user_birthdate_update_wtf.data = data_user["user_birthdate"]

    except Exception as Exception_user_update_wtf:
        raise ExceptionUserUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{user_update_wtf.__name__} ; "
                                     f"{Exception_user_update_wtf}")

    return render_template("user/user_update_wtf.html", form_update_user=form_update_user)


"""Effacer(delete) un user qui a été sélectionné dans le formulaire "user_userrole_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /user_delete
    
Test : ex. cliquer sur le menu "utilisateur" puis cliquer sur le bouton "DELETE" d'un "utilisateur"
    
Paramètres : sans

Remarque :  Dans le champ "nom_user_delete_wtf" du formulaire "user/user_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/user_delete", methods=['GET', 'POST'])
def user_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_user_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_user"
    id_user_delete = request.values['id_user_btn_delete_html']

    # Objet formulaire pour effacer le user sélectionné.
    form_delete_user = FormWTFDeleteUser()
    try:
        # Si on clique sur "ANNULER", afficher tous les user.
        if form_delete_user.submit_btn_annuler.data:
            return redirect(url_for("user_userrole_afficher", id_user_sel=0))

        if form_delete_user.submit_btn_conf_del_user.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "user/user_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_user_delete = session['data_user_delete']
            print("data_user_delete ", data_user_delete)

            flash(f"Effacer l'utilisateur de façon définitive de la base de données !!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer role" qui va irrémédiablement EFFACER le role
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_user.submit_btn_del_user.data:
            valeur_delete_dictionnaire = {"value_id_user": id_user_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_user_userrole = """DELETE FROM t_user_has_userrole WHERE fk_user = %(value_id_user)s"""
            str_sql_delete_user = """DELETE FROM t_user WHERE id_user = %(value_id_user)s"""
            # Manière brutale d'effacer d'abord la "fk_user", même si elle n'existe pas dans la "t_userrole_user"
            # Ensuite on peut effacer le user vu qu'il n'est plus "lié" (INNODB) dans la "t_userrole_user"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_user_userrole, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_user, valeur_delete_dictionnaire)

            flash(f"Utilisateur définitivement effacé !!", "success")
            print(f"Utilisateur définitivement effacé !!")

            # afficher les données
            return redirect(url_for('user_userrole_afficher', id_user_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_user": id_user_delete}
            print(id_user_delete, type(id_user_delete))

            # Requête qui affiche l'utilisateur qui doit être efffacé.
            str_sql_user_userrole_delete = """SELECT id_user, user_firstname, user_lastname, user_birthdate FROM t_user WHERE id_user = %(value_id_user)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_user_userrole_delete, valeur_select_dictionnaire)
                data_user_delete = mydb_conn.fetchall()
                print("data_user_delete...", data_user_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "user/user_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_user_delete'] = data_user_delete

            # Le bouton pour l'action "DELETE" dans le form. "user_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_user_delete_wtf:
        raise ExceptionUserDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{user_delete_wtf.__name__} ; "
                                     f"{Exception_user_delete_wtf}")

    return render_template("user/user_delete_wtf.html",
                           form_delete_user=form_delete_user,
                           btn_submit_del=btn_submit_del,
                           data_user_del=data_user_delete
                           )
