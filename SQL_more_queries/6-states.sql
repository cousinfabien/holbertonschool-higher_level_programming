-- Creates the database hbtn_0d_usa and the table states with id INT primary key auto-increment and name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);