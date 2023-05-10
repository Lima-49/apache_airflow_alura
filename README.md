# Extração dos dados climáticos da API Visual Crossing 
Nesse repositório foi desenvolvido um projeto em Python, responsável por automatizar a extração dos dados tem tempo da api VISUAL CROSSING 

## Instalação do Airflow via Docker 
O Apache Airflow é uma ferramenta open source orquestradora de fluxos, de fácil acesso para sistemas operacionais Linux e MAC, mas para windows é necessário algumas gambiarras kkkk, nesse caso, foi utilizado um docker para rodar a ferramenta

1. Instalar o [Docker Descktop](https://www.docker.com)
2. Acessar o site do [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) e procurar o arquivo docker-compose.yaml
![imagem_2023-05-10_164230007](https://github.com/Lima-49/apache_airflow_alura/assets/56659896/ae2c07f6-5b8d-48d1-b11f-bfc3d49b8f5d)
3. Copiar o arquivo docker-compose.yaml para um diretorio local
4. Criar um ambiente virtual para encpasular as bibliotecas dessa aplicação
````cmd
# Instala a biblioteca venv do Python
pip install venv 

# Cria um ambiente virtual
python -m venv ./venv

# Ativa o ambiente virtual
venv/Scripts/activate
````
5. Dentro do diretório que o arquivo docker-compose.yaml está, ativar o docker seguindo os comandos 
````cmd
# Inicializa o docker
docker-compose up airflow-init

# Roda o docker-compose
docker-compose up
````
6. Acessar o Localhost para visualizar a Interface do Apache Airflow
5. No repositório do arquivo docker-compose.yaml, criar tres novas pastas:
- dags: pasta que terá os arquivos .py que serão executados 
- logs: relatório das execução das dags
- plugins: contem os plugins utilizados na execução da dag
