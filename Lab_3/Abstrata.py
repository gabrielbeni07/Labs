class tipo_de_bolo:
    def __init__(self, tipo_de_bolo=None):
        self.tipo_de_bolo = tipo_de_bolo

    def mostrar_tipo_de_bolo(self):
        tp = self.tipo_de_bolo()
        print('Deseja-se que o bolo de {tp} seja fabricado')


class chocolate:

    def __str__(self):
        return "chocolate"

    def cobertura(self):
        return "chocolate"

    def estilo(self):
        return "aniversario"


class mandioca:

    def __str__(self):
        return "mandioca"

    def cobertura(self):
        return "none"

    def estilo(self):
        return "festa informal"


class caramelo:

    def __str__(self):
        return 'caramelo'

    def cobertura(self):
        return "caramelo"

    def estilo(self):
        return "casamento"
