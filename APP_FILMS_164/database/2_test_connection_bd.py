"""Démonstration d'envoi d'une requête SQL à la BD
Fichier : 2_test_connection_bd.py
Auteur : OM 2021.03.03
"""

from APP_FILMS_164.database.database_tools import DBconnection

try:
    """
        Une seule requête pour montrer la récupération des données de la BD en MySql.
    """
    strsql_userrole_afficher = """SELECT id_config, userpseudo, config_rating, config_use_case, cpu_manufacturer, cpu_name, CONCAT(motherboard_brand, ' ', motherboard_model),
CONCAT(aircooling_brand, ' ', aircooling_model), CONCAT(watercooling_brand, ' ', watercooling_model), CONCAT(ram_brand, ' ', ram_name), 
ram_capacity, CONCAT(gpu_brand, ' ', gpu_name), CONCAT(case_brand, ' ', case_model), CONCAT(supply_brand, ' ', supply_model), 
CONCAT(ssd_brand, ' ', ssd_model), ssd_capacity, CONCAT(hdd_brand, ' ', hdd_name), hdd_capacity
FROM t_config
LEFT JOIN t_config_has_cpu ON t_config.id_config = t_config_has_cpu.fk_config
LEFT JOIN t_cpu ON t_cpu.id_cpu = t_config_has_cpu.fk_cpu
LEFT JOIN t_cpumanufacturer_produce_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
LEFT JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
LEFT JOIN t_config_has_motherboard ON t_config.id_config = t_config_has_motherboard.fk_config
LEFT JOIN t_motherboard ON t_motherboard.id_motherboard = t_config_has_motherboard.fk_motherboard
LEFT JOIN t_config_has_ram ON t_config.id_config = t_config_has_ram.fk_config
LEFT JOIN t_ram ON t_ram.id_ram = t_config_has_ram.fk_ram
LEFT JOIN t_config_has_gpu ON t_config.id_config = t_config_has_gpu.fk_config
LEFT JOIN t_gpu ON t_gpu.id_gpu = t_config_has_gpu.fk_gpu
LEFT JOIN t_config_has_aircooling ON t_config.id_config = t_config_has_aircooling.fk_config
LEFT JOIN t_aircooling ON t_aircooling.id_aircooling = t_config_has_aircooling.fk_aircooling
LEFT JOIN t_config_has_watercooling ON t_config.id_config = t_config_has_watercooling.fk_config
LEFT JOIN t_watercooling ON t_watercooling.id_watercooling = t_config_has_watercooling.fk_watercooling
LEFT JOIN t_config_has_case ON t_config.id_config = t_config_has_case.fk_config
LEFT JOIN t_case ON t_case.id_case = t_config_has_case.fk_case
LEFT JOIN t_config_has_supply ON t_config.id_config = t_config_has_supply.fk_config
LEFT JOIN t_supply ON t_supply.id_supply = t_config_has_supply.fk_supply
LEFT JOIN t_config_has_ssd ON t_config.id_config = t_config_has_ssd.fk_config
LEFT JOIN t_ssd ON t_ssd.id_ssd = t_config_has_ssd.fk_ssd
LEFT JOIN t_config_has_hdd ON t_config.id_config = t_config_has_hdd.fk_config
LEFT JOIN t_hdd ON t_hdd.id_hdd = t_config_has_hdd.fk_hdd
LEFT JOIN t_user_created_config ON t_config.id_config = t_user_created_config.fk_config
LEFT JOIN t_user ON t_user.id_user = t_user_created_config.fk_user
INNER JOIN t_user_has_userpseudo ON t_user.id_user = t_user_has_userpseudo.fk_user
INNER JOIN t_userpseudo ON t_userpseudo.id_pseudo = t_user_has_userpseudo.fk_pseudo
WHERE userpseudo = 'Cricko';"""

    with DBconnection() as db:
        db.execute(strsql_userrole_afficher)
        result = db.fetchall()
        print("data_genres ", result, " Type : ", type(result))


except Exception as erreur:
    # print(f"2547821146 Connection à la BD Impossible ! {type(erreur)} args {erreur.args}")
    print(f"2547821146 Test connection BD !"
          f"{__name__,erreur} , "
          f"{repr(erreur)}, "
          f"{type(erreur)}")
