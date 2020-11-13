import spacy


class AnaliseSentimentos:
  def __init__(self):
    self.__pln = spacy.load('pt_core_news_sm')
    self.__dicionario = {}
    self.__criar_dicionario()

  def __criar_dicionario(self):
    with open('./lexico.txt') as file:
      for linha in file.readlines():
        partes = linha.split(',')
        self.__dicionario[partes[0]] = int(partes[2])

  def avaliar(self, texto):
    tokens = self.__pln(texto)
    polaridade = 0

    for token in tokens:
      palavra = str(token.lemma_).lower()
      if palavra in self.__dicionario:
        polaridade += self.__dicionario[palavra]

    return {
      'polaridade': polaridade,
      'entidades': tokens.ents
    }
