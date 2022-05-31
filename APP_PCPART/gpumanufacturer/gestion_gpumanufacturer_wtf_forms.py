"""
    Fichier : gestion_gpumanufacturer_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAjoutergpumanufacturer(FlaskForm):
    """
        Dans le formulaire "gpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_gpumanufacturer_wtf = StringField("Manufacturer ", widget=TextArea())
    submit = SubmitField("Save manufacturer")


class FormWTFUpdategpumanufacturer(FlaskForm):
    """
        Dans le formulaire "gpumanufacturer_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_gpumanufacturer_update_wtf = StringField("Manufacturer", widget=TextArea())
    submit = SubmitField("Update manufacturer")


class FormWTFDeletegpumanufacturer(FlaskForm):
    """
        Dans le formulaire "gpumanufacturer_delete_wtf.html"

        nom_gpumanufacturer_delete_wtf : Champ qui reçoit la valeur du manufacturer, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "manufacturer".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_gpumanufacturer".
    """
    nom_gpumanufacturer_delete_wtf = StringField("Delete this manufacturer")
    submit_btn_del = SubmitField("Delete manufacturer")
    submit_btn_conf_del = SubmitField("Are you sure you want to delete it ?")
    submit_btn_annuler = SubmitField("Cancel")
