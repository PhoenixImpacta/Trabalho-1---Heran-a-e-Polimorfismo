class Disciplina():
    def __init__(self, nome, carga_horaria, teoria, pratica, ementa, competencias, habilidades, conteudo, bibliografia_basica, bibliografia_complementar):
        self._nome = nome
        self._carga_horaria = carga_horaria
        self._teoria = teoria
        self._pratica = pratica
        self._ementa = ementa
        self._competencias = competencias
        self._habilidades = habilidades
        self._conteudo = conteudo
        self._bibliografia_basica = bibliografia_basica
        self._bibliografia_complementar = bibliografia_complementar

    def set_nome(self, nome):
        if len(nome) > 0:
            self._nome = nome
            return True
        else:
            return False

    def get_nome(self):
        return self._nome

    def set_carga_horaria(self, carga_horaria):
        if carga_horaria > 0:
            self._carga_horaria = carga_horaria

    def get_carga_horaria(self):
        return self._carga_horaria

    def set_teoria(self, teoria):
        if teoria > 0:
            self._teoria = teoria

    def get_teoria(self):
        return self._teoria

    def set_pratica(self, pratica):
        if pratica > 0:
            self._pratica = pratica

    def get_pratica(self):
        return self._pratica

    def set_ementa(self, ementa):
        if len(ementa) > 0:
            self._ementa = ementa
            return True
        else:
            return False


    def get_ementa(self):
        return self._ementa

    def set_competencias(self, competencias):
        if len(competencias) > 0:
            self._competencias = competencias
            return True
        else:
            return False


    def get_competencias(self):
        return self._competencias

    def set_habilidades(self, habilidades):
        if len(habilidades) > 0:
            self._habilidades = habilidades
            return True
        else:
            return False


    def get_habilidades(self):
        return self._habilidades

    def set_conteudo(self, conteudo):
        if len(conteudo) > 0:
            self._conteudo = conteudo
            return True
        else:
            return False


    def get_conteudo(self):
        return self._conteudo

    def set_bibliografia_basica(self, bibliografia_basica):
        if len(bibliografia_basica) > 0:
            self._bibliografia_basica = bibliografia_basica
            return True
        else:
            return False


    def get_bibliografia_basica(self):
        return self._bibliografia_basica

    def set_bibliografia_complementar(self, bibliografia_complementar):
        if len(bibliografia_complementar) > 0:
            self._bibliografia_complementar = bibliografia_complementar
            return True
        else:
            return False


    def get_bibliografia_complementar(self):
        return self._bibliografia_complementar