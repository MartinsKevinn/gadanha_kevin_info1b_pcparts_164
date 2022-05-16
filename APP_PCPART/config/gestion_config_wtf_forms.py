"""
    Fichier : gestion_config_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterConfig(FlaskForm):
    """
        Dans le formulaire "config_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_config_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_config_wtf = StringField("Clavioter la config ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_config_regexp,
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
    nom_config_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    config_use_case_update_wtf = StringField("Clavioter la config ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_config_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    config_rating_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])
    submit = SubmitField("Update config")


class FormWTFDeleteConfig(FlaskForm):
    """
        Dans le formulaire "config_delete_wtf.html"

        nom_config_delete_wtf : Champ qui reçoit la valeur de la config, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer une "config".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_config".
    """
    nom_config_delete_wtf = StringField("Effacer cette config")
    submit_btn_del = SubmitField("Effacer config")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")