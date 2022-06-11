"""
    Fichier : gestion_ram_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAjouterRam(FlaskForm):
    """
        Dans le formulaire "motherboard_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    brand_ram_wtf = StringField("Ram Brand", widget=TextArea())
    name_ram_wtf = StringField("Ram name", widget=TextArea())
    capacity_ram_wtf = StringField("Ram capacity", widget=TextArea())
    timings_ram_wtf = StringField("Ram timings", widget=TextArea())
    data_rate_ram_wtf = StringField("Ram data rate", widget=TextArea())
    submit = SubmitField("Save ram")


class FormWTFUpdateRam(FlaskForm):
    """
        Dans le formulaire "motherboard_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    brand_ram_update_wtf = StringField("Ram brand", widget=TextArea())
    name_ram_update_wtf = StringField("Ram name", widget=TextArea())
    capacity_ram_update_wtf = StringField("Ram capacity", widget=TextArea())
    timings_ram_update_wtf = StringField("Ram timings", widget=TextArea())
    data_rate_ram_update_wtf = StringField("Ram data rate", widget=TextArea())
    submit = SubmitField("Update ram")


class FormWTFDeleteRam(FlaskForm):
    """
        Dans le formulaire "motherboard_delete_wtf.html"

        nom_motherboard_delete_wtf : Champ qui reçoit la valeur de la motherboard, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer une "motherboard".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_motherboard".
    """
    brand_ram_delete_wtf = StringField("Ram Brand")
    name_ram_delete_wtf = StringField("Ram Name")
    submit_btn_del = SubmitField("Delete ram")
    submit_btn_conf_del = SubmitField("Are you sure you want to delete it ?")
    submit_btn_annuler = SubmitField("Cancel")
