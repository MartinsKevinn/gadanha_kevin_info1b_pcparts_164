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
  `config_rating` enum('5/5','4/5','3/5','2/5','1/5') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_config`
--

INSERT INTO `t_config` (`id_config`, `config_use_case`, `config_rating`) VALUES
(1, 'Gaming', '3/5'),
(2, 'Work', '1/5'),
(3, 'Gaming', '5/5');

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
(8, 2, 183, '2022-03-18 10:28:42'),
(9, 1, 75, '2022-05-25 05:51:44'),
(10, 2, 242, '2022-05-27 14:51:55'),
(11, 2, 241, '2022-05-27 14:52:12');

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

--
-- Dumping data for table `t_cpu_compatible_motherboard`
--

INSERT INTO `t_cpu_compatible_motherboard` (`id_cpu_compatible_motherboard`, `fk_cpu`, `fk_motherboard`, `date_cpu_compatible_motherboard`) VALUES
(1, 239, 7, '2022-05-14 13:33:25'),
(2, 239, 6, '2022-05-14 13:34:01'),
(3, 236, 6, '2022-05-14 13:35:16'),
(4, 236, 1, '2022-05-14 13:42:10'),
(5, 236, 2, '2022-05-14 13:42:10'),
(6, 236, 3, '2022-05-14 13:42:10');

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
(5, 'ASRock', 'RX 6900 XT Phantom Gaming D OC', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1925, 2000, 5120, 320, 128, 350, '2020-10-28'),
(6, 'GIGABYTE', 'AORUS RX 6900 XT MASTER', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1950, 2000, 5120, 320, 128, 300, '2020-10-28'),
(7, 'MSI', 'RX 6900 XT GAMING Z TRIO', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 2050, 2430, 5120, 320, 128, 300, '2020-10-28'),
(8, 'PowerColor', 'Red Devil RX 6900 XT', 'Navi 21', 'PCIe 4.0 x16', '16GB GDDR6, 256 bit', 1925, 2000, 5120, 320, 128, 300, '2020-10-28');

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
  `motherboard_release_year` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_motherboard`
--

INSERT INTO `t_motherboard` (`id_motherboard`, `motherboard_brand`, `motherboard_model`, `motherboard_socket`, `motherboard_release_year`) VALUES
(1, 'Gigabyte ', 'B450 Aorus Elite', '1x AM4', '2018-01-01'),
(2, 'Asrock ', 'B450 Steel Legend', '1x AM4', '2019-01-01'),
(3, 'Asus ', 'ROG Strix X570-E Gaming', '1x AM4', '2019-01-01'),
(4, 'Gigabyte	', 'B550 Aorus Master', '1x AM4', '2020-01-01'),
(5, 'Asrock', 'B550 Taichi', '1x AM4', '2020-01-01'),
(6, 'MSI', 'MEG X570 Godlike', '1x AM4', '2019-01-01'),
(7, 'MSI', 'MEG X570 Creation', '1x AM4', '2019-01-01'),
(8, 'Asrock ', 'X570 Aqua', '1x AM4', '2019-01-01');

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
(1, 'G.Skill', 'Trident Z RGB', '32GB (2 x 16GB)', 'DDR5-6000 (XMP)', '36-36-36-76'),
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
(5, 5, 2, '2022-03-14 19:04:41'),
(6, 1, 2, '2022-05-26 16:21:58');

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
  `User_birthdate` date DEFAULT NULL,
  `User_photo` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_user`
--

INSERT INTO `t_user` (`id_user`, `User_firstname`, `User_lastname`, `User_birthdate`, `User_photo`) VALUES
(28, 'Pierre', 'Poirier', '1989-05-27', 'data:image/png;base64,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'),
(29, 'Paul', 'Tier', '2022-04-27', 'data:image/png;base64,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'),
(31, 'Noam', 'Brid', '2022-04-30', 'data:image/jpeg;base64,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'),
(32, 'Ali', 'Fair', '2004-05-14', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuKoXZ9RUzidNz40ZuSpkjPGmDAywSEW8S-g&usqp=CAU'),
(33, 'Michel', 'Terrier', '1999-05-28', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVT01Y1xw38z-0eHMN2f5YqwDK4sEYnXq9mw&usqp=CAU');

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
(2, 'Helper'),
(3, 'User'),
(5, 'Superadmin'),
(8, 'SuperHelperPythonSQL'),
(9, 'Admin');

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
(5, 29, 3, '2022-05-24 19:51:57');

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
(39, 28, 5, '2022-05-24 17:26:50'),
(40, 28, 9, '2022-05-24 17:33:02'),
(41, 32, 3, '2022-05-26 16:48:46'),
(42, 33, 3, '2022-05-30 12:00:47'),
(43, 31, 3, '2022-05-30 12:00:58'),
(44, 28, 3, '2022-05-30 12:01:07'),
(45, 29, 2, '2022-05-30 12:01:14'),
(46, 29, 3, '2022-05-30 12:01:14');

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
  ADD PRIMARY KEY (`id_user`) USING BTREE;

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
  ADD PRIMARY KEY (`id_user_created_config`) USING BTREE,
  ADD KEY `fk_user` (`fk_user`) USING BTREE,
  ADD KEY `fk_config` (`fk_config`) USING BTREE;

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
  ADD KEY `fk_user` (`fk_user`) USING BTREE,
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
  MODIFY `id_cpumanufacturer_produce_cpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `t_cpu_compatible_motherboard`
--
ALTER TABLE `t_cpu_compatible_motherboard`
  MODIFY `id_cpu_compatible_motherboard` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
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
  MODIFY `id_ram_is_ramgen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
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
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
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
  MODIFY `id_userrole` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `t_user_created_config`
--
ALTER TABLE `t_user_created_config`
  MODIFY `id_user_created_config` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `t_user_has_usermail`
--
ALTER TABLE `t_user_has_usermail`
  MODIFY `id_user_has_usermail` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `t_user_has_userpseudo`
--
ALTER TABLE `t_user_has_userpseudo`
  MODIFY `id_user_has_userpseudo` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `t_user_has_userrole`
--
ALTER TABLE `t_user_has_userrole`
  MODIFY `id_user_has_userrole` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
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
  ADD CONSTRAINT `t_cpumanufacturer_produce_cpu_ibfk_1` FOREIGN KEY (`fk_cpumanufacturer`) REFERENCES `t_cpumanufacturer` (`id_cpu_manufacturer`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `t_cpumanufacturer_produce_cpu_ibfk_2` FOREIGN KEY (`fk_cpu`) REFERENCES `t_cpu` (`id_cpu`) ON DELETE CASCADE ON UPDATE CASCADE;

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
  ADD CONSTRAINT `t_user_created_config_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `t_user_created_config_ibfk_2` FOREIGN KEY (`fk_config`) REFERENCES `t_config` (`id_config`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `t_user_has_usermail`
--
ALTER TABLE `t_user_has_usermail`
  ADD CONSTRAINT `t_user_has_usermail_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `t_user_has_usermail_ibfk_2` FOREIGN KEY (`fk_mail`) REFERENCES `t_usermail` (`id_mail`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `t_user_has_userpseudo`
--
ALTER TABLE `t_user_has_userpseudo`
  ADD CONSTRAINT `t_user_has_userpseudo_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `t_user_has_userpseudo_ibfk_2` FOREIGN KEY (`fk_pseudo`) REFERENCES `t_userpseudo` (`id_pseudo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `t_user_has_userrole`
--
ALTER TABLE `t_user_has_userrole`
  ADD CONSTRAINT `t_user_has_userrole_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `t_user_has_userrole_ibfk_2` FOREIGN KEY (`fk_userrole`) REFERENCES `t_userrole` (`id_userrole`) ON DELETE CASCADE ON UPDATE CASCADE;