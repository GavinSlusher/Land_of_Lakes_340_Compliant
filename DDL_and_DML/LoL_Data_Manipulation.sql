-- This file will represent the queries needed for each page on the frontend of
-- our website. Any variable that we expect the backend code to pass to these 
-- queries will be denoted by surrounding brackets: {} 


-- Add Client Page
-- This Form will add a Client and their Address to the database. A client must 
-- have an address, and so the form is consolodated here.

INSERT INTO `addresses` (`city`, `state`, `house_number`, `zip_code`)
VALUES ('{city}', '{state}', '{house_number}', '{zip_code}');

INSERT INTO `clients`(`ssn`, `first_name`, `last_name`, `email`, `address_id`)
VALUES ({ssn}, '{first_name}', '{last_name}', '{email}', '{address_id}');



-- Add Financial Advisor Page
-- This form will an advisor to the database. By default, advisors do not have 
-- a book of clients

INSERT INTO `financial_advisors` (`area_of_expertise`, `first_name`, `last_name`)
VALUES ('{area_of_expertise}', '{first_name}', '{last_name}');


-- Add an Account Page
-- This form will add an account for the requested client(s).

-- First we create the account

INSERT INTO `accounts` (`balance`)
VALUES ({balance});

-- Second, we link the account with the client(s) that the user asked to make an
-- account for (accounts MUST have users. Only joint accounts allowed for multi-
-- users)

INSERT INTO `clients_accounts` (`client_id`, `account_id`)
VALUES ('{client_id}', '{account_id}');
-- (Do again for joint accounts)


-- Update Client Page
-- This form will update all fields for the client passed in with their ID
-- It will also update their address, if wanted.

UPDATE `clients`
SET
        `ssn` = {ssn},
        `first_name` = {first_name},
        `last_name` = {last_name},
        `email` = {email}
WHERE
        `client_id` = {client_id};

UPDATE `addresses`
SET
        `city` = {city},
        `state` = {state},
        `house_number` = {house_number},
        `zip_code` = {zip_code}
WHERE
        `address_id` = {address_id};


-- Delete Client Page
-- This form will delete the client connected to the passed ID.
-- NOTE: TO DO
-- If the client has a Financial Advisor, the relationship will be de-linked.
-- If the client is the sole account owner of an account,
-- the account will be deleted. And if the client is a joint owner of an account,
-- the account will remain.

DELETE FROM `clients` WHERE `client_id` = {client_id};

-- Connect Advisor Page
-- This form will connect an advisor with a client using their respective IDs

INSERT INTO `clients_advisors` (`client_id`, `advisor_id`)
VALUES ('{client_id}', '{advisor_id}');


-- Search The Database
-- TO DO: We will search a client by id and populate requested data

-- View Tables
-- TO DO: Join Tables/Queries for more useful tables


SELECT * FROM `clients` WHERE last_name LIKE '{search_term}%'

-- Clients

SELECT
        `client_id` as 'Client ID',
        `ssn` as 'Social Security Number',
        CONCAT(`first_name`, ' ', `last_name`) as 'Client Name',
        `email` as 'Email'
FROM
        `clients`;

-- Accounts

SELECT
        `account_id` as 'Account Number',
        `balance` as 'Account Balance'
FROM
        `accounts`;

-- Clients Accounts

SELECT
        `client_account_id` as 'Client Account ID',
        `client_id` as 'Client ID',
        `account_id` as 'Account ID'
FROM
        `clients_accounts`;

-- Addresses

SELECT
        `address_id` as 'Address ID',
        `city` as 'City',
        `state` as 'State',
        `house_number` as 'House Number',
        `zip_code` as 'Zip Code'
FROM
        `addresses`;

-- Financial Advisors

SELECT
        `advisor_id` as 'Advisor ID',
        CONCAT(`first_name`, ' ', `last_name`) as 'Advisor Name',
        `area_of_expertise` as 'Area of Expertise'
FROM
        `financial_advisors`;

-- Clients Advisors

SELECT
        `client_advisor_id` as 'Client Advisor ID',
        `client_id` as 'Client ID',
        `advisor_id` as 'Advisor ID'
FROM
        `clients_advisors`;
