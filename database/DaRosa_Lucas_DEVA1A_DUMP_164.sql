-- phpMyAdmin SQL Dump
-- version 6.0.0-dev+20260224.690be10763
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 01, 2026 at 10:45 AM
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
  `nom` varchar(70) DEFAULT NULL,
  `race` varchar(70) DEFAULT NULL,
  `age` varchar(30) DEFAULT NULL,
  `taille` varchar(100) DEFAULT NULL,
  `notes` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `t_chien`
--

INSERT INTO `t_chien` (`id_chien`, `nom`, `race`, `age`, `taille`, `notes`) VALUES
(4, 'Rex', 'Labrador', '4', '60', 'Gentil'),
(5, 'Bella', 'Golden Retriever', '5', '55', 'Joueur'),
(6, 'Max', 'Berger Allemand', '2', '65', 'Energique'),
(7, 'Luna', 'Caniche', '4', '35', 'Calme'),
(8, 'Rocky', 'Husky', '6', '58', 'Actif'),
(9, 'Nala', 'Beagle', '1', '38', 'Curieux'),
(10, 'Zeus', 'Rottweiler', '4', '70', 'Protecteur'),
(11, 'Lily', 'Chihuahua', '3', '20', 'Nerveux'),
(12, 'Bruno ', 'Bouledogue', '7', '45', 'Paresseux'),
(13, 'Mia', 'Dalmatien', '2', '52', 'Playdul');

-- --------------------------------------------------------

--
-- Table structure for table `t_client`
--

CREATE TABLE `t_client` (
  `id_client` int NOT NULL,
  `nom` varchar(70) DEFAULT NULL,
  `prenom` varchar(70) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `adresse` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `t_client`
--

INSERT INTO `t_client` (`id_client`, `nom`, `prenom`, `email`, `telephone`, `adresse`) VALUES
(2, 'Dubois', 'Marie', 'marie.dubois@gmail.com', '0791111111', 'Rue de la Paix 12, Lausanne'),
(3, 'Blanc', 'Paul', 'paul.blanc@gmail.com', '0792222222', 'Avenue du Lac 5, Genève'),
(4, 'Noir', 'Claire', 'claire.noir@gmail.com', '0793333333', 'Rue du Moulin 3, Berne'),
(5, 'Roux', 'Nicolas', 'nicolas.roux@gmail.com', '0794444444', 'Chemin des Fleurs 8, Zurich'),
(6, 'Girard', 'Isabelle', 'isabelle.girard@gmail.com', '0795555555', 'Rue du Centre 12, Fribourg'),
(7, 'Bonnet', 'François', 'francois.bonnet@gmail.com', '0796666666', 'Avenue de la Gare 2, Neuchâtel'),
(8, 'Garnier', 'Sylvie', 'sylvie.garnier@gmail.com', '0797777777', 'Rue des Alpes 7, Sion'),
(9, 'Faure', 'Michel', 'michel.faure@gmail.com', '0798888888', 'Chemin du Parc 4, Lugano'),
(10, 'Rousseau', 'Nathalie', 'nathalie.rousseau@gmail.com', '0799999999', 'Rue de la Forêt 9, Lucerne'),
(11, 'Vincent', 'David', 'david.vincent@gmail.com', '0790000000', 'Avenue des Sports 6, Bâle');

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

--
-- Dumping data for table `t_client_chien`
--

INSERT INTO `t_client_chien` (`id_client_chien`, `FK_client`, `FK_chien`, `date_d'aquisition`) VALUES
(4, 2, 4, 1),
(5, 11, 5, 1),
(6, 3, 6, 1),
(7, 4, 7, 1),
(8, 5, 8, 1),
(9, 6, 9, 1),
(10, 7, 10, 1),
(11, 8, 11, 1),
(12, 9, 12, 1),
(13, 10, 13, 1);

-- --------------------------------------------------------

--
-- Table structure for table `t_promeneur`
--

CREATE TABLE `t_promeneur` (
  `id_promeneur` int NOT NULL,
  `nom` varchar(70) DEFAULT NULL,
  `prenom` varchar(70) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `t_promeneur`
--

INSERT INTO `t_promeneur` (`id_promeneur`, `nom`, `prenom`, `email`, `telephone`) VALUES
(4, 'Dupont', 'Jean', 'jean.dupont@gmail.com', '0791234567'),
(5, 'Martin', 'Sophie', 'sophie.martin@gmail.com', '0797654321'),
(6, 'Bernard', 'Jules', 'jules.bernard@gmail.com', '0781234567'),
(7, 'Petit', 'Emma', 'emma.petit@gmail.com', '0787654321'),
(8, 'Durand', 'Thomas', 'thomas.durand@gmail.com', '0761234567'),
(9, 'Leroy', 'Camille', 'camille.leroy@gmail.com', '0767654321'),
(10, 'Moreau', 'Antoine', 'antoine.moreau@gmail.com', '0771234567'),
(11, 'Simon', 'Julie', 'julie.simon@gmail.com', '0777654321'),
(12, 'Laurent', 'Pierre', 'pierre.laurent@gmail.com', '0751234567'),
(13, 'Michel', 'Laura', 'laura.michel@gmail.com', '0757654321');

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

--
-- Dumping data for table `t_promeneur_chien_service`
--

INSERT INTO `t_promeneur_chien_service` (`id_promeneur_chien_service`, `FK_promeneur`, `FK_chien`, `FK_service`, `date_promenade`) VALUES
(2, 4, 4, 24, 1),
(3, 4, 5, 25, 1),
(4, 5, 4, 25, 1),
(5, 5, 6, 26, 1),
(6, 6, 7, 24, 1),
(7, 6, 8, 28, 1),
(8, 7, 5, 26, 1),
(9, 8, 9, 29, 1),
(10, 9, 10, 25, 1),
(11, 10, 11, 31, 1);

-- --------------------------------------------------------

--
-- Table structure for table `t_reservation`
--

CREATE TABLE `t_reservation` (
  `id_reservation` int NOT NULL,
  `date` varchar(20) DEFAULT NULL,
  `heure_debut` varchar(10) DEFAULT NULL,
  `heure_fin` varchar(10) DEFAULT NULL,
  `statut` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `t_reservation`
--

INSERT INTO `t_reservation` (`id_reservation`, `date`, `heure_debut`, `heure_fin`, `statut`) VALUES
(2, '2026-06-01', '08h00', '09h00', 'Terminée'),
(3, '2026-06-02', '10h00', '11h30', 'Confirmée'),
(4, '2026-06-03', '14h00', '15h00', 'En attente'),
(5, '2026-06-04', '09h00', '10h00', 'Confirmée'),
(7, '2026-06-06', '15h00', '16h00', 'Confirmée'),
(8, '2026-06-07', '08h30', '09h30', 'En attente'),
(9, '2026-06-08', '13h00', '14h00', 'Annulée '),
(10, '2026-06-09', '16h00', '17h30', 'En attente'),
(11, '2026-06-10', '10h00', '11h00', 'Confirmée');

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
(24, 'Toilettage ', 60, 55),
(25, 'Promenade courte', 30, 20),
(26, 'Garde journée', 480, 80),
(27, 'Garde nuit', 720, 60),
(28, 'Bain', 45, 40),
(29, 'Coupe poils', 60, 45),
(30, 'Vaccination', 30, 70),
(31, 'Dressage', 60, 55),
(32, 'Consult. vétérinaire', 30, 90);

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
  MODIFY `id_chien` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `t_client`
--
ALTER TABLE `t_client`
  MODIFY `id_client` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `t_client_chien`
--
ALTER TABLE `t_client_chien`
  MODIFY `id_client_chien` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `t_promeneur`
--
ALTER TABLE `t_promeneur`
  MODIFY `id_promeneur` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `t_promeneur_chien_service`
--
ALTER TABLE `t_promeneur_chien_service`
  MODIFY `id_promeneur_chien_service` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `t_reservation`
--
ALTER TABLE `t_reservation`
  MODIFY `id_reservation` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `t_service`
--
ALTER TABLE `t_service`
  MODIFY `id_service` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

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
