CREATE TABLE
    Category (
        category_id int NOT NULL AUTO_INCREMENT,
        category_name varchar(50) NOT NULL,
        PRIMARY KEY (category_id)
    );

INSERT INTO
    Category
VALUES
    (1, 'Musique Live'),
    (2, 'Théâtre - Cinéma'),
    (3, 'Séminaires - Communauté'),
    (4, 'Sciences - Conférences'),
    (5, 'Fitness - Sports');

CREATE TABLE
    User (
        user_id int NOT NULL AUTO_INCREMENT,
        fullname varchar(255) NOT NULL,
        phone char(10) NOT NULL,
        email varchar(30) NOT NULL,
        address varchar(100) NOT NULL,
        level int DEFAULT 1,
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        last_login datetime DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id),
        KEY email_idx (email)
    );

INSERT INTO
    User
VALUES
    (
        1,
        'Pierre Dubois',
        '0767916592',
        'nkeyskuo124@gmail.com',
        '94 Avenue de la République, 75012 Paris',
        0,
        DEFAULT,
        DEFAULT
    ),
    (
        2,
        'Léa Garnier',
        '0903740813',
        'sheldon1247@gmail.com',
        '429 Rue Nationale, 69003 Lyon',
        0,
        DEFAULT,
        DEFAULT
    );

CREATE TABLE
    Event (
        event_id int NOT NULL AUTO_INCREMENT,
        event_name varchar(100) NOT NULL,
        occur_date date NOT NULL,
        occur_time varchar(50) NOT NULL,
        location varchar(50) NOT NULL,
        address varchar(255) NOT NULL,
        introduce text,
        banner varchar(255) NOT NULL,
        status varchar(10) NOT NULL CHECK (status IN ('pending', 'published', 'ended')),
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime DEFAULT CURRENT_TIMESTAMP,
        author_id int NOT NULL,
        category_id int NOT NULL,
        PRIMARY KEY (event_id),
        CONSTRAINT fk_event_author FOREIGN KEY (author_id) REFERENCES User (user_id),
        CONSTRAINT fk_event_category FOREIGN KEY (category_id) REFERENCES Category (category_id)
    );

INSERT INTO
    Event
VALUES
    (
        1,
        'CÉRÉMONIE DE REMISE DE PRIX ONDE VERTE 2023',
        '2024-01-24',
        '07:30 PM - 11:30 PM',
        'Théâtre de la Paix',
        '240 Boulevard du 3 Février, 12e Arrondissement, 10e District, Paris',
        '<p>Làn Sóng Xanh là giải thưởng âm nhạc thường niên, lâu đời nhất và là bảng đo nhiệt độ các ca khúc, các ca sĩ được yêu thích tại Việt Nam.&nbsp;</p><p>Tiếp nối sự thành công của các năm trước, chương trình hứa hẹn mang tới những màu sắc âm nhạc riêng biệt của thế hệ nghệ sĩ mới. Những màn trình diễn sáng tạo độc đáo, chỉ có duy nhất tại Lễ trao giải Làn Sóng Xanh 2023.</p><p>Bước sang năm thứ 26, VietNam Event Group (VEG) vinh dự được trở thành đơn vị phối hợp tổ chức cùng với Đài tiếng nói nhân dân TP.HCM, để có thể cùng nhau phát triển chương trình Làn Sóng Xanh trong tương lai.</p><p>------------------------------------------------------------</p><p><strong>TICKET PRICE:&nbsp;</strong></p><p><strong>27.12.2023</strong>: ZONE 1: 1.200.000 VND/ ZONE 4: 700.000 VND</p><p><strong>05.01.2024: </strong>ZONE 2: 1.000.000 VND/ ZONE 5: 500.000 VND</p><p><strong>07.01.2024: </strong>ZONE 3: 800.000 VND/ ZONE 6: 300.000 VND</p><p>&nbsp;</p><figure class="image"><img style="aspect-ratio:1600/1066;" src="http://res.cloudinary.com/dx9ybqdfi/image/upload/v1708194559/rqmxrjky659trnabokzo.jpg" width="1600" height="1066"></figure><p>&nbsp;</p><figure class="image"><img style="aspect-ratio:1600/1066;" src="http://res.cloudinary.com/dx9ybqdfi/image/upload/v1708194563/qc3paqrbzw0rijy6uk3k.jpg" width="1600" height="1066"></figure>',
        'http://res.cloudinary.com/dx9ybqdfi/image/upload/v1706546920/fb6p6vsqqxw8o7h5nuoi.jpg',
        'published',
        DEFAULT,
        DEFAULT,
        1,
        1
    ),
    (
        2,
        'SUPER JUNIOR-L.S.S. THE SHOW : Th3ee Guys à PARIS',
        '2024-03-23',
        '18:00 - 20:00',
        'Complexe Sportif Couvert Zone 7',
        '202 Rue Hoang Van Thu, 9e Arrondissement, District Phu Nhuan, Paris',
        '<figure class="image"><img style="aspect-ratio:1200/1200;" src="http://res.cloudinary.com/dx9ybqdfi/image/upload/v1706452747/jgh2bspvqb8qjqqdz6zj.jpg" width="1200" height="1200"></figure>',
        'http://res.cloudinary.com/dx9ybqdfi/image/upload/v1706452754/jdkuhri4muznzoynhowu.jpg',
        'published',
        DEFAULT,
        DEFAULT,
        2,
        1
    ),
    (
        3,
        'VIETNAM COCKTAIL FESTIVAL 2024',
        '2024-03-28',
        '15:00 - 22:00',
        'Sheraton Saigon Hotel & Towers',
        'Sheraton Saigon Hotel & Towers  88 Đ. Đồng Khởi, Bến Nghé, Quận 1, Thành Phố Hồ Chí Minh',
        '<p><strong>Lễ hội Cocktail lớn nhất Việt Nam đã trở lại&nbsp;vào mùa hè năm&nbsp;nay.</strong></p><p>&nbsp;</p><p>Lễ hội Gin Festival&nbsp;lớn nhất Sài Gòn lần thứ 6 sẽ trở lại vào tháng 6 này với tên gọi mới là VIETNAM COCKTAIL FESTIVAL, nhằm giới thiệu đa dạng các loại rượu mạnh bao gồm Whisky, Gin, Tequila, Vodka,...</p><p>&nbsp;</p><p>Lễ hội hứa hẹn một cuối tuần thú vị đầy ắp những hoạt động như thưởng thức các loại rượu mạnh và cocktail không giới hạn, tham gia các lớp Master Class để trau dồi thêm thông tin bổ ích, nhạc sống, cửa hàng bán lẻ, trải nghiệm phòng VIP Tasting -&nbsp;nơi trưng bày đa dạng các thương hiệu danh giá.&nbsp;</p><p>&nbsp;</p><p>Hãy tham gia cùng chúng tôi tại Sheraton Saigon Hotel &amp; Towers, một địa điểm sang trọng bật nhất để bắt đầu hành trình khám phá, học hỏi và tận hưởng các loại rượu mạnh hảo hạng đang có mặt tại Việt Nam.&nbsp;</p><p>&nbsp;</p><p><strong>Vé bao gồm:&nbsp;</strong></p><ul><li>Thỏa sức thưởng thức các loại rượu mạnh và cocktail không giới hạn từ 3PM đến 10PM.</li><li>Cơ hội tham dự 06 lớp Master Class trên 1 ngày.&nbsp;</li><li>Hòa mình vào không gian triển lãm với sự góp mặt hơn 50 thương hiệu.&nbsp;</li><li>Các hoạt động giải trí: Show ảo thuật, DJ &amp; Vũ điệu&nbsp;Carnival sôi động</li><li>Có cơ hội&nbsp;khám phá Phòng Thử Rượu Thượng Hạng&nbsp;chỉ với 1.000.000 VNĐ mỗi lần vào để nếm thử 4 shot rượu đặc biệt&nbsp;trong sự kiện.</li></ul><p>&nbsp;</p><p><strong>*Quà tặng đi kèm:</strong>&nbsp;</p><ul><li>01 Bình đựng rượu inox&nbsp;khắc logo&nbsp;sự kiện (trị giá 200.000 VNĐ)</li><li>01 món ăn nhẹ đẳng cấp 5 sao từ Sheraton Saigon Hotel &amp; Towers&nbsp;</li></ul><p>&nbsp;</p><p><strong>Mua vé trước để </strong><i><strong>tiết kiệm lên đến 15%</strong>. Xem chi tiết vé để biết thêm thông tin.</i></p><p>&nbsp;</p><p><strong>Thông tin sự kiện:</strong>&nbsp;</p><ul><li>Ngày diễn ra sự kiện: Thứ Sáu&nbsp;&amp; Thứ Bảy, ngày 14&nbsp;&amp; 15&nbsp;Tháng 6 năm 2024</li><li>Địa điểm: Sheraton Saigon Hotel &amp; Towers</li><li>Thời gian: Từ 3 giờ chiều đến 10 giờ tối</li></ul><p>&nbsp;</p><p><i>*Người tham gia phải đủ 18 tuổi trở lên, không phù hợp cho phụ nữ đang mang thai và cho con bú.</i></p><p><i>*Giá vé đã bao gồm VAT, vui lòng yêu cầu xuất hóa đơn VAT ngay sau khi mua vé.</i></p><p><i>*Không hoàn trả vé.</i></p><p><i>*Việc mua vé thể hiện rằng người mua đã đồng ý với tất cả điều kiện và quy định của Ban tổ chức.</i></p><p><i>*Giữ kỹ QR Code trên vé điện tử của bạn. Không chia sẻ mã này với bất kỳ ai hoặc trên mạng xã hội. Mã này chứa thông tin cá nhân và chi tiết về vé sự kiện của bạn.</i></p><p>&nbsp;</p><p><i><strong>THƯỞNG THỨC CÓ TRÁCH NHIỆM</strong></i></p><p>&nbsp;</p><p>----//</p><p>&nbsp;</p><p><strong>THE VIETNAM COCKTAIL FESTIVAL RETURNS THIS SUMMER WITH A VIBRANT CARNIVAL THEME.</strong></p><p>&nbsp;</p><p>The 6th Biggest Gin Festival&nbsp;will be back in Saigon this June with a new name, VIETNAM COCKTAIL FESTIVAL, showcasing a diverse selection of Spirits including Whisky, Gin, Tequila, Vodka,...</p><p>&nbsp;</p><p>The festival promises a delightful weekend filled with tastings of both free-flowing spirits and cocktails, along with informative masterclasses, live music, retail boutique, VIP tasting room, and immersive experiences with esteemed brands.</p><p>&nbsp;</p><p>Join us at the Sheraton Saigon Hotel &amp; Towers, a captivating venue, to embark on a journey of exploration, learning, and indulgence as you savor the finest spirits Vietnam has to offer.</p><p>&nbsp;</p><p><strong>Ticket Includes:</strong></p><ul><li>Free-Flowing Fine Spirits and Cocktails from 3PM – 10PM</li><li>06 Master Classes per Day</li><li>Exhibition more than 50 Spirits Brands</li><li>Entertainments- Magic Show, DJ &amp; Carnival Dancing</li><li>Get a chance to explore the Exclusive room with only 1,000,000 VND per entrance to taste 4 shots of Exclusive Spirits in event.</li></ul><p>&nbsp;</p><p><strong>*Special Door Gift:</strong>&nbsp;</p><ul><li>01 Stainless Steel Hip Flask (Value of 200.000 VND)</li><li>01&nbsp;5-star food item&nbsp;from Sheraton&nbsp;Saigon Hotel &amp; Towers</li></ul><p>&nbsp;</p><p><strong>Save up to 15% by purchasing tickets in advance</strong><i><strong>.</strong> See ticket details for more information.</i></p><p>&nbsp;</p><p><strong>Event Information:</strong></p><ul><li>Dates: Friday&nbsp;14th &amp; Saturday 15th June 2024</li><li>Location: Sheraton Saigon Hotel &amp; Towers</li><li>Times: 3PM – 10PM</li></ul><p>&nbsp;</p><p><i>*Participants must be at least 18 years old to enter the event, unsuitable for breast feeding and pregnant women.</i></p><p><i>*Ticket price included VAT, please request to issue VAT invoice right after buying ticket.</i></p><p><i>*Not refund.</i></p><p><i>*By purchasing a ticket, the buyer agrees to all the terms and conditions set by the organizer</i>.</p><p><i>*Avoid sharing it with anyone or on social media. This code holds your personal information and unique ticket details.</i></p><p>&nbsp;</p><p><i><strong>ENJOY RESPONSIBLY</strong></i></p>',
        'http://res.cloudinary.com/dx9ybqdfi/image/upload/v1710598050/tki8bmnynkykfrxf8o7z.jpg',
        'pending',
        DEFAULT,
        DEFAULT,
        1,
        2
    );

CREATE TABLE
    Ticket_Type (
        ticket_type_id int NOT NULL AUTO_INCREMENT,
        ticket_type_name varchar(100) NOT NULL,
        event_id int NOT NULL,
        price int NOT NULL DEFAULT 0,
        n_sold int NOT NULL DEFAULT 0,
        n_stock int NOT NULL DEFAULT 0,
        is_selling boolean NOT NULL DEFAULT false,
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (ticket_type_id),
        CONSTRAINT fk_tickettype_event FOREIGN KEY (event_id) REFERENCES Event (event_id)
    );

INSERT INTO
    Ticket_Type
VALUES
    (
        1,
        'Billet Standard',
        1,
        300000,
        0,
        20,
        true,
        DEFAULT,
        DEFAULT
    ),
    (
        2,
        'Vé nâng cao',
        1,
        500000,
        0,
        10,
        true,
        DEFAULT,
        DEFAULT
    ),
    (
        3,
        'Vé VIP',
        1,
        1000000,
        0,
        5,
        true,
        DEFAULT,
        DEFAULT
    ),
    (
        4,
        'Vé khu A',
        3,
        500000,
        0,
        100,
        false,
        DEFAULT,
        DEFAULT
    ),
    (
        5,
        'Vé khu B',
        3,
        700000,
        0,
        60,
        true,
        DEFAULT,
        DEFAULT
    ),
    (
        6,
        'Vé khu C',
        3,
        900000,
        0,
        20,
        true,
        DEFAULT,
        DEFAULT
    );

CREATE TABLE
    Booking (
        booking_id varchar(20) NOT NULL,
        customer_id int NOT NULL,
        payment_method varchar(10) CHECK (payment_method IN ('stripe', 'paypal', 'amazon')),
        temp_cost int NOT NULL,
        status varchar(20) CHECK (status IN ('pending', 'completed', 'canceled')) DEFAULT 'pending',
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (booking_id),
        CONSTRAINT fk_booking_user FOREIGN KEY (customer_id) REFERENCES User (user_id)
    );

INSERT INTO
    Booking
VALUES
    (
        'EZ39375738',
        2,
        'stripe',
        1300000,
        DEFAULT,
        DEFAULT,
        DEFAULT
    ),
    (
        'EZ69530648',
        1,
        'paypal',
        700000,
        DEFAULT,
        DEFAULT,
        DEFAULT
    ),
    (
        'EZ83495254',
        2,
        'stripe',
        1800000,
        DEFAULT,
        DEFAULT,
        DEFAULT
    );

CREATE TABLE
    Booking_Detail (
        booking_id varchar(20) NOT NULL,
        ticket_type_id int NOT NULL,
        quantity int NOT NULL,
        PRIMARY KEY (booking_id, ticket_type_id),
        CONSTRAINT fk_bookingdetail_booking FOREIGN KEY (booking_id) REFERENCES Booking (booking_id),
        CONSTRAINT fk_bookingdetail_tickettype FOREIGN KEY (ticket_type_id) REFERENCES Ticket_Type (ticket_type_id)
    );

INSERT INTO
    Booking_Detail
VALUES
    ('EZ39375738', 2, 2),
    ('EZ39375738', 1, 1),
    ('EZ69530648', 5, 1),
    ('EZ83495254', 1, 1),
    ('EZ83495254', 2, 1),
    ('EZ83495254', 3, 1);

CREATE TABLE
    Checkout (
        checkout_id int NOT NULL AUTO_INCREMENT,
        booking_id varchar(20) NOT NULL,
        tax float NOT NULL,
        total int NOT NULL,
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (checkout_id),
        CONSTRAINT fk_checkout_booking FOREIGN KEY (booking_id) REFERENCES Booking (booking_id)
    );

CREATE TABLE
    Ticket (
        ticket_id int NOT NULL AUTO_INCREMENT,
        ticket_type_id int NOT NULL,
        ticket_code varchar(20) NOT NULL,
        expiry date NOT NULL,
        status varchar(20) CHECK (status IN ('available', 'sold')),
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (ticket_id),
        CONSTRAINT fk_ticket_tickettype FOREIGN KEY (ticket_type_id) REFERENCES Ticket_Type (ticket_type_id)
    );

CREATE TABLE
    Transaction_Detail (
        checkout_id int NOT NULL,
        ticket_id int NOT NULL,
        PRIMARY KEY (checkout_id, ticket_id),
        CONSTRAINT fk_transactiondetail_checkout FOREIGN KEY (checkout_id) REFERENCES Checkout (checkout_id),
        CONSTRAINT fk_transactiondetail_ticket FOREIGN KEY (ticket_id) REFERENCES Ticket (ticket_id)
    );

INSERT INTO
    Checkout
VALUES
    (1, 'EZ69530648', 0.08, 1404000, DEFAULT, DEFAULT),
    (2, 'EZ39375738', 0.08, 756000, DEFAULT, DEFAULT);

INSERT INTO
    Ticket
Values
    (
        1,
        1,
        'FJSF-85FS-AAM3-6ZUT',
        '2024-05-24',
        'sold',
        DEFAULT
    ),
    (
        2,
        2,
        'PFA9-HG22-MMS8-13FC',
        '2024-05-24',
        'sold',
        DEFAULT
    ),
    (
        3,
        2,
        '28SC-TIFJ-AA10-73SM',
        '2024-05-24',
        'sold',
        DEFAULT
    ),
    (
        4,
        5,
        'UFJM-528F-FA2B-31HJ',
        '2024-05-24',
        'sold',
        DEFAULT
    ),
    (
        5,
        1,
        'XJFD-31KG-48K3-22V1',
        '2024-05-24',
        'available',
        DEFAULT
    ),
    (
        6,
        2,
        'MKF2-FF22-78DV-FAFJ',
        '2024-05-24',
        'available',
        DEFAULT
    ),
    (
        7,
        3,
        '84JF-3FBG-14FV-BFJ2',
        '2024-05-24',
        'available',
        DEFAULT
    ),
    (
        8,
        4,
        '4TJS-2F2M-51FV-143D',
        '2024-05-24',
        'available',
        DEFAULT
    ),
    (
        9,
        6,
        '524F-0F2E-134C-GGRD',
        '2024-05-24',
        'available',
        DEFAULT
    );

INSERT INTO
    Transaction_Detail
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4);