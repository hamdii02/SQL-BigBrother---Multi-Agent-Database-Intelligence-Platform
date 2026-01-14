CREATE TABLE
    Categories (
        CategoryID INT PRIMARY KEY AUTO_INCREMENT,
        CategoryName VARCHAR(100) NOT NULL,
        Description TEXT
    );
    
CREATE TABLE
    Products (
        ProductID INT PRIMARY KEY AUTO_INCREMENT,
        ProductName VARCHAR(100) NOT NULL,
        CategoryID INT,
        Price DECIMAL(10, 2) NOT NULL,
        Stock INT NOT NULL,
        Description TEXT,
        FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
    );

CREATE TABLE
    Customers (
        CustomerID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(100) NOT NULL,
        LastName VARCHAR(100) NOT NULL,
        Email VARCHAR(100) UNIQUE NOT NULL,
        Password VARCHAR(100) NOT NULL,
        Address TEXT,
        Phone VARCHAR(15)
    );

CREATE TABLE
    Orders (
        OrderID INT PRIMARY KEY AUTO_INCREMENT,
        CustomerID INT,
        OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        Total DECIMAL(10, 2),
        Status VARCHAR(50),
        FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
    );

CREATE TABLE
    OrderDetails (
        OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
        OrderID INT,
        ProductID INT,
        Quantity INT NOT NULL,
        Price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
    );

INSERT INTO
    Categories (CategoryName, Description)
VALUES
    (
        'Électronique',
        'Appareils et gadgets incluant téléphones, ordinateurs portables, et plus'
    ),
    (
        'Livres',
        'Large gamme de livres de divers genres et auteurs'
    ),
    (
        'Vêtements',
        'Vêtements pour hommes, femmes et enfants'
    ),
    (
        'Maison & Cuisine',
        'Produits pour l’amélioration de la maison et l’utilisation en cuisine'
    ),
    (
        'Sports & Plein Air',
        'Équipements et matériel pour activités de plein air et sports'
    );

INSERT INTO
    Products (
        ProductName,
        CategoryID,
        Price,
        Stock,
        Description
    )
VALUES
    (
        'Smartphone',
        1,
        699.99,
        50,
        'Smartphone dernier modèle avec fonctionnalités avancées'
    ),
    (
        'Ordinateur Portable',
        1,
        1199.99,
        30,
        'Ordinateur portable haute performance pour jeux et travail'
    ),
    (
        'Roman',
        2,
        19.99,
        100,
        'Roman best-seller d’un auteur populaire'
    ),
    (
        'T-shirt',
        3,
        15.99,
        200,
        'T-shirt en coton confortable en diverses tailles'
    ),
    (
        'Mixeur',
        4,
        49.99,
        60,
        'Mixeur haute vitesse parfait pour faire des smoothies'
    ),
    (
        'Tente',
        5,
        89.99,
        40,
        'Tente 4 personnes idéale pour le camping'
    ),
    (
        'Tablette',
        1,
        499.99,
        75,
        'Tablette portable avec écran haute résolution'
    ),
    (
        'Livre de Cuisine',
        2,
        24.99,
        120,
        'Livre de recettes avec des plats délicieux et faciles à faire'
    ),
    (
        'Jean',
        3,
        39.99,
        150,
        'Jean en denim avec coupe élégante'
    ),
    (
        'Ballon de Football',
        5,
        25.99,
        80,
        'Ballon de football durable pour entraînements et matchs'
    );

INSERT INTO
    Customers (
        FirstName,
        LastName,
        Email,
        Password,
        Address,
        Phone
    )
VALUES
    (
        'Jean',
        'Dupont',
        'jean.dupont@example.com',
        'password123',
        '123 Rue Principale, Marseille, France',
        '04-91-12-34'
    ),
    (
        'Marie',
        'Martin',
        'marie.martin@example.com',
        'password456',
        '456 Rue du Chêne, Lyon, France',
        '04-78-56-78'
    ),
    (
        'Alice',
        'Bernard',
        'alice.bernard@example.com',
        'password789',
        '789 Rue des Pins, Toulouse, France',
        '05-61-87-65'
    ),
    (
        'Robert',
        'Petit',
        'robert.petit@example.com',
        'password101',
        '101 Rue de l’Érable, Nice, France',
        '04-93-43-21'
    ),
    (
        'Charlie',
        'Davis',
        'charlie.davis@example.com',
        'password102',
        '102 Elm St, Anytown, USA',
        '555-8764'
    );

INSERT INTO
    Orders (CustomerID, OrderDate, Total, Status)
VALUES
    (1, '2023-06-15 14:30:00', 749.98, 'Shipped'),
    (2, '2023-06-16 09:45:00', 19.99, 'Processing'),
    (3, '2023-06-17 12:00:00', 65.98, 'Delivered'),
    (4, '2023-06-18 16:20:00', 119.98, 'Cancelled'),
    (5, '2023-06-19 11:30:00', 89.99, 'Shipped');

INSERT INTO
    OrderDetails (OrderID, ProductID, Quantity, Price)
VALUES
    (1, 1, 1, 699.99),
    (1, 3, 1, 19.99),
    (2, 3, 1, 19.99),
    (3, 5, 1, 49.99),
    (3, 9, 1, 15.99),
    (4, 10, 2, 25.99),
    (5, 6, 1, 89.99),
    (5, 2, 1, 1199.99),
    (5, 4, 1, 24.99),
    (5, 7, 1, 499.99);