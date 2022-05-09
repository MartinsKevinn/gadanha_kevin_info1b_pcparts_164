"""Gestion des formulaires avec WTF pour les users
Fichier : gestion_user_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddUser(FlaskForm):
    """
        Dans le formulaire "userrole_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_film_regexp = ""
    user_firstname_add_wtf = StringField("user_firstname", widget=TextArea())
    user_lastname_add_wtf = StringField("user_lastname", widget=TextArea())
    user_birthdate_add_wtf = DateField("user_birthdate", validators=[InputRequired("Date obligatoire"),
                                                                  DataRequired("Date non valide")])

    submit = SubmitField("Enregistrer utilisateur")


class FormWTFUpdateUser(FlaskForm):
    """
        Dans le formulaire "user_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    user_firstname_update_wtf = StringField("Firstname", widget=TextArea())
    user_lastname_update_wtf = StringField("Lastname", widget=TextArea())
    user_birthdate_update_wtf = DateField("Birthdate", validators=[InputRequired("Date obligatoire"),
                                                                     DataRequired("Date non valide")])

    submit = SubmitField("Update utilisateur")


class FormWTFDeleteUser(FlaskForm):
    """
        Dans le formulaire "user_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_film_delete_wtf = StringField("Effacer cet utilisateur")
    submit_btn_del_user = SubmitField("Effacer utilisateur")
    submit_btn_conf_del_film = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
