CREATE TABLE
    Customer (
        customer_id int NOT NULL AUTO_INCREMENT,
        customer_name VARCHAR(50) NOT NULL,
        customer_email VARCHAR(50) NOT NULL,
        customer_phone VARCHAR(10) NOT NULL,
        PRIMARY KEY (customer_id)
    );

CREATE TABLE
    Product (
        product_id int NOT NULL AUTO_INCREMENT,
        product_name varchar(255) NOT NULL,
        description text,
        price float NOT NULL,
        category varchar(50),
        PRIMARY KEY (product_id)
    );

CREATE TABLE
    Orders (
        order_id int NOT NULL AUTO_INCREMENT,
        customer_id int NOT NULL,
        order_date datetime DEFAULT CURRENT_TIMESTAMP,
        total_amount int NOT NULL,
        status varchar(10) NOT NULL CHECK (status IN ('pending', 'complete', 'cancelled')),
        PRIMARY KEY (order_id),
        CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES Customer (customer_id)
    );

CREATE TABLE
    Order_Items (
        order_item_id int NOT NULL AUTO_INCREMENT,
        order_id int NOT NULL,
        product_id int NOT NULL,
        quantity int NOT NULL,
        total_price float NOT NULL,
        PRIMARY KEY (order_item_id),
        CONSTRAINT fk_order_id FOREIGN KEY (order_id) REFERENCES Orders (order_id),
        CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES Product (product_id)
    );

CREATE TABLE
    Receipt (
        receipt_id int NOT NULL AUTO_INCREMENT,
        order_id int NOT NULL,
        issue_date datetime DEFAULT CURRENT_TIMESTAMP,
        payment_method varchar(10) NOT NULL CHECK (payment_method IN ('stripe', 'paypal', 'amazon')),
        payment_amount float NOT NULL,
        payment_status varchar(10) NOT NULL CHECK (payment_status IN ('paid', 'unpaid')),
        PRIMARY KEY (receipt_id),
        CONSTRAINT fk_order_id2 FOREIGN KEY (order_id) REFERENCES Orders (order_id)
    );

CREATE TABLE
    Payment (
        payment_id int NOT NULL AUTO_INCREMENT,
        receipt_id int NOT NULL,
        payment_date datetime DEFAULT CURRENT_TIMESTAMP,
        amount_paid float NOT NULL,
        payment_method varchar(10) NOT NULL CHECK (payment_method IN ('stripe', 'paypal', 'amazon')),
        PRIMARY KEY (payment_id),
        CONSTRAINT pk_receipt_id2 FOREIGN KEY (receipt_id) REFERENCES Receipt (receipt_id)
    );

INSERT INTO
    Customer
VALUES
    (
        1,
        'Émilie Dubois',
        'leonarderika@example.com',
        '3972515948'
    ),
    (
        2,
        'Michel Garnier',
        'huntjames@example.com',
        '7244101727'
    ),
    (
        3,
        'Sophie Hernández',
        'chadevans@example.org',
        '9858458046'
    ),
    (
        4,
        'David Ramírez',
        'kevinpatel@example.net',
        '6045244937'
    ),
    (
        5,
        'Jessica Moreau',
        'scottmullins@example.org',
        '3865942427'
    ),
    (
        6,
        'Christophe Rey',
        'prush@example.net',
        '5802277723'
    ),
    (
        7,
        'Olivia Díaz',
        'jimenezsheryl@example.org',
        '5159187370'
    ),
    (
        8,
        'Daniel Castillo',
        'kmiller@example.org',
        '3664067330'
    );

INSERT INTO
    Product
VALUES
    (
        1,
        'Hamburgers de Bœuf Gourmet',
        'Galettes de bœuf 100% artisanales',
        9.99,
        'Viande & Volaille'
    ),
    (
        2,
        'Salade d’Épinards Bio',
        'Épinards biologiques frais avec garnitures',
        7.99,
        'Produits Frais'
    ),
    (
        3,
        'Pain de Seigle Artisanal',
        'Pain de seigle croûtillant fraîchement cuit',
        5.49,
        'Boulangerie'
    ),
    (
        4,
        'Filets de Saumon Sauvage',
        'Portions de saumon de source durable',
        14.99,
        'Fruits de Mer'
    ),
    (
        5,
        'Mélange de Légumes Bio',
        'Légumes biologiques de saison assortis',
        6.99,
        'Produce'
    ),
    (
        6,
        'Gourmet Mac and Cheese',
        'Creamy homemade macaroni and cheese',
        8.99,
        'Prepared Foods'
    ),
    (
        7,
        'Free-Range Chicken Breasts',
        'Hormone-free and antibiotic-free chicken',
        7.99,
        'Meat & Poultry'
    ),
    (
        8,
        'Artisanal Cheese Platter',
        'Selection of premium artisanal cheeses',
        19.99,
        'Dairy'
    );

INSERT INTO
    Orders
VALUES
    (1, 2, '2016-01-19T05:26:25+00:00', 2, 'complete'),
    (2, 5, '2008-12-03T11:38:27+00:00', 1, 'complete'),
    (3, 7, '2014-02-24T16:01:32+00:00', 3, 'pending'),
    (4, 6, '2004-11-23T00:37:05+00:00', 2, 'pending'),
    (5, 8, '2018-08-09T09:18:33+00:00', 3, 'cancelled'),
    (6, 4, '2006-03-28T22:13:27+00:00', 1, 'complete'),
    (7, 3, '2008-11-10T18:48:01+00:00', 1, 'pending'),
    (8, 1, '2007-08-10T21:55:37+00:00', 2, 'cancelled');

INSERT INTO
    Order_Items
VALUES
    (1, 1, 1, 1, 9.99),
    (2, 1, 8, 1, 19.99),
    (3, 2, 4, 1, 14.99),
    (4, 3, 3, 3, 16.47),
    (5, 4, 2, 2, 15.98),
    (6, 5, 6, 3, 26.97),
    (7, 6, 5, 1, 6.99),
    (8, 7, 1, 1, 9.99),
    (9, 8, 4, 1, 14.99),
    (10, 8, 5, 1, 6.99);

INSERT INTO
    Receipt
VALUES
    (
        1,
        1,
        '2011-08-29T20:33:57+00:00',
        'stripe',
        29.98,
        'paid'
    ),
    (
        2,
        2,
        '2020-02-23T07:23:24+00:00',
        'stripe',
        14.99,
        'paid'
    ),
    (
        3,
        3,
        '2015-02-04T11:47:15+00:00',
        'amazon',
        16.47,
        'paid'
    ),
    (
        4,
        4,
        '2014-12-13T21:32:25+00:00',
        'stripe',
        15.98,
        'paid'
    ),
    (
        5,
        5,
        '2009-05-16T22:47:22+00:00',
        'amazon',
        26.97,
        'unpaid'
    ),
    (
        6,
        6,
        '2008-10-12T20:11:37+00:00',
        'amazon',
        6.99,
        'paid'
    ),
    (
        7,
        7,
        '2018-10-23T00:56:36+00:00',
        'paypal',
        9.99,
        'paid'
    ),
    (
        8,
        8,
        '2020-08-20T20:15:38+00:00',
        'paypal',
        21.98,
        'unpaid'
    );

INSERT INTO
    Payment
VALUES
    (
        1,
        1,
        '2011-08-29T20:33:57+00:00',
        29.98,
        'stripe'
    ),
    (
        2,
        2,
        '2020-02-23T07:23:24+00:00',
        14.99,
        'stripe'
    ),
    (
        3,
        3,
        '2015-02-04T11:47:15+00:00',
        16.47,
        'amazon'
    ),
    (
        4,
        4,
        '2014-12-13T21:32:25+00:00',
        15.98,
        'stripe'
    ),
    (5, 6, '2008-10-12T20:11:37+00:00', 6.99, 'amazon'),
    (6, 7, '2018-10-23T00:56:36+00:00', 9.99, 'paypal');