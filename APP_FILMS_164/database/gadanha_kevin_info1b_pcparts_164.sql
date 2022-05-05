-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
--

-- Database: gadanha_kevin_info1b_pcparts_164
-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS gadanha_kevin_info1b_pcparts_164;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS gadanha_kevin_info1b_pcparts_164;

-- Utilisation de cette base de donnée

USE gadanha_kevin_info1b_pcparts_164;


-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 23, 2022 at 07:47 AM
-- Server version: 5.7.11
-- PHP Version: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gadanha_kevin_info1b_pcparts_164`
--

-- --------------------------------------------------------

--
-- Table structure for table `t_aircooling`
--

CREATE TABLE `t_aircooling` (
  `id_aircooling` int(11) NOT NULL,
  `aircooling_brand` varchar(50) DEFAULT NULL,
  `aircooling_model` varchar(50) DEFAULT NULL,
  `aircooling_dimensions` varchar(50) DEFAULT NULL,
  `aircooling_fans` varchar(50) DEFAULT NULL,
  `aircooling_socket_support` varchar(350) DEFAULT NULL,
  `aircooling_fan_speed` varchar(25) DEFAULT NULL,
  `aircooling_noise_level` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_aircooling`
--

INSERT INTO `t_aircooling` (`id_aircooling`, `aircooling_brand`, `aircooling_model`, `aircooling_dimensions`, `aircooling_fans`, `aircooling_socket_support`, `aircooling_fan_speed`, `aircooling_noise_level`) VALUES
(1, 'Cooler Master', 'MasterAir MA624 Stealth', '165.1 x 149.4 x 127.0 mm', '2x 140 x 25 mm', '115x, 1366, 1200, 2011x, 2066; FM2(+), FM1, AM2(+), AM3(+), AM4', NULL, 'Max 27dB(A)'),
(2, 'Noctua', 'NH-U14S', '171.45 x 151.4 x 52.3mm', '1x 140 x 25mm', 'Intel: LGA2066, LGA2011-0 & LGA2011-3 (Square ILM), LGA1200, LGA1156, LGA1155, LGA1151, LGA1150 & AMD: AM2, AM2+, AM3, AM3+, FM1, FM2, FM2+ (backplate requis), AM4 (included since 2019, older coolers require NM-AM4-UxS)', '300–1500RPM', 'Max 24,6 dB(A)'),
(3, 'Deepcool ', 'Assassin III', '171.5 x 139.7 x 133.4mm', '2x 140 x 25mm', '115x, 1366, 2011x, 2066; FM2(+), FM1, AM2(+), AM3(+), AM4', NULL, NULL),
(4, 'Noctua ', 'NH-D15 Chromax Black', '161 x 150 x 165mm', '2x 140 x 25mm', 'Intel LGA: 1150, 1151, 1155, 1156, 1200, 2011, 2011-3, 2066, AMD: AM4, AM3, AM2, FM2 & FM1', '300–1500RPM', 'Max 24.6dB(A)');

-- --------------------------------------------------------

--
-- Table structure for table `t_case`
--

