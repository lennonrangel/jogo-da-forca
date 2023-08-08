# JOGO DA FORCA

#Importando biblioteca random para escolher uma palavra aleatória a partir de uma lista.
import random

#Definindo palavras
palavras = ['academia', 'algoritmo', 'computador', 'brasil', 'python']

palavra = random.choice(palavras)

#Variáveis
tentativas = 0
vidas = 6
letras_escolhidas = []

#A função "len" é usada para retornar o comprimento de um objeto, ou seja, número de itens contidos em uma sequência.
estado_atual = ['_'] * len(palavra)

print('Você tem', vidas, 'vidas restantes')

#Lógica do jogo

#A função ".join()" é usada para juntar elementos de uma sequência (como uma lista) em uma única string
#separada por um caractere especificado.
while tentativas < vidas and ''.join(estado_atual) != palavra:

    letra = input("\nAdivinhe uma letra: ")

    #Não repetir letra já escolhida
    while letra in letras_escolhidas:
        print("Letra já escolhida, escolha outra")
        letra = input("\nAdivinhe uma letra: ")

    #A função "append" é usada para adicionar um elemento ao final de uma lista existente.
    letras_escolhidas.append(letra)

    if letra in palavra:
        print("Parabéns, você acertou uma letra!")
        for i in range(len(palavra)):
            if letra == palavra[i]:
                estado_atual[i] = letra
    else:
        print("Que pena, você errou!")
        tentativas += 1

    #Número de tentativas
    print(f"Você fez {tentativas} tentativas erradas e ainda tem {vidas - tentativas} tentativas")

    #Estado atual da palavra
    print(f"Esse é o estado atual {estado_atual}")

    #letras tentadas
    print(f"As letras que você tentou são {letras_escolhidas}")

#Jogada final
if tentativas == vidas:
    print("\nVocê perdeu, suas tentativas acabaram!")
else:
    print("\nVocê ganhou, parabéns!")

print(f"A palavra era {palavra}")
