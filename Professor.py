from Pessoa import Pessoa
from Usuario import Usuario


class Professor(Pessoa, Usuario):
    def __init__(self, nome, email, celular, ra, senha, apelido, disciplinas):
        Pessoa.__init__(self, nome, email, celular)
        Usuario.__init__(self, ra, senha)
        self._apelido = apelido
        self._disciplinas = disciplinas

    def adiciona_disciplina(self, disciplina):
        if not(disciplina in self._disciplinas):
            self._disciplinas.append(disciplina)
            return True
        else:
            return False

    def remove_disciplina(self, disciplina):
        if disciplina in self._disciplinas:
            self._disciplinas.remove(disciplina)
            return True
        else:
            return False

    def disciplinas_professor(self):
        lista = []
        for x in self._disciplinas:
            lista.append(x.get_nome())
        return lista

    def carga_horaria_total(self):
        total = 0
        for x in self._disciplinas:
            total += x.get_carga_horaria()
        return total

    