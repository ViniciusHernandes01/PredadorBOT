# Usar uma imagem base do Python
FROM python:3.11

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o diretório de trabalho
COPY . .

# Instalar as dependências necessárias
RUN pip install -r requirements.txt

# Comando para rodar o bot
CMD ["python", "main.py"]  # Substitua "main.py" pelo nome do seu arquivo principal, se necessário
