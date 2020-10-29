import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

csv = pd.read_csv('./dados.csv').drop(columns=['lote'])
csv['fruta'] = LabelEncoder().fit_transform(csv['fruta'])

dados = csv.values
classificadores = dados[:, 0]
atributos = dados[:, 1:]

modelo = Sequential()
modelo.add(Dense(units=100, activation='sigmoid'))
modelo.add(Dense(units=100, activation='sigmoid'))
modelo.add(Dense(units=1, activation='sigmoid'))

modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])
modelo.fit(atributos, classificadores, batch_size=10, epochs=100)

novos_dados = np.array([
  [3.1, 122],
  [4.1, 146],
  [2.2, 86]
])

respostas = modelo.predict(novos_dados)
print(['Limão' if r > 0.5 else 'Laranja' for r in respostas])
