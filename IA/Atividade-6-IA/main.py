from googletrans import Translator

from analise_sentimentos import AnaliseSentimentos

tradutor = Translator()
analisador = AnaliseSentimentos()

frase = input('Digite uma frase\n> ')

traduzida = tradutor.translate(frase, dest='pt').text
print(f'Tradução: {traduzida}')

resultado = analisador.avaliar(traduzida)['polaridade']

if resultado == 0:
  print('Frase neutra')
elif resultado > 0:
  print('Frase positiva')
elif resultado < 0:
  print('Frase negativa')
