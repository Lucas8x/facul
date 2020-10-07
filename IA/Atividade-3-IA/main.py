"""
- Durante o período em que o mundo passa pela Crise do Corona Vírus, um hospital solicitou que você desenvolvesse um
algoritmo que faça a triagem dos pacientes que podem conter o corona vírus.
- Foi disponibilizado uma pequena base de dados com os sintomas dos pacientes representados por 1 (possui sintoma)
ou 0 (Não possui o sintoma).
- Crie o algoritmo com Machine Learning para classificar se o paciente possui ou não o risco de estar com o
corona vírus, como no exemplo do próximo slide.
"""
import os
import pickle
from sklearn.naive_bayes import GaussianNB

from dados import atributos, resultados

SINTOMAS = ('Febre', 'Cansaço', 'Tosse', 'Espirro', 'Dores no Corpo', 'Coriza',
            'Dor de Garganta', 'Diarreia', 'Dor de Cabeça', 'Falta de Ar')


def train() -> None:
  modelo = GaussianNB()
  modelo.fit(atributos, resultados)
  pickle.dump(modelo, open('modelo.sav', 'wb'))


def init() -> None:
  print('Responda as perguntas com 0 para Não e 1 para Sim.\n')
  respostas = [int(input(f'Apresenta {sintoma}? ')) for sintoma in SINTOMAS]

  modelo = pickle.load(open('modelo.sav', 'rb'))
  resultado = modelo.predict([respostas])

  print('\nResultado:',
        '\nRecomenda-se fazer o teste de corona vírus' 
        if resultado[0] else 
        '\nPaciente não apresenta sintomas de corona vírus')


if __name__ == '__main__':
  if not os.path.exists('./modelo.sav'):
    train()
  init()
