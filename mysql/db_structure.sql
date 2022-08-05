CREATE DATABASE IF NOT EXISTS db_spacex;
USE db_spacex;

CREATE TABLE IF NOT EXISTS starlink_hst (
  id VARCHAR(25),
  latitude FLOAT,
  longitude FLOAT,
  creation_date TIMESTAMP
);

CREATE TABLE IF NOT EXISTS starklink_last_position (
  id VARCHAR(25) NOT NULL,
  latitude FLOAT,
  longitude FLOAT,
  creation_date TIMESTAMP,
  PRIMARY KEY (id)
);