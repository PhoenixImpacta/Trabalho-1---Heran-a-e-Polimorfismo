class Matricula():
    def __init__(self, aluno, disciplina, data_matricula, data_confirmacao=None, data_cancelamento=None):
        self._aluno = aluno
        self._disciplina = disciplina
        self._data_matricula = data_matricula
        self._data_confirmacao = data_confirmacao
        self._data_cancelamento = data_cancelamento

    def set_aluno(self, aluno):
        if aluno:
            self._aluno = aluno
            return True
        else:
            return False

    def get_aluno(self):
        return self._aluno

    def set_disciplina(self, disciplina):
        if disciplina:
            self._disciplina = disciplina
            return True
        else:
            return False

    def get_disciplina(self):
        return self._disciplina

    def set_data_matricula(self, data_matricula):
        if data_matricula:
            self._data_matricula = data_matricula
            return True
        else:
            return False

    def get_data_matricula(self):
        return self._data_matricula

    def set_data_confirmacao(self, data_confirmacao):
        if data_confirmacao:
            self._data_confirmacao = data_confirmacao
            return True
        else:
            return False

    def get_data_confirmacao(self):
        return self._data_confirmacao

    def set_data_cancelamento(self, data_cancelamento):

        if data_cancelamento:
            self._data_cancelamento = data_cancelamento
            return True
        else:
            return False

    def get_data_cancelamento(self):
        return self._data_cancelamento
