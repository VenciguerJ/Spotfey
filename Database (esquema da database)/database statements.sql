	use spotfei;

create table users(
	id int not null auto_increment,
    username varchar(20) not null,
    senha varchar(20) not null,
    foto_perfil varchar(100), 
    email varchar(90) not null,
    primary key (id)
);

CREATE TABLE musicas (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_criador INT NOT NULL,
    foto_musica VARCHAR(100),
    data_criacao DATETIME NOT NULL,
    caminho_arquivo VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (id_criador) REFERENCES users(id)
);


select * from users where username = 'teste2';
truncate table users;

select id, username, senha, foto_perfil, email from users where id = 1;

select * from users;

select username from users where username = 'jean';
insert into users (username, senha,foto_perfil, email) values ('teste2', 'testesenha', 'kajsdh', 'email@email.com')