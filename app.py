import os
from flask import Flask

app = Flask(__name__)
nome = os.getenv("NAME", "João ninguem")

@app.route('/')
def index():
  return f"<H1>testando minha imagem docker - {nome}!!!!</H1>"