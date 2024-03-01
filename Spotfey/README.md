# Spotfey

Spotfey é um clone básico do Spotify, desenvolvido com Flask e JavaScript. Ele permite visualizar músicas em destaque, álbuns e reproduzir músicas.

## Requisitos

- Python 3.x
- Flask
- MySQL
- Navegador da web compatível com HTML5

## Instalação

1. Clone o repositório para o seu ambiente local:

```bash
git clone linkdogit.com
```

2. Navegue até o diretório do projeto:

```bash
cd spotifeio
```

3. Instale as dependências do Python:

```bash
pip install flask mysql-connector-python
```

4. Importe o banco de dados MySQL. Você pode encontrar o script SQL no diretório `database`.

5. Inicie o servidor Flask:

```bash
python server.py
```

6. Abra o arquivo index.html para visualizar o Spotifeio

## Uso

O Spotifeio oferece uma interface simples com as seguintes seções:

- **Início:** Visualize músicas em destaque.
- **Explorar:** Explore todos os álbuns disponíveis.
- **Biblioteca:** Visualize sua biblioteca de músicas.
- **Buscar:** Pesquise por músicas ou álbuns específicos.

Clique nas músicas para reproduzi-las no player de áudio na parte inferior da tela.