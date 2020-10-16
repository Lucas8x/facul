import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

perguntas = ['Infomre o número do tipo da postagem Foto[0]|Link[1]|Status[2]|Vídeo[3]: ',
             'Mês: ',
             'Dia da semana: D[1]|S[2]|T[3]|Q[4]|S[6]|S[7]: ',
             'Hora: ',
             'Pago: SIM[1]|NÃO[0]: ']

# Dados
csv = pd.read_csv('dados.csv', sep=';')

# Filtro
le = LabelEncoder()
csv['Tipo'] = le.fit_transform(csv['Tipo'])

# Dados
entrada = csv.values[:, :5]
comments = csv.values[:, 5]
likes = csv.values[:, 6]
share = csv.values[:, 7]

# Modelos
comments_model = LinearRegression().fit(entrada, comments)
likes_model = LinearRegression().fit(entrada, likes)
share_model = LinearRegression().fit(entrada, share)

# Pergunta
respostas = [int(input(pergunta)) for pergunta in perguntas]

# Predict
comments_result = comments_model.predict([respostas])
likes_result = likes_model.predict([respostas])
share_result = share_model.predict([respostas])

print('Resultado:'
      f'\nMédia de Likes: {likes_result[0]:.0f}'
      f'\nMédia de Compartilhameto: {share_result[0]:.0f}'
      f'\nMédia de Comentários: {comments_result[0]:.0f}')
