"""
    Fichier : gestion_cpumanufacturer_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAjouterCpumanufacturer(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_cpumanufacturer_wtf = StringField("Manufacturer ", widget=TextArea())
    submit = SubmitField("Save manufacturer")


class FormWTFUpdateCpumanufacturer(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_cpumanufacturer_update_wtf = StringField("Manufacturer", widget=TextArea())
    submit = SubmitField("Update manufacturer")


class FormWTFDeleteCpumanufacturer(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_delete_wtf.html"

        nom_cpumanufacturer_delete_wtf : Champ qui reçoit la valeur du manufacturer, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "manufacturer".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_cpumanufacturer".
    """
    nom_cpumanufacturer_delete_wtf = StringField("Delete this manufacturer")
    submit_btn_del = SubmitField("Delete manufacturer")
    submit_btn_conf_del = SubmitField("Are you sure you want to delete it ?")
    submit_btn_annuler = SubmitField("Cancel")
