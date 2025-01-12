# Pokémon Data Analysis

## Descrição
Este projeto realiza a extração, transformação e análise de dados de Pokémon utilizando a PokeAPI. Ele é estruturado como um pipeline, com etapas para extrair dados, transformá-los e gerar relatórios e gráficos. Além disso, o projeto está configurado para ser executado tanto localmente quanto em um contêiner Docker.

## Estrutura do Projeto
```bash
poke-data-analysis/
├── reports/              # Relatórios e gráficos gerados
├── src/                  # Código-fonte do projeto
│   ├── extraction.py     # Extração de dados da PokeAPI
│   ├── transformation.py # Transformação e análise de dados
│   ├── report.py         # Geração de relatórios e gráficos
│   ├── pipeline.py       # Execução do pipeline completo
│   └── utils.py          # Funções auxiliares, como mapeamento de cores dos tipos de Pokémon
├── Dockerfile            # Arquivo Dockerfile para contêiner Docker
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo

```

## Instrução de instalação
### 1. Instalando dependências no ambiente local
Certifique-se de ter o Python 3.13 ou superior instalado. Você pode verificar sua versão do Python com o comando:
```bash
python --version
```
Para instalar as dependências localmente, siga os seguintes passos:
  1. Clone o repositório para sua máquina local:
     ```bash
     git clone https://github.com/seu-usuario/poke-data-analysis.git
     cd poke-data-analysis
     ```
  2. Crie e ative um ambiente virtual  
     **- Linux/MacOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
     **- Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
  3. instale as dependências com o pip:
     ```bash
     pip install -r requirements.txt
     ```

### 2. Executando o pipeline localmente
Após a instalação das dependências, você pode executar o pipeline localmente. O comando a seguir irá executar o script `pipeline.py`, que realiza a extração dos dados, transformação e geração do relatório:
```bash
python src/pipeline.py
```
Este comando irá:
1. Extrair os dados de Pokémons da PokeAPI
2. Transformar os dados, gerando análises e categorização.
3. Gerar gráficos e relatórios em formato CSV e PNG.

### 3. Executando o pipeline com Docker
Se preferir rodar o projeto dentro de um contêiner Docker, siga as instruções abaixo.  
#### 3.1. Construindo a imagem Docker  
Com o Docker instalado, você pode construir a imagem Docker do projeto com o seguinte comando (certifique-se de estar na raiz do projeto, onde o `Dockerfile` está localizado):
```bash
docker build -t pokemon-pipeline .
```
#### 3.2. Executando o contêiner Docker
```bash
docker run pokemon-pipeline
```
Os resultados serão salvos na pasta `/app/reports` no contêiner. Certifique-se de montar volumes, se quiser acessar os relatórios no host.

## Gerenciamento de Logs
### 1. Localmente
Os logs da execução do pipeline são gravados no arquivo `pipeline.log` na raiz do projeto.
### 2. Docker
Para acessar os logs do pipeline rodando no Docker, use o comando:
```bash
docker logs -f <container_id>
```

## Relatórios e Gráficos
Após a execução do pipeline, os seguintes arquivos são gerados na pasta `reports`/:
* `top_5_experience.csv`: Tabela com os 5 Pokémon com maior experiência base.
* `stats_by_type.csv`: Tabela com a média de ataque, defesa e HP por tipo.
* `types_distribution.png`: Gráfico de distribuição de Pokémon por tipo.
