-- =============================================
-- Fichier : DaRosa_Lucas_DEVA1A.sql
-- Auteur : DaRosa Lucas
-- Classe : DEVA1A
-- Description : Requêtes CRUD du projet
-- =============================================


-- ===========================
-- TABLE : t_service
-- ===========================

-- READ (afficher tous)
SELECT * FROM t_service ORDER BY id_service ASC;

-- READ (afficher un seul)
SELECT * FROM t_service WHERE id_service = 1;

-- CREATE (ajouter)
INSERT INTO t_service (id_service, type_service, duree, prix)
VALUES (NULL, 'Toilettage', '60', '50');

-- UPDATE (modifier)
UPDATE t_service SET type_service = 'Toilettage', duree = '60', prix = '50'
WHERE id_service = 1;

-- DELETE
DELETE FROM t_promeneur_chien_service WHERE FK_service = 1;
DELETE FROM t_service WHERE id_service = 1;


-- ===========================
-- TABLE : t_chien
-- ===========================

-- READ (afficher tous)
SELECT * FROM t_chien ORDER BY id_chien ASC;

-- READ (afficher un seul)
SELECT * FROM t_chien WHERE id_chien = 1;

-- READ (promeneurs liés)
SELECT t_promeneur.nom, t_promeneur.prenom
FROM t_promeneur_chien_service
INNER JOIN t_promeneur ON t_promeneur_chien_service.FK_promeneur = t_promeneur.id_promeneur
WHERE FK_chien = 1;

-- READ (clients liés)
SELECT t_client.nom, t_client.prenom
FROM t_client_chien
INNER JOIN t_client ON t_client_chien.FK_client = t_client.id_client
WHERE t_client_chien.FK_chien = 1;

-- CREATE
INSERT INTO t_chien (id_chien, nom, race, age, taille, notes)
VALUES (NULL, 'Rex', 'Labrador', '3', '60', 'Gentil');

-- UPDATE
UPDATE t_chien SET nom = 'Rex', race = 'Labrador', age = '3', taille = '60', notes = 'Gentil'
WHERE id_chien = 1;

-- DELETE
DELETE FROM t_promeneur_chien_service WHERE FK_chien = 1;
DELETE FROM t_client_chien WHERE FK_chien = 1;
DELETE FROM t_chien WHERE id_chien = 1;


-- ===========================
-- TABLE : t_promeneur
-- ===========================

-- READ (afficher tous)
SELECT * FROM t_promeneur ORDER BY id_promeneur ASC;

-- READ (afficher un seul)
SELECT * FROM t_promeneur WHERE id_promeneur = 1;

-- READ (chiens liés)
SELECT t_chien.nom
FROM t_promeneur_chien_service
INNER JOIN t_chien ON t_promeneur_chien_service.FK_chien = t_chien.id_chien
WHERE FK_promeneur = 1;

-- CREATE
INSERT INTO t_promeneur (id_promeneur, nom, prenom, email, telephone)
VALUES (NULL, 'Dupont', 'Jean', 'jean.dupont@gmail.com', '0791234567');

-- UPDATE
UPDATE t_promeneur SET nom = 'Dupont', prenom = 'Jean', email = 'jean.dupont@gmail.com', telephone = '0791234567'
WHERE id_promeneur = 1;

-- DELETE
DELETE FROM t_promeneur_chien_service WHERE FK_promeneur = 1;
DELETE FROM t_promeneur WHERE id_promeneur = 1;


-- ===========================
-- TABLE : t_client
-- ===========================

-- READ (afficher tous)
SELECT * FROM t_client ORDER BY id_client ASC;

-- READ (afficher un seul)
SELECT * FROM t_client WHERE id_client = 1;

-- READ (chiens liés)
SELECT t_chien.nom
FROM t_client_chien
INNER JOIN t_chien ON t_client_chien.FK_chien = t_chien.id_chien
WHERE t_client_chien.FK_client = 1;

-- CREATE
INSERT INTO t_client (id_client, nom, prenom, email, telephone, adresse)
VALUES (NULL, 'Dubois', 'Marie', 'marie.dubois@gmail.com', '0791111111', 'Rue de la Paix 1, Lausanne');

-- UPDATE
UPDATE t_client SET nom = 'Dubois', prenom = 'Marie', email = 'marie.dubois@gmail.com',
telephone = '0791111111', adresse = 'Rue de la Paix 1, Lausanne'
WHERE id_client = 1;

-- DELETE
DELETE FROM t_client_chien WHERE FK_client = 1;
DELETE FROM t_client WHERE id_client = 1;


-- ===========================
-- TABLE : t_reservation
-- ===========================

-- READ (afficher tous)
SELECT * FROM t_reservation ORDER BY id_reservation ASC;

-- READ (afficher un seul)
SELECT * FROM t_reservation WHERE id_reservation = 1;

-- CREATE
INSERT INTO t_reservation (id_reservation, date, heure_debut, heure_fin, statut)
VALUES (NULL, '2026-06-01', '08h00', '09h00', 'Confirmée');

-- UPDATE
UPDATE t_reservation SET date = '2026-06-01', heure_debut = '08h00',
heure_fin = '09h00', statut = 'Confirmée'
WHERE id_reservation = 1;

-- DELETE
DELETE FROM t_reservation WHERE id_reservation = 1;


-- ===========================
-- TABLE DE LIAISON : t_promeneur_chien_service
-- ===========================

-- READ
SELECT * FROM t_promeneur_chien_service;

-- CREATE
INSERT INTO t_promeneur_chien_service (FK_promeneur, FK_chien, FK_service, date_promenade)
VALUES (1, 1, 1, 1);

-- DELETE
DELETE FROM t_promeneur_chien_service WHERE id_promeneur_chien_service = 1;


-- ===========================
-- TABLE DE LIAISON : t_client_chien
-- ===========================

-- READ
SELECT * FROM t_client_chien;

-- CREATE
INSERT INTO t_client_chien (FK_client, FK_chien, `date_d'aquisition`)
VALUES (1, 1, 1);

-- DELETE
DELETE FROM t_client_chien WHERE id_client_chien = 1;