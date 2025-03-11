from flask import render_template, request

jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'quemario', 'Trop', 'Aspax', 'maxxdiego']    

# Dicionario em Pyhton (objeto)
# Array de objetos ; lista de games
gamelist = [{
            'Titulo' : 'CS-GO',
            'Ano' : 2012,
            'Categoria' : 'FPS Online'
        }]

def init_app(app):
    # Criando a primeira rota do site

    @app.route('/')
    # Criando função no pyton
    def home():

        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])

    def games():
        game = gamelist[0]
 
     
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            #Verificar se o campo jogador existe
            if request.form.get('jogador'):
                # O append add o item a lista
                jogadores.append(request.form.get('jogador'))
        
            

        
        jogos = ['Valorant', 'League Of Legends', 'Minecraft', 'GTA V', 'Free Fire', 'EA FC 25']
        return render_template('games.html',
                            game = game,
                            jogadores=jogadores,
                            jogos = jogos)
    
    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames' , methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Titulo: ' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')}
                                )
        return render_template('cadgames.html', gamelist=gamelist)