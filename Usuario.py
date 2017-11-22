class Usuario():
    def __init__(self, ra, senha):
        self._ra = ra
        self._senha = senha

    def setRa(self, ra):
        if ra.length > 0:
            self._ra = ra
            return True
        else:
            return False


    def getRa(self):
        return self._ra

    def setSenha(self, senha):
        if senha.length > 0:
            self._senha = senha
            return True
        else:
            return False

    def getSenha(self):
        return self._senha