CREATE DATABASE IF NOT EXISTS db_spacex;
USE db_spacex;

CREATE TABLE IF NOT EXISTS starlink_hst (
  id VARCHAR(25),
  latitude FLOAT,
  longitude FLOAT,
  creation_date TIMESTAMP,
  INDEX(id)
);

--CREATE TABLE IF NOT EXISTS starlink_last_position (
-- id VARCHAR(25),
--  latitude FLOAT,
--  longitude FLOAT,
--  creation_date TIMESTAMP,
--  INDEX(id)
--);