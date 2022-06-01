"""Gestion des "routes" FLASK et des données pour les gpu.
Fichier : gestion_gpu_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_PCPART.database.database_tools import DBconnection
from APP_PCPART.erreurs.exceptions import *
from APP_PCPART.gpu.gestion_gpu_wtf_forms import FormWTFUpdateGpu, FormWTFAddGpu, FormWTFDeleteGpu

"""Ajouter un gpu grâce au formulaire "user_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /gpu_add

Test : exemple: cliquer sur le menu "gpu/manufacturer" puis cliquer sur le bouton "ADD" d'un "gpu"

Paramètres : sans


Remarque :  Dans le champ "nom_gpu_update_wtf" du formulaire "gpu/gpu_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/gpu_afficher/<int:id_gpu_sel>", methods=['GET', 'POST'])
def gpu_afficher(id_gpu_sel):
    print(" gpu_afficher id_gpu_sel ", id_gpu_sel)
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                strsql_gpu_afficher_data = """SELECT id_gpu, GPU_Brand, GPU_Name, GPU_Codename, GPU_Bus, GPU_Memory, GPU_Clock, Memory_Clock, GPU_TDP, GPU_Released FROM t_gpu GROUP BY id_gpu"""
                if id_gpu_sel == 0:
                    # le paramètre 0 permet d'afficher tous les gpu
                    # Sinon le paramètre représente la valeur de l'id du gpu
                    mc_afficher.execute(strsql_gpu_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du gpu sélectionné avec un nom de variable
                    valeur_id_gpu_selected_dictionnaire = {"value_id_gpu_selected": id_gpu_sel}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalablement définie.
                    strsql_gpu_afficher_data += """ HAVING id_gpu= %(value_id_gpu_selected)s"""

                    mc_afficher.execute(strsql_gpu_afficher_data, valeur_id_gpu_selected_dictionnaire)

                # Récupère les données de la requête.
                data_gpu_afficher = mc_afficher.fetchall()
                print("data_gpu ", data_gpu_afficher, " Type : ",
                      type(data_gpu_afficher))

                # Différencier les messages.
                if not data_gpu_afficher and id_gpu_sel == 0:
                    flash("""Table "t_gpu" is empty !""", "warning")
                elif not data_gpu_afficher and id_gpu_sel > 0:
                    # Si l'utilisateur change l'id_gpu dans l'URL et qu'il ne correspond à aucun gpu
                    flash(f"Searched GPU {id_gpu_sel} doesn't exist !!", "warning")
                else:
                    flash(f"Data GPUs shown !!", "success")

        except Exception as Exception_gpu_afficher:
            raise ExceptionGpuAfficher(
                f"fichier : {Path(__file__).name}  ;  {gpu_afficher.__name__} ;"
                f"{Exception_gpu_afficher}")

    print("gpu_afficher  ", data_gpu_afficher)
    # Envoie la page "HTML" au serveur.
    return render_template("gpu/gpu_afficher.html",
                           data=data_gpu_afficher)


@app.route("/gpu_add", methods=['GET', 'POST'])
def gpu_add_wtf():
    # Objet formulaire pour AJOUTER un gpu
    form_add_gpu = FormWTFAddGpu()
    if request.method == "POST":
        try:
            if form_add_gpu.validate_on_submit():
                brand_gpu_add = form_add_gpu.brand_gpu_add_wtf.data
                nom_gpu_add = form_add_gpu.name_gpu_add_wtf.data
                codename_gpu_add = form_add_gpu.codename_gpu_add_wtf.data
                bus_gpu_add = form_add_gpu.bus_gpu_add_wtf.data
                memory_gpu_add = form_add_gpu.memory_gpu_add_wtf.data
                clock_gpu_add = form_add_gpu.clock_gpu_add_wtf.data
                clock_memory_gpu_add = form_add_gpu.clock_memory_gpu_add_wtf.data
                tdp_gpu_add = form_add_gpu.tdp_gpu_add_wtf.data
                released_gpu_add = form_add_gpu.released_gpu_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_gpu_brand": brand_gpu_add,
                                                  "value_gpu_name": nom_gpu_add,
                                                  "value_gpu_codename": codename_gpu_add,
                                                  "value_gpu_bus": bus_gpu_add,
                                                  "value_gpu_memory": memory_gpu_add,
                                                  "value_gpu_clock": clock_gpu_add,
                                                  "value_gpu_memory_clock": clock_memory_gpu_add,
                                                  "value_gpu_tdp": tdp_gpu_add,
                                                  "value_gpu_released": released_gpu_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_gpu = """INSERT INTO t_gpu (id_gpu,GPU_Brand,GPU_Name,GPU_Codename,GPU_Bus,GPU_Memory,GPU_Clock,Memory_Clock,GPU_TDP,GPU_Released) 
                VALUES (NULL,%(value_gpu_brand)s,%(value_gpu_name)s,%(value_gpu_codename)s,%(value_gpu_bus)s,%(value_gpu_memory)s,%(value_gpu_clock)s,%(value_gpu_memory_clock)s,%(value_gpu_tdp)s,%(value_gpu_released)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_gpu, valeurs_insertion_dictionnaire)

                flash(f"Data inserted !!", "success")
                print(f"Data inserted !!")

                # Pour afficher et constater l'insertion du nouveau gpu (id_gpu_sel=0 => afficher tous les gpu)
                return redirect(url_for('gpu_gpumanufacturer_afficher', id_gpu_sel=0))

        except Exception as Exception_gpumanufacturer_ajouter_wtf:
            raise ExceptionGpumanufacturerAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                                     f"{gpu_add_wtf.__name__} ; "
                                                     f"{Exception_gpumanufacturer_ajouter_wtf}")

    return render_template("gpu/gpu_add_wtf.html", form_add_gpu=form_add_gpu)


"""Editer(update) un gpu qui a été sélectionné dans le formulaire "gpu_gpumanufacturer_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /gpu_update

Test : exemple: cliquer sur le menu "gpu/manufacturer" puis cliquer sur le bouton "EDIT" d'un "gpu"

Paramètres : sans

But : Editer(update) un manufacturer qui a été sélectionné dans le formulaire "gpumanufacturer_afficher.html"

Remarque :  Dans le champ "nom_gpu_update_wtf" du formulaire "gpu/gpu_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/gpu_update", methods=['GET', 'POST'])
def gpu_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_gpu"
    id_gpu_update = request.values['id_gpu_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_gpu = FormWTFUpdateGpu()
    try:
        print(" on submit ", form_update_gpu.validate_on_submit())
        if form_update_gpu.validate_on_submit():
            # Récupèrer la valeur du champ depuis "gpumanufacturer_update_wtf.html" après avoir cliqué sur "SUBMIT".
            brand_gpu_update = form_update_gpu.brand_gpu_update_wtf.data
            nom_gpu_update = form_update_gpu.nom_gpu_update_wtf.data
            gpu_codename_update = form_update_gpu.gpu_codename_update_wtf.data
            gpu_bus_update = form_update_gpu.gpu_bus_update_wtf.data
            gpu_memory_update = form_update_gpu.gpu_memory_update_wtf.data
            gpu_clock_update = form_update_gpu.gpu_clock_update_wtf.data
            gpu_memory_clock_update = form_update_gpu.gpu_memory_clock_update_wtf.data
            gpu_tdp_update = form_update_gpu.gpu_tdp_update_wtf.data
            gpu_released_update = form_update_gpu.gpu_released_update_wtf.data

            valeur_update_dictionnaire = {"value_id_gpu": id_gpu_update,
                                          "value_gpu_brand": brand_gpu_update,
                                          "value_gpu_name": nom_gpu_update,
                                          "value_gpu_codename": gpu_codename_update,
                                          "value_gpu_bus": gpu_bus_update,
                                          "value_gpu_memory": gpu_memory_update,
                                          "value_gpu_clock": gpu_clock_update,
                                          "value_gpu_memory_clock": gpu_memory_clock_update,
                                          "value_gpu_tdp": gpu_tdp_update,
                                          "value_gpu_released": gpu_released_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_gpu = """UPDATE t_gpu SET GPU_Brand = %(value_gpu_brand)s,
                                                         GPU_Name = %(value_gpu_name)s,
                                                         GPU_Codename = %(value_gpu_codename)s,
                                                         GPU_Bus = %(value_gpu_bus)s,
                                                         GPU_Memory = %(value_gpu_memory)s,
                                                         GPU_Clock = %(value_gpu_clock)s,
                                                         Memory_Clock = %(value_gpu_memory_clock)s,
                                                         GPU_TDP = %(value_gpu_tdp)s,
                                                         GPU_Released = %(value_gpu_released)s
                                                         WHERE id_gpu = %(value_id_gpu)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_gpu, valeur_update_dictionnaire)

            flash(f"Data updated !!", "success")
            print(f"Data updated !!")

            # afficher et constater que la donnée est mise à jour.
            # Show seulement le gpu modifié, "ASC" et l'"id_gpu_update"
            return redirect(url_for('gpu_gpumanufacturer_afficher', id_gpu_sel=id_gpu_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_gpu" et "GPU_Manufacturer" de la "t_gpumanufacturer"

            str_sql_id_gpu = "SELECT id_gpu, GPU_Brand, GPU_Name, GPU_Codename, GPU_Bus, GPU_Memory, GPU_Clock, Memory_Clock, GPU_TDP, GPU_Released FROM t_gpu WHERE id_gpu = %(value_id_gpu)s"

            valeur_select_dictionnaire = {"value_id_gpu": id_gpu_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_gpu, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom manufacturer" pour l'UPDATE
            data_gpu = mybd_conn.fetchone()
            print("data_gpu ", data_gpu, " type ", type(data_gpu), " gpumanufacturer ",
                  data_gpu["GPU_Name"])

            # Show la valeur sélectionnée dans le champ du formulaire "gpu_update_wtf.html"
            form_update_gpu.brand_gpu_update_wtf.data = data_gpu["GPU_Brand"]
            form_update_gpu.nom_gpu_update_wtf.data = data_gpu["GPU_Name"]
            form_update_gpu.gpu_codename_update_wtf.data = data_gpu["GPU_Codename"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" gpu codename ", data_gpu["GPU_Codename"], "  type ", type(data_gpu["GPU_Codename"]))
            form_update_gpu.gpu_bus_update_wtf.data = data_gpu["GPU_Bus"]
            form_update_gpu.gpu_memory_update_wtf.data = data_gpu["GPU_Memory"]
            form_update_gpu.gpu_clock_update_wtf.data = data_gpu["GPU_Clock"]
            form_update_gpu.gpu_memory_clock_update_wtf.data = data_gpu["Memory_Clock"]
            form_update_gpu.gpu_tdp_update_wtf.data = data_gpu["GPU_TDP"]
            form_update_gpu.gpu_released_update_wtf.data = data_gpu["GPU_Released"]

    except Exception as Exception_gpu_update_wtf:
        raise ExceptionGpuUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                    f"{gpu_update_wtf.__name__} ; "
                                    f"{Exception_gpu_update_wtf}")

    return render_template("gpu/gpu_update_wtf.html", form_update_gpu=form_update_gpu)


"""Effacer(delete) un gpu qui a été sélectionné dans le formulaire "gpu_gpumanufacturer_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /gpu_delete
    
Test : ex. cliquer sur le menu "gpu" puis cliquer sur le bouton "DELETE" d'un "gpu"
    
Paramètres : sans

Remarque :  Dans le champ "GPU_Name_delete_wtf" du formulaire "gpu/gpu_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/gpu_delete", methods=['GET', 'POST'])
def gpu_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_gpu_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_gpu"
    id_gpu_delete = request.values['id_gpu_btn_delete_html']

    # Objet formulaire pour effacer le gpu sélectionné.
    form_delete_gpu = FormWTFDeleteGpu()
    try:
        # Si on clique sur "ANNULER", afficher tous les gpu.
        if form_delete_gpu.submit_btn_annuler.data:
            return redirect(url_for("gpu_gpumanufacturer_afficher", id_gpu_sel=0))

        if form_delete_gpu.submit_btn_conf_del_gpu.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "gpu/gpu_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_gpu_delete = session['data_gpu_delete']
            print("data_gpu_delete ", data_gpu_delete)

            flash(f"Delete permanently the GPU !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer manufacturer" qui va irrémédiablement EFFACER le manufacturer
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_gpu.submit_btn_del_gpu.data:
            valeur_delete_dictionnaire = {"value_id_gpu": id_gpu_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_gpu_gpumanufacturer = """DELETE FROM t_gpumanufacturer_produce_gpu WHERE fk_gpu = %(value_id_gpu)s"""
            str_sql_delete_gpu = """DELETE FROM t_gpu WHERE id_gpu = %(value_id_gpu)s"""
            # Manière brutale d'effacer d'abord la "fk_gpu", même si elle n'existe pas dans la "t_gpumanufacturer_produce_gpu"
            # Ensuite on peut effacer le gpu vu qu'il n'est plus "lié" (INNODB) dans la "t_gpumanufacturer_produce_gpu"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_gpu_gpumanufacturer, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_gpu, valeur_delete_dictionnaire)

            flash(f"GPU permanently erased !!", "success")
            print(f"GPU permanently erased !!")

            # afficher les données
            return redirect(url_for('gpu_gpumanufacturer_afficher', id_gpu_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_gpu": id_gpu_delete}
            print(id_gpu_delete, type(id_gpu_delete))

            # Requête qui affiche le gpu qui doit être efffacé.
            str_sql_gpumanufacturer_gpu_delete = """SELECT * FROM t_gpu WHERE id_gpu = %(value_id_gpu)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_gpumanufacturer_gpu_delete, valeur_select_dictionnaire)
                data_gpu_delete = mydb_conn.fetchall()
                print("data_gpu_delete...", data_gpu_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "gpu/gpu_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_gpu_delete'] = data_gpu_delete

            # Le bouton pour l'action "DELETE" dans le form. "gpu_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_gpu_delete_wtf:
        raise ExceptionGpuDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                    f"{gpu_delete_wtf.__name__} ; "
                                    f"{Exception_gpu_delete_wtf}")

    return render_template("gpu/gpu_delete_wtf.html",
                           form_delete_gpu=form_delete_gpu,
                           btn_submit_del=btn_submit_del,
                           data_gpu_del=data_gpu_delete
                           )
