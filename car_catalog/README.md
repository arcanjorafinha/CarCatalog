# Catálogo Automobilístico

Este é um simples projeto de catálogo automobilístico usando FastAPI, Jinja2 e Uvicorn. O projeto permite criar, ler, atualizar e deletar informações sobre carros (nome, potência e preço).

## Estrutura do Projeto

car_catalog/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── create.html
│ │ ├── update.html
│ ├── static/
│ ├── styles.css
│
├── requirements.txt
├── README.md

## Configuração

Instale as dependências:


"""
 pip install -r requirements.txt
"""


Execute a aplicação:

"""
uvicorn app.main:app --reload
"""

Se pedir, instale tb: 

"""
pip install python-multipart
"""

A aplicação estará disponível em http://127.0.0.1:8000.