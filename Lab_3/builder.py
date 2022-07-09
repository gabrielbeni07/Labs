class tipo_de_bolo:
    def __init__(self):
        self.cobertura()
        self.estilo()

    def cobertura(self):
        raise NotImplementedError

    def estilo(self):
        raise NotImplementedError


class chocolate:

    def __str__(self):
        return "chocolate"

    def cobertura(self):
        self.cobertura = "chocolate"

    def estilo(self):
        self.estilo = "aniversario"


class mandioca:

    def __str__(self):
        return "mandioca"

    def cobertura(self):
        self.cobertura = "none"

    def estilo(self):
        self.estilo = "festa informal"


class caramelo:

    def __str__(self):
        return 'caramelo'

    def cobertura(self):
        self.cobertura = "caramelo"

    def estilo(self):
        self.estilo = "casamento"


def construc_tipo_de_bolo(tp):
    Tipodb = tp()
    Tipodb.cobertura()
    Tipodb.estilo()

    return Tipodb
