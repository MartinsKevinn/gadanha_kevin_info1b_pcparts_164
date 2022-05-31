"""Gestion des "routes" FLASK et des données pour les cpu.
Fichier : gestion_cpu_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_PCPART.database.database_tools import DBconnection
from APP_PCPART.erreurs.exceptions import *
from APP_PCPART.cpu.gestion_cpu_wtf_forms import FormWTFUpdateCpu, FormWTFAddCpu, FormWTFDeleteCpu

"""Ajouter un cpu grâce au formulaire "user_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /cpu_add

Test : exemple: cliquer sur le menu "cpu/manufacturer" puis cliquer sur le bouton "ADD" d'un "cpu"

Paramètres : sans


Remarque :  Dans le champ "nom_cpu_update_wtf" du formulaire "cpu/cpu_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/cpu_afficher/<int:id_cpu_sel>", methods=['GET', 'POST'])
def cpu_afficher(id_cpu_sel):
    print(" cpu_afficher id_cpu_sel ", id_cpu_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_cpu_afficher_data = """SELECT id_cpu, CPU_Name, CPU_Codename, CPU_Cores, CPU_Clock, CPU_Socket, CPU_Released FROM t_cpu GROUP BY id_cpu"""
                if id_cpu_sel == 0:
                    # le paramètre 0 permet d'afficher tous les cpu
                    # Sinon le paramètre représente la valeur de l'id du cpu
                    mc_afficher.execute(strsql_cpu_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du cpu sélectionné avec un nom de variable
                    valeur_id_cpu_selected_dictionnaire = {"value_id_cpu_selected": id_cpu_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_cpu_afficher_data += """ HAVING id_cpu= %(value_id_cpu_selected)s"""

                    mc_afficher.execute(strsql_cpu_afficher_data, valeur_id_cpu_selected_dictionnaire)

                # Récupère les données de la requête.
                data_cpu_afficher = mc_afficher.fetchall()
                print("data_cpu ", data_cpu_afficher, " Type : ",
                      type(data_cpu_afficher))

                # Différencier les messages.
                if not data_cpu_afficher and id_cpu_sel == 0:
                    flash("""Table "t_cpu" is empty !""", "warning")
                elif not data_cpu_afficher and id_cpu_sel > 0:
                    # Si l'utilisateur change l'id_cpu dans l'URL et qu'il ne correspond à aucun cpu
                    flash(f"Searched CPU {id_cpu_sel} doesn't exist !!", "warning")
                else:
                    flash(f"Data CPUs shown !!", "success")

        except Exception as Exception_cpu_afficher:
            raise ExceptionCpuAfficher(
                f"fichier : {Path(__file__).name}  ;  {cpu_afficher.__name__} ;"
                f"{Exception_cpu_afficher}")

    print("cpu_afficher  ", data_cpu_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("cpu/cpu_afficher.html",
                           data=data_cpu_afficher)


@app.route("/cpu_add", methods=['GET', 'POST'])
def cpu_add_wtf():
    # Objet formulaire pour AJOUTER un cpu
    form_add_cpu = FormWTFAddCpu()
    if request.method == "POST":
        try:
            if form_add_cpu.validate_on_submit():
                nom_cpu_add = form_add_cpu.name_cpu_add_wtf.data
                codename_cpu_add = form_add_cpu.codename_cpu_add_wtf.data
                socket_cpu_add = form_add_cpu.socket_cpu_add_wtf.data
                cores_cpu_add = form_add_cpu.cores_cpu_add_wtf.data
                clock_cpu_add = form_add_cpu.clock_cpu_add_wtf.data
                tdp_cpu_add = form_add_cpu.tdp_cpu_add_wtf.data
                released_cpu_add = form_add_cpu.released_cpu_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_cpu_name": nom_cpu_add,
                                                  "value_cpu_codename": codename_cpu_add,
                                                  "value_cpu_socket": socket_cpu_add,
                                                  "value_cpu_cores": cores_cpu_add,
                                                  "value_cpu_clock": clock_cpu_add,
                                                  "value_cpu_tdp": tdp_cpu_add,
                                                  "value_cpu_released": released_cpu_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_cpu = """INSERT INTO t_cpu (id_cpu,CPU_Name,CPU_Codename,CPU_Socket,CPU_Cores,CPU_Clock,CPU_TDP,CPU_Released) 
                VALUES (NULL,%(value_cpu_name)s,%(value_cpu_codename)s,%(value_cpu_tdp)s,%(value_cpu_cores)s,%(value_cpu_clock)s,%(value_cpu_tdp)s,%(value_cpu_released)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_cpu, valeurs_insertion_dictionnaire)

                flash(f"Data inserted !!", "success")
                print(f"Data inserted !!")

                # Pour afficher et constater l'insertion du nouveau cpu (id_cpu_sel=0 => afficher tous les cpu)
                return redirect(url_for('cpu_cpumanufacturer_afficher', id_cpu_sel=0))

        except Exception as Exception_cpumanufacturer_ajouter_wtf:
            raise ExceptionCpumanufacturerAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                                     f"{cpu_add_wtf.__name__} ; "
                                                     f"{Exception_cpumanufacturer_ajouter_wtf}")

    return render_template("cpu/cpu_add_wtf.html", form_add_cpu=form_add_cpu)


"""Editer(update) un cpu qui a été sélectionné dans le formulaire "cpu_cpumanufacturer_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /cpu_update

Test : exemple: cliquer sur le menu "cpu/manufacturer" puis cliquer sur le bouton "EDIT" d'un "cpu"

Paramètres : sans

But : Editer(update) un manufacturer qui a été sélectionné dans le formulaire "cpumanufacturer_afficher.html"

Remarque :  Dans le champ "nom_cpu_update_wtf" du formulaire "cpu/cpu_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/cpu_update", methods=['GET', 'POST'])
def cpu_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_cpu"
    id_cpu_update = request.values['id_cpu_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_cpu = FormWTFUpdateCpu()
    try:
        print(" on submit ", form_update_cpu.validate_on_submit())
        if form_update_cpu.validate_on_submit():
            # Récupèrer la valeur du champ depuis "cpumanufacturer_update_wtf.html" après avoir cliqué sur "SUBMIT".
            nom_cpu_update = form_update_cpu.nom_cpu_update_wtf.data
            cpu_codename_update = form_update_cpu.cpu_codename_update_wtf.data
            cpu_cores_update = form_update_cpu.cpu_cores_update_wtf.data
            cpu_clock_update = form_update_cpu.cpu_clock_update_wtf.data
            cpu_socket_update = form_update_cpu.cpu_socket_update_wtf.data
            cpu_released_update = form_update_cpu.cpu_released_update_wtf.data

            valeur_update_dictionnaire = {"value_id_cpu": id_cpu_update,
                                          "value_cpu_name": nom_cpu_update,
                                          "value_cpu_codename": cpu_codename_update,
                                          "value_cpu_cores": cpu_cores_update,
                                          "value_cpu_clock": cpu_clock_update,
                                          "value_cpu_socket": cpu_socket_update,
                                          "value_cpu_released": cpu_released_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_cpu = """UPDATE t_cpu SET CPU_Name = %(value_cpu_name)s,
                                                         CPU_Codename = %(value_cpu_codename)s,
                                                         CPU_Cores = %(value_cpu_cores)s,
                                                         CPU_Clock = %(value_cpu_clock)s,
                                                         CPU_Socket = %(value_cpu_socket)s,
                                                         CPU_Released = %(value_cpu_released)s
                                                         WHERE id_cpu = %(value_id_cpu)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_cpu, valeur_update_dictionnaire)

            flash(f"Data updated !!", "success")
            print(f"Data updated !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le cpu modifié, "ASC" et l'"id_cpu_update"
            return redirect(url_for('cpu_cpumanufacturer_afficher', id_cpu_sel=id_cpu_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_cpu" et "CPU_Manufacturer" de la "t_cpumanufacturer"

            str_sql_id_cpu = "SELECT id_cpu, CPU_Name, CPU_Codename, CPU_Cores, CPU_Clock, CPU_Socket, CPU_Released FROM t_cpu WHERE id_cpu = %(value_id_cpu)s"

            valeur_select_dictionnaire = {"value_id_cpu": id_cpu_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_cpu, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom manufacturer" pour l'UPDATE
            data_cpu = mybd_conn.fetchone()
            print("data_cpu ", data_cpu, " type ", type(data_cpu), " cpumanufacturer ",
                  data_cpu["CPU_Name"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "cpu_update_wtf.html"
            form_update_cpu.nom_cpu_update_wtf.data = data_cpu["CPU_Name"]
            form_update_cpu.cpu_codename_update_wtf.data = data_cpu["CPU_Codename"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" cpu codename ", data_cpu["CPU_Codename"], "  type ", type(data_cpu["CPU_Codename"]))
            form_update_cpu.cpu_socket_update_wtf.data = data_cpu["CPU_Socket"]
            form_update_cpu.cpu_cores_update_wtf.data = data_cpu["CPU_Cores"]
            form_update_cpu.cpu_clock_update_wtf.data = data_cpu["CPU_Clock"]
            form_update_cpu.cpu_tdp_update_wtf.data = data_cpu["CPU_TDP"]
            form_update_cpu.cpu_released_update_wtf.data = data_cpu["CPU_Released"]

    except Exception as Exception_cpu_update_wtf:
        raise ExceptionCpuUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                    f"{cpu_update_wtf.__name__} ; "
                                    f"{Exception_cpu_update_wtf}")

    return render_template("cpu/cpu_update_wtf.html", form_update_cpu=form_update_cpu)


"""Effacer(delete) un cpu qui a été sélectionné dans le formulaire "cpu_cpumanufacturer_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /cpu_delete
    
Test : ex. cliquer sur le menu "cpu" puis cliquer sur le bouton "DELETE" d'un "cpu"
    
Paramètres : sans

Remarque :  Dans le champ "CPU_Name_delete_wtf" du formulaire "cpu/cpu_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/cpu_delete", methods=['GET', 'POST'])
def cpu_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_cpu_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_cpu"
    id_cpu_delete = request.values['id_cpu_btn_delete_html']

    # Objet formulaire pour effacer le cpu sélectionné.
    form_delete_cpu = FormWTFDeleteCpu()
    try:
        # Si on clique sur "ANNULER", afficher tous les cpu.
        if form_delete_cpu.submit_btn_annuler.data:
            return redirect(url_for("cpu_cpumanufacturer_afficher", id_cpu_sel=0))

        if form_delete_cpu.submit_btn_conf_del_cpu.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "cpu/cpu_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_cpu_delete = session['data_cpu_delete']
            print("data_cpu_delete ", data_cpu_delete)

            flash(f"Delete permanently the CPU !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer manufacturer" qui va irrémédiablement EFFACER le manufacturer
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_cpu.submit_btn_del_cpu.data:
            valeur_delete_dictionnaire = {"value_id_cpu": id_cpu_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_cpu_cpumanufacturer = """DELETE FROM t_cpumanufacturer_produce_cpu WHERE fk_cpu = %(value_id_cpu)s"""
            str_sql_delete_cpu = """DELETE FROM t_cpu WHERE id_cpu = %(value_id_cpu)s"""
            # Manière brutale d'effacer d'abord la "fk_cpu", même si elle n'existe pas dans la "t_cpumanufacturer_produce_cpu"
            # Ensuite on peut effacer le cpu vu qu'il n'est plus "lié" (INNODB) dans la "t_cpumanufacturer_produce_cpu"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_cpu_cpumanufacturer, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_cpu, valeur_delete_dictionnaire)

            flash(f"CPU permanently erased !!", "success")
            print(f"CPU permanently erased !!")

            # afficher les données
            return redirect(url_for('cpu_cpumanufacturer_afficher', id_cpu_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_cpu": id_cpu_delete}
            print(id_cpu_delete, type(id_cpu_delete))

            # Requête qui affiche le cpu qui doit être efffacé.
            str_sql_cpumanufacturer_cpu_delete = """SELECT * FROM t_cpu WHERE id_cpu = %(value_id_cpu)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_cpumanufacturer_cpu_delete, valeur_select_dictionnaire)
                data_cpu_delete = mydb_conn.fetchall()
                print("data_cpu_delete...", data_cpu_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "cpu/cpu_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_cpu_delete'] = data_cpu_delete

            # Le bouton pour l'action "DELETE" dans le form. "cpu_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_cpu_delete_wtf:
        raise ExceptionCpuDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                    f"{cpu_delete_wtf.__name__} ; "
                                    f"{Exception_cpu_delete_wtf}")

    return render_template("cpu/cpu_delete_wtf.html",
                           form_delete_cpu=form_delete_cpu,
                           btn_submit_del=btn_submit_del,
                           data_cpu_del=data_cpu_delete
                           )
