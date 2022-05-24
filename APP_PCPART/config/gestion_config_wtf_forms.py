"""
    Fichier : gestion_config_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import *
from wtforms import *
from wtforms.validators import *


class FormWTFAjouterConfig(FlaskForm):
    """
        Dans le formulaire "config_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    config_use_case_wtf = SelectField("Config Use Case", choices=['Gaming', 'Work'])
    config_rating_wtf = SelectField("Config rating", choices=['1/5', '2/5', '3/5', '4/5', '5/5'])
    cpu_manufacturer_wtf = StringField("CPU Manufacturer")
    cpu_name_wtf = StringField("CPU Name")
    cpu_codename_wtf = StringField("CPU Codename")
    cpu_cores_wtf = StringField("CPU Cores")
    cpu_clock_wtf = StringField("CPU Clock")
    cpu_tdp_wtf = StringField("CPU TDP")
    cpu_released_wtf = StringField("CPU Released", validators=[InputRequired("Mandatory date"),
                                                               DataRequired("Invalid date")])
    motherboard_brand_wtf = StringField("Motherboard Brand")
    motherboard_model_wtf = StringField("Motherboard Model")
    motherboard_release_year_wtf = DateField("Motherboard Release Year", validators=[InputRequired("Mandatory date"),
                                                                                     DataRequired("Invalid date")])
    ram_brand_wtf = StringField("RAM Brand")
    ram_name_wtf = StringField("RAM Name")
    ram_capacity_wtf = StringField("RAM Capacity")
    ram_data_rate_wtf = StringField("RAM Data Rate")
    gpu_manufacturer_wtf = StringField("GPU Manufacturer")
    gpu_brand_wtf = StringField("GPU Brand")
    gpu_name_wtf = StringField("GPU Name")
    gpu_codename_wtf = StringField("GPU Codename")
    gpu_memory_wtf = StringField("GPU Memory")
    gpu_tdp_wtf = StringField("GPU TDP")
    gpu_released_wtf = DateField("GPU Released", validators=[InputRequired("Mandatory date"),
                                                             DataRequired("Invalid date")])
    supply_brand_wtf = StringField("Supply Brand")
    supply_model_wtf = StringField("Supply Model")
    supply_power_wtf = StringField("Supply Power")
    supply_certification_wtf = StringField("Supply Certification")
    ssd_brand_wtf = StringField("SSD Brand")
    ssd_model_wtf = StringField("SSD Model")
    ssd_interface_wtf = StringField("SSD Interface")
    ssd_form_factor_wtf = StringField("SSD Form Factor")
    ssd_capacity_wtf = StringField("SSD Capacity")
    ssd_nand_type_wtf = StringField("SSD Nand Type")
    hdd_brand_wtf = StringField("HDD Brand")
    hdd_model_wtf = StringField("HDD Model")
    hdd_interface_wtf = StringField("HDD Interface")
    hdd_capacity_wtf = StringField("HDD Capacity")
    hdd_rpm_wtf = StringField("HDD RPM")
    case_brand_wtf = StringField("Case Brand")
    case_model_wtf = StringField("Case Model")
    case_color_wtf = StringField("Case Color")
    aircooling_brand_wtf = StringField("Aircooling Brand")
    aircooling_model_wtf = StringField("Aircooling Model")
    aircooling_dimensions_wtf = StringField("Aircooling Dimensions")
    aircooling_fans_wtf = StringField("Aircooling Fans")
    aircooling_socket_support_wtf = StringField("Aircooling Socket Support")
    aircooling_fan_speed_wtf = StringField("Aircooling Fan Speed")
    watercooling_brand_wtf = StringField("Watercooling Brand")
    watercooling_model_wtf = StringField("Watercooling Model")
    watercooling_dimensions_wtf = StringField("Watercooling Dimensions")
    watercooling_scale_wtf = StringField("Watercooling Scale")
    watercooling_socket_support_wtf = StringField("Watercooling Socket Support")
    watercooling_fan_speed_wtf = StringField("Watercooling Fan Speed")

    submit = SubmitField("Save config")


class FormWTFUpdateConfig(FlaskForm):
    """
        Dans le formulaire "config_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    config_use_case_update_wtf = SelectField("Config Use Case", choices=['Gaming', 'Work'])
    config_rating_update_wtf = SelectField("Config rating", choices=['1/5', '2/5', '3/5', '4/5', '5/5'])
    submit = SubmitField("Update config")


class FormWTFDeleteConfig(FlaskForm):
    """
        Dans le formulaire "config_delete_wtf.html"

        config_use_case_delete_wtf : Champ qui reçoit la valeur de la config, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer une "config".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_config".
    """
    config_use_case_delete_wtf = StringField("Delete this configuration")

    submit_btn_del = SubmitField("Delete configuration")
    submit_btn_conf_del = SubmitField("Are you sure you want to delete ?")
    submit_btn_annuler = SubmitField("Cancel")
