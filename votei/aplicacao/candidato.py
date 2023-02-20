class Candidato():
    """    Classe candidato, projeto votei   """
    counter = -1
    def __init__(self, name="", cargo="", estado="", partido="", \
                 inicio="", fim="", propostas=""):
        Candidato.counter += 1
        self.__id = Candidato.counter
        self.__name = name
        self.__cargo = cargo
        self.__estado = estado
        self.__partido = partido
        self.__inicioMandato = inicio
        self.__fimMandato = fim
        self.__propostasLegs = propostas

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado

    @property
    def partido(self):
        return self.__partido

    @partido.setter
    def partido(self, partido):
        self.__partido = partido

    @property
    def inicioMandato(self):
        return self.__inicioMandato

    @inicioMandato.setter
    def inicioMandato(self, inicio):
        self.__inicioMandato = inicio

    @property
    def fimMandato(self):
        return self.__fimMandato

    @fimMandato.setter
    def fimMandato(self, fim):
        self.__fimMandato = fim

    @property
    def propostasLegs(self):
        return self.__propostasLegs

    @propostasLegs.setter
    def propostasLegs(self, propostas):
        self.__propostasLegs = propostas