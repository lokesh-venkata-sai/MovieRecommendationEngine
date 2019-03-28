create database movieRecommendataion;

use movieRecommendataion;

create table users(
id int primary key auto_increment, 
username varchar(30) not null, 
email varchar(50) not null unique, 
password varchar(50) not null,
Action	int,Adventure int,	Animation int, Comedy int,Drama int,Fantasy int,
Horror int,Romance int,Sci_Fi	int,Thriller int)engine=InnoDB default charset=latin1 ;
alter table users auto_increment=10000;

drop table users;

select * from users;

select id,username,email from users where email='mamidil.sai@st.niituniversity.in';

insert into users  values(NULL,'exam','exam@gmail.com',aes_encrypt('exam','passkey'),0,0,1,0,0,0,1,0,0,0);
insert into users  values(NULL,'exam1','exam1@gmail.com',aes_encrypt('exam1','passkey'),0,1,1,0,0,1,0,0,0,0);
insert into users values(Null,'username','user@email.com',aes_encrypt('username','passkey'),0,0,0,0,0,0,0,0,0,0);

update users
set Action=1,Adventure=0,Animation=0,Comedy=1,Drama=0,Fantasy=0,Horror=0,Romance=1,Sci_Fi=0,Thriller=0
where username='exam';

SELECT username,id,email, cast(aes_decrypt(password,'passkey') as char(50)) as password FROM users;

create table movies(ID int primary key,	poster_url	varchar(200),Movie varchar(100),
unknown int,Action	int,Adventure int,	Animation int,
Children int, Comedy int,Crime int,Documentary int,Drama int,Fantasy int,
Film_Noir int,Horror int,Musical int,Mystery int,Romance int,Sci_Fi	int,Thriller int,War int,Western int);

drop table movies;
select * from movies;
describe movies;

WITH Ordered AS ( SELECT ROW_NUMBER() OVER (ORDER BY ID) AS RowNumber, poster_url,movie FROM movies)
SELECT * FROM Ordered
WHERE RowNumber >6 && RowNumber <15;
