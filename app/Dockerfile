FROM python:3.8-slim-buster
LABEL Mantainer: Leonardo Diniz <dinizleonardo5@icloud.com>

# Creating folders and copying needed files
RUN mkdir -p /app/source
RUN mkdir -p /app/scripts
COPY requirements.txt /app
COPY ./source /app/source
COPY ./scripts /app/scripts

# Install requirements if needed
RUN pip install -r /app/requirements.txt