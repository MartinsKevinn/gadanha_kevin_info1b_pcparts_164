"""Gestion des formulaires avec WTF pour les gpu
Fichier : gestion_gpu_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAddCpu(FlaskForm):
    """
        Dans le formulaire "gpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    name_gpu_add_wtf = StringField("CPU Name ", widget=TextArea())
    codename_gpu_add_wtf = StringField("CPU Codename", widget=TextArea())
    cores_gpu_add_wtf = StringField("CPU Cores", widget=TextArea())
    clock_gpu_add_wtf = StringField("CPU Clock", widget=TextArea())
    socket_gpu_add_wtf = StringField("CPU Socket", widget=TextArea())
    released_gpu_add_wtf = DateField("CPU Release date")
    submit = SubmitField("Save gpu")


class FormWTFUpdateCpu(FlaskForm):
    """
        Dans le formulaire "gpu_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_gpu_update_wtf = StringField("CPU Name", widget=TextArea())
    gpu_codename_update_wtf = StringField("CPU Codename", widget=TextArea())
    gpu_cores_update_wtf = StringField("CPU Cores", widget=TextArea())
    gpu_clock_update_wtf = StringField("CPU Clock", widget=TextArea())
    gpu_socket_update_wtf = StringField("CPU Socket", widget=TextArea())
    gpu_released_update_wtf = DateField("CPU Release date")

    submit = SubmitField("Update gpu")


class FormWTFDeleteCpu(FlaskForm):
    """
        Dans le formulaire "gpu_delete_wtf.html"

        CPU_Name_delete_wtf : Champ qui reçoit la valeur du gpu, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "gpu".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_gpu".
    """
    CPU_Name_delete_wtf = StringField("Delete this CPU")
    submit_btn_del_gpu = SubmitField("Delete CPU")
    submit_btn_conf_del_gpu = SubmitField("Are you sure you want to delete ?")
    submit_btn_annuler = SubmitField("Cancel")
