
-- Creating the Tables

DROP TABLE IF EXISTS `addresses`;
CREATE TABLE `addresses` (
  `address_id` int NOT NULL AUTO_INCREMENT,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `house_number` int,
  `zip_code` int(5),
  -- `client_id` int NOT NULL,
  PRIMARY KEY (`address_id`)
  -- FOREIGN KEY (`client_id`) REFERENCES `clients`(`client_id`)
);

DROP TABLE IF EXISTS `clients`;
CREATE TABLE `clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `ssn` int NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address_id` int NOT NULL,
  -- `client_account_id` int NOT NULL,
  -- `client_advisor_id` int NOT NULL,
  PRIMARY KEY (`client_id`),
  FOREIGN KEY (`address_id`) REFERENCES `addresses`(`address_id`)
  -- FOREIGN KEY (`client_account_id`) REFERENCES `clients_accounts`(`client_account_id`),
  -- FOREIGN KEY (`client_advisor_id`) REFERENCES `clients_advisors`(`client_advisor_id`)
);

DROP TABLE IF EXISTS `accounts`;
CREATE TABLE `accounts` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `balance` float,
  -- `client_id` int NOT NULL,
  PRIMARY KEY (`account_id`)
  -- FOREIGN KEY (`client_id`) REFERENCES `clients`(`client_id`)
);

DROP TABLE IF EXISTS `clients_accounts`;
CREATE TABLE `clients_accounts` (
  `client_account_id` int NOT NULL AUTO_INCREMENT,
  `client_id` int NOT NULL,
  `account_id` int NOT NULL,
  PRIMARY KEY (`client_account_id`),
  FOREIGN KEY (`client_id`) REFERENCES `clients`(`client_id`),
  FOREIGN KEY (`account_id`) REFERENCES `accounts`(`account_id`)
);

DROP TABLE IF EXISTS `financial_advisors`;
CREATE TABLE `financial_advisors` (
  `advisor_id` int NOT NULL AUTO_INCREMENT,
  `area_of_expertise` ENUM('Taxation', 'Estate Planning', 'Portfolio Management'),
  -- `client_advisor_id` int NOT NULL,
  `last_name` varchar(255),
  `first_name` varchar(255),
  PRIMARY KEY (`advisor_id`)
  -- FOREIGN KEY (`client_advisor_id`) REFERENCES `clients_advisors`(`client_advisor_id`)
);

DROP TABLE IF EXISTS `clients_advisors`;
CREATE TABLE `clients_advisors` (
  `client_advisor_id` int NOT NULL AUTO_INCREMENT,
  `client_id` int NOT NULL,
  `advisor_id` int NOT NULL,
  PRIMARY KEY (`client_advisor_id`),
  FOREIGN KEY (`client_id`) REFERENCES `clients`(`client_id`),
  FOREIGN KEY (`advisor_id`) REFERENCES `financial_advisors`(`advisor_id`)
);

-- Inserting Data

-- Default Client 1
INSERT INTO `addresses` (`city`, `state`, `house_number`, `zip_code`)
VALUES ('Reno', 'NV', '123', '00000');

INSERT INTO `clients`(`ssn`, `first_name`, `last_name`, `email`, `address_id`)
VALUES (1234, 'Thomas', 'Prange', 'tjprange@gmail.com', '1' );

-- NOTE: in the future, can populate address_id with a SQL Query (order by most recent?)

INSERT INTO `accounts` (`balance`)
VALUES (350);

INSERT INTO `clients_accounts` (`client_id`, `account_id`)
VALUES ('1', '1');

INSERT INTO `financial_advisors` (`area_of_expertise`, `last_name`, `first_name`)
VALUES ('Taxation', 'Wayne', 'Campbell');

INSERT INTO `clients_advisors` (`client_id`, `advisor_id`)
VALUES ('1', '1');

-- NOTE: in the future, can populate address_id with a SQL Query (order by most recent?)

-- Default Client 2
INSERT INTO `addresses` (`city`, `state`, `house_number`, `zip_code`)
VALUES ('Cleveland', 'OH', '456', '11111');

INSERT INTO `clients`(`ssn`, `first_name`, `last_name`, `email`, `address_id`)
VALUES (4567, 'Gavin', 'Slusher', 'gavins@gmail.com', '2' );

-- NOTE: in the future, can populate address_id with a SQL Query (order by most recent?)

INSERT INTO `accounts` (`balance`)
VALUES (350.00);

INSERT INTO `clients_accounts` (`client_id`, `account_id`)
VALUES ('2', '2');

INSERT INTO `financial_advisors` (`area_of_expertise`, `last_name`, `first_name`)
VALUES ('Portfolio Management', 'Peter', 'Lynch');

INSERT INTO `clients_advisors` (`client_id`, `advisor_id`)
VALUES ('2', '2');
