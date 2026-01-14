CREATE TABLE
    film (
        id_film INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        titre_film VARCHAR(255) NOT NULL,
        genre VARCHAR(255),
        duree INT,
        realisateur VARCHAR(255),
        acteurs VARCHAR(255),
        description TEXT,
        poster VARCHAR(255),
        date_sortie DATE
    );

CREATE TABLE
    salle_cinema (
        id_salle INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nom_salle VARCHAR(50) NOT NULL,
        nombre_sieges INT
    );

CREATE TABLE
    seance (
        id_seance INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        id_film INT,
        id_salle INT,
        date_seance DATE,
        heure_seance VARCHAR(20),
        prix_billet DECIMAL(10, 2),
        FOREIGN KEY (id_film) REFERENCES film (id_film),
        FOREIGN KEY (id_salle) REFERENCES salle_cinema (id_salle)
    );

CREATE TABLE
    billet (
        id_billet INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        id_seance INT,
        numero_siege VARCHAR(10),
        prix_billet DECIMAL(10, 2),
        FOREIGN KEY (id_seance) REFERENCES seance (id_seance)
    );

CREATE TABLE
    client (
        id_client INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nom_client VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE,
        numero_telephone VARCHAR(20)
    );

CREATE TABLE
    recette_quotidienne (
        id INT PRIMARY KEY AUTO_INCREMENT,
        date_recette DATE NOT NULL,
        id_seance INT,
        recette_totale DECIMAL(12, 2),
        billets_vendus INT,
        FOREIGN KEY (id_seance) REFERENCES seance (id_seance)
    );

CREATE TABLE
    facture (
        id_facture INT PRIMARY KEY AUTO_INCREMENT,
        id_client INT,
        date_creation DATE,
        montant_total DECIMAL(12, 2),
        FOREIGN KEY (id_client) REFERENCES client (id_client)
    );

CREATE TABLE
    detail_facture (
        id_detail INT PRIMARY KEY AUTO_INCREMENT,
        id_facture INT,
        id_billet INT,
        FOREIGN KEY (id_facture) REFERENCES facture (id_facture),
        FOREIGN KEY (id_billet) REFERENCES billet (id_billet)
    );

INSERT INTO
    film (
        titre_film,
        genre,
        duree,
        realisateur,
        acteurs,
        description,
        poster,
        date_sortie
    )
VALUES
    (
        'Spider-Man: No Way Home',
        'Action, Aventure',
        148,
        'Jon Watts',
        'Tom Holland, Zendaya',
        'Peter Parker cherche de l\'aide auprès du Docteur Strange lorsque son identité est révélée.',
        'https://example.com/poster_spiderman.jpg',
        '2024-07-05'
    ),
    (
        'Dune',
        'Science-fiction',
        155,
        'Denis Villeneuve',
        'Timothée Chalamet, Rebecca Ferguson',
        'L\'histoire de Paul Atréides, destiné à gouverner la planète désertique d\'Arrakis.',
        'https://example.com/poster_dune.jpg',
        '2024-07-12'
    ),
    (
        'The Batman',
        'Action, Policier',
        176,
        'Matt Reeves',
        'Robert Pattinson, Zoë Kravitz',
        'Batman dans sa deuxième année de lutte contre le crime à Gotham City, face au Riddler.',
        'https://example.com/poster_batman.jpg',
        '2024-07-19'
    ),
    (
        'Everything Everywhere All at Once',
        'Action, Aventure, Comédie',
        139,
        'Daniel Kwan, Daniel Scheinert',
        'Michelle Yeoh, Stephanie Hsu',
        'Une Américaine d\'origine chinoise d\'âge moyen se retrouve dans une aventure folle.',
        'https://example.com/poster_eeaao.jpg',
        '2024-07-26'
    ),
    (
        'Top Gun: Maverick',
        'Action, Drame',
        130,
        'Joseph Kosinski',
        'Tom Cruise, Miles Teller',
        'Pete "Maverick" Mitchell entraîne un groupe de jeunes pilotes pour une mission spéciale.',
        'https://example.com/poster_topgun.jpg',
        '2024-08-02'
    ),
    (
        'The Northman',
        'Action, Aventure, Drame',
        136,
        'Robert Eggers',
        'Alexander Skarsgård, Nicole Kidman',
        'Un prince viking cherche à venger la mort de son père.',
        'https://example.com/poster_northman.jpg',
        '2024-08-09'
    ),
    (
        'Elvis',
        'Biographie, Musical',
        159,
        'Baz Luhrmann',
        'Austin Butler, Tom Hanks',
        'L\'histoire de la vie et de la carrière d\'Elvis Presley.',
        'https://example.com/poster_elvis.jpg',
        '2024-08-16'
    ),
    (
        'Thor: Love and Thunder',
        'Action, Aventure, Comédie',
        119,
        'Taika Waititi',
        'Chris Hemsworth, Natalie Portman',
        'Thor s\'associe avec Valkyrie, Korg et Jane Foster pour combattre Gorr le Boucher des Dieux.',
        'https://example.com/poster_thor.jpg',
        '2024-08-23'
    ),
    (
        'Doctor Strange in the Multiverse of Madness',
        'Action, Aventure, Fantastique',
        126,
        'Sam Raimi',
        'Benedict Cumberbatch, Elizabeth Olsen',
        'Doctor Strange voyage dans le multivers pour affronter une nouvelle menace.',
        'https://example.com/poster_drstrange.jpg',
        '2024-08-30'
    ),
    (
        'The Lost City',
        'Action, Aventure, Comédie',
        112,
        'Aaron Nee, Adam Nee',
        'Sandra Bullock, Channing Tatum',
        'Une romancière est kidnappée et forcée de participer à une aventure.',
        'https://example.com/poster_lostcity.jpg',
        '2024-09-06'
    );

INSERT INTO
    salle_cinema (nom_salle, nombre_sieges)
VALUES
    ('Salle 1', 100),
    ('Salle 2', 150),
    ('Salle 3', 80),
    ('Salle 4', 120),
    ('Salle 5', 90),
    ('Salle 6', 110),
    ('Salle 7', 70),
    ('Salle 8', 130),
    ('Salle 9', 140),
    ('Salle 10', 60);

INSERT INTO
    seance (id_film, id_salle, date_seance, heure_seance, prix_billet)
VALUES
    (1, 1, '2024-07-05', '10:30:00', 8.00),
    (1, 2, '2024-07-05', '13:00:00', 8.00),
    (2, 3, '2024-07-12', '15:45:00', 10.00),
    (3, 1, '2024-07-19', '18:15:00', 9.00),
    (4, 2, '2024-07-26', '20:30:00', 8.50),
    (5, 3, '2024-08-02', '10:00:00', 9.50),
    (6, 1, '2024-08-09', '12:15:00', 11.00),
    (7, 2, '2024-08-16', '14:30:00', 10.50),
    (8, 3, '2024-08-23', '17:00:00', 9.00),
    (9, 1, '2024-08-30', '19:30:00', 8.50);

INSERT INTO
    billet (id_seance, numero_siege, prix_billet)
VALUES
    (1, 'A1', 8.00),
    (1, 'A2', 8.00),
    (2, 'B5', 10.00),
    (3, 'C10', 9.00),
    (4, 'D8', 8.50),
    (5, 'E3', 9.50),
    (6, 'F12', 11.00),
    (7, 'G7', 10.50),
    (8, 'H4', 9.00),
    (9, 'I9', 8.50);

INSERT INTO
    client (nom_client, email, numero_telephone)
VALUES
    (
        'Pierre Dubois',
        'pierre.dubois@gmail.com',
        '0612345678'
    ),
    ('Marie Martin', 'marie.martin@gmail.com', '0687654321'),
    ('Jean Durand', 'jean.durand@yahoo.com', '0601234567'),
    ('Sophie Moreau', 'sophie.moreau@gmail.com', '0687654322'),
    ('Paul Laurent', 'paul.laurent@yahoo.com', '0612345679'),
    ('Claire Bernard', 'claire.bernard@gmail.com', '0687654323'),
    ('Michel Petit', 'michel.petit@yahoo.com', '0601234568'),
    (
        'Isabelle Thomas',
        'isabelle.thomas@gmail.com',
        '0687654324'
    ),
    ('François Robert', 'francois.robert@yahoo.com', '0612345680'),
    ('Sylvie Richard', 'sylvie.richard@gmail.com', '0687654325');

INSERT INTO
    recette_quotidienne (
        date_recette,
        id_seance,
        recette_totale,
        billets_vendus
    )
VALUES
    ('2024-07-05', 1, 16.00, 2),
    ('2024-07-05', 2, 16.00, 2),
    ('2024-07-12', 3, 10.00, 1),
    ('2024-07-19', 4, 9.00, 1),
    ('2024-07-26', 5, 8.50, 1),
    ('2024-08-02', 6, 9.50, 1),
    ('2024-08-09', 7, 11.00, 1),
    ('2024-08-16', 8, 10.50, 1),
    ('2024-08-23', 9, 9.00, 1),
    ('2024-08-30', 10, 8.50, 1);

INSERT INTO
    facture (id_client, date_creation, montant_total)
VALUES
    (1, '2024-07-05', 16.00), -- Client 1 achète des billets le 5/7/2024
    (2, '2024-07-05', 8.00), -- Client 2 achète un billet le 5/7/2024
    (3, '2024-07-12', 10.00), -- Client 3 achète un billet le 12/7/2024
    (4, '2024-07-19', 9.00), -- Client 4 achète un billet le 19/7/2024
    (5, '2024-07-26', 8.50), -- Client 5 achète un billet le 26/7/2024
    (6, '2024-08-02', 9.50), -- Client 6 achète un billet le 2/8/2024
    (7, '2024-08-09', 11.00), -- Client 7 achète un billet le 9/8/2024
    (8, '2024-08-16', 10.50), -- Client 8 achète un billet le 16/8/2024
    (9, '2024-08-23', 9.00), -- Client 9 achète un billet le 23/8/2024
    (10, '2024-08-30', 8.50);

INSERT INTO
    detail_facture (id_facture, id_billet)
VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 10);

