"""
    Fichier : gestion_motherboard_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAjouterMotherboard(FlaskForm):
    """
        Dans le formulaire "motherboard_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_motherboard_wtf = StringField("Motherboard Brand", widget=TextArea())
    model_motherboard_wtf = StringField("Motherboard Model", widget=TextArea())
    release_year_motherboard_wtf = DateField("Motherboard release year")
    submit = SubmitField("Save motherboard")


class FormWTFUpdateMotherboard(FlaskForm):
    """
        Dans le formulaire "motherboard_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_motherboard_update_wtf = StringField("Motherboard brand", widget=TextArea())
    model_motherboard_update_wtf = StringField("Motherboard model", widget=TextArea())
    release_year_motherboard_update_wtf = DateField("Motherboard release year")
    submit = SubmitField("Update motherboard")


class FormWTFDeleteMotherboard(FlaskForm):
    """
        Dans le formulaire "motherboard_delete_wtf.html"

        nom_motherboard_delete_wtf : Champ qui reçoit la valeur de la motherboard, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer une "motherboard".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_motherboard".
    """
    nom_motherboard_delete_wtf = StringField("Motherboard Brand")
    model_motherboard_delete_wtf = StringField("Motherboard Model")
    submit_btn_del = SubmitField("Delete motherboard")
    submit_btn_conf_del = SubmitField("Are you sure you want to delete it ?")
    submit_btn_annuler = SubmitField("Cancel")
