CREATE DATABASE foodcompositiondb
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    
CREATE TABLE food_brand
(
	id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
	brand VARCHAR(200) NOT NULL,
	inactive BOOLEAN NOT NULL
);

ALTER TABLE food_brand
ADD CONSTRAINT pk_food_brand_id_01
PRIMARY KEY(id);

ALTER TABLE food_brand
ADD CONSTRAINT uq_food_brand_brand_01
UNIQUE(brand);

CREATE TABLE food_category
(
	id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(100) NOT NULL
);

ALTER TABLE food_category
ADD CONSTRAINT pk_food_category_id_01
PRIMARY KEY(id);

ALTER TABLE food_category
ADD CONSTRAINT uq_food_category_name_01
UNIQUE(name);

CREATE TABLE food
(
	id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(200) NOT NULL,
	food_category BIGINT NOT NULL,
	food_brand BIGINT NOT NULL
);

ALTER TABLE food
ADD CONSTRAINT pf_food_id_01
PRIMARY KEY(ID);

ALTER TABLE food
ADD CONSTRAINT fk_food_food_category_01
FOREIGN KEY (food_category) REFERENCES food_category(id);

ALTER TABLE food
ADD CONSTRAINT fk_food_food_brand_01
FOREIGN KEY (food_brand) REFERENCES food_brand(id);


CREATE TABLE food_composition
(
	id BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY,
	food_id BIGINT NOT NULL,
	calories DECIMAL NOT NULL,
	protein DECIMAL NOT NULL,
	carbohydrate DECIMAL NOT NULL,
	totalfat DECIMAL NOT NULL,
	saturated_fat DECIMAL NOT NULL,
	trans_fat DECIMAL NOT NULL,
	monounsaturated_fat DECIMAL NOT NULL,
	polyunsaturated_fat DECIMAL NOT NULL,
	fiber DECIMAL NOT NULL,
	sodium DECIMAL NOT NULL,
	iron DECIMAL NOT NULL,
	calcium DECIMAL NOT NULL,
	sugar DECIMAL NOT NULL,
	cholesterol DECIMAL NOT NULL,
	beta_glucan DECIMAL NOT NULL,
	omega3 DECIMAL NOT NULL,
	portion_size INT NOT NULL
);

ALTER TABLE food_composition
ADD CONSTRAINT pk_food_composition_id_01
PRIMARY KEY(id);

ALTER TABLE food_composition
ADD CONSTRAINT fk_food_food_composition_id_01
FOREIGN KEY(food_id) REFERENCES food(id);

ALTER TABLE food_composition
ADD CONSTRAINT uq_food_composition_food_portion_01
UNIQUE(food_id, portion_size)