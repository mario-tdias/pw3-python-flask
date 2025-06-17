from flask import render_template, request, redirect, url_for
from models.database import Game, Console, db
# Lista de jogadores
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Array de objetos - Lista de games
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    # Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4', 'Jogo 5', 'Jogo 6']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
    
    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)

    #Rota de Estoque (CRUD)
    @app.route('/estoqueGames', methods=['GET', 'POST'])
    @app.route('/estoqueGames/<int:id>')
    def estoqueGames(id=None):
        if id:
            # buscando o jogo pela id
            jogo = Game.query.get(id)
            if jogo:
                # deletando o jogo
                db.session.delete(jogo)
                db.session.commit()
            return redirect(url_for('estoqueGames'))

        # Verificando se a requisição é POST:
        if request.method == 'POST' and request.form.get("CadastrarJogo") == "true":
           # Cadastra um novo jogo
            newgame = Game(request.form['titulo'], request.form['ano'],
            request.form['categoria'], request.form['plataforma'], request.form['preco'],
            request.form['quantidade'])
            db.session.add(newgame)
            db.session.commit()
            return redirect(url_for('estoqueGames'))
        else:
 # Captura o valor de 'page' que foi passado pelo método GET
 # Define como padrão o valor 1 e o tipo inteiro
            page = request.args.get('page', 1, type=int)
 # Valor padrão de registros por página (definimos 3)
        per_page = 3
 # Faz um SELECT no banco a partir da pagina informada (page)
 # Filtrando os registro de 3 em 3 (per_page)
        games_page = Game.query.paginate(page=page,per_page=per_page)
        return render_template('estoqueGames.html', gamesestoque=games_page)
        
        
        # fazendo um SELECT no banco (pegando todos os jogos da tabela)
        gamesestoque = Game.query.all()
        return render_template('estoqueGames.html', gamesestoque=gamesestoque)

    @app.route('/estoqueConsoles', methods=['GET', 'POST'])
    @app.route('/estoqueConsoles/<int:id>')
    def estoqueConsoles(id=None):
        if id:
            # buscando o console pela id
            console = Console.query.get(id)
            if console:
                # deletando o console
                db.session.delete(console)
                db.session.commit()
            return redirect(url_for('estoqueConsoles'))

        # Verificando se a requisição é POST:
        if request.method == 'POST' and request.form.get("CadastrarConsole") == "true":
            # Cadastra um novo console
            novoconsole = Console(
                request.form['nome'],
                request.form['fabricante'],
                request.form['preco'],
                request.form['quantidade']
            )
            db.session.add(novoconsole)
            db.session.commit()
            return redirect(url_for('estoqueConsoles'))
        
        # Captura o valor de 'page' que foi passado pelo método GET
        # Define como padrão o valor 1 e o tipo inteiro
        page = request.args.get('page', 1, type=int)
        # Valor padrão de registros por página (definimos 3)
        per_page = 3
        # Faz um SELECT no banco a partir da pagina informada (page)
        # Filtrando os registros de 3 em 3 (per_page)
        consoles_page = Console.query.paginate(page=page, per_page=per_page)
        return render_template('estoqueConsoles.html', consolesestoque=consoles_page)

    # CRUD - EDIÇÃO GAME
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        g = Game.query.get(id)
        if request.method == 'POST':
            g.titulo = request.form['titulo']
            g.ano = request.form['ano']
            g.categoria = request.form['categoria']
            g.plataforma = request.form['plataforma']
            g.preco = request.form['preco']
            g.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoqueGames'))
        # GET request - show the edit form
        return render_template('editgame.html', g=g)
    
    # CRUD - EDIÇÃO DE CONSOLE
    @app.route('/editconsole/<int:id>', methods=['GET', 'POST'])
    def editconsole(id):
        c = Console.query.get(id)
        if request.method == 'POST':
            c.nome = request.form['nome']
            c.fabricante = request.form['fabricante']
            c.preco = request.form['preco']
            c.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoqueConsoles'))
        # GET request - mostra o formulário preenchido
        return render_template('editconsole.html', c=c)
    
