import datetime

class Nota:
    def __init__(self, titulo, texto, categoria, classe):
        self.titulo = titulo
        self.texto = texto
        self.categoria = categoria
        self.classe = classe

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f"[{self.data}] ({self.classe}) {self.texto}"