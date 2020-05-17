SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `clients`;
CREATE TABLE `clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `ssn` int NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address_id` int NOT NULL,
  `client_account_id` int NOT NULL,
  `client_advisor_id` int NOT NULL,
  PRIMARY KEY (`client_id`),
  FOREIGN KEY (`address_id`) REFERENCES `addresses`(`address_id`),
  FOREIGN KEY (`client_account_id`) REFERENCES `clients_accounts`(`client_account_id`),
  FOREIGN KEY (`client_advisor_id`) REFERENCES `clients_advisors`(`client_advisor_id`)
); 

DROP TABLE IF EXISTS `accounts`;
CREATE TABLE `accounts` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `balance` float,
  `client_id` int NOT NULL,
  PRIMARY KEY (`account_id`),
  FOREIGN KEY (`client_id`) REFERENCES `clients`(`client_id`)
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

DROP TABLE IF EXISTS `clients_advisors`;
CREATE TABLE `clients_advisors` (
  `client_advisor_id` int NOT NULL AUTO_INCREMENT,
  `client_id` int NOT NULL,
  `advisor_id` int NOT NULL,
  PRIMARY KEY (`client_advisor_id`),
  FOREIGN KEY (`client_id`) REFERENCES `clients`(`client_id`),
  FOREIGN KEY (`advisor_id`) REFERENCES `financial_advisors`(`advisor_id`)  
); 

DROP TABLE IF EXISTS `addresses`;
CREATE TABLE `addresses` (
  `address_id` int NOT NULL AUTO_INCREMENT,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `house_number` int,
  `zip_code` int(5),
  `client_id` int NOT NULL,
  PRIMARY KEY (`address_id`),
  FOREIGN KEY (`client_id`) REFERENCES `clients`(`client_id`)
); 

DROP TABLE IF EXISTS `financial_advisors`;
CREATE TABLE `financial_advisors` (
  `advisor_id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `area_of_expertise` ENUM('Taxation', 'Estate Planning', 'Portfolio Management'),
  `client_advisor_id` int NOT NULL,
  `last_name` varchar(255),
  `first_name` varchar(255),
  PRIMARY KEY (`advisor_id`),
  FOREIGN KEY (`client_advisor_id`) REFERENCES `clients_advisors`(`client_advisor_id`)
);

SET FOREIGN_KEY_CHECKS=0;