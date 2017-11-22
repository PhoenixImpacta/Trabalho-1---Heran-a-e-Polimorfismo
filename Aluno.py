from Pessoa import Pessoa
from Usuario import Usuario
import datetime


class Aluno(Pessoa, Usuario):
    def __init__(self, nome, email, celular, ra, senha, sigla_curso, matriculas):
        Pessoa.__init__(self, nome, email, celular)
        Usuario.__init__(self, ra, senha)
        self._sigla_curso = sigla_curso
        self._matriculas = matriculas

    def disciplinas_aluno(self):
        lista = []
        for x in self._matriculas:
            lista.append(x.get_disciplina().get_nome())
        return lista

    def matricular(self, matricula):
        if not(matricula in self._matriculas):
            self._matriculas.append(matricula)
            return True
        else:
            return False

    def confirmar_matricular(self, matricula):
        if matricula in self._matriculas:
            index = self._matriculas.index(matricula)
            self._matriculas[index].set_data_confirmacao(datetime.datetime.now())
            return True
        else:
            return False

    def cancelar_matricular(self, matricula):
        if matricula in self._matriculas:
            index = self._matriculas.index(matricula)
            self._matriculas[index].set_data_cancelamento(datetime.datetime.now())
            return True
        else:
            return False
