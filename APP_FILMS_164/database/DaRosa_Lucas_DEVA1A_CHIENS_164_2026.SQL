-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: MACCAUD_OLIVIER_INFO1X_FILMS_164_2023

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS DaRosa_Lucas_DEVA1A_CHIENS_164_2026;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS DaRosa_Lucas_DEVA1A_CHIENS_164_2026;

-- Utilisation de cette base de donnée

USE DaRosa_Lucas_DEVA1A_CHIENS_164_2026;
-- --------------------------------------------------------

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
  `type_service` int DEFAULT NULL,
  `duree` int DEFAULT NULL,
  `prix` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  MODIFY `id_service` int NOT NULL AUTO_INCREMENT;

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