CREATE TABLE `t_case` (
  `id_case` int(11) NOT NULL,
  `case_brand` varchar(20) DEFAULT NULL,
  `case_model` varchar(40) DEFAULT NULL,
  `case_color` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_case`
--

INSERT INTO `t_case` (`id_case`, `case_brand`, `case_model`, `case_color`) VALUES
(1, 'Cooler Master', 'H500P', 'White');

-- --------------------------------------------------------

--
-- Table structure for table `t_case_is_format`
--

CREATE TABLE `t_case_is_format` (
  `id_case_is_format` int(11) NOT NULL,
  `fk_case` int(11) NOT NULL,
  `fk_format` int(11) NOT NULL,
  `date_case_is_format` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_case_is_format`
--

INSERT INTO `t_case_is_format` (`id_case_is_format`, `fk_case`, `fk_format`, `date_case_is_format`) VALUES
(1, 1, 2, '2022-03-13 10:17:39');

-- --------------------------------------------------------

--
-- Table structure for table `t_config`
--

CREATE TABLE `t_config` (
  `id_config` int(11) NOT NULL,
  `config_use_case` set('Gaming','Work','Home') DEFAULT NULL,
  `config_rating` enum('5','4','3','2','1') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config`
--

INSERT INTO `t_config` (`id_config`, `config_use_case`, `config_rating`) VALUES
(1, 'Gaming', '4'),
(2, 'Gaming,Work', '5'),
(3, 'Gaming', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_aircooling`
--

CREATE TABLE `t_config_has_aircooling` (
  `id_config_has_aircooling` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_aircooling` int(11) NOT NULL,
  `date_config_has_aircooling` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_aircooling`
--

INSERT INTO `t_config_has_aircooling` (`id_config_has_aircooling`, `fk_config`, `fk_aircooling`, `date_config_has_aircooling`) VALUES
(1, 1, 2, '2022-03-14 18:39:58'),
(2, 3, 3, '2022-03-18 07:20:34');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_case`
--

CREATE TABLE `t_config_has_case` (
  `id_config_has_case` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_case` int(11) NOT NULL,
  `date_config_has_case` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_case`
--

INSERT INTO `t_config_has_case` (`id_config_has_case`, `fk_config`, `fk_case`, `date_config_has_case`) VALUES
(1, 1, 1, '2022-03-14 18:40:19'),
(2, 2, 1, '2022-03-17 18:25:12');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_cpu`
--

CREATE TABLE `t_config_has_cpu` (
  `id_config_has_cpu` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_cpu` int(11) NOT NULL,
  `date_config_has_cpu` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_cpu`
--

INSERT INTO `t_config_has_cpu` (`id_config_has_cpu`, `fk_config`, `fk_cpu`, `date_config_has_cpu`) VALUES
(1, 1, 184, '2022-03-14 18:41:16'),
(2, 2, 183, '2022-03-17 18:24:27'),
(3, 3, 236, '2022-03-18 07:21:21');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_gpu`
--

CREATE TABLE `t_config_has_gpu` (
  `id_config_has_gpu` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_gpu` int(11) NOT NULL,
  `date_config_has_gpu` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_gpu`
--

INSERT INTO `t_config_has_gpu` (`id_config_has_gpu`, `fk_config`, `fk_gpu`, `date_config_has_gpu`) VALUES
(1, 1, 7, '2022-03-14 18:41:39'),
(2, 2, 3, '2022-03-17 18:33:05');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_hdd`
--

CREATE TABLE `t_config_has_hdd` (
  `id_config_has_hdd` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_hdd` int(11) NOT NULL,
  `date_config_has_hdd` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_hdd`
--

INSERT INTO `t_config_has_hdd` (`id_config_has_hdd`, `fk_config`, `fk_hdd`, `date_config_has_hdd`) VALUES
(1, 1, 1, '2022-03-14 19:48:49'),
(2, 3, 2, '2022-03-18 07:42:35');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_motherboard`
--

CREATE TABLE `t_config_has_motherboard` (
  `id_config_has_motherboard` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_motherboard` int(11) NOT NULL,
  `date_config_has_motherboard` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_motherboard`
--

INSERT INTO `t_config_has_motherboard` (`id_config_has_motherboard`, `fk_config`, `fk_motherboard`, `date_config_has_motherboard`) VALUES
(1, 1, 3, '2022-03-14 18:43:14'),
(2, 2, 3, '2022-03-17 18:31:48'),
(3, 3, 6, '2022-03-18 07:25:19');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_ram`
--

CREATE TABLE `t_config_has_ram` (
  `id_config_has_ram` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_ram` int(11) NOT NULL,
  `date_config_has_ram` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_ram`
--

INSERT INTO `t_config_has_ram` (`id_config_has_ram`, `fk_config`, `fk_ram`, `date_config_has_ram`) VALUES
(1, 1, 5, '2022-03-14 19:05:03'),
(2, 2, 4, '2022-03-17 18:26:15'),
(3, 3, 1, '2022-03-18 07:25:57');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_ssd`
--

CREATE TABLE `t_config_has_ssd` (
  `id_config_has_ssd` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_ssd` int(11) NOT NULL,
  `date_config_has_ssd` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_ssd`
--

INSERT INTO `t_config_has_ssd` (`id_config_has_ssd`, `fk_config`, `fk_ssd`, `date_config_has_ssd`) VALUES
(2, 1, 17, '2022-03-14 19:05:57'),
(3, 2, 16, '2022-03-17 18:33:50');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_supply`
--

CREATE TABLE `t_config_has_supply` (
  `id_config_has_supply` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_supply` int(11) NOT NULL,
  `date_config_has_supply` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_supply`
--

INSERT INTO `t_config_has_supply` (`id_config_has_supply`, `fk_config`, `fk_supply`, `date_config_has_supply`) VALUES
(1, 1, 1, '2022-03-14 19:40:26'),
(2, 2, 1, '2022-03-17 18:35:45');

-- --------------------------------------------------------

--
-- Table structure for table `t_config_has_watercooling`
--

CREATE TABLE `t_config_has_watercooling` (
  `id_config_has_watercooling` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `fk_watercooling` int(11) DEFAULT NULL,
  `date_config_has_watercooling` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config_has_watercooling`
--

INSERT INTO `t_config_has_watercooling` (`id_config_has_watercooling`, `fk_config`, `fk_watercooling`, `date_config_has_watercooling`) VALUES
(1, 2, 1, '2022-03-17 18:00:03');

-- --------------------------------------------------------

--
-- Table structure for table `t_cpu`
--

CREATE TABLE `t_cpu` (
  `id_cpu` int(11) NOT NULL,
  `CPU_Name` varchar(45) DEFAULT NULL,
  `CPU_Codename` varchar(45) DEFAULT NULL,
  `CPU_Cores` varchar(20) DEFAULT NULL,
  `CPU_Clock` varchar(30) DEFAULT NULL,
  `CPU_Socket` varchar(10) DEFAULT NULL,
  `CPU_Process` tinyint(5) DEFAULT NULL,
  `CPU_L3_Cache` smallint(6) DEFAULT NULL,
  `CPU_TDP` smallint(6) DEFAULT NULL,
  `CPU_Released` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_cpu`
--

INSERT INTO `t_cpu` (`id_cpu`, `CPU_Name`, `CPU_Codename`, `CPU_Cores`, `CPU_Clock`, `CPU_Socket`, `CPU_Process`, `CPU_L3_Cache`, `CPU_TDP`, `CPU_Released`) VALUES
(5, 'Celeron G6900', 'Alder Lake-S', '2', '3.4 GHz', '1700', 10, 4, 46, '2022-01-04'),
(6, 'Celeron G6900E', 'Alder Lake-S', '2', '3 GHz', '1700', 10, 4, 46, '2022-01-04'),
(28, 'Celeron G6900T', 'Alder Lake-S', '2', '2.8 GHz', '1700', 10, 4, 35, '2022-01-04'),
(29, 'Celeron G6900TE', 'Alder Lake-S', '2', '2.4 GHz', '1700', 10, 4, 35, '2022-01-04'),
(30, 'Core i3_12100', 'Alder Lake-S', '4 / 8', '3.3-4.3 GHz', '1700', 10, 12, 60, '2022-01-31'),
(31, 'Core i3_12100E', 'Alder Lake-S', '4 / 8', '3.2-4.2 GHz', '1700', 10, 12, 60, '2022-01-31'),
(32, 'Core i3_12100F', 'Alder Lake-S', '4 / 8', '3.3-4.3 GHz', '1700', 10, 12, 58, '2022-01-31'),
(33, 'Core i3_12100T', 'Alder Lake-S', '4 / 8', '2.2-4.1 GHz', '1700', 10, 12, 35, '2022-01-31'),
(34, 'Core i3_12100TE', 'Alder Lake-S', '4 / 8', '2.1-4 GHz', '1700', 10, 12, 35, '2022-01-31'),
(35, 'Core i3_12300', 'Alder Lake-S', '4 / 8', '3.5-4.4 GHz', '1700', 10, 12, 60, '2022-01-31'),
(36, 'Core i3_12300T', 'Alder Lake-S', '4 / 8', '2.3-4.2 GHz', '1700', 10, 12, 35, '2022-01-31'),
(37, 'Core i5_12400', 'Alder Lake-S', '6 / 12', '2.5-4.4 GHz', '1700', 10, 18, 65, '2022-01-31'),
(38, 'Core i5_12400F', 'Alder Lake-S', '6 / 12', '2.5-4.4 GHz', '1700', 10, 18, 65, '2022-01-31'),
(39, 'Core i5_12400T', 'Alder Lake-S', '6 / 12', '1.8-4.2 GHz', '1700', 10, 18, 35, '2022-01-31'),
(40, 'Core i5_12500', 'Alder Lake-S', '6 / 12', '3-4.6 GHz', '1700', 10, 18, 65, '2022-01-31'),
(41, 'Core i5_12500E', 'Alder Lake-S', '6 / 12', '2.9-4.5 GHz', '1700', 10, 18, 65, '2022-01-31'),
(42, 'Core i5_12500T', 'Alder Lake-S', '6 / 12', '2-4.4 GHz', '1700', 10, 18, 35, '2022-01-31'),
(43, 'Core i5_12500TE', 'Alder Lake-S', '6 / 12', '1.9-4.3 GHz', '1700', 10, 18, 35, '2022-01-31'),
(44, 'Core i5_12600', 'Alder Lake-S', '6 / 12', '3.3-4.8 GHz', '1700', 10, 18, 65, '2022-01-31'),
(45, 'Core i5_12600T', 'Alder Lake-S', '6 / 12', '2.1-4.6 GHz', '1700', 10, 18, 35, '2022-01-31'),
(46, 'Core i7_12700', 'Alder Lake-S', '12 / 20', '3.3-4.9 GHz', '1700', 10, 25, 65, '2022-01-31'),
(47, 'Core i7_12700E', 'Alder Lake-S', '12 / 20', '2.1-4.8 GHz', '1700', 10, 25, 65, '2022-01-31'),
(48, 'Core i7_12700F', 'Alder Lake-S', '12 / 20', '3.3-4.9 GHz', '1700', 10, 25, 65, '2022-01-31'),
(49, 'Core i7_12700T', 'Alder Lake-S', '12 / 20', '1.4-4.7 GHz', '1700', 10, 25, 35, '2022-01-31'),
(50, 'Core i7_12700TE', 'Alder Lake-S', '12 / 20', '1.4-4.6 GHz', '1700', 10, 25, 35, '2022-01-31'),
(51, 'Core i9_12900', 'Alder Lake-S', '16 / 24', '2.4-5.1 GHz', '1700', 10, 30, 65, '2022-01-04'),
(52, 'Core i9_12900E', 'Alder Lake-S', '16 / 24', '2.3-5 GHz', '1700', 10, 30, 65, '2022-01-04'),
(53, 'Core i9_12900F', 'Alder Lake-S', '16 / 24', '2.4-5.1 GHz', '1700', 10, 30, 65, '2022-01-04'),
(54, 'Core i9_12900T', 'Alder Lake-S', '16 / 24', '1.4-4.9 GHz', '1700', 10, 30, 35, '2022-01-04'),
(55, 'Core i9_12900TE', 'Alder Lake-S', '16 / 24', '1.1-4.8 GHz', '1700', 10, 30, 35, '2022-01-04'),
(56, 'Pentium Gold G7400', 'Alder Lake-S', '2 / 4', '3.7 GHz', '1700', 10, 6, 46, '2022-01-04'),
(57, 'Pentium Gold G7400E', 'Alder Lake-S', '2 / 4', '3.6 GHz', '1700', 10, 6, 46, '2022-01-04'),
(58, 'Pentium Gold G7400T', 'Alder Lake-S', '2 / 4', '3.1 GHz', '1700', 10, 6, 35, '2022-01-04'),
(59, 'Pentium Gold G7400TE', 'Alder Lake-S', '2 / 4', '3 GHz', '1700', 10, 6, 35, '2022-01-04'),
(60, 'Core i5-12600K', 'Alder Lake-S', '10 / 16', '3.7-4.9 GHz', '1700', 10, 20, 125, '2021-11-04'),
(61, 'Core i5-12600KF', 'Alder Lake-S', '10 / 16', '3.7-4.9 GHz', '1700', 10, 20, 125, '2021-11-04'),
(62, 'Core i7-12700K', 'Alder Lake-S', '12 / 20', '3.6-5 GHz', '1700', 10, 25, 125, '2021-11-04'),
(63, 'Core i7-12700KF', 'Alder Lake-S', '12 / 20', '3.6-5 GHz', '1700', 10, 25, 125, '2021-11-04'),
(64, 'Core i9-12900K', 'Alder Lake-S', '16 / 24', '3.2-5.2 GHz', '1700', 10, 30, 125, '2021-11-04'),
(65, 'Core i9-12900KF', 'Alder Lake-S', '16 / 24', '3.2-5.2 GHz', '1700', 10, 30, 125, '2021-11-04'),
(66, 'Core i3-10105', 'Comet Lake-R', '4 / 8', '3.7-4.4 GHz', '1200', 14, 6, 65, '2021-03-16'),
(67, 'Core i3-10105F', 'Comet Lake-R', '4 / 8', '3.7-4.4 GHz', '1200', 14, 6, 65, '2021-03-16'),
(68, 'Core i3-10105T', 'Comet Lake-R', '4 / 8', '3-3.9 GHz', '1200', 14, 6, 35, '2021-03-16'),
(69, 'Core i3-10305', 'Comet Lake-R', '4 / 8', '3.8-4.5 GHz', '1200', 14, 8, 65, '2021-03-16'),
(70, 'Core i3-10305T', 'Comet Lake-R', '4 / 8', '3-4 GHz', '1200', 14, 8, 35, '2021-03-16'),
(71, 'Core i3-10325', 'Comet Lake-R', '4 / 8', '3.9-4.7 GHz', '1200', 14, 8, 65, '2021-03-16'),
(72, 'Core i5-11400', 'Rocket Lake', '6 / 12', '2.6-4.4 GHz', '1200', 14, 12, 65, '2021-03-16'),
(73, 'Core i5-11400F', 'Rocket Lake', '6 / 12', '2.6-4.4 GHz', '1200', 14, 12, 65, '2021-03-16'),
(74, 'Core i5-11400T', 'Rocket Lake', '6 / 12', '1.3-3.7 GHz', '1200', 14, 12, 35, '2021-03-16'),
(75, 'Core i5-11500', 'Rocket Lake', '6 / 12', '2.7-4.6 GHz', '1200', 14, 12, 65, '2021-03-16'),
(76, 'Core i5-11500T', 'Rocket Lake', '6 / 12', '1.5-3.9 GHz', '1200', 14, 12, 35, '2021-03-16'),
(77, 'Core i5-11600', 'Rocket Lake', '6 / 12', '2.8-4.8 GHz', '1200', 14, 12, 65, '2021-03-16'),
(78, 'Core i5-11600K', 'Rocket Lake', '6 / 12', '3.9-4.9 GHz', '1200', 14, 12, 125, '2021-03-16'),
(79, 'Core i5-11600KF', 'Rocket Lake', '6 / 12', '3.9-4.9 GHz', '1200', 14, 12, 125, '2021-03-16'),
(80, 'Core i5-11600T', 'Rocket Lake', '6 / 12', '1.7-4.1 GHz', '1200', 14, 12, 35, '2021-03-16'),
(81, 'Core i7-11700', 'Rocket Lake', '8 / 16', '2.5-4.9 GHz', '1200', 14, 16, 65, '2021-03-16'),
(82, 'Core i7-11700F', 'Rocket Lake', '8 / 16', '2.5-4.9 GHz', '1200', 14, 16, 65, '2021-03-16'),
(83, 'Core i7-11700K', 'Rocket Lake', '8 / 16', '3.6-5 GHz', '1200', 14, 16, 125, '2021-03-16'),
(84, 'Core i7-11700KF', 'Rocket Lake', '8 / 16', '3.6-5 GHz', '1200', 14, 16, 125, '2021-03-16'),
(85, 'Core i7-11700T', 'Rocket Lake', '8 / 16', '1.4-4.6 GHz', '1200', 14, 16, 35, '2021-03-16'),
(86, 'Core i9-11900', 'Rocket Lake', '8 / 16', '2.5-5.2 GHz', '1200', 14, 16, 65, '2021-03-16'),
(87, 'Core i9-11900F', 'Rocket Lake', '8 / 16', '2.5-5.2 GHz', '1200', 14, 16, 65, '2021-03-16'),
(88, 'Core i9-11900K', 'Rocket Lake', '8 / 16', '3.5-5.3 GHz', '1200', 14, 16, 125, '2021-03-16'),
(89, 'Core i9-11900KF', 'Rocket Lake', '8 / 16', '3.5-5.3 GHz', '1200', 14, 16, 125, '2021-03-16'),
(90, 'Core i9-11900T', 'Rocket Lake', '8 / 16', '1.5-4.9 GHz', '1200', 14, 16, 35, '2021-03-16'),
(91, 'Pentium Gold G6405', 'Comet Lake-R', '2 / 4', '4.1 GHz', '1200', 14, 4, 65, '2021-03-16'),
(92, 'Pentium Gold G6405T', 'Comet Lake-R', '2 / 4', '3.5 GHz', '1200', 14, 4, 35, '2021-03-16'),
(93, 'Pentium Gold G6505', 'Comet Lake-R', '2 / 4', '4.2 GHz', '1200', 14, 4, 65, '2021-03-16'),
(94, 'Pentium Gold G6505T', 'Comet Lake-R', '2 / 4', '3.6 GHz', '1200', 14, 4, 35, '2021-03-16'),
(95, 'Pentium Gold G6605', 'Comet Lake-R', '2 / 4', '4.3 GHz', '1200', 14, 4, 65, '2021-03-16'),
(96, 'Core i9-10850K', 'Comet Lake', '10 / 20', '3.6-5.2 GHz', '1200', 14, 20, 125, '2020-07-27'),
(97, 'Celeron G5900', 'Comet Lake', '2', '3.4 GHz', '1200', 14, 2, 58, '2020-04-30'),
(98, 'Celeron G5920', 'Comet Lake', '2', '3.5 GHz', '1200', 14, 2, 58, '2020-04-30'),
(99, 'Core i3-10100', 'Comet Lake', '4 / 8', '3.6-4.3 GHz', '1200', 14, 6, 65, '2020-04-30'),
(100, 'Core i3-10300', 'Comet Lake', '4 / 8', '3.7-4.4 GHz', '1200', 14, 8, 62, '2020-04-30'),
(101, 'Core i3-10320', 'Comet Lake', '4 / 8', '3.8-4.6 GHz', '1200', 14, 8, 91, '2020-04-30'),
(102, 'Core i3-10350K', 'Comet Lake', '4 / 8', '4.1-4.8 GHz', '1200', 14, 8, 91, '2020-04-30'),
(103, 'Core i5-10400', 'Comet Lake', '6 / 12', '2.9-4.3 GHz', '1200', 14, 12, 65, '2020-04-30'),
(104, 'Core i5-10400F', 'Comet Lake', '6 / 12', '2.9-4.3 GHz', '1200', 14, 12, 65, '2020-04-30'),
(105, 'Core i5-10500', 'Comet Lake', '6 / 12', '3.1-4.5 GHz', '1200', 14, 12, 65, '2020-04-30'),
(106, 'Core i5-10600', 'Comet Lake', '6 / 12', '3.3-4.8 GHz', '1200', 14, 12, 65, '2020-04-30'),
(107, 'Core i5-10600K', 'Comet Lake', '6 / 12', '4.1-4.8 GHz', '1200', 14, 12, 125, '2020-04-30'),
(108, 'Core i5-10600KF', 'Comet Lake', '6 / 12', '4.1-4.8 GHz', '1200', 14, 12, 95, '2020-04-30'),
(109, 'Core i7-10700', 'Comet Lake', '8 / 16', '2.9-4.8 GHz', '1200', 14, 16, 65, '2020-04-30'),
(110, 'Core i7-10700F', 'Comet Lake', '8 / 16', '2.9-4.8 GHz', '1200', 14, 16, 65, '2020-04-30'),
(111, 'Core i7-10700K', 'Comet Lake', '8 / 16', '3.8-5.1 GHz', '1200', 14, 16, 125, '2020-04-30'),
(112, 'Core i7-10700KF', 'Comet Lake', '8 / 16', '3.8-5.1 GHz', '1200', 14, 16, 125, '2020-04-30'),
(113, 'Core i9-10800F', 'Comet Lake', '10 / 20', '2.7-5 GHz', '1200', 14, 20, 65, '2020-04-30'),
(114, 'Core i9-10900', 'Comet Lake', '10 / 20', '2.8-5.2 GHz', '1200', 14, 20, 65, '2020-04-30'),
(115, 'Core i9-10900F', 'Comet Lake', '10 / 20', '2.8-5.2 GHz', '1200', 14, 20, 65, '2020-04-30'),
(116, 'Core i9-10900K', 'Comet Lake', '10 / 20', '3.7-5.3 GHz', '1200', 14, 20, 125, '2020-04-30'),
(117, 'Core i9-10900KF', 'Comet Lake', '10 / 20', '3.7-5.3 GHz', '1200', 14, 20, 125, '2020-04-30'),
(118, 'Pentium Gold G6400', 'Comet Lake', '2 / 4', '4 GHz', '1200', 14, 4, 58, '2020-04-30'),
(119, 'Pentium Gold G6500', 'Comet Lake', '2 / 4', '4.1 GHz', '1200', 14, 4, 58, '2020-04-30'),
(120, 'Pentium Gold G6600', 'Comet Lake', '2 / 4', '4.2 GHz', '1200', 14, 4, 58, '2020-04-30'),
(122, 'Core i9-9900KS', 'Coffee Lake-R', '8 / 16', '4-5 GHz', '1151', 14, 16, 127, '2019-10-28'),
(123, 'Core i9-10900X', 'Cascade Lake-X', '10 / 20', '3.7-4.7 GHz', '2066', 14, 19, 165, '2019-10-19'),
(124, 'Core i9-10920X', 'Cascade Lake-X', '12 / 24', '3.5-4.8 GHz', '2066', 14, 19, 165, '2019-10-19'),
(125, 'Core i9-10940X', 'Cascade Lake-X', '14 / 28', '3.3-4.8 GHz', '2066', 14, 19, 165, '2019-10-19'),
(126, 'Core i9-10980XE', 'Cascade Lake-X', '18 / 36', '3-4.8 GHz', '2066', 14, 25, 165, '2019-10-19'),
(127, 'Core i3-9100F', 'Coffee Lake', '4', '3.6-4.2 GHz', '1151', 14, 6, 65, '2019-04-23'),
(128, 'Core i3-9300', 'Coffee Lake', '4', '3.7-4.3 GHz', '1151', 14, 8, 62, '2019-04-23'),
(129, 'Core i3-9320', 'Coffee Lake', '4', '3.7-4.4 GHz', '1151', 14, 8, 62, '2019-04-23'),
(130, 'Core i3-9350K', 'Coffee Lake', '4', '4-4.6 GHz', '1151', 14, 8, 91, '2019-04-23'),
(131, 'Core i5-9500F', 'Coffee Lake', '6', '3-4.4 GHz', '1151', 14, 9, 65, '2019-04-23'),
(132, 'Core i7-9700', 'Coffee Lake', '8', '3-4.7 GHz', '1151', 14, 12, 65, '2019-04-23'),
(133, 'Core i7-9700F', 'Coffee Lake', '8', '3-4.7 GHz', '1151', 14, 12, 65, '2019-04-23'),
(134, 'Core i9-9900', 'Coffee Lake-R', '8 / 16', '3.1-5 GHz', '1151', 14, 16, 65, '2019-04-23'),
(135, 'Pentium Gold G5620', 'Coffee Lake', '2 / 4', '4 GHz', '1151', 14, 4, 51, '2019-02-20'),
(136, 'Core i3-9350KF', 'Coffee Lake', '4', '4-4.6 GHz', '1151', 14, 8, 91, '2019-01-08'),
(137, 'Core i5-9400F', 'Coffee Lake', '6', '2.9-4.1 GHz', '1151', 14, 9, 65, '2019-01-08'),
(138, 'Core i5-9600KF', 'Coffee Lake', '6', '3.7-4.6 GHz', '1151', 14, 9, 95, '2019-01-08'),
(139, 'Core i7-9700KF', 'Coffee Lake', '8', '3.6-4.9 GHz', '1151', 14, 12, 95, '2019-01-08'),
(140, 'Core i9-9900KF', 'Coffee Lake-R', '8 / 16', '3.6-5 GHz', '1151', 14, 16, 95, '2019-01-08'),
(180, 'Ryzen 3 5300G', 'Cezanne', '4 / 8', '4-4.2 GHz', 'AM4', 7, 8, 65, '2021-04-13'),
(181, 'Ryzen 5 5600G', 'Cezanne', '6 / 12', '3.9-4.4 GHz', 'AM4', 7, 16, 65, '2021-04-13'),
(182, 'Ryzen 7 5700G', 'Cezanne', '8 / 16', '3.8-4.6 GHz', 'AM4', 7, 16, 65, '2021-04-13'),
(183, 'Ryzen 5 5600X', 'Vermeer', '6 / 12', '3.7-4.6 GHz', 'AM4', 7, 32, 65, '2020-11-05'),
(184, 'Ryzen 7 5800X', 'Vermeer', '8 / 16', '3.8-4.7 GHz', 'AM4', 7, 32, 105, '2020-11-05'),
(185, 'Ryzen 9 5900X', 'Vermeer', '12 / 24', '3.7-4.8 GHz', 'AM4', 7, 64, 105, '2020-11-05'),
(186, 'Ryzen 9 5950X', 'Vermeer', '16 / 32', '3.4-4.9 GHz', 'AM4', 7, 64, 105, '2020-11-05'),
(187, 'Athlon Gold 3150G', 'Dali', '4', '3.5-3.9 GHz', 'AM4', 12, 4, 65, '2020-07-21'),
(188, 'Athlon Gold 3150GE', 'Dali', '4', '3.5-3.8 GHz', 'AM4', 12, 4, 35, '2020-07-21'),
(189, 'Athlon Gold PRO 3150G', 'Dali', '4', '3.5-3.9 GHz', 'AM4', 12, 4, 65, '2020-07-21'),
(190, 'Athlon Gold PRO 3150GE', 'Dali', '4', '3.5-3.8 GHz', 'AM4', 12, 4, 35, '2020-07-21'),
(191, 'Athlon Silver 3050GE', 'Dali', '2 / 4', '3.4 GHz', 'AM4', 12, 4, 35, '2020-07-21'),
(192, 'Athlon Silver PRO 3125GE', 'Dali', '2 / 4', '3.4 GHz', 'AM4', 12, 4, 35, '2020-07-21'),
(193, 'Ryzen 3 4300G', 'Renoir', '4 / 8', '3.8-4 GHz', 'AM4', 7, 4, 65, '2020-07-21'),
(194, 'Ryzen 3 4300GE', 'Renoir', '4 / 8', '3.5-4 GHz', 'AM4', 7, 4, 35, '2020-07-21'),
(208, 'Ryzen 3 PRO 4350G', 'Renoir', '4 / 8', '3.8-4 GHz', 'AM4', 7, 4, 65, '2020-07-21'),
(209, 'Ryzen 3 PRO 4350GE', 'Renoir', '4 / 8', '3.5-4 GHz', 'AM4', 7, 4, 35, '2020-07-21'),
(210, 'Ryzen 5 4600G', 'Renoir', '6 / 12', '3.7-4.2 GHz', 'AM4', 7, 8, 65, '2020-07-21'),
(211, 'Ryzen 5 4600GE', 'Renoir', '6 / 12', '3.3-4.2 GHz', 'AM4', 7, 8, 35, '2020-07-21'),
(212, 'Ryzen 5 PRO 4650G', 'Renoir', '6 / 12', '3.7-4.2 GHz', 'AM4', 7, 8, 65, '2020-07-21'),
(213, 'Ryzen 5 PRO 4650GE', 'Renoir', '6 / 12', '3.3-4.2 GHz', 'AM4', 7, 8, 35, '2020-07-21'),
(214, 'Ryzen 7 4700G', 'Renoir', '8 / 16', '3.6-4.4 GHz', 'AM4', 7, 8, 65, '2020-07-21'),
(215, 'Ryzen 7 4700GE', 'Renoir', '8 / 16', '3.1-4.3 GHz', 'AM4', 7, 8, 35, '2020-07-21'),
(216, 'Ryzen 7 PRO 4750G', 'Renoir', '8 / 16', '3.6-4.4 GHz', 'AM4', 7, 8, 65, '2020-07-21'),
(217, 'Ryzen 7 PRO 4750GE', 'Renoir', '8 / 16', '3.1-4.3 GHz', 'AM4', 7, 8, 35, '2020-07-21'),
(218, 'Ryzen Threadripper PRO 3945WX', 'Matisse', '12 / 24', '4-4.3 GHz', 'WRX8', 7, 64, 280, '2020-07-14'),
(219, 'Ryzen Threadripper PRO 3955WX', 'Matisse', '16 / 32', '3.9-4.3 GHz', 'WRX8', 7, 64, 280, '2020-07-14'),
(220, 'Ryzen Threadripper PRO 3975WX', 'Matisse', '32 / 64', '3.5-4.2 GHz', 'WRX8', 7, 128, 280, '2020-07-14'),
(221, 'Ryzen Threadripper PRO 3995WX', 'Matisse', '64 / 128', '2.7-4.2 GHz', 'WRX8', 7, 256, 280, '2020-07-14'),
(222, 'Ryzen 7 3800XT', 'Matisse', '8 / 16', '3.8-4.7 GHz', 'AM4', 7, 32, 105, '2020-07-07'),
(223, 'Ryzen 9 3900XT', 'Matisse', '12 / 24', '3.9-4.7 GHz', 'AM4', 7, 64, 105, '2020-07-07'),
(224, 'Ryzen 3 3100', 'Matisse', '4 / 8', '3.6-3.9 GHz', 'AM4', 7, 16, 65, '2020-04-24'),
(225, 'Ryzen 3 3300X', 'Matisse', '4 / 8', '3.8-4.3 GHz', 'AM4', 7, 16, 65, '2020-04-24'),
(226, 'Ryzen Threadripper 3990X', 'Matisse', '64 / 128', '2.9-4.3 GHz', 'TRX4', 7, 128, 280, '2020-02-07'),
(227, 'Ryzen Threadripper 3960X', 'Matisse', '24 / 48', '3.8-4.5 GHz', 'TRX4', 7, 128, 280, '2019-11-25'),
(228, 'Ryzen Threadripper 3970X', 'Matisse', '32 / 64', '3.7-4.5 GHz', 'TRX4', 7, 128, 280, '2019-11-25'),
(229, 'Athlon 3000G', 'Zen', '2 / 4', '3.5 GHz', 'AM4', 14, 4, 35, '2019-11-20'),
(230, 'Ryzen 9 3950X', 'Matisse', '16 / 32', '3.5-4.7 GHz', 'AM4', 7, 64, 105, '2019-11-14'),
(231, 'Ryzen Threadripper 3980X', 'Matisse', '48 / 96', '3.5-4.7 GHz', 'TRX4', 7, 128, 280, '2019-11-14'),
(232, 'Ryzen 5 1600AF', 'Zen', '6 / 12', '3.2-3.6 GHz', 'AM4', 12, 16, 65, '2019-10-11'),
(233, 'Ryzen 5 3500X', 'Matisse', '6', '3.6-4.1 GHz', 'AM4', 7, 32, 65, '2019-09-24'),
(234, 'Ryzen 3 3200G', 'Picasso', '4', '3.6-4 GHz', 'AM4', 12, 4, 65, '2019-07-07'),
(235, 'Ryzen 5 3400G', 'Picasso', '4 / 8', '3.7-4.2 GHz', 'AM4', 12, 4, 65, '2019-07-07'),
(236, 'Ryzen 5 3600', 'Matisse', '6 / 12', '3.6-4.2 GHz', 'AM4', 7, 32, 65, '2019-07-07'),
(237, 'Ryzen 5 3600X', 'Matisse', '6 / 12', '3.8-4.4 GHz', 'AM4', 7, 32, 95, '2019-07-07'),
(238, 'Ryzen 5 3600XT', 'Matisse', '6 / 12', '3.8-4.5 GHz', 'AM4', 7, 32, 95, '2019-07-07'),
(239, 'Ryzen 7 3700X', 'Matisse', '8 / 16', '3.6-4.4 GHz', 'AM4', 7, 32, 65, '2019-07-07'),
(240, 'Ryzen 7 3800X', 'Matisse', '8 / 16', '3.9-4.5 GHz', 'AM4', 7, 32, 105, '2019-07-07'),
(241, 'Ryzen 9 3900X', 'Matisse', '12 / 24', '3.8-4.6 GHz', 'AM4', 7, 64, 105, '2019-07-07'),
(242, 'Ryzen 7 2700X 50th Anniversary', 'Zen', '8 / 16', '3.7-4.35 GHz', 'AM4', 12, 16, 105, '2019-04-29');

-- --------------------------------------------------------

--
-- Table structure for table `t_cpumanufacturer`
--

CREATE TABLE `t_cpumanufacturer` (
  `id_cpu_manufacturer` int(11) NOT NULL,
  `CPU_Manufacturer` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_cpumanufacturer`
--

INSERT INTO `t_cpumanufacturer` (`id_cpu_manufacturer`, `CPU_Manufacturer`) VALUES
(1, 'INTEL'),
(2, 'AMD');

-- --------------------------------------------------------

--
-- Table structure for table `t_cpumanufacturer_produce_cpu`
--

CREATE TABLE `t_cpumanufacturer_produce_cpu` (
  `id_cpumanufacturer_produce_cpu` int(11) NOT NULL,
  `fk_cpumanufacturer` int(11) NOT NULL,
  `fk_cpu` int(11) NOT NULL,
  `date_cpumanufacturer_produce_cpu` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_cpumanufacturer_produce_cpu`
--

INSERT INTO `t_cpumanufacturer_produce_cpu` (`id_cpumanufacturer_produce_cpu`, `fk_cpumanufacturer`, `fk_cpu`, `date_cpumanufacturer_produce_cpu`) VALUES
(1, 1, 5, '2022-03-14 14:01:23'),
(2, 1, 6, '2022-03-14 14:02:12'),
(3, 1, 99, '2022-03-14 14:02:25'),
(4, 2, 215, '2022-03-14 14:04:49'),
(5, 2, 236, '2022-03-18 10:26:15'),
(6, 2, 239, '2022-03-18 10:26:45'),
(7, 2, 184, '2022-03-18 10:28:13'),
(8, 2, 183, '2022-03-18 10:28:42');

-- --------------------------------------------------------

--
-- Table structure for table `t_cpu_compatible_motherboard`
--

CREATE TABLE `t_cpu_compatible_motherboard` (
  `id_cpu_compatible_motherboard` int(11) NOT NULL,
  `fk_cpu` int(11) NOT NULL,
  `fk_motherboard` int(11) NOT NULL,
  `date_cpu_compatible_motherboard` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `t_cpu_compatible_ramgen`
--

CREATE TABLE `t_cpu_compatible_ramgen` (
  `id_cpu_compatible_ramgen` int(11) NOT NULL,
  `fk_cpu` int(11) NOT NULL,
  `fk_ramgen` int(11) NOT NULL,
  `date_cpu_compatible_ramgen` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `t_format`
--

CREATE TABLE `t_format` (
  `id_format` int(11) NOT NULL,
  `format` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_format`
--

INSERT INTO `t_format` (`id_format`, `format`) VALUES
(1, 'ATX'),
(2, 'EATX'),
(3, 'Micro ATX'),
(4, 'Mini ITX'),
(5, 'ITX');

-- --------------------------------------------------------

--
-- Table structure for table `t_gpu`
--

CREATE TABLE `t_gpu` (
  `id_gpu` int(11) NOT NULL,
  `GPU_Brand` varchar(50) DEFAULT NULL,
  `GPU_Name` varchar(50) DEFAULT NULL,
  `GPU_Codename` varchar(50) DEFAULT NULL,
  `GPU_Bus` varchar(25) DEFAULT NULL,
  `GPU_Memory` varchar(25) DEFAULT NULL,
  `GPU_Clock` smallint(5) DEFAULT NULL,
  `Memory_Clock` smallint(5) DEFAULT NULL,
  `Shaders` int(25) DEFAULT NULL,
  `TMUs` int(25) DEFAULT NULL,
  `ROPs` int(25) DEFAULT NULL,
  `GPU_TDP` int(5) DEFAULT NULL,
  `GPU_Released` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_gpu`
--

INSERT INTO `t_gpu` (`id_gpu`, `GPU_Brand`, `GPU_Name`, `GPU_Codename`, `GPU_Bus`, `GPU_Memory`, `GPU_Clock`, `Memory_Clock`, `Shaders`, `TMUs`, `ROPs`, `GPU_TDP`, `GPU_Released`) VALUES
(1, 'AMD', 'Radeon RX 5600 XT', 'Navi 10', 'PCIe 4.0 x16', '6GB GDDR6, 192 bit', 1130, 1500, 2304, 144, 64, 150, '2020-01-21'),
(2, 'AMD', 'Radeon RX 6800', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1700, 2000, 3840, 240, 96, 250, '2020-10-28'),
(3, 'AMD', 'Radeon RX 6800 XT', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1825, 2000, 4608, 288, 128, 300, '2020-10-28'),
(4, 'AMD', 'Radeon RX 6900 XT', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1825, 2000, 5120, 320, 128, 300, '2020-10-28'),
(5, 'ASRock', 'ASRock RX 6900 XT Phantom Gaming D OC', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1925, 2000, 5120, 320, 128, 350, '2020-10-28'),
(6, 'GIGABYTE', 'GIGABYTE AORUS RX 6900 XT MASTER', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1950, 2000, 5120, 320, 128, 300, '2020-10-28'),
(7, 'MSI', 'MSI RX 6900 XT GAMING Z TRIO', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 2050, 2430, 5120, 320, 128, 300, '2020-10-28'),
(8, 'PowerColor', 'PowerColor Red Devil RX 6900 XT', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1925, 2000, 5120, 320, 128, 300, '2020-10-28');

-- --------------------------------------------------------

--
-- Table structure for table `t_gpumanufacturer`
--

CREATE TABLE `t_gpumanufacturer` (
  `id_gpumanufacturer` int(11) NOT NULL,
  `GPU_Manufacturer` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_gpumanufacturer`
--

INSERT INTO `t_gpumanufacturer` (`id_gpumanufacturer`, `GPU_Manufacturer`) VALUES
(1, 'Nvidia'),
(2, 'AMD');

-- --------------------------------------------------------

--
-- Table structure for table `t_gpumanufacturer_produce_gpu`
--

CREATE TABLE `t_gpumanufacturer_produce_gpu` (
  `id_gpumanufacturer_produce_gpu` int(11) NOT NULL,
  `fk_gpumanufacturer` int(11) NOT NULL,
  `fk_gpu` int(11) NOT NULL,
  `date_gpumanufacturer_produce_gpu` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_gpumanufacturer_produce_gpu`
--

INSERT INTO `t_gpumanufacturer_produce_gpu` (`id_gpumanufacturer_produce_gpu`, `fk_gpumanufacturer`, `fk_gpu`, `date_gpumanufacturer_produce_gpu`) VALUES
(1, 2, 1, '2022-03-14 13:57:34'),
(2, 2, 2, '2022-03-14 13:57:43'),
(3, 2, 3, '2022-03-14 13:57:50'),
(4, 2, 4, '2022-03-14 13:58:01'),
(5, 2, 5, '2022-03-14 13:58:19'),
(6, 2, 6, '2022-03-14 13:58:27'),
(7, 2, 7, '2022-03-14 13:58:37'),
(8, 2, 8, '2022-03-14 13:58:43');

-- --------------------------------------------------------

--
-- Table structure for table `t_hdd`
--

CREATE TABLE `t_hdd` (
  `id_hdd` int(11) NOT NULL,
  `hdd_brand` varchar(50) DEFAULT NULL,
  `hdd_name` varchar(50) DEFAULT NULL,
  `hdd_interface` varchar(50) DEFAULT NULL,
  `hdd_capacity` varchar(50) DEFAULT NULL,
  `hdd_RPM` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_hdd`
--

INSERT INTO `t_hdd` (`id_hdd`, `hdd_brand`, `hdd_name`, `hdd_interface`, `hdd_capacity`, `hdd_RPM`) VALUES
(1, 'Seagate', 'BarraCuda', 'SATA 6Gbps', '2TB', '7200'),
(2, 'Seagate', 'BarraCuda', 'SATA 6Gbps', '3TB', '7200');

-- --------------------------------------------------------

--
-- Table structure for table `t_motherboard`
--

CREATE TABLE `t_motherboard` (
  `id_motherboard` int(11) NOT NULL,
  `motherboard_brand` varchar(20) DEFAULT NULL,
  `motherboard_model` varchar(50) DEFAULT NULL,
  `motherboard_socket` varchar(20) DEFAULT NULL,
  `motherboard_chipset` varchar(20) DEFAULT NULL,
  `motherboard_release_year` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_motherboard`
--

INSERT INTO `t_motherboard` (`id_motherboard`, `motherboard_brand`, `motherboard_model`, `motherboard_socket`, `motherboard_chipset`, `motherboard_release_year`) VALUES
(1, 'Gigabyte ', 'B450 Aorus Elite', '1x AM4', 'AMD B450', 2018),
(2, 'Asrock ', 'B450 Steel Legend', '1x AM4', 'AMD B450', 2019),
(3, 'Asus ', 'ROG Strix X570-E Gaming', '1x AM4', 'AMD X570', 2019),
(4, 'Gigabyte	', 'B550 Aorus Master', '1x AM4', 'AMD B550', 2020),
(5, 'Asrock', 'B550 Taichi', '1x AM4', 'AMD B550', 2020),
(6, 'MSI', 'MEG X570 Godlike', '1x AM4', 'AMD X570', 2019),
(7, 'MSI', 'MEG X570 Creation', '1x AM4', 'AMD X570', 2019),
(8, 'Asrock ', 'X570 Aqua', '1x AM4', 'AMD X570', 2019);

-- --------------------------------------------------------

--
-- Table structure for table `t_motherboard_is_format`
--

CREATE TABLE `t_motherboard_is_format` (
  `id_motherboard_is_format` int(11) NOT NULL,
  `fk_motherboard` int(11) NOT NULL,
  `fk_format` int(11) NOT NULL,
  `date_motherboard_is_format` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_motherboard_is_format`
--

INSERT INTO `t_motherboard_is_format` (`id_motherboard_is_format`, `fk_motherboard`, `fk_format`, `date_motherboard_is_format`) VALUES
(1, 1, 1, '2022-03-14 13:42:02'),
(2, 2, 1, '2022-03-14 13:42:13'),
(3, 3, 1, '2022-03-14 13:42:21'),
(4, 4, 1, '2022-03-14 13:42:36'),
(5, 5, 1, '2022-03-14 13:42:46'),
(6, 6, 2, '2022-03-14 13:43:14'),
(7, 7, 2, '2022-03-14 13:43:26'),
(8, 8, 2, '2022-03-14 13:43:34');

-- --------------------------------------------------------

--
-- Table structure for table `t_ram`
--

CREATE TABLE `t_ram` (
  `id_ram` int(11) NOT NULL,
  `ram_brand` varchar(25) DEFAULT NULL,
  `ram_name` varchar(50) DEFAULT NULL,
  `ram_capacity` varchar(50) DEFAULT NULL,
  `ram_data_rate` varchar(50) DEFAULT NULL,
  `ram_timings` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_ram`
--

INSERT INTO `t_ram` (`id_ram`, `ram_brand`, `ram_name`, `ram_capacity`, `ram_data_rate`, `ram_timings`) VALUES
(1, 'G.Skill', 'Trident Z5 RGB', '32GB (2 x 16GB)', 'DDR5-6000 (XMP)', '36-36-36-76'),
(2, 'TeamGroup', 'T-Force Xtreem ARGB', '16GB (2 x 8GB)', 'DDR4-3600 (XMP)', '14-15-15-35 '),
(3, 'Patriot', 'Viper Steel', '16GB (2 x 8GB)', 'DDR4-4400 (XMP)', '19-19-19-39'),
(4, 'Patriot', 'Viper RGB', '16GB (2 x 8GB)', 'DDR4-3600 (XMP)', '16-18-18-36'),
(5, 'Corsair', 'Vengeance RGB Pro', '32GB (4 x 8GB)', 'DDR4-3200 (XMP)', '16-18-18-36');

-- --------------------------------------------------------

--
-- Table structure for table `t_ramgen`
--

CREATE TABLE `t_ramgen` (
  `id_ramgen` int(11) NOT NULL,
  `ram_generation` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_ramgen`
--

INSERT INTO `t_ramgen` (`id_ramgen`, `ram_generation`) VALUES
(1, 'DDR3'),
(2, 'DDR4'),
(3, 'DDR5');

-- --------------------------------------------------------

--
-- Table structure for table `t_ram_is_ramgen`
--

CREATE TABLE `t_ram_is_ramgen` (
  `id_ram_is_ramgen` int(11) NOT NULL,
  `fk_ram` int(11) NOT NULL,
  `fk_ramgen` int(11) NOT NULL,
  `date_ram_is_ramgen` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_ram_is_ramgen`
--

INSERT INTO `t_ram_is_ramgen` (`id_ram_is_ramgen`, `fk_ram`, `fk_ramgen`, `date_ram_is_ramgen`) VALUES
(1, 1, 3, '2022-03-14 19:03:54'),
(2, 2, 2, '2022-03-14 19:04:06'),
(3, 3, 2, '2022-03-14 19:04:19'),
(4, 4, 2, '2022-03-14 19:04:30'),
(5, 5, 2, '2022-03-14 19:04:41');

-- --------------------------------------------------------

--
-- Table structure for table `t_ssd`
--

CREATE TABLE `t_ssd` (
  `id_ssd` int(11) NOT NULL,
  `ssd_brand` varchar(50) DEFAULT NULL,
  `ssd_model` varchar(50) DEFAULT NULL,
  `ssd_interface` varchar(50) DEFAULT NULL,
  `ssd_form_factor` varchar(50) DEFAULT NULL,
  `ssd_capacity` varchar(50) DEFAULT NULL,
  `ssd_dram` varchar(50) DEFAULT NULL,
  `ssd_hmb` varchar(50) DEFAULT NULL,
  `ssd_nand_brand` varchar(50) DEFAULT NULL,
  `ssd_nand_type` varchar(50) DEFAULT NULL,
  `ssd_layer` varchar(50) DEFAULT NULL,
  `ssd_read_write_in_mbs` varchar(50) DEFAULT NULL,
  `ssd_categorie` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_ssd`
--

INSERT INTO `t_ssd` (`id_ssd`, `ssd_brand`, `ssd_model`, `ssd_interface`, `ssd_form_factor`, `ssd_capacity`, `ssd_dram`, `ssd_hmb`, `ssd_nand_brand`, `ssd_nand_type`, `ssd_layer`, `ssd_read_write_in_mbs`, `ssd_categorie`) VALUES
(1, 'Corsair', 'MP300', 'x2 PCIe 3.0/NVMe', 'M.2', '120GB', 'Yes', 'No', 'Kioxia', 'TLC', '64', '1600/1080', 'Budget NVMe'),
(2, 'Corsair', 'MP400', 'x4 PCIe 3.0/NVMe', 'M.2', '1TB', 'Yes', 'No', 'Intel', 'QLC', '96', '3400/3000', 'Moderate NVMe'),
(3, 'Corsair', 'MP510', 'x4 PCIe 3.0/NVMe', 'M.2', '240GB', 'Yes', 'No', 'Kioxia', 'TLC', '64', '3480/3000', 'Consumer NVMe'),
(4, 'Corsair', 'MP600', 'x4 PCIe 4.0/NVMe', 'M.2', '500GB', 'Yes', 'No', 'Kioxia', 'TLC', '96', '4950/4250', 'Prosumer NVMe'),
(5, 'Corsair', 'MP600 CORE', 'x4 PCIe 4.0/NVMe', 'M.2', '1TB-4TB', 'Yes', 'No', 'Micron', 'QLC', '96', '4950/3950', 'Prosumer NVMe'),
(6, 'Corsair', 'MP600 PRO', 'x4 PCIe 4.0/NVMe', 'M.2', '1TB-4TB', 'Yes', 'N/A', 'Micron', 'TLC', '96', '7000/6850', 'Prosumer NVMe'),
(7, 'Corsair', 'MP600 Pro Hydro X', 'x4 PCIe 4.0/NVMe', 'M.2', '1TB-2TB', 'Yes', 'N/A', 'Micron', 'TLC', '96', '7000/6850', 'Prosumer NVMe'),
(8, 'Corsair', 'MP600 Pro LPX', 'x4 PCIe 4.0/NVMe', 'M.2', '1TB-4TB', 'Yes', 'N/A', 'Micron', 'TLC', '176', '7100/6800', 'Prosumer NVMe'),
(9, 'Corsair', 'MP600 PRO XT', 'x4 PCIe 4.0/NVMe', 'M.2', '1TB-4TB', 'Yes', 'N/A', 'Micron', 'TLC', '176', '7300/6900', 'Prosumer NVMe'),
(10, 'Corsair', 'MP600 PRO XT Hydro X', 'x4 PCIe 4.0/NVMe', 'M.2', '2TB-4TB', 'Yes', 'N/A', 'Micron', 'TLC', '96', '7100/6800', 'Prosumer NVMe'),
(11, 'Crucial', 'BX500', 'SATA/AHCI', '2.5', '120GB-2TB', 'No', 'N/A', 'Micron', 'TLC/QLC', '64/96', '540/500', 'Storage SATA'),
(12, 'Crucial', 'MX300', 'SATA/AHCI', '2.5" & M.2 (1TB)', '256GB-2TB', 'Yes', 'N/A', 'Micron', 'TLC', '32', '530/500', 'Budget SATA'),
(13, 'Crucial', 'MX500', 'SATA/AHCI', '2.5" & M.2 (1TB)', '250GB-2TB', 'Yes', 'N/A', 'Micron', 'TLC', '64/96', '550/510', 'Performance SATA'),
(14, 'Crucial', 'P1', 'x4 PCIe 3.0/NVMe', 'M.2', '500GB-2TB', 'Yes', 'No', 'Micron', 'QLC', '64', '2000/1700', 'Budget NVMe'),
(15, 'Crucial', 'P2', 'x4 PCIe 3.0/NVMe', 'M.2', '250GB-2TB', 'No', 'Yes', 'Micron', 'TLC/QLC', '96', '2400/1900', 'Budget NVMe'),
(16, 'Crucial', 'P5', 'x4 PCIe 3.0/NVMe', 'M.2', '250GB-2TB', 'Yes', 'No', 'Micron', 'TLC', '96', '3400/3000', 'Consumer NVMe'),
(17, 'Crucial', 'P5 Plus', 'x4 PCIe 4.0/NVMe', 'M.2', '500GB', 'Yes', 'No', 'Micron', 'TLC', '176', '6600/5000', 'Prosumer NVMe'),
(18, 'Corsair', 'MP300', 'x2 PCIe 3.0/NVMe', 'M.2', '960GB', 'Yes', 'No', 'Kioxia', 'TLC', '64', '1600/1080', 'Budget NVMe'),
(19, 'Corsair', 'MP400', 'x4 PCIe 3.0/NVMe', 'M.2', '4TB', 'Yes', 'No', 'Intel', 'QLC', '96', '3400/3000', 'Moderate NVMe'),
(20, 'Corsair', 'MP400', 'x4 PCIe 3.0/NVMe', 'M.2', '8TB', 'Yes', 'No', 'Intel', 'QLC', '96', '3400/3000', 'Moderate NVMe'),
(21, 'Crucial', 'P5 Plus', 'x4 PCIe 4.0/NVMe', 'M.2', '1TB', 'Yes', 'No', 'Micron', 'TLC', '176', '6600/5000', 'Prosumer NVMe'),
(22, 'Crucial', 'P5 Plus', 'x4 PCIe 4.0/NVMe', 'M.2', '2TB', 'Yes', 'No', 'Micron', 'TLC', '176', '6600/5000', 'Prosumer NVMe'),
(23, 'Corsair', 'MP510', 'x4 PCIe 3.0/NVMe', 'M.2', '4TB', 'Yes', 'No', 'Kioxia', 'TLC', '64', '3480/3000', 'Consumer NVMe'),
(24, 'Corsair', 'MP600', 'x4 PCIe 4.0/NVMe', 'M.2', '1TB', 'Yes', 'No', 'Kioxia', 'TLC', '96', '4950/4250', 'Prosumer NVMe'),
(25, 'Corsair', 'MP600', 'x4 PCIe 4.0/NVMe', 'M.2', '2TB', 'Yes', 'No', 'Kioxia', 'TLC', '96', '4950/4250', 'Prosumer NVMe');

-- --------------------------------------------------------

--
-- Table structure for table `t_supply`
--

CREATE TABLE `t_supply` (
  `id_supply` int(11) NOT NULL,
  `supply_brand` varchar(20) NOT NULL,
  `supply_model` varchar(20) NOT NULL,
  `supply_power` varchar(10) NOT NULL,
  `supply_certification` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_supply`
--

INSERT INTO `t_supply` (`id_supply`, `supply_brand`, `supply_model`, `supply_power`, `supply_certification`) VALUES
(1, 'Corsair', 'RM850', '850W', '80+ Gold');

-- --------------------------------------------------------

--
-- Table structure for table `t_supply_is_format`
--

CREATE TABLE `t_supply_is_format` (
  `id_supply_is_format` int(11) NOT NULL,
  `fk_supply` int(11) NOT NULL,
  `fk_format` int(11) NOT NULL,
  `date_supply_is_format` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `t_user`
--

CREATE TABLE `t_user` (
  `id_user` int(11) NOT NULL,
  `User_firstname` varchar(50) DEFAULT NULL,
  `User_lastname` varchar(50) DEFAULT NULL,
  `User_birthdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_user`
--

INSERT INTO `t_user` (`id_user`, `User_firstname`, `User_lastname`, `User_birthdate`) VALUES
(1, 'Kevin', 'Martins', '2003-06-01'),
(2, 'Pierre', '', '2022-03-16');

-- --------------------------------------------------------

--
-- Table structure for table `t_usermail`
--

CREATE TABLE `t_usermail` (
  `id_mail` int(11) NOT NULL,
  `Mail` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_usermail`
--

INSERT INTO `t_usermail` (`id_mail`, `Mail`) VALUES
(1, 'kevin.gadanha.martins@gmail.com'),
(2, 'test@test.ch');

-- --------------------------------------------------------

--
-- Table structure for table `t_userpseudo`
--

CREATE TABLE `t_userpseudo` (
  `id_pseudo` int(11) NOT NULL,
  `userpseudo` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_userpseudo`
--

INSERT INTO `t_userpseudo` (`id_pseudo`, `userpseudo`) VALUES
(1, 'Cricko'),
(2, 'Yometa'),
(3, 'Marlon'),
(4, 'Gantil'),
(5, 'Jeff 1er');

-- --------------------------------------------------------

--
-- Table structure for table `t_userrole`
--

CREATE TABLE `t_userrole` (
  `id_userrole` int(11) NOT NULL,
  `userrole` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_userrole`
--

INSERT INTO `t_userrole` (`id_userrole`, `userrole`) VALUES
(1, 'Admin'),
(2, 'Helper'),
(4, 'Test1'),
(3, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `t_user_created_config`
--

CREATE TABLE `t_user_created_config` (
  `id_user_created_config` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_config` int(11) NOT NULL,
  `date_user_created_config` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_user_created_config`
--

INSERT INTO `t_user_created_config` (`id_user_created_config`, `fk_user`, `fk_config`, `date_user_created_config`) VALUES
(1, 1, 1, '2022-03-14 14:18:01'),
(2, 1, 2, '2022-03-18 07:33:49'),
(3, 1, 3, '2022-03-18 07:33:56');

-- --------------------------------------------------------

--
-- Table structure for table `t_user_has_usermail`
--

CREATE TABLE `t_user_has_usermail` (
  `id_user_has_usermail` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_mail` int(11) NOT NULL,
  `date_user_has_mail` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `t_user_has_userpseudo`
--

CREATE TABLE `t_user_has_userpseudo` (
  `id_user_has_userpseudo` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_pseudo` int(11) NOT NULL,
  `date_user_has_pseudo` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_user_has_userpseudo`
--

INSERT INTO `t_user_has_userpseudo` (`id_user_has_userpseudo`, `fk_user`, `fk_pseudo`, `date_user_has_pseudo`) VALUES
(1, 1, 1, '2022-03-14 13:56:47');

-- --------------------------------------------------------

--
-- Table structure for table `t_user_has_userrole`
--

CREATE TABLE `t_user_has_userrole` (
  `id_user_has_userrole` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_userrole` int(11) NOT NULL,
  `date_user_has_role` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_user_has_userrole`
--

INSERT INTO `t_user_has_userrole` (`id_user_has_userrole`, `fk_user`, `fk_userrole`, `date_user_has_role`) VALUES
(2, 1, 1, '2022-03-15 09:44:48');

-- --------------------------------------------------------

--
-- Table structure for table `t_watercooling`
--

CREATE TABLE `t_watercooling` (
  `id_watercooling` int(11) NOT NULL,
  `watercooling_brand` varchar(50) DEFAULT NULL,
  `watercooling_model` varchar(50) DEFAULT NULL,
  `watercooling_scale` varchar(50) DEFAULT NULL,
  `watercooling_dimensions` varchar(50) DEFAULT NULL,
  `watercooling_socket_support` varchar(100) DEFAULT NULL,
  `watercooling_fan_speed` varchar(25) DEFAULT NULL,
  `watercooling_noise_level` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_watercooling`
--

INSERT INTO `t_watercooling` (`id_watercooling`, `watercooling_brand`, `watercooling_model`, `watercooling_scale`, `watercooling_dimensions`, `watercooling_socket_support`, `watercooling_fan_speed`, `watercooling_noise_level`) VALUES
(1, 'EK-AIO', 'Basic 240', '240mm', '275 x 120 x 27mm', 'Intel LGA: 1150, 1151, 1155, 1156, 1200, 2011, 2011-3, 2066, AMD: AM4', '550–2200RPM', 'Up to 33.5dB(A)');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `t_aircooling`
--
ALTER TABLE `t_aircooling`
  ADD PRIMARY KEY (`id_aircooling`);

--
-- Indexes for table `t_case`
--
ALTER TABLE `t_case`
  ADD PRIMARY KEY (`id_case`);

--
-- Indexes for table `t_case_is_format`
--
ALTER TABLE `t_case_is_format`
  ADD PRIMARY KEY (`id_case_is_format`) USING BTREE,
  ADD KEY `fk_case` (`fk_case`),
  ADD KEY `fk_format` (`fk_format`);

--
-- Indexes for table `t_config`
--
ALTER TABLE `t_config`
  ADD PRIMARY KEY (`id_config`);

--
-- Indexes for table `t_config_has_aircooling`
--
ALTER TABLE `t_config_has_aircooling`
  ADD PRIMARY KEY (`id_config_has_aircooling`) USING BTREE,
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_cooling` (`fk_aircooling`) USING BTREE;

--
-- Indexes for table `t_config_has_case`
--
ALTER TABLE `t_config_has_case`
  ADD PRIMARY KEY (`id_config_has_case`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_case` (`fk_case`);

--
-- Indexes for table `t_config_has_cpu`
--
ALTER TABLE `t_config_has_cpu`
  ADD PRIMARY KEY (`id_config_has_cpu`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_cpu` (`fk_cpu`);

--
-- Indexes for table `t_config_has_gpu`
--
ALTER TABLE `t_config_has_gpu`
  ADD PRIMARY KEY (`id_config_has_gpu`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_gpu` (`fk_gpu`);

--
-- Indexes for table `t_config_has_hdd`
--
ALTER TABLE `t_config_has_hdd`
  ADD PRIMARY KEY (`id_config_has_hdd`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_hdd` (`fk_hdd`);

--
-- Indexes for table `t_config_has_motherboard`
--
ALTER TABLE `t_config_has_motherboard`
  ADD PRIMARY KEY (`id_config_has_motherboard`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_motherboard` (`fk_motherboard`);

--
-- Indexes for table `t_config_has_ram`
--
ALTER TABLE `t_config_has_ram`
  ADD PRIMARY KEY (`id_config_has_ram`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_ram` (`fk_ram`);

--
-- Indexes for table `t_config_has_ssd`
--
ALTER TABLE `t_config_has_ssd`
  ADD PRIMARY KEY (`id_config_has_ssd`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_ssd` (`fk_ssd`);

--
-- Indexes for table `t_config_has_supply`
--
ALTER TABLE `t_config_has_supply`
  ADD PRIMARY KEY (`id_config_has_supply`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_supply` (`fk_supply`);

--
-- Indexes for table `t_config_has_watercooling`
--
ALTER TABLE `t_config_has_watercooling`
  ADD PRIMARY KEY (`id_config_has_watercooling`),
  ADD KEY `fk_config` (`fk_config`),
  ADD KEY `fk_watercooling` (`fk_watercooling`);

--
-- Indexes for table `t_cpu`
--
ALTER TABLE `t_cpu`
  ADD PRIMARY KEY (`id_cpu`);

--
-- Indexes for table `t_cpumanufacturer`
--
ALTER TABLE `t_cpumanufacturer`
  ADD PRIMARY KEY (`id_cpu_manufacturer`);

--
-- Indexes for table `t_cpumanufacturer_produce_cpu`
--
ALTER TABLE `t_cpumanufacturer_produce_cpu`
  ADD PRIMARY KEY (`id_cpumanufacturer_produce_cpu`),
  ADD KEY `fk_cpu` (`fk_cpu`),
  ADD KEY `fk_cpumanufacturer` (`fk_cpumanufacturer`);

--
-- Indexes for table `t_cpu_compatible_motherboard`
--
ALTER TABLE `t_cpu_compatible_motherboard`
  ADD PRIMARY KEY (`id_cpu_compatible_motherboard`) USING BTREE,
  ADD KEY `fk_cpu` (`fk_cpu`),
  ADD KEY `fk_motherboard` (`fk_motherboard`);

--
-- Indexes for table `t_cpu_compatible_ramgen`
--
ALTER TABLE `t_cpu_compatible_ramgen`
  ADD PRIMARY KEY (`id_cpu_compatible_ramgen`) USING BTREE,
  ADD KEY `fk_ramgen` (`fk_ramgen`),
  ADD KEY `fk_cpu` (`fk_cpu`) USING BTREE;

--
-- Indexes for table `t_format`
--
ALTER TABLE `t_format`
  ADD PRIMARY KEY (`id_format`);

--
-- Indexes for table `t_gpu`
--
ALTER TABLE `t_gpu`
  ADD PRIMARY KEY (`id_gpu`);

--
-- Indexes for table `t_gpumanufacturer`
--
ALTER TABLE `t_gpumanufacturer`
  ADD PRIMARY KEY (`id_gpumanufacturer`) USING BTREE;

--
-- Indexes for table `t_gpumanufacturer_produce_gpu`
--
ALTER TABLE `t_gpumanufacturer_produce_gpu`
  ADD PRIMARY KEY (`id_gpumanufacturer_produce_gpu`),
  ADD KEY `fk_gpumanufacturer` (`fk_gpumanufacturer`),
  ADD KEY `fk_gpu` (`fk_gpu`);

--
-- Indexes for table `t_hdd`
--
ALTER TABLE `t_hdd`
  ADD PRIMARY KEY (`id_hdd`);

--
-- Indexes for table `t_motherboard`
--
ALTER TABLE `t_motherboard`
  ADD PRIMARY KEY (`id_motherboard`);

--
-- Indexes for table `t_motherboard_is_format`
--
ALTER TABLE `t_motherboard_is_format`
  ADD PRIMARY KEY (`id_motherboard_is_format`) USING BTREE,
  ADD KEY `fk_motherboard` (`fk_motherboard`),
  ADD KEY `fk_format` (`fk_format`);

--
-- Indexes for table `t_ram`
--
ALTER TABLE `t_ram`
  ADD PRIMARY KEY (`id_ram`);

--
-- Indexes for table `t_ramgen`
--
ALTER TABLE `t_ramgen`
  ADD PRIMARY KEY (`id_ramgen`);

--
-- Indexes for table `t_ram_is_ramgen`
--
ALTER TABLE `t_ram_is_ramgen`
  ADD PRIMARY KEY (`id_ram_is_ramgen`) USING BTREE,
  ADD KEY `fk_ram` (`fk_ram`),
  ADD KEY `fk_ramgen` (`fk_ramgen`);

--
-- Indexes for table `t_ssd`
--
ALTER TABLE `t_ssd`
  ADD PRIMARY KEY (`id_ssd`);

--
-- Indexes for table `t_supply`
--
ALTER TABLE `t_supply`
  ADD PRIMARY KEY (`id_supply`);

--
-- Indexes for table `t_supply_is_format`
--
ALTER TABLE `t_supply_is_format`
  ADD PRIMARY KEY (`id_supply_is_format`) USING BTREE,
  ADD KEY `fk_supply` (`fk_supply`),
  ADD KEY `fk_format` (`fk_format`);

--
-- Indexes for table `t_user`
--
ALTER TABLE `t_user`
  ADD PRIMARY KEY (`id_user`);

--
-- Indexes for table `t_usermail`
--
ALTER TABLE `t_usermail`
  ADD PRIMARY KEY (`id_mail`);

--
-- Indexes for table `t_userpseudo`
--
ALTER TABLE `t_userpseudo`
  ADD PRIMARY KEY (`id_pseudo`);

--
-- Indexes for table `t_userrole`
--
ALTER TABLE `t_userrole`
  ADD PRIMARY KEY (`id_userrole`) USING BTREE;

--
-- Indexes for table `t_user_created_config`
--
ALTER TABLE `t_user_created_config`
  ADD PRIMARY KEY (`id_user_created_config`),
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_config` (`fk_config`);

--
-- Indexes for table `t_user_has_usermail`
--
ALTER TABLE `t_user_has_usermail`
  ADD PRIMARY KEY (`id_user_has_usermail`) USING BTREE,
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_mail` (`fk_mail`);

--
-- Indexes for table `t_user_has_userpseudo`
--
ALTER TABLE `t_user_has_userpseudo`
  ADD PRIMARY KEY (`id_user_has_userpseudo`) USING BTREE,
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_pseudo` (`fk_pseudo`);

--
-- Indexes for table `t_user_has_userrole`
--
ALTER TABLE `t_user_has_userrole`
  ADD PRIMARY KEY (`id_user_has_userrole`) USING BTREE,
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_role` (`fk_userrole`) USING BTREE;

--
-- Indexes for table `t_watercooling`
--
ALTER TABLE `t_watercooling`
  ADD PRIMARY KEY (`id_watercooling`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `t_aircooling`
--
ALTER TABLE `t_aircooling`
  MODIFY `id_aircooling` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `t_case`
--
ALTER TABLE `t_case`
  MODIFY `id_case` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `t_case_is_format`
--
ALTER TABLE `t_case_is_format`
  MODIFY `id_case_is_format` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `t_config`
--
ALTER TABLE `t_config`
  MODIFY `id_config` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_config_has_aircooling`
--
ALTER TABLE `t_config_has_aircooling`
  MODIFY `id_config_has_aircooling` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_config_has_case`
--
ALTER TABLE `t_config_has_case`
  MODIFY `id_config_has_case` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_config_has_cpu`
--
ALTER TABLE `t_config_has_cpu`
  MODIFY `id_config_has_cpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_config_has_gpu`
--
ALTER TABLE `t_config_has_gpu`
  MODIFY `id_config_has_gpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_config_has_hdd`
--
ALTER TABLE `t_config_has_hdd`
  MODIFY `id_config_has_hdd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_config_has_motherboard`
--
ALTER TABLE `t_config_has_motherboard`
  MODIFY `id_config_has_motherboard` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_config_has_ram`
--
ALTER TABLE `t_config_has_ram`
  MODIFY `id_config_has_ram` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_config_has_ssd`
--
ALTER TABLE `t_config_has_ssd`
  MODIFY `id_config_has_ssd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_config_has_supply`
--
ALTER TABLE `t_config_has_supply`
  MODIFY `id_config_has_supply` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_config_has_watercooling`
--
ALTER TABLE `t_config_has_watercooling`
  MODIFY `id_config_has_watercooling` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `t_cpu`
--
ALTER TABLE `t_cpu`
  MODIFY `id_cpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=243;
--
-- AUTO_INCREMENT for table `t_cpumanufacturer`
--
ALTER TABLE `t_cpumanufacturer`
  MODIFY `id_cpu_manufacturer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_cpumanufacturer_produce_cpu`
--
ALTER TABLE `t_cpumanufacturer_produce_cpu`
  MODIFY `id_cpumanufacturer_produce_cpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `t_cpu_compatible_motherboard`
--
ALTER TABLE `t_cpu_compatible_motherboard`
  MODIFY `id_cpu_compatible_motherboard` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `t_cpu_compatible_ramgen`
--
ALTER TABLE `t_cpu_compatible_ramgen`
  MODIFY `id_cpu_compatible_ramgen` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `t_format`
--
ALTER TABLE `t_format`
  MODIFY `id_format` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `t_gpu`
--
ALTER TABLE `t_gpu`
  MODIFY `id_gpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `t_gpumanufacturer`
--
ALTER TABLE `t_gpumanufacturer`
  MODIFY `id_gpumanufacturer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_gpumanufacturer_produce_gpu`
--
ALTER TABLE `t_gpumanufacturer_produce_gpu`
  MODIFY `id_gpumanufacturer_produce_gpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `t_hdd`
--
ALTER TABLE `t_hdd`
  MODIFY `id_hdd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_motherboard`
--
ALTER TABLE `t_motherboard`
  MODIFY `id_motherboard` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `t_motherboard_is_format`
--
ALTER TABLE `t_motherboard_is_format`
  MODIFY `id_motherboard_is_format` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `t_ram`
--
ALTER TABLE `t_ram`
  MODIFY `id_ram` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `t_ramgen`
--
ALTER TABLE `t_ramgen`
  MODIFY `id_ramgen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_ram_is_ramgen`
--
ALTER TABLE `t_ram_is_ramgen`
  MODIFY `id_ram_is_ramgen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `t_ssd`
--
ALTER TABLE `t_ssd`
  MODIFY `id_ssd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `t_supply`
--
ALTER TABLE `t_supply`
  MODIFY `id_supply` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `t_supply_is_format`
--
ALTER TABLE `t_supply_is_format`
  MODIFY `id_supply_is_format` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `t_user`
--
ALTER TABLE `t_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_usermail`
--
ALTER TABLE `t_usermail`
  MODIFY `id_mail` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_userpseudo`
--
ALTER TABLE `t_userpseudo`
  MODIFY `id_pseudo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `t_userrole`
--
ALTER TABLE `t_userrole`
  MODIFY `id_userrole` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_user_created_config`
--
ALTER TABLE `t_user_created_config`
  MODIFY `id_user_created_config` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_user_has_usermail`
--
ALTER TABLE `t_user_has_usermail`
  MODIFY `id_user_has_usermail` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `t_user_has_userpseudo`
--
ALTER TABLE `t_user_has_userpseudo`
  MODIFY `id_user_has_userpseudo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `t_user_has_userrole`
--
ALTER TABLE `t_user_has_userrole`
  MODIFY `id_user_has_userrole` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `t_watercooling`
--
ALTER TABLE `t_watercooling`
  MODIFY `id_watercooling` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `t_case_is_format`
--
ALTER TABLE `t_case_is_format`
  ADD CONSTRAINT `t_case_is_format_ibfk_1` FOREIGN KEY (`fk_case`) REFERENCES `t_case` (`id_case`),
  ADD CONSTRAINT `t_case_is_format_ibfk_2` FOREIGN KEY (`fk_format`) REFERENCES `t_format` (`id_format`);

--
-- Constraints for table `t_config_has_aircooling`
--
ALTER TABLE `t_config_has_aircooling`
  ADD CONSTRAINT `t_config_has_aircooling_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_aircooling_ibfk_2` FOREIGN KEY (`fk_aircooling`) REFERENCES `t_aircooling` (`id_aircooling`);

--
-- Constraints for table `t_config_has_case`
--
ALTER TABLE `t_config_has_case`
  ADD CONSTRAINT `t_config_has_case_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_case_ibfk_2` FOREIGN KEY (`fk_case`) REFERENCES `t_case` (`id_case`);

--
-- Constraints for table `t_config_has_cpu`
--
ALTER TABLE `t_config_has_cpu`
  ADD CONSTRAINT `t_config_has_cpu_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_cpu_ibfk_2` FOREIGN KEY (`fk_cpu`) REFERENCES `t_cpu` (`id_cpu`);

--
-- Constraints for table `t_config_has_gpu`
--
ALTER TABLE `t_config_has_gpu`
  ADD CONSTRAINT `t_config_has_gpu_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_gpu_ibfk_2` FOREIGN KEY (`fk_gpu`) REFERENCES `t_gpu` (`id_gpu`);

--
-- Constraints for table `t_config_has_hdd`
--
ALTER TABLE `t_config_has_hdd`
  ADD CONSTRAINT `t_config_has_hdd_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_hdd_ibfk_2` FOREIGN KEY (`fk_hdd`) REFERENCES `t_hdd` (`id_hdd`);

--
-- Constraints for table `t_config_has_motherboard`
--
ALTER TABLE `t_config_has_motherboard`
  ADD CONSTRAINT `t_config_has_motherboard_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_motherboard_ibfk_2` FOREIGN KEY (`fk_motherboard`) REFERENCES `t_motherboard` (`id_motherboard`);

--
-- Constraints for table `t_config_has_ram`
--
ALTER TABLE `t_config_has_ram`
  ADD CONSTRAINT `t_config_has_ram_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_ram_ibfk_2` FOREIGN KEY (`fk_ram`) REFERENCES `t_ram` (`id_ram`);

--
-- Constraints for table `t_config_has_ssd`
--
ALTER TABLE `t_config_has_ssd`
  ADD CONSTRAINT `t_config_has_ssd_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_ssd_ibfk_2` FOREIGN KEY (`fk_ssd`) REFERENCES `t_ssd` (`id_ssd`);

--
-- Constraints for table `t_config_has_supply`
--
ALTER TABLE `t_config_has_supply`
  ADD CONSTRAINT `t_config_has_supply_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_supply_ibfk_2` FOREIGN KEY (`fk_supply`) REFERENCES `t_supply` (`id_supply`);

--
-- Constraints for table `t_config_has_watercooling`
--
ALTER TABLE `t_config_has_watercooling`
  ADD CONSTRAINT `t_config_has_watercooling_ibfk_1` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`),
  ADD CONSTRAINT `t_config_has_watercooling_ibfk_2` FOREIGN KEY (`fk_watercooling`) REFERENCES `t_watercooling` (`id_watercooling`);

--
-- Constraints for table `t_cpumanufacturer_produce_cpu`
--
ALTER TABLE `t_cpumanufacturer_produce_cpu`
  ADD CONSTRAINT `t_cpumanufacturer_produce_cpu_ibfk_1` FOREIGN KEY (`fk_cpumanufacturer`) REFERENCES `t_cpumanufacturer` (`id_cpu_manufacturer`),
  ADD CONSTRAINT `t_cpumanufacturer_produce_cpu_ibfk_2` FOREIGN KEY (`fk_cpu`) REFERENCES `t_cpu` (`id_cpu`);

--
-- Constraints for table `t_cpu_compatible_motherboard`
--
ALTER TABLE `t_cpu_compatible_motherboard`
  ADD CONSTRAINT `t_cpu_compatible_motherboard_ibfk_1` FOREIGN KEY (`fk_cpu`) REFERENCES `t_cpu` (`id_cpu`),
  ADD CONSTRAINT `t_cpu_compatible_motherboard_ibfk_2` FOREIGN KEY (`fk_motherboard`) REFERENCES `t_motherboard` (`id_motherboard`);

--
-- Constraints for table `t_cpu_compatible_ramgen`
--
ALTER TABLE `t_cpu_compatible_ramgen`
  ADD CONSTRAINT `t_cpu_compatible_ramgen_ibfk_1` FOREIGN KEY (`fk_cpu`) REFERENCES `t_cpu` (`id_cpu`),
  ADD CONSTRAINT `t_cpu_compatible_ramgen_ibfk_2` FOREIGN KEY (`fk_ramgen`) REFERENCES `t_ramgen` (`id_ramgen`);

--
-- Constraints for table `t_gpumanufacturer_produce_gpu`
--
ALTER TABLE `t_gpumanufacturer_produce_gpu`
  ADD CONSTRAINT `t_gpumanufacturer_produce_gpu_ibfk_1` FOREIGN KEY (`fk_gpumanufacturer`) REFERENCES `t_gpumanufacturer` (`id_gpumanufacturer`),
  ADD CONSTRAINT `t_gpumanufacturer_produce_gpu_ibfk_2` FOREIGN KEY (`fk_gpu`) REFERENCES `t_gpu` (`id_gpu`);

--
-- Constraints for table `t_motherboard_is_format`
--
ALTER TABLE `t_motherboard_is_format`
  ADD CONSTRAINT `t_motherboard_is_format_ibfk_1` FOREIGN KEY (`fk_motherboard`) REFERENCES `t_motherboard` (`id_motherboard`),
  ADD CONSTRAINT `t_motherboard_is_format_ibfk_2` FOREIGN KEY (`fk_format`) REFERENCES `t_format` (`id_format`);

--
-- Constraints for table `t_ram_is_ramgen`
--
ALTER TABLE `t_ram_is_ramgen`
  ADD CONSTRAINT `t_ram_is_ramgen_ibfk_1` FOREIGN KEY (`fk_ram`) REFERENCES `t_ram` (`id_ram`),
  ADD CONSTRAINT `t_ram_is_ramgen_ibfk_2` FOREIGN KEY (`fk_ramgen`) REFERENCES `t_ramgen` (`id_ramgen`);

--
-- Constraints for table `t_supply_is_format`
--
ALTER TABLE `t_supply_is_format`
  ADD CONSTRAINT `t_supply_is_format_ibfk_1` FOREIGN KEY (`fk_supply`) REFERENCES `t_supply` (`id_supply`),
  ADD CONSTRAINT `t_supply_is_format_ibfk_2` FOREIGN KEY (`fk_format`) REFERENCES `t_format` (`id_format`);

--
-- Constraints for table `t_user_created_config`
--
ALTER TABLE `t_user_created_config`
  ADD CONSTRAINT `t_user_created_config_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_user_created_config_ibfk_2` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`);

--
-- Constraints for table `t_user_has_usermail`
--
ALTER TABLE `t_user_has_usermail`
  ADD CONSTRAINT `t_user_has_usermail_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_user_has_usermail_ibfk_2` FOREIGN KEY (`fk_mail`) REFERENCES `t_usermail` (`id_mail`);

--
-- Constraints for table `t_user_has_userpseudo`
--
ALTER TABLE `t_user_has_userpseudo`
  ADD CONSTRAINT `t_user_has_userpseudo_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_user_has_userpseudo_ibfk_2` FOREIGN KEY (`fk_pseudo`) REFERENCES `t_userpseudo` (`id_pseudo`);

--
-- Constraints for table `t_user_has_userrole`
--
ALTER TABLE `t_user_has_userrole`
  ADD CONSTRAINT `t_user_has_userrole_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_user_has_userrole_ibfk_2` FOREIGN KEY (`fk_userrole`) REFERENCES `t_userrole` (`id_userrole`);
