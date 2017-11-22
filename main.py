from Aluno import Aluno
from Disciplina import Disciplina
from Matricula import Matricula
from Pessoa import Pessoa
from Professor import Professor
from Usuario import Usuario
from datetime import datetime


# CRIANDO 5 DISCIPLINAS
disciplina01 = Disciplina('Analise e Desenvolvimento de Sistema', 3500, 500, 3000, 'ementa', 'competencia para  disciplina', 'realizar analise de sistemas de empresas corporativas','conteudo pesado passado pelos mestrados','curso voltado para programadores', 'prefiro java')
disciplina02 = Disciplina('Banco de dados', 5000, 2000, 3000, 'ementa', 'competencia para  disciplina', 'realizar analise, manutenção e implementaçao de banco de dados em empresas corporativas','conteudo pesado passado pelos mestrados','curso voltado para DBAs', 'nada a complementar')
disciplina03 = Disciplina('Desenvolvimento de Jogos', 3500, 500, 3000, 'ementa', 'competencia para  disciplina', 'realizar desenvolvimento de jogos para empresas corporativas','conteudo pesado passado pelos mestrados','curso voltado para programadores', 'prefiro java')
disciplina04 = Disciplina('Redes de computadores', 3500, 500, 3000, 'ementa', 'competencia para  disciplina', 'realizar analise, definição e implementação de redes para empresas corporativas','conteudo pesado passado pelos mestrados','curso voltado para implementação de redes', 'prefiro java')
disciplina05 = Disciplina('Mecatronica', 3500, 500, 3000, 'ementa', 'competencia para  disciplina', 'realizar desenvolvimento de mecanismos para empresas corporativas','conteudo pesado passado pelos mestrados','curso voltado para programadores', 'prefiro java')


# CRIANDO 5 PESSOAS
pessoa01 = Pessoa('Michael Jordan', 'michael.jordan.java@gmail.com', '11988294003')
pessoa02 = Pessoa('Lucas Cirino', 'lucasrodrigues@hotmail.com', '1170707070')
pessoa03 = Pessoa('Enio ferreira', 'enioferreira@gmail.com', '1170707070')
pessoa04 = Pessoa('Adilson Araujo', 'adilsonaraujo@gmail.com', '1170707070')
pessoa05 = Pessoa('Henrique Borges', 'borges@gmail.com', '1170707070')


# CRIANDO 5 USUARIOS
usuario01 = Usuario('1700620', '1')
usuario02 = Usuario('1700665', '2')
usuario03 = Usuario('160002', '3')
usuario04 = Usuario('1700660', '4')
usuario05 = Usuario('1700000', '5')


# CRIANDO 2 PROFESSORES
professor01 = Professor(pessoa01.getNome(), pessoa01.getEmail(), pessoa01.getCelular(), usuario01.getRa(), usuario01.getSenha(), 'Jucilei', [])
professor02 = Professor(pessoa02.getNome(), pessoa02.getEmail(), pessoa02.getCelular(), usuario02.getRa(), usuario02.getSenha(), 'Cara de Rato', [])


# CRIANDO 5 ALUNOS
aluno01 = Aluno(pessoa01.getNome(), pessoa01.getEmail(), pessoa01.getCelular(), usuario01.getRa(), usuario01.getSenha(), 'ADS', [])
aluno02 = Aluno(pessoa02.getNome(), pessoa02.getEmail(), pessoa02.getCelular(), usuario02.getRa(), usuario02.getSenha(), 'BD', [])
aluno03 = Aluno(pessoa03.getNome(), pessoa03.getEmail(), pessoa03.getCelular(), usuario03.getRa(), usuario03.getSenha(), 'DJ', [])
aluno04 = Aluno(pessoa04.getNome(), pessoa04.getEmail(), pessoa04.getCelular(), usuario04.getRa(), usuario04.getSenha(), 'RC', [])
aluno05 = Aluno(pessoa05.getNome(), pessoa05.getEmail(), pessoa05.getCelular(), usuario05.getRa(), usuario05.getSenha(), 'MEC', [])


# CRIANDO 5 MATRICULAS
matricula01 = Matricula(aluno01, disciplina01, datetime.now())
matricula02 = Matricula(aluno02, disciplina02, datetime.now())
matricula03 = Matricula(aluno03, disciplina03, datetime.now())
matricula04 = Matricula(aluno04, disciplina04, datetime.now())
matricula05 = Matricula(aluno05, disciplina05, datetime.now())


# MATRICULANDO OS 5 ALUNOS AS 5 DISCIPLINAS
aluno01.matricular(matricula01)
aluno02.matricular(matricula02)
aluno03.matricular(matricula03)
aluno04.matricular(matricula04)
aluno05.matricular(matricula05)


# ADICIONANDO 2 DISCIPLINAS A UM PROFESSOR E 3 AO OUTRO
professor01.adiciona_disciplina(disciplina01)
professor01.adiciona_disciplina(disciplina02)
professor02.adiciona_disciplina(disciplina03)
professor02.adiciona_disciplina(disciplina04)
professor02.adiciona_disciplina(disciplina05)


# MOSTRA AS DISCIPLINAS DE CADA ALUNO
print('ALUNOS \n')
print('Nome: {}\nDisciplinas: {} \n'.format(aluno01.getNome(), aluno01.disciplinas_aluno()))
print('Nome: {}\nDisciplinas: {} \n'.format(aluno02.getNome(), aluno02.disciplinas_aluno()))
print('Nome: {}\nDisciplinas: {} \n'.format(aluno03.getNome(), aluno03.disciplinas_aluno()))
print('Nome: {}\nDisciplinas: {} \n'.format(aluno04.getNome(), aluno04.disciplinas_aluno()))
print('Nome: {}\nDisciplinas: {} \n'.format(aluno05.getNome(), aluno05.disciplinas_aluno()))
print('-----------------------------------')


# MOSTRA AS DISCIPLINAS DE CADA PROFESSOR
print('PROFESSORES \n')
print('Nome: {}\nDisciplinas: {} \n'.format(professor01.getNome(), professor01.disciplinas_professor()))
print('Nome: {}\nDisciplinas: {} \n'.format(professor02.getNome(), professor02.disciplinas_professor()))
print('-----------------------------------')


# MOSTRAR CARGA HORARIA DE CADA PROFESSOR
print('PROFESSORES \n')
print('Nome: {}\nCarga Horária Total: {} \n'.format(professor01.getNome(), professor01.carga_horaria_total()))
print('Nome: {}\nCarga Horária Total: {} \n'.format(professor02.getNome(), professor02.carga_horaria_total()))
print('-----------------------------------')


# CONFIRMANDO A MATRICULA DE 4 ALUNOS EM 5 DISCIPLINAS
aluno01.confirmar_matricular(matricula01)
aluno01.confirmar_matricular(matricula05)
aluno02.confirmar_matricular(matricula02)
aluno03.confirmar_matricular(matricula03)
aluno04.confirmar_matricular(matricula04)


# CONFIRMAR A MATRICULA DE 1 ALUNO EM 4 DISCIPLINAS
aluno02.confirmar_matricular(matricula01)
aluno02.confirmar_matricular(matricula03)
aluno02.confirmar_matricular(matricula04)
aluno02.confirmar_matricular(matricula05)

