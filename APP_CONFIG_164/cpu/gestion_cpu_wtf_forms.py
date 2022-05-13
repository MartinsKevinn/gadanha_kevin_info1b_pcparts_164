"""Gestion des formulaires avec WTF pour les cpu
Fichier : gestion_cpu_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddCpu(FlaskForm):
    """
        Dans le formulaire "cpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_film_regexp = ""
    nom_cpu_add_wtf = StringField("Nom du cpu ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(nom_film_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])

    submit = SubmitField("Enregistrer cpu")


class FormWTFUpdateCpu(FlaskForm):
    """
        Dans le formulaire "cpu_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_cpu_update_wtf = StringField("Name", widget=TextArea())
    cpu_codename_update_wtf = StringField("Codename", widget=TextArea())
    cpu_cores_update_wtf = StringField("Cores", widget=TextArea())
    cpu_clock_update_wtf = StringField("Clock", widget=TextArea())
    cpu_socket_update_wtf = StringField("Socket", widget=TextArea())

    submit = SubmitField("Update cpu")


class FormWTFDeleteCpu(FlaskForm):
    """
        Dans le formulaire "cpu_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du cpu, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "cpu".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_cpu".
    """
    nom_film_delete_wtf = StringField("Effacer ce cpu")
    submit_btn_del_cpu = SubmitField("Effacer cpu")
    submit_btn_conf_del_cpu = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
