/* Requêtes avec des variables en exemple */

/* Liste par rapport au composant choisi */
SELECT * 
FROM $VarComponent;

/* Liste par rapport au composant choisi avec un filtre*/
SELECT * 
FROM $VarComponent
WHERE $VarFilter IS ;






/* Vérification des compatibilités entre les CPUs et les motherboards */
SELECT CONCAT(cpu_manufacturer, ' ', cpu_name), CONCAT(motherboard_brand, ' ', motherboard_model)
FROM t_cpu
INNER JOIN t_cpu_compatible_motherboard ON t_cpu.id_cpu = t_cpu_compatible_motherboard.fk_cpu
INNER JOIN t_motherboard ON t_motherboard.id_motherboard = t_cpu_compatible_motherboard.fk_motherboard
LEFT JOIN t_cpumanufacturer_produce_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
LEFT JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
GROUP BY motherboard_socket;

/* Voir la RAM compatible avec le cpu choisi */
SELECT CONCAT(ram_brand, ' ', ram_name), CONCAT(cpu_manufacturer, ' ', cpu_name)
FROM t_cpu
INNER JOIN t_ram ON t_ram.id_ram = t_ram_is_ramgen.fk_ram
INNER JOIN t_ram_is_ramgen ON t_ram_is_ramgen.fk_ram = t_ram.id_ram
INNER JOIN t_cpu_compatible_ramgen ON t_cpu_compatible_ramgen.fk_cpu = t_cpu.id_cpu
INNER JOIN t_ramgen ON t_ramgen.id_ramgen = t_cpu_compatible_ramgen.fk_ramgen
LEFT JOIN t_cpumanufacturer_produce_cpu ON t_cpu.id_cpu = t_cpumanufacturer_produce_cpu.fk_cpu
LEFT JOIN t_cpumanufacturer ON t_cpumanufacturer.id_cpu_manufacturer = t_cpumanufacturer_produce_cpu.fk_cpumanufacturer
WHERE cpu_name = 'ryzen 5800x';




/* Recherche des composants avec les informations principales d'une config par rapport au pseudo de l'utilisateur qui l'a créé. */
SELECT id_config, userpseudo, config_rating, config_use_case, cpu_manufacturer, cpu_name, CONCAT(motherboard_brand, ' ', motherboard_model),
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
WHERE userpseudo = 'Cricko';

/* Recherche de toutes les configurations avec leurs composants et les informations principales */
SELECT config_rating, config_use_case, cpu_manufacturer, cpu_name, CONCAT(motherboard_brand, ' ', motherboard_model),
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
ORDER BY id_config;

/* Recherche des configurations par rapport au style de configuration que c'est, avec leurs composants et les informations principales */
SELECT config_rating, config_use_case, cpu_manufacturer, cpu_name, CONCAT(motherboard_brand, ' ', motherboard_model),
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
WHERE config_use_case = 'Gaming';

/* Recherche des configurations par rapport à la note, avec leurs composants et les informations principales */
SELECT config_rating, config_use_case, cpu_manufacturer, cpu_name, CONCAT(motherboard_brand, ' ', motherboard_model),
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
WHERE config_rating = '3';

/* Liste des utilisateurs par pseudo avec leur nom et prénom et mail et role si ils l'ont renseigné */
SELECT id_user, user_firstname, user_lastname, userpseudo, mail
FROM t_user
RIGHT JOIN t_user_has_userpseudo ON t_user.id_user = t_user_has_userpseudo.fk_user
RIGHT JOIN t_userpseudo ON t_userpseudo.id_pseudo = t_user_has_userpseudo.fk_pseudo
LEFT JOIN t_user_has_usermail ON t_user.id_user = t_user_has_usermail.fk_user
LEFT JOIN t_usermail ON t_usermail.id_mail = t_user_has_usermail.fk_mail
LEFT JOIN t_user_has_userrole ON t_user.id_user = t_user_has_userrole.fk_user
LEFT JOIN t_userrole ON t_userrole.id_userrole = t_user_has_userrole.fk_userrole;

/* Création d'une configuration */
INSERT INTO t_config (config_use_case, config_rating)
VALUES (NULL, NULL);

INSERT INTO t_config_has_cpu (fk_config, fk_cpu)
VALUES (4, 1);

INSERT INTO t_config_has_motherboard (fk_config, fk_motherboard)
VALUES (4, 1);

INSERT INTO t_config_has_ram (fk_config, fk_ram)
VALUES (4, 1);

INSERT INTO t_config_has_aircooling (fk_config, fk_aircooling)
VALUES (4, 1);

INSERT INTO t_config_has_gpu (fk_config, fk_gpu)
VALUES (4, 1);

INSERT INTO t_config_has_supply (fk_config, fk_supply)
VALUES (4, 1);

INSERT INTO t_config_has_case (fk_config, fk_case)
VALUES (4, 1);

INSERT INTO t_config_has_ssd (fk_config, fk_ssd)
VALUES (4, 1);

INSERT INTO t_config_has_hdd (fk_config, fk_hdd)
VALUES (4, 1);




/* Gestion des utilisateurs */

CREATE USER 'UserTest1'
IDENTIFIED BY 'PseudoForUserTest1';

DROP USER 'UserTest1';


GRANT SELECT
ON *
TO UserTest1;

GRANT SELECT
ON *
TO UserTest1;

SHOW GRANTS FOR UserTest1;

/*REVOKE ALL PRIVILEGES
ON *
TO UserTest1;*/


/* Backup de la DB */

/*BACKUP DATABASE gadanha_kevin_info1b_pcparts
TO DISK = 'C:\uWamp\UwAmp';*/