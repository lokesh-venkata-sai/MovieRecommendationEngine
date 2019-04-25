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

create table movies(ID int primary key,	poster_url	varchar(200),Movie varchar(100),
unknown int,Action	int,Adventure int,	Animation int,
Children int, Comedy int,Crime int,Documentary int,Drama int,Fantasy int,
Film_Noir int,Horror int,Musical int,Mystery int,Romance int,Sci_Fi	int,Thriller int,War int,Western int);

create table ratings(userID int ,movieId int,rating int,
primary key(userID,movieId)
)engine=InnoDB default charset=latin1;

create table recommend(user_id int,movie_id int,
primary key(user_id,movie_id)
);

