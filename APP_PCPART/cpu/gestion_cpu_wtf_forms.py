"""Gestion des formulaires avec WTF pour les cpu
Fichier : gestion_cpu_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddCpu(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_cpu_add_wtf = StringField("Nom du cpu ", widget=TextArea())
    cpu_codename_wtf = StringField("Codename", widget=TextArea())
    cpu_cores_wtf = StringField("Cores", widget=TextArea())
    cpu_clock_wtf = StringField("Clock", widget=TextArea())
    cpu_socket_wtf = StringField("Socket", widget=TextArea())
    cpu_released_wtf = StringField("Release date", widget=TextArea())
    submit = SubmitField("Save cpu")


class FormWTFUpdateCpu(FlaskForm):
    """
        Dans le formulaire "cpu_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_cpu_update_wtf = StringField("Name", widget=TextArea())
    cpu_codename_update_wtf = StringField("Codename", widget=TextArea())
    cpu_cores_update_wtf = StringField("Cores", widget=TextArea())
    cpu_clock_update_wtf = StringField("Clock", widget=TextArea())
    cpu_socket_update_wtf = StringField("Socket", widget=TextArea())
    cpu_released_update_wtf = StringField("Release date", widget=TextArea())

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
