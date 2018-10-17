CREATE TABLE users (
user_id uuid not null,
password text not null,
access_key text not null,
phone_number int not null,
preferences jsonb);

CREATE TABLE flex_info (
user_id uuid not null,
meal_plan text,
current_flex real
);

CREATE TABLE product_info (
product_id uuid not null,
barcode int,
name text,
price real,
location jsonb
);
