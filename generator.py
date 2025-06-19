import random
import string

def gerador_de_senha():
 senha_nova = []

 gerador = 0
 while gerador < 5:
  letra_aleatoria = random.choice(string.ascii_letters)
  senha_nova.append(letra_aleatoria)

  numero_aleatorio = random.choice(string.digits)
  senha_nova.append(numero_aleatorio)

  caractere_aleatorio = random.choice(string.punctuation)
  senha_nova.append(caractere_aleatorio)

  gerador += 1

 # excluir ' da senha
 while "'" in senha_nova:
  senha_nova.remove("'")
  numero_extra = random.choice(string.digits)
  senha_nova.append(numero_extra)

 while "," in senha_nova:
  senha_nova.remove(",")
  numero_extra = random.choice(string.ascii_lowercase)
  senha_nova.append(numero_extra)

 juntar = "".join(senha_nova)
 return juntar

