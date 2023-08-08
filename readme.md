# JOGO DA FORCA

## Introdução

Este é um simples jogo da forca implementado em Python. O jogo escolhe aleatoriamente uma palavra de uma lista e o jogador deve adivinhar as letras da palavra até acertar todas as letras ou esgotar suas vidas.

## Como jogar

1. O programa escolhe aleatoriamente uma palavra da lista de palavras fornecida.
2. Você começa com um número de vidas iniciais.
3. Tente adivinhar uma letra por vez, digitando-a no terminal.
4. O jogo não diferencia letras maiúsculas de minúsculas.
5. Você não pode repetir letras que já foram escolhidas.
6. Se a letra que você adivinhou estiver na palavra escolhida, ela será exibida na posição correta.
7. Caso contrário, você perderá uma vida.
8. O jogo informa quantas tentativas erradas você fez e quantas tentativas restantes você ainda tem.
9. O estado atual da palavra é exibido com letras adivinhadas corretamente e espaços para letras não adivinhadas.
10. O jogo continua até que você adivinhe todas as letras corretamente ou suas vidas se esgotem.

## Requisitos e Execução

Para jogar o jogo, siga estas etapas:

1. Certifique-se de ter o Python instalado no seu sistema.
2. Faça o download deste repositório ou clone-o para o seu computador.
3. Abra um terminal e navegue até o diretório onde você baixou/clonou o repositório.

## Exemplo de Uso

```bash
Bem-vindo ao Jogo da Forca!
Você tem 6 vidas restantes

Adivinhe uma letra: a

Esse é o estado atual _ _ _ _ _ _ 

Você fez 0 tentativas erradas e ainda tem 6 tentativas
As letras que você tentou são ['a']

Adivinhe uma letra: e

Esse é o estado atual _ _ _ _ _ _ 

Você fez 1 tentativa errada e ainda tem 5 tentativas
As letras que você tentou são ['a', 'e']

Adivinhe uma letra: o

Esse é o estado atual _ _ _ _ o _ 

Você fez 1 tentativa errada e ainda tem 5 tentativas
As letras que você tentou são ['a', 'e', 'o']
...
```

## Personalização

Você pode personalizar o código para ajustar as regras do jogo.

## Contribuições

Se você gostaria de contribuir para este projeto, sinta-se à vontade para fazer um fork do repositório, fazer melhorias e enviar um pull request.

Divirta-se jogando Jogo da Forca! 🎮🔤

