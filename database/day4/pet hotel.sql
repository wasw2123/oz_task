-- CREATE DB
CREATE DATABASE pet_hotel;
USE pet_hotel;

-- create table
CREATE TABLE customers(
	customerID INT PRIMARY KEY AUTO_INCREMENT,
    c_name VARCHAR(255),
    c_phone INT
);

CREATE TABLE pets(
	petID INT PRIMARY KEY AUTO_INCREMENT,
    customerID INT,
    FOREIGN KEY (customerID) REFERENCES customers(customerID),
    p_name VARCHAR(255),
    p_species VARCHAR(255),
    p_breed VARCHAR(255)
);

CREATE TABLE rooms(
	roomID INT PRIMARY KEY AUTO_INCREMENT,
    r_number INT,
    r_type VARCHAR(255),
    r_price INT
);

CREATE TABLE books(
	bookID INT PRIMARY KEY AUTO_INCREMENT,
    roomID INT,
    FOREIGN KEY (roomID) REFERENCES rooms(roomID),
    indate DATE,
    outdate DATE,
    petID INT,
    FOREIGN KEY (petID) REFERENCES pets(petID)
);

CREATE TABLE service(
	serviceID INT PRIMARY KEY AUTO_INCREMENT,
    bookID INT,
    FOREIGN KEY (bookID) REFERENCES books(bookID),
    s_name VARCHAR(255),
    s_price INT
);