class Pessoa():
    def __init__(self, nome, email, celular):
        self._nome = nome
        self._email = email
        self._celular = celular

    def setNome(self, nome):
        if nome.length > 0:
            self._nome = nome
            return True
        else:
            return False

    def getNome(self):
        return self._nome

    def setEmail(self, email):
        if email.length > 0:
            self._email = email
            return True
        else:
            return False


    def getEmail(self):
        return self._email

    def setCelular(self, celular):
        if celular.length > 0:
            self._celular = celular
            return True
        else:
            return False

    def getCelular(self):
        return self._celular