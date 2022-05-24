"""Gestion des formulaires avec WTF pour les users
Fichier : gestion_user_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAddUser(FlaskForm):
    """
        Dans le formulaire "userrole_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_user_regexp = ""
    user_firstname_add_wtf = StringField("Firstname", widget=TextArea())
    user_lastname_add_wtf = StringField("Lastname", widget=TextArea())
    user_birthdate_add_wtf = DateField("Birthdate", validators=[InputRequired("Mandatory date"),
                                                                DataRequired("Invalid date")])
    user_photo_add_wtf = StringField("Photo", widget=TextArea())

    submit = SubmitField("Save user")


class FormWTFUpdateUser(FlaskForm):
    """
        Dans le formulaire "user_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    user_firstname_update_wtf = StringField("Firstname", widget=TextArea())
    user_lastname_update_wtf = StringField("Lastname", widget=TextArea())
    user_birthdate_update_wtf = DateField("Birthdate", validators=[InputRequired("Mandatory date"),
                                                                   DataRequired("Invalid date")])
    user_photo_update_wtf = StringField("Photo", widget=TextArea())
    submit = SubmitField("Update user")


class FormWTFDeleteUser(FlaskForm):
    """
        Dans le formulaire "user_delete_wtf.html"

        nom_user_delete_wtf : Champ qui reçoit la valeur du user, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "user".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_user".
    """
    nom_user_delete_wtf = StringField("Delete this user")
    submit_btn_del_user = SubmitField("Delete user")
    submit_btn_conf_del_user = SubmitField("Are you sure you want to delete ?")
    submit_btn_annuler = SubmitField("Cancel")
