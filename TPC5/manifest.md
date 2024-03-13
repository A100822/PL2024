# Manifest TPC5

## Autor: 

**Nome:** Maya Gomes

**ID:** A100822

## Enunciado : 

**Objetivo do tpc:** Construir uma Máquina de Vending.

## Etapas:

Começou-se por criar um analisador lexico para os nossos token (como 'LISTAR', 'MOEDA', etc.) e uma expressão regular que corresponde a esse tipo de token. De seguida foi utilizado o `'|'.join('(?P<%s>%s)'` para compilar todas as expressões regulares numa única expressão regular que irá reconhecer qualquer um dos tokens especificados.
Criou-se um ficheiro json com diversos produtos para efeitos de teste.
A medida que o utilizador escreve no terminal procuramos a correspondencia com o comando e em função da mesma efetuamos a respetiva função. 
A função `add_coins` adiciona as moedas carregadas e atualiza o saldo.
A `parse_coins` analisa uma string de moedas e retorna o seu valor em centimos.
A `select_product` seleciona um produto com base no seu ID e verifica o saldo atual. Se este último for superior ao preço do produto é atualizado o saldo, caso contrário é enviada uma mensagem de erro. 
A `return_change` devolve o troco.

## Resultados:
\>> listar
ID: 1, agua; 50c
ID: 2, bolo; 60c
ID: 3, café; 80c
ID: 4, sanduíche; 150c
ID: 5, refrigerante; 120c
\>> moeda 1e30c
\>> selecionar 2
Balance = 0e70c
\>> sair
Change: 0e70c


