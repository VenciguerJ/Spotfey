-- users

use spotfei;

create table users(
	id int not null auto_increment,
    username varchar(20) not null,
    senha varchar(20) not null,
    foto_perfil varchar(100), 
    email varchar(90) not null,
    primary key (id)
);

select * from users where username = 'teste2';
truncate table users;

select id, username, senha, foto_perfil, email from users where id = 1;

select * from users;

select username from users where username = 'jean';
insert into users (username, senha,foto_perfil, email) values ('teste2', 'testesenha', 'kajsdh', 'email@email.com')

-- musicas

use spotfei;
create table musics(
id int not null auto_increment,
nome varchar(100) not null,
id_criador int not null,
foto_musica varchar(100),
data_criacao datetime not null,
caminho_arquivo varchar(100),

primary key (id),
foreign key(id_criador) references users(id)
)

select * from musics