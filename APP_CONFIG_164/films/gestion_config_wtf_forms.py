"""Gestion des formulaires avec WTF pour les configs
Fichier : gestion_config_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddConfig(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_film_regexp = ""
    config_use_case_add_wtf = StringField("Config use case", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(nom_film_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])

    submit = SubmitField("Enregistrer config")


class FormWTFUpdateConfig(FlaskForm):
    """
        Dans le formulaire "config_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    config_use_case_update_wtf = StringField("Use case", widget=TextArea())
    config_rating_update_wtf = StringField("Rate", widget=TextArea())
    
    submit = SubmitField("Update film")


class FormWTFDeleteConfig(FlaskForm):
    """
        Dans le formulaire "config_delete_wtf.html"

        config_use_case_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_config".
    """
    config_use_case_delete_wtf = StringField("Effacer ce film")
    submit_btn_del_config = SubmitField("Effacer film")
    submit_btn_conf_del_config = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
