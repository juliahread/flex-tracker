CREATE TABLE users (
user_id uuid DEFAULT uuid_generate_v4 (),
password text not null,
access_key text not null,
email text not null,
phone_number int not null,
full_name int not null,
preferences jsonb
);

CREATE TABLE flex_info (
user_id uuid not null,
meal_plan text,
current_flex real
);

CREATE TABLE product_info (
product_id uuid DEFAULT uuid_generate_v4 (),
barcode int,
name text,
price real,
location jsonb
);

CREATE TABLE users_test (
user_id uuid DEFAULT uuid_generate_v4 (),
password text not null,
access_key text not null,
email text not null,
phone_number int not null,
full_name int not null,
preferences jsonb
);

CREATE TABLE flex_info_test (
user_id uuid not null,
meal_plan text,
current_flex real
);

CREATE TABLE product_info_test (
product_id uuid DEFAULT uuid_generate_v4 (),
barcode int,
name text,
price real,
location jsonb
);
