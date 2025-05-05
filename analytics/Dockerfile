FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala diretamente no sistema (sem virtualenv)
RUN pip install --no-cache-dir -r requirements.txt

# Define o PYTHONPATH para dentro do projeto
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Comando padrão (sobrescrito pelo docker-compose)
CMD ["python", "main.py"]