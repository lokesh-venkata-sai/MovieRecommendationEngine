create database movieRecommendataion;

use movieRecommendataion;

create table users(
id int primary key auto_increment, 
username varchar(30) not null, 
email varchar(50) not null unique, 
password varchar(50) not null
)engine=InnoDB default charset=latin1 ;
alter table users auto_increment=10000;

drop table users;

select * from users;

insert into users  values(NULL,'exam','exam@gmail.com',aes_encrypt('exam','passkey'));
insert into users  values(NULL,'exam1','exam1@gmail.com',aes_encrypt('exam1','passkey'));

SELECT username,id,email, cast(aes_decrypt(password,'passkey') as char(50)) as password FROM users;


