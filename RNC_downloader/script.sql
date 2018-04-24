create database rnc_db;

create user rnc_viewer identified by 'Password22';
grant all on rnc_db.* to rnc_viewer;


use rnc_db;

create table rnc_info(
id int not null unsigned,
owner_name varchar(100) not null,
business_name varchar(100) not null,
descripton varchar(200) not null default 'NO DESCRIPCION',
management varchar(100) not null,
location varchar(200) not null,
employees_amount int not null,
district varchar(100)not null,
phone_number varchar(30) not null,
registration_date timestamp not null,
status varchar(100) not null,
payment_method varchar(100) not null,
constraint pkid primary key(id));

