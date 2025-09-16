create database projeto3;
use projeto3;

create table locais(
idlocal int primary key auto_increment,
nome varchar(255) not null,
endereco varchar(255) not null,
tipo_acessibilidade varchar(255) not null
);