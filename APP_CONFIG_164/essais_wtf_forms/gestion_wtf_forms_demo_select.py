"""
    Fichier : gestion_userrole_crud.py
    Auteur : OM 2021.03.16
    Gestions des "routes" FLASK et des données pour les userrole.
"""
import sys

import pymysql
from flask import flash
from flask import render_template
from flask import request
from flask import session

from APP_CONFIG_164 import app
from APP_CONFIG_164.database.database_tools import DBconnection
from APP_CONFIG_164.erreurs.msg_erreurs import *
from APP_CONFIG_164.essais_wtf_forms.wtf_forms_demo_select import DemoFormSelectWTF

"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /userrole_delete
    
    Test : ex. cliquer sur le menu "userrole" puis cliquer sur le bouton "DELETE" d'un "role"
    
    Paramètres : sans
    
    But : Effacer(delete) un role qui a été sélectionné dans le formulaire "userrole_afficher.html"
    
    Remarque :  Dans le champ "nom_userrole_delete_wtf" du formulaire "userrole/userrole_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/demo_select_wtf", methods=['GET', 'POST'])
def demo_select_wtf():
    userrole_selectionne = None
    # Objet formulaire pour montrer une liste déroulante basé sur la table "t_userrole"
    form_demo = DemoFormSelectWTF()
    try:
        if request.method == "POST" and form_demo.submit_btn_ok_dplist_userrole.data:

            if form_demo.submit_btn_ok_dplist_userrole.data:
                print("Role sélectionné : ",
                      form_demo.userrole_dropdown_wtf.data)
                userrole_selectionne = form_demo.userrole_dropdown_wtf.data
                form_demo.userrole_dropdown_wtf.choices = session['userrole_val_list_dropdown']

        if request.method == "GET":
            with DBconnection() as mc_afficher:
                strsql_userrole_afficher = """SELECT id_userrole, userrole FROM t_userrole ORDER BY id_userrole ASC"""
                mc_afficher.execute(strsql_userrole_afficher)

            data_userrole = mc_afficher.fetchall()
            print("demo_select_wtf data_userrole ", data_userrole, " Type : ", type(data_userrole))

            """
                Préparer les valeurs pour la liste déroulante de l'objet "form_demo"
                la liste déroulante est définie dans le "wtf_forms_demo_select.py" 
                le formulaire qui utilise la liste déroulante "zzz_essais_om_104/demo_form_select_wtf.html"
            """
            userrole_val_list_dropdown = []
            for i in data_userrole:
                userrole_val_list_dropdown.append(i['userrole'])

            # Aussi possible d'avoir un id numérique et un texte en correspondance
            # userrole_val_list_dropdown = [(i["id_userrole"], i["userrole"]) for i in data_userrole]

            print("userrole_val_list_dropdown ", userrole_val_list_dropdown)

            form_demo.userrole_dropdown_wtf.choices = userrole_val_list_dropdown
            session['userrole_val_list_dropdown'] = userrole_val_list_dropdown
            # Ceci est simplement une petite démo. on fixe la valeur PRESELECTIONNEE de la liste
            form_demo.userrole_dropdown_wtf.data = "philosophique"
            userrole_selectionne = form_demo.userrole_dropdown_wtf.data
            print("role choisi dans la liste :", userrole_selectionne)
            session['userrole_selectionne_get'] = userrole_selectionne

    # OM 2020.04.16 ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
    except KeyError:
        flash(f"__KeyError dans wtf_forms_demo_select : {sys.exc_info()[0]} {sys.exc_info()[1]} {sys.exc_info()[2]}",
              "danger")
    except ValueError:
        flash(f"Erreur dans wtf_forms_demo_select : {sys.exc_info()[0]} {sys.exc_info()[1]}", "danger")
    except (pymysql.err.OperationalError,
            pymysql.ProgrammingError,
            pymysql.InternalError,
            pymysql.err.IntegrityError,
            TypeError) as erreur_gest_userrole_crud:
        code, msg = erreur_gest_userrole_crud.args
        flash(f"attention : {error_codes.get(code, msg)} {erreur_gest_userrole_crud} ", "danger")

        flash(f"Erreur dans wtf_forms_demo_select : {sys.exc_info()[0]} "
              f"{erreur_gest_userrole_crud.args[0]} , "
              f"{erreur_gest_userrole_crud}", "danger")

        flash(f"__KeyError dans wtf_forms_demo_select : {sys.exc_info()[0]} {sys.exc_info()[1]} {sys.exc_info()[2]}",
              "danger")

    return render_template("zzz_essais_om_104/demo_form_select_wtf.html",
                           form=form_demo,
                           userrole_selectionne=userrole_selectionne,
                           data_userrole_drop_down=data_userrole)


@app.route("/demo_select_dropdown_bootstrap", methods=['GET', 'POST'])
def demo_select_dropdown_bootstrap():
    print("userrole choisi dans la liste :")
    if request.method == 'POST':
        choix_list_drop_down = request.form.getlist("ma_petite_liste_unique")
        print("choix_list_drop_down ", choix_list_drop_down)
        for x in choix_list_drop_down:
            print("x", x)
    return render_template("zzz_essais_om_104/essai_form_result_dropdown.html")