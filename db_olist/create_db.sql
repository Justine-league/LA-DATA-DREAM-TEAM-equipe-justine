
-- Création des tables
--

CREATE TABLE IF NOT EXISTS product (  
  id INT PRIMARY KEY NOT NULL,
  name VARCHAR(50) NOT NULL,
  name_lenght INT(5) NOT NULL,
  description_lenght INT(5) NOT NULL,
  photos_qty INT(5) NOT NULL,
  weight_g INT(11) NOT NULL,
  lenght_cm INT(11) NOT NULL,
  height_cm INT(11) NOT NULL,
  wight_cm INT(11) NOT NULL
);

CREATE TABLE IF NOT EXISTS product_cat (  
  name VARCHAR(50) NOT NULL,
  english VARCHAR(50) NOT NULL,
  FOREIGN KEY (name) REFERENCES product(name)
) ;

CREATE TABLE IF NOT EXISTS geolocation (
    zip_code INT(5) PRIMARY KEY NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    city VARCHAR(50),
    state VARCHAR(50)
) ;

CREATE TABLE IF NOT EXISTS customer (
    id VARCHAR(50) PRIMARY KEY NOT NULL,
    unique_id VARCHAR(50),
    zip_code INT(5),
    FOREIGN KEY(zip_code) REFERENCES geolocation(zip_code)
) ;

CREATE TABLE IF NOT EXISTS seller (  
  id VARCHAR(50) NOT NULL PRIMARY KEY,
  zip_code INT(5) NOT NULL,
  FOREIGN KEY (zip_code) REFERENCES geolocation(zip_code) 
) ;

CREATE TABLE IF NOT EXISTS order_dataset (
    order_id varchar(50) PRIMARY KEY NOT NULL,
    customer_id varchar(50),
    status varchar(50),
    purchase_timestamp DATETIME,
    approuved DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_estimated_delivery_date DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
) ;

CREATE TABLE IF NOT EXISTS order_item (  
  order_id VARCHAR(50) NOT NULL,
  item_id INT(5) NOT NULL,
  product_id VARCHAR(50) NOT NULL,
  seller_id VARCHAR(50) NOT NULL,
  limit_date DATETIME NOT NULL,
  price FLOAT NOT NULL,
  freight_value FLOAT NOT NULL,
  FOREIGN KEY (order_id) REFERENCES order_dataset(order_id),
  FOREIGN KEY (product_id) REFERENCES product(id),
  FOREIGN KEY (seller_id) REFERENCES seller(id)
) ;

CREATE TABLE IF NOT EXISTS order_paiement(
    order_id varchar(50),
    sequential INT,
    type varchar(50),
    installments INT,
    value FLOAT,
    FOREIGN KEY (order_id) REFERENCES order_dataset(order_id)
) ;

CREATE TABLE IF NOT EXISTS order_review(
    id varchar(50) PRIMARY KEY NOT NULL,
    order_id VARCHAR(50),
    score INT,
    comment_title VARCHAR(250),
    comment_msg TEXT,
    creation_date DATETIME,
    answer_timestamp DATETIME,
    FOREIGN KEY (order_id) REFERENCES order_dataset(order_id)
) ;



