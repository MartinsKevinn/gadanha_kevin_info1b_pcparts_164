"""
    Fichier : gestion_cpumanufacturer_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterCpumanufacturer(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_cpumanufacturer_regexp = "([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_cpumanufacturer_wtf = StringField("Manufacturer ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_cpumanufacturer_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Save manufacturer")


class FormWTFUpdateCpumanufacturer(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_cpumanufacturer_update_regexp = "([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_cpumanufacturer_update_wtf = StringField("Manufacturer", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                        Regexp(nom_cpumanufacturer_update_regexp,
                                                                               message="Pas de chiffres, de "
                                                                                       "caractères "
                                                                                       "spéciaux, "
                                                                                       "d'espace à double, de double "
                                                                                       "apostrophe, de double trait "
                                                                                       "union")
                                                                        ])
    submit = SubmitField("Update manufacturer")


class FormWTFDeleteCpumanufacturer(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_delete_wtf.html"

        nom_cpumanufacturer_delete_wtf : Champ qui reçoit la valeur du manufacturer, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "manufacturer".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_cpumanufacturer".
    """
    nom_cpumanufacturer_delete_wtf = StringField("Effacer ce manufacturer")
    submit_btn_del = SubmitField("Effacer manufacturer")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
