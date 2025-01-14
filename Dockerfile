# Imagem base oficial do Python
FROM python:3.13.1-slim

# Definindo o diretório de trabalho no contêiner
WORKDIR /app

# Copiando o conteúdo do diretório local para o diretório de trabalho no contêiner
COPY . .

# Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o pipeline ao iniciar o contêiner
CMD ["python", "pipeline.py"]
