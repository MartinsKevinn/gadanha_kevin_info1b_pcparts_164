"""
    Fichier : gestion_userrole_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterUserrole(FlaskForm):
    """
        Dans le formulaire "userrole_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_userrole_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_userrole_wtf = StringField("Role", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_userrole_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Save role")


class FormWTFUpdateUserrole(FlaskForm):
    """
        Dans le formulaire "userrole_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_userrole_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_userrole_update_wtf = StringField("Role", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_userrole_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    submit = SubmitField("Update role")


class FormWTFDeleteUserrole(FlaskForm):
    """
        Dans le formulaire "userrole_delete_wtf.html"

        nom_userrole_delete_wtf : Champ qui reçoit la valeur du userrole, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "userrole".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_userrole".
    """
    nom_userrole_delete_wtf = StringField("Delete this role")
    submit_btn_del = SubmitField("Delete role")
    submit_btn_conf_del = SubmitField("Are you sure you want to delete it ?")
    submit_btn_annuler = SubmitField("Cancel")
