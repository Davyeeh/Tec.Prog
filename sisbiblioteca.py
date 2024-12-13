class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        # _ é protegido só pode ser acessado por classe e subclasse __ é privado só é acessad pela classe        
        self.titulo = titulo 
        self.autor = autor
        self.isbn = isbn
        self.quantidade = 1

    # dicionário é uma forma de coleção de dados em que se guarda uma chave e um valor correspondente. É similar a um dicionário mesmo, em que há sempre um termo e uma tradução. 
    # lista é uma sequência de valores. É um tipo de “contêiner” usado para armazenar um número indefinido de dados arbitrários do mesmo tipo ou de tipos diferentes

    def adicionar_exemplar(self, quantidade: int) -> None: # Adiciona um exemplar
        self.quantidade += quantidade 

    def remover_exemplar(self, quantidade: int) -> None: # Remove um exemplar
        self.quantidade -= quantidade

    # -> None quando o método não tem um return é um procedimento, e -> str/float/int é método que funciona como uma função

    def __str__(self) -> str: # __str__ retorna os atributos como str
        return self.titulo, self.autor, self.isbn, self.quantidade  

class Usuario:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = []

    def emprestar_livro(self, livro : Livro):
        livro = Livro()
        self.livros_emprestados.append(livro)
        livro.remover_exemplar(1)

    
        