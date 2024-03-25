# Manifest TPC6

## Autor: 

**Nome:** Maya Gomes

**ID:** A100822

## Enunciado : 

**Objetivo do tpc:** Construir um Parser para a linguagem criada na aula.

**Linguagem para o tpc:** 
`?a`
`=> b=a*2/(27-3)`
`!a+b`
`c=a*b/(a/b)`

## Etapas:

Numa primeiro fase, criou-se o ficheiro `analex.py` que implementa um analisador léxico usando a biblioteca Ply. Este define os tokens para as variáveis, números e operadores, incluindo funções para reconhecer e manipular esses mesmos tokens de acordo com as regras da linguagem.
De seguida, criou-se o ficheiro `anasin.py` que implementa um analisador sintático usando, mais uma vez, a biblioteca Ply. Aí define-se as regras gramaticais para a interpretação das expressões matemáticas, atribuições de valores às variáveis, comandos de impressão ('!' imprime o resultado) e leitura de variáveis ('?' lê um valor do terminal para uma variável e devolve o seu valor), garantindo a correta ordenação e execução das operações.

## Resultados:
\>> ?a
Entrada inválida. Assumindo 0.
\>> b=a*2/(27-3)
Erro: Divisão por zero.
\>> !a+b
0
\>> c=a*b/(a/b)
Erro: Divisão por zero.




