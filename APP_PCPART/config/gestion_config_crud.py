"""Gestion des "routes" FLASK et des données pour les config.
Fichier : gestion_config_crud.py
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
from APP_PCPART.config.gestion_config_wtf_forms import *


"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /config_afficher
    
    Test : ex : http://127.0.0.1:5005/config_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_config_sel = 0 >> tous les config.
                id_config_sel = "n" affiche la config dont l'id est "n"
"""


@app.route("/config_afficher/<string:order_by>/<int:id_config_sel>", methods=['GET', 'POST'])
def config_afficher(order_by, id_config_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_config_sel == 0:
                    strsql_config_afficher = """SELECT id_config, config_use_case, config_rating FROM t_config ORDER BY id_config ASC"""
                    mc_afficher.execute(strsql_config_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_config"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id de la config sélectionné avec un nom de variable
                    valeur_id_config_selected_dictionnaire = {"value_id_config_selected": id_config_sel}
                    strsql_config_afficher = """SELECT id_config, userpseudo, config_rating, config_use_case, cpu_manufacturer, cpu_name, CONCAT(motherboard_brand, ' ', motherboard_model),
CONCAT(aircooling_brand, ' ', aircooling_model), CONCAT(watercooling_brand, ' ', watercooling_model), CONCAT(ram_brand, ' ', ram_name), 
ram_capacity, CONCAT(gpu_brand, ' ', gpu_name), CONCAT(case_brand, ' ', case_model), CONCAT(supply_brand, ' ', supply_model), 
CONCAT(ssd_brand, ' ', ssd_model), ssd_capacity, CONCAT(hdd_brand, ' ', hdd_name), hdd_capacity
FROM t_config
LEFT JOIN t_config_has_cpu ON t_config.id_config = t_config_has_cpu.fk_config
LEFT JOIN t_cpu ON t_cpu.id_cpu = t_config_has_cpu.fk_cpu
LEFT JOIN t_cpumanufacturer_produce_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
LEFT JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
LEFT JOIN t_config_has_motherboard ON t_config.id_config = t_config_has_motherboard.fk_config
LEFT JOIN t_motherboard ON t_motherboard.id_motherboard = t_config_has_motherboard.fk_motherboard
LEFT JOIN t_config_has_ram ON t_config.id_config = t_config_has_ram.fk_config
LEFT JOIN t_ram ON t_ram.id_ram = t_config_has_ram.fk_ram
LEFT JOIN t_config_has_gpu ON t_config.id_config = t_config_has_gpu.fk_config
LEFT JOIN t_gpu ON t_gpu.id_gpu = t_config_has_gpu.fk_gpu
LEFT JOIN t_config_has_aircooling ON t_config.id_config = t_config_has_aircooling.fk_config
LEFT JOIN t_aircooling ON t_aircooling.id_aircooling = t_config_has_aircooling.fk_aircooling
LEFT JOIN t_config_has_watercooling ON t_config.id_config = t_config_has_watercooling.fk_config
LEFT JOIN t_watercooling ON t_watercooling.id_watercooling = t_config_has_watercooling.fk_watercooling
LEFT JOIN t_config_has_case ON t_config.id_config = t_config_has_case.fk_config
LEFT JOIN t_case ON t_case.id_case = t_config_has_case.fk_case
LEFT JOIN t_config_has_supply ON t_config.id_config = t_config_has_supply.fk_config
LEFT JOIN t_supply ON t_supply.id_supply = t_config_has_supply.fk_supply
LEFT JOIN t_config_has_ssd ON t_config.id_config = t_config_has_ssd.fk_config
LEFT JOIN t_ssd ON t_ssd.id_ssd = t_config_has_ssd.fk_ssd
LEFT JOIN t_config_has_hdd ON t_config.id_config = t_config_has_hdd.fk_config
LEFT JOIN t_hdd ON t_hdd.id_hdd = t_config_has_hdd.fk_hdd
LEFT JOIN t_user_created_config ON t_config.id_config = t_user_created_config.fk_config
LEFT JOIN t_user ON t_user.id_user = t_user_created_config.fk_user
INNER JOIN t_user_has_userpseudo ON t_user.id_user = t_user_has_userpseudo.fk_user
INNER JOIN t_userpseudo ON t_userpseudo.id_pseudo = t_user_has_userpseudo.fk_pseudo
WHERE userpseudo = 'Cricko';"""

                    mc_afficher.execute(strsql_config_afficher, valeur_id_config_selected_dictionnaire)
                else:
                    strsql_config_afficher = """SELECT id_config, config_use_case, config_rating  FROM t_config ORDER BY id_config DESC"""

                    mc_afficher.execute(strsql_config_afficher)

                data_config = mc_afficher.fetchall()

                print("data_config ", data_config, " Type : ", type(data_config))

                # Différencier les messages si la table est vide.
                if not data_config and id_config_sel == 0:
                    flash("""La table "t_config" est vide. !!""", "warning")
                elif not data_config and id_config_sel > 0:
                    # Si l'utilisateur change l'id_config dans l'URL et que le config n'existe pas,
                    flash(f"La config demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_config" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données config affichés !!", "success")

        except Exception as Exception_config_afficher:
            raise ExceptionConfigAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{config_afficher.__name__} ; "
                                          f"{Exception_config_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("config/config_afficher.html", data=data_config)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /config_ajouter
    
    Test : ex : http://127.0.0.1:5005/config_ajouter
    
    Paramètres : sans
    
    But : Ajouter une config pour un utilisateur
    
    Remarque :  Dans le champ "name_config_html" du formulaire "config/config_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/config_ajouter", methods=['GET', 'POST'])
def config_ajouter_wtf():
    form = FormWTFAjouterConfig()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_config_wtf = form.nom_config_wtf.data
                name_config = name_config_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_config_use_case": name_config}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_config = """INSERT INTO t_config (id_config,config_use_case) VALUES (NULL,%(value_config_use_case)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_config, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('config_afficher', order_by='DESC', id_config_sel=0))

        except Exception as Exception_config_ajouter_wtf:
            raise ExceptionConfigAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{config_ajouter_wtf.__name__} ; "
                                            f"{Exception_config_ajouter_wtf}")

    return render_template("config/config_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /config_update
    
    Test : ex cliquer sur le menu "config" puis cliquer sur le bouton "EDIT" d'une "config"
    
    Paramètres : sans
    
    But : Editer(update) une config qui a été sélectionné dans le formulaire "config_afficher.html"
    
    Remarque :  Dans le champ "config_use_case_update_wtf" du formulaire "config/config_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/config_update", methods=['GET', 'POST'])
def config_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_config"
    id_config_update = request.values['id_config_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateConfig()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "config_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            config_use_case_update = form_update.config_use_case_update_wtf.data
            config_use_case_update = config_use_case_update.lower()
            config_rating = form_update.config_rating_wtf_essai.data

            valeur_update_dictionnaire = {"value_id_config": id_config_update,
                                          "value_config_use_case": config_use_case_update,
                                          "value_config_rating": config_rating
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_config_use_case = """UPDATE t_config SET config_use_case = %(value_config_use_case)s, 
            config_rating = %(value_config_rating)s WHERE id_config = %(value_id_config)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_config_use_case, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_config_update"
            return redirect(url_for('config_afficher', order_by="ASC", id_config_sel=id_config_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_config" et "config_use_case" de la "t_config"
            str_sql_id_config = "SELECT id_config, config_use_case, config_rating FROM t_config " \
                               "WHERE id_config = %(value_id_config)s"
            valeur_select_dictionnaire = {"value_id_config": id_config_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_config, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom config" pour l'UPDATE
            data_config_use_case = mybd_conn.fetchone()
            print("data_config_use_case ", data_config_use_case, " type ", type(data_config_use_case), " use case ",
                  data_config_use_case["config_use_case"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "config_update_wtf.html"
            form_update.config_use_case_update_wtf.data = data_config_use_case["config_use_case"]
            form_update.config_rating_wtf_essai.data = data_config_use_case["config_rating"]

    except Exception as Exception_config_update_wtf:
        raise ExceptionConfigUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{config_update_wtf.__name__} ; "
                                      f"{Exception_config_update_wtf}")

    return render_template("config/config_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /config_delete
    
    Test : ex. cliquer sur le menu "config" puis cliquer sur le bouton "DELETE" d'un "config"
    
    Paramètres : sans
    
    But : Effacer(delete) une config qui a été sélectionné dans le formulaire "config_afficher.html"
    
    Remarque :  Dans le champ "nom_config_delete_wtf" du formulaire "config/config_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/config_delete", methods=['GET', 'POST'])
def config_delete_wtf():
    data_user_attribue_config_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_config"
    id_config_delete = request.values['id_config_btn_delete_html']

    # Objet formulaire pour effacer la config sélectionné.
    form_delete = FormWTFDeleteConfig()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("config_afficher", order_by="ASC", id_config_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "config/config_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_user_attribue_config_delete = session['data_user_attribue_config_delete']
                print("data_user_attribue_config_delete ", data_user_attribue_config_delete)

                flash(f"Effacer la config de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer config" qui va irrémédiablement EFFACER la config
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_config": id_config_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_user_config = """DELETE FROM t_user_created_config WHERE fk_config = %(value_id_config)s"""
                str_sql_delete_idconfig = """DELETE FROM t_config WHERE id_config = %(value_id_config)s"""
                # Manière brutale d'effacer d'abord la "fk_config", même si elle n'existe pas dans la "t_user_created_config"
                # Ensuite on peut effacer la config vu qu'il n'est plus "lié" (INNODB) dans la "t_user_created_config"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_user_config, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idconfig, valeur_delete_dictionnaire)

                flash(f"Config définitivement effacé !!", "success")
                print(f"Config définitivement effacé !!")

                # afficher les données
                return redirect(url_for('config_afficher', order_by="ASC", id_config_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_config": id_config_delete}
            print(id_config_delete, type(id_config_delete))

            # Requête qui affiche tous les user_config qui ont la config que l'utilisateur veut effacer
            str_sql_config_user_delete = """SELECT id_user_created_config, user_firstname, id_config, config_use_case FROM t_user_created_config 
                                            INNER JOIN t_user ON t_user_created_config.fk_user = t_user.id_user
                                            INNER JOIN t_config ON t_user_created_config.fk_config = t_config.id_config
                                            WHERE fk_config = %(value_id_config)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_config_user_delete, valeur_select_dictionnaire)
                data_user_attribue_config_delete = mydb_conn.fetchall()
                print("data_user_attribue_config_delete...", data_user_attribue_config_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "config/config_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_user_attribue_config_delete'] = data_user_attribue_config_delete

                # Opération sur la BD pour récupérer "id_config" et "config_use_case" de la "t_config"
                str_sql_id_config = "SELECT id_config, config_use_case FROM t_config WHERE id_config = %(value_id_config)s"

                mydb_conn.execute(str_sql_id_config, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "config use case" pour l'action DELETE
                data_config_use_case = mydb_conn.fetchone()
                print("data_config_use_case ", data_config_use_case, " type ", type(data_config_use_case), " config ",
                      data_config_use_case["config_use_case"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "config_delete_wtf.html"
            form_delete.nom_config_delete_wtf.data = data_config_use_case["config_use_case"]

            # Le bouton pour l'action "DELETE" dans le form. "config_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_config_delete_wtf:
        raise ExceptionConfigDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{config_delete_wtf.__name__} ; "
                                      f"{Exception_config_delete_wtf}")

    return render_template("config/config_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_config_associes=data_user_attribue_config_delete)
