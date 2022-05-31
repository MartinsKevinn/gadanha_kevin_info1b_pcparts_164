"""Gestion des formulaires avec WTF pour les cpu
Fichier : gestion_cpu_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAddCpu(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    name_cpu_add_wtf = StringField("CPU Name ", widget=TextArea())
    codename_cpu_add_wtf = StringField("CPU Codename", widget=TextArea())
    cores_cpu_add_wtf = StringField("CPU Cores", widget=TextArea())
    clock_cpu_add_wtf = StringField("CPU Clock", widget=TextArea())
    socket_cpu_add_wtf = StringField("CPU Socket", widget=TextArea())
    released_cpu_add_wtf = DateField("CPU Release date")
    submit = SubmitField("Save cpu")


class FormWTFUpdateCpu(FlaskForm):
    """
        Dans le formulaire "cpu_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_cpu_update_wtf = StringField("CPU Name", widget=TextArea())
    cpu_codename_update_wtf = StringField("CPU Codename", widget=TextArea())
    cpu_cores_update_wtf = StringField("CPU Cores", widget=TextArea())
    cpu_clock_update_wtf = StringField("CPU Clock", widget=TextArea())
    cpu_socket_update_wtf = StringField("CPU Socket", widget=TextArea())
    cpu_released_update_wtf = DateField("CPU Release date")

    submit = SubmitField("Update cpu")


class FormWTFDeleteCpu(FlaskForm):
    """
        Dans le formulaire "cpu_delete_wtf.html"

        CPU_Name_delete_wtf : Champ qui reçoit la valeur du cpu, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "cpu".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_cpu".
    """
    CPU_Name_delete_wtf = StringField("Delete this CPU")
    submit_btn_del_cpu = SubmitField("Delete CPU")
    submit_btn_conf_del_cpu = SubmitField("Are you sure you want to delete ?")
    submit_btn_annuler = SubmitField("Cancel")
