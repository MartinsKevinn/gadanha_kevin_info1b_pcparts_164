"""Gestion des "routes" FLASK et des données pour les films.
Fichier : gestion_config_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.films.gestion_films_wtf_forms import FormWTFUpdateConfig, FormWTFAddConfig, FormWTFDeleteConfig

"""Ajouter un config grâce au formulaire "config_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /config_add

Test : exemple: cliquer sur le menu "Utilisateurs/Configurations" puis cliquer sur le bouton "ADD" d'une "config"

Paramètres : sans


Remarque :  Dans le champ "config_use_case_update_wtf" du formulaire "films/config_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/config_add", methods=['GET', 'POST'])
def config_add_wtf():
    # Objet formulaire pour AJOUTER un config
    form_add_config = FormWTFAddConfig()
    if request.method == "POST":
        try:
            if form_add_config.validate_on_submit():
                config_use_case_add = form_add_config.config_use_case_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_config_use_case": config_use_case_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_config = """INSERT INTO t_config (id_config,config_use_case) VALUES (NULL,%(value_config_use_case)s """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_config, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau config (id_config_sel=0 => afficher toutes les configs)
                return redirect(url_for('user_created_config_afficher', id_config_sel=0))

        except Exception as Exception_user_ajouter_wtf:
            raise ExceptionUserAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{config_add_wtf.__name__} ; "
                                            f"{Exception_user_ajouter_wtf}")

    return render_template("films/config_add_wtf.html", form_add_config=form_add_config)


"""Editer(update) un config qui a été sélectionné dans le formulaire "user_created_config_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "config"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

Remarque :  Dans le champ "config_use_case_update_wtf" du formulaire "films/config_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/film_update", methods=['GET', 'POST'])
def config_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_config"
    id_config_update = request.values['id_film_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_config = FormWTFUpdateConfig()
    try:
        print(" on submit ", form_update_config.validate_on_submit())
        if form_update_config.validate_on_submit():
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            config_use_case_update = form_update_config.config_use_case_update_wtf.data
            config_rating_update = form_update_config.config_rating_update_wtf.data

            valeur_update_dictionnaire = {"value_id_config": id_config_update,
                                          "value_config_use_case": config_use_case_update,
                                          "value_config_rating": config_rating_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_config_use_case = """UPDATE t_config SET config_use_case = %(value_config_use_case)s,
                                                            config_rating = %(value_config_rating)s
                                                            WHERE id_config = %(value_id_config)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_config_use_case, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le config modifié, "ASC" et l'"id_config_update"
            return redirect(url_for('user_created_config_afficher', id_config_sel=id_config_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_config" et "user_firstname" de la "t_user"
            str_sql_id_config = "SELECT * FROM t_config WHERE id_config = %(value_id_config)s"
            valeur_select_dictionnaire = {"value_id_config": id_config_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_config, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_config = mybd_conn.fetchone()
            print("data_config ", data_config, " type ", type(data_config), " user ",
                  data_config["config_use_case"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "config_update_wtf.html"
            form_update_config.config_use_case_update_wtf.data = data_config["config_use_case"]
            form_update_config.config_rating_update_wtf.data = data_config["config_rating"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" duree film  ", data_config["config_rating"], "  type ", type(data_config["config_rating"]))

    except Exception as Exception_config_update_wtf:
        raise ExceptionConfigUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{config_update_wtf.__name__} ; "
                                     f"{Exception_config_update_wtf}")

    return render_template("films/config_update_wtf.html", form_update_config=form_update_config)


"""Effacer(delete) un config qui a été sélectionné dans le formulaire "config_user_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /config_delete
    
Test : ex. cliquer sur le menu "config" puis cliquer sur le bouton "DELETE" d'un "config"
    
Paramètres : sans

Remarque :  Dans le champ "config_use_case_delete_wtf" du formulaire "films/config_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/config_delete", methods=['GET', 'POST'])
def config_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_config_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_config"
    id_config_delete = request.values['id_config_btn_delete_html']

    # Objet formulaire pour effacer le config sélectionné.
    form_delete_config = FormWTFDeleteConfig()
    try:
        # Si on clique sur "ANNULER", afficher tous les films.
        if form_delete_config.submit_btn_annuler.data:
            return redirect(url_for("user_created_config_afficher", id_config_sel=0))

        if form_delete_config.submit_btn_conf_del_config.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "films/config_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_config_delete = session['data_config_delete']
            print("data_config_delete ", data_config_delete)

            flash(f"Effacer le config de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_config.submit_btn_del_config.data:
            valeur_delete_dictionnaire = {"value_id_config": id_config_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_config_user = """DELETE FROM t_user_created_config WHERE fk_config = %(value_id_config)s"""
            str_sql_delete_config = """DELETE FROM t_config WHERE id_config = %(value_id_config)s"""
            # Manière brutale d'effacer d'abord la "fk_config", même si elle n'existe pas dans la "t_user_created_config"
            # Ensuite on peut effacer la config vu qu'elle n'est plus "liée" (INNODB) dans la "t_user_created_config"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_config_user, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_config, valeur_delete_dictionnaire)

            flash(f"Config définitivement effacé !!", "success")
            print(f"Config définitivement effacé !!")

            # afficher les données
            return redirect(url_for('user_created_config_afficher', id_config_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_config": id_config_delete}
            print(id_config_delete, type(id_config_delete))

            # Requête qui affiche le config qui doit être efffacé.
            str_sql_config_user_delete = """SELECT * FROM t_config WHERE id_config = %(value_id_config)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_config_user_delete, valeur_select_dictionnaire)
                data_config_delete = mydb_conn.fetchall()
                print("data_config_delete...", data_config_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "films/config_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_config_delete'] = data_config_delete

            # Le bouton pour l'action "DELETE" dans le form. "config_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_config_delete_wtf:
        raise ExceptionConfigDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{config_delete_wtf.__name__} ; "
                                     f"{Exception_config_delete_wtf}")

    return render_template("films/config_delete_wtf.html",
                           form_delete_config=form_delete_config,
                           btn_submit_del=btn_submit_del,
                           data_config_del=data_config_delete
                           )
