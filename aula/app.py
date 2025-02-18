# Importando o Flask 
from flask import Flask, render_template

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Criando a primeira rota do site

@app.route('/')
# Criando função no pyton
def home():

    return render_template('index.html')

@app.route('/games')

def games():
    titulo = 'CS-GO'
    ano = 2012
    categoria = 'FPS Online'
    jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'quemario', 'Trop', 'Aspax', 'maxxdiego']
    jogos = ['Valorant', 'League Of Legends', 'Minecraft', 'GTA V', 'Free Fire', 'EA FC 25']
    return render_template('games.html',
                           titulo = titulo,
                           ano = ano,
                           categoria = categoria,
                           jogadores=jogadores,
                           jogos = jogos)

# Iniciando servidor no Localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)