-- phpMyAdmin SQL Dump
-- version 6.0.0-dev+20260224.690be10763
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 29, 2026 at 12:33 PM
-- Server version: 8.4.3
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `darosa_lucas_deva1a_chiens_164_2026`
--

-- --------------------------------------------------------

--
-- Table structure for table `t_chien`
--

CREATE TABLE `t_chien` (
  `id_chien` int NOT NULL,
  `nom` int DEFAULT NULL,
  `race` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `taille` int DEFAULT NULL,
  `notes` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_client`
--

CREATE TABLE `t_client` (
  `id_client` int NOT NULL,
  `nom` int DEFAULT NULL,
  `prenom` int DEFAULT NULL,
  `email` int DEFAULT NULL,
  `telephone` int DEFAULT NULL,
  `adresse` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_client_chien`
--

CREATE TABLE `t_client_chien` (
  `id_client_chien` int NOT NULL,
  `FK_client` int DEFAULT NULL,
  `FK_chien` int DEFAULT NULL,
  `date_d'aquisition` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_promeneur`
--

CREATE TABLE `t_promeneur` (
  `id_promeneur` int NOT NULL,
  `nom` int DEFAULT NULL,
  `prenom` int DEFAULT NULL,
  `email` int DEFAULT NULL,
  `telephone` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_promeneur_chien_service`
--

CREATE TABLE `t_promeneur_chien_service` (
  `id_promeneur_chien_service` int NOT NULL,
  `FK_promeneur` int DEFAULT NULL,
  `FK_chien` int DEFAULT NULL,
  `FK_service` int DEFAULT NULL,
  `date_promenade` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_reservation`
--

CREATE TABLE `t_reservation` (
  `id_reservation` int NOT NULL,
  `date` int DEFAULT NULL,
  `heure_debut` int DEFAULT NULL,
  `heure_fin` int DEFAULT NULL,
  `statut` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `t_service`
--

CREATE TABLE `t_service` (
  `id_service` int NOT NULL,
  `type_service` varchar(70) DEFAULT NULL,
  `duree` int DEFAULT NULL,
  `prix` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `t_service`
--

INSERT INTO `t_service` (`id_service`, `type_service`, `duree`, `prix`) VALUES
(2, 'wdad1d2313', 11111, 223),
(3, 'merde', 12313, 2442),
(4, 'wswsd', NULL, NULL),
(5, 'xsxxa', NULL, NULL),
(6, 'wdwdwa', 45, 2322323),
(7, 'dadwa', 23323, 32323),
(8, 'journée', 2324, 244),
(9, 'dadad', 1111, 1111),
(10, 'wdad', 122, 333),
(11, 'wwdwada', 1323, 1231321),
(12, 'wads', 1212, 32332332),
(13, 'dasddwg', 12323, 324555),
(14, 'dadawd', 53227, 72828),
(15, 'dasdadsawds', 1121, 21123),
(16, 'promeneur', 5023, 23);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `t_chien`
--
ALTER TABLE `t_chien`
  ADD PRIMARY KEY (`id_chien`);

--
-- Indexes for table `t_client`
--
ALTER TABLE `t_client`
  ADD PRIMARY KEY (`id_client`);

--
-- Indexes for table `t_client_chien`
--
ALTER TABLE `t_client_chien`
  ADD PRIMARY KEY (`id_client_chien`),
  ADD KEY `t_chien_FK` (`FK_chien`),
  ADD KEY `t_client_FK` (`FK_client`);

--
-- Indexes for table `t_promeneur`
--
ALTER TABLE `t_promeneur`
  ADD PRIMARY KEY (`id_promeneur`);

--
-- Indexes for table `t_promeneur_chien_service`
--
ALTER TABLE `t_promeneur_chien_service`
  ADD PRIMARY KEY (`id_promeneur_chien_service`),
  ADD KEY `t_promeneur_FK` (`FK_promeneur`),
  ADD KEY `t_service_FK` (`FK_service`),
  ADD KEY `t_chien_client_FK$` (`FK_chien`);

--
-- Indexes for table `t_reservation`
--
ALTER TABLE `t_reservation`
  ADD PRIMARY KEY (`id_reservation`);

--
-- Indexes for table `t_service`
--
ALTER TABLE `t_service`
  ADD PRIMARY KEY (`id_service`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `t_chien`
--
ALTER TABLE `t_chien`
  MODIFY `id_chien` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `t_client`
--
ALTER TABLE `t_client`
  MODIFY `id_client` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `t_client_chien`
--
ALTER TABLE `t_client_chien`
  MODIFY `id_client_chien` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `t_promeneur`
--
ALTER TABLE `t_promeneur`
  MODIFY `id_promeneur` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `t_promeneur_chien_service`
--
ALTER TABLE `t_promeneur_chien_service`
  MODIFY `id_promeneur_chien_service` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `t_reservation`
--
ALTER TABLE `t_reservation`
  MODIFY `id_reservation` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `t_service`
--
ALTER TABLE `t_service`
  MODIFY `id_service` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `t_client_chien`
--
ALTER TABLE `t_client_chien`
  ADD CONSTRAINT `t_chien_FK` FOREIGN KEY (`FK_chien`) REFERENCES `t_chien` (`id_chien`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `t_client_FK` FOREIGN KEY (`FK_client`) REFERENCES `t_client` (`id_client`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `t_promeneur_chien_service`
--
ALTER TABLE `t_promeneur_chien_service`
  ADD CONSTRAINT `t_chien_client_FK$` FOREIGN KEY (`FK_chien`) REFERENCES `t_chien` (`id_chien`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `t_promeneur_FK` FOREIGN KEY (`FK_promeneur`) REFERENCES `t_promeneur` (`id_promeneur`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `t_service_FK` FOREIGN KEY (`FK_service`) REFERENCES `t_service` (`id_service`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
