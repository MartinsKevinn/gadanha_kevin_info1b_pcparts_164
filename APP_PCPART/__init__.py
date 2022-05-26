"""Initialisation des variables d'environnement
    Auteur : OM 2021.03.03 Indispensable pour définir les variables indispensables dans tout le projet.
"""
import sys

from environs import Env
from flask import Flask

try:
    try:
        obj_env = Env()
        obj_env.read_env()
        HOST_MYSQL = obj_env("HOST_MYSQL")
        USER_MYSQL = obj_env("USER_MYSQL")
        PASS_MYSQL = obj_env("PASS_MYSQL")
        PORT_MYSQL = int(obj_env("PORT_MYSQL"))
        NAME_BD_MYSQL = obj_env("NAME_BD_MYSQL")
        NAME_FILE_DUMP_SQL_BD = obj_env("NAME_FILE_DUMP_SQL_BD")

        ADRESSE_SRV_FLASK = obj_env("ADRESSE_SRV_FLASK")
        DEBUG_FLASK = obj_env("DEBUG_FLASK")
        PORT_FLASK = obj_env("PORT_FLASK")
        SECRET_KEY_FLASK = obj_env("SECRET_KEY_FLASK")

        # OM 2022.04.11 Début de l'application
        app = Flask(__name__, template_folder="templates")
        print("app.url_map ____> ", app.url_map)

    except Exception as erreur:
        print(f"45677564530 init application variables d'environnement ou avec le fichier (son nom, son contenu)\n"
              f"{__name__}, "
              f"{erreur.args[0]}, "
              f"{repr(erreur)}, "
              f"{type(erreur)}")
        sys.exit()

    """
        Tout commence ici. Il faut "indiquer" les routes de l'applicationn.    
        Dans l'application les lignes ci-dessous doivent se trouver ici... soit après l'instanciation de la classe "Flask"
    """
    from APP_PCPART.database import database_tools
    from APP_PCPART.essais_wtf_forms import gestion_essai_wtf
    from APP_PCPART.essais_wtf_forms import gestion_wtf_forms_demo_select
    from APP_PCPART.demos_om_164 import routes_demos

    # User
    from APP_PCPART.user import gestion_user_crud
    from APP_PCPART.user import gestion_user_wtf_forms

    # Userrole
    from APP_PCPART.userrole import gestion_userrole_crud
    from APP_PCPART.user_userrole import gestion_user_userrole_crud
    from APP_PCPART.erreurs import msg_avertissements

    # CPU
    from APP_PCPART.cpu_cpumanufacturer import gestion_cpu_cpumanufacturer_crud
    from APP_PCPART.cpumanufacturer import gestion_cpumanufacturer_crud
    from APP_PCPART.cpu import gestion_cpu_crud
    from APP_PCPART.cpu import gestion_cpu_wtf_forms

    # Config
    from APP_PCPART.config import gestion_config_crud
    from APP_PCPART.user_config import gestion_user_config_crud

    # Motherboard
    from APP_PCPART.motherboard import gestion_motherboard_crud
    from APP_PCPART.cpu_motherboard import gestion_cpu_motherboard_crud

    # Ram
    from APP_PCPART.ram import gestion_ram_crud

except Exception as Exception_init_app_pcpart_164:
    print(f"4567756434 Une erreur est survenue {type(Exception_init_app_pcpart_164)} dans"
          f"__init__ {Exception_init_app_pcpart_164.args}")
    sys.exit()
