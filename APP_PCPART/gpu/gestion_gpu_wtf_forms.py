"""Gestion des formulaires avec WTF pour les gpu
Fichier : gestion_gpu_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.widgets import TextArea


class FormWTFAddGpu(FlaskForm):
    """
        Dans le formulaire "gpumanufacturer_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    brand_gpu_add_wtf = StringField("GPU Brand", widget=TextArea())
    name_gpu_add_wtf = StringField("GPU Name", widget=TextArea())
    codename_gpu_add_wtf = StringField("GPU Codename", widget=TextArea())
    bus_gpu_add_wtf = StringField("GPU Bus", widget=TextArea())
    memory_gpu_add_wtf = StringField("GPU Memory", widget=TextArea())
    clock_gpu_add_wtf = IntegerField("GPU Clock")
    clock_memory_gpu_add_wtf = IntegerField("Memory Clock")
    tdp_gpu_add_wtf = IntegerField("GPU TDP")
    released_gpu_add_wtf = DateField("GPU Release date")

    submit = SubmitField("Save gpu")


class FormWTFUpdateGpu(FlaskForm):
    """
        Dans le formulaire "gpu_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    brand_gpu_update_wtf = StringField("GPU Brand", widget=TextArea())
    nom_gpu_update_wtf = StringField("GPU Name", widget=TextArea())
    gpu_codename_update_wtf = StringField("GPU Codename", widget=TextArea())
    gpu_bus_update_wtf = StringField("GPU Bus", widget=TextArea())
    gpu_memory_update_wtf = StringField("GPU Memory", widget=TextArea())
    gpu_clock_update_wtf = IntegerField("GPU Clock")
    gpu_memory_clock_update_wtf = IntegerField("Memory Clock")
    gpu_tdp_update_wtf = IntegerField("GPU TDP")
    gpu_released_update_wtf = DateField("GPU Release date")

    submit = SubmitField("Update gpu")


class FormWTFDeleteGpu(FlaskForm):
    """
        Dans le formulaire "gpu_delete_wtf.html"

        GPU_Name_delete_wtf : Champ qui reçoit la valeur du gpu, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "gpu".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_gpu".
    """
    GPU_Name_delete_wtf = StringField("Delete this GPU")
    submit_btn_del_gpu = SubmitField("Delete GPU")
    submit_btn_conf_del_gpu = SubmitField("Are you sure you want to delete ?")
    submit_btn_annuler = SubmitField("Cancel")
