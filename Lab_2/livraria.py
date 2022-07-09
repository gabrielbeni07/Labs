class CadastrarCliente(self):
    def __init__(self, nome, email, id, compras_passadas):
        self.nome = nome
        self.email = email
        self.id = id
        self.compras_passadas = compras_passadas


class RemoverCliente(self):

    self.nome = None
    self.email = None
    self.id = None
    self.compras_passadas = None


class CadastrarAutor(self):
    def __init__(self, nome, email, titulos_publicados):
        self.nome = nome
        self.email = email
        self.titulos_publicados = titulos_publicados


class CadastrarOrdemdeCompra(self):
    def __init__(self, cliente, livro, data):
        self.cliente = cliente
        self.livro = livro
        self.data = data


class RemoverOrdemdeCompra(self):

    self.cliente = None
    self.livro = None
    self.data = None


class CadastrarLivro(self):
    def __init__(self, título, autor, gênero, edição, editora, preço_de_venda, preço_de_compra,  impostos):
        self.titulo = título
        self.autor = autor
        self.gênero = gênero
        self.edição = edição
        self.editora = editora
        self.preço_de_venda = preço_de_venda
        self.preço_de_compra = preço_de_compra
        self.impostos = impostos


class RemoverLivro(self):

    self.titulo = None
    self.autor = None
    self.gênero = None
    self.edição = None
    self.editora = None
    self.preço_de_venda = None
    self.preço_de_compra = None
    self.impostos = None
