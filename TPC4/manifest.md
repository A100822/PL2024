# Manifest TPC4

## Autor: 

**Nome:** Maya Gomes

**ID:** A100822

## Enunciado : 

**Objetivo do tpc:** Construir um analisador léxico para:
- select id, nome, salario from empregados where salario >= 820

## Etapas:

Começou-se por criar uma lista de tuplos, onde cada tuplo contém um tipo de token (como 'SELECT', 'FROM', ',', etc.) e uma expressão regular que corresponde a esse tipo de token. De seguida foi utilizado o `tok_regex = '|'.join('(?P<%s>%s)'` para compilar todas as expressões regulares numa única expressão regular que irá reconhecer qualquer um dos tokens especificados. Finalmente, iteramos sobre a query e procuramos as correspondências. Preenchemos uma lista com tuplos contendo o tipo de token e o valor correspondente encontrado na consulta SQL. Finalmente, a função retorna a lista de tokens após o loop de iteração.

## Resultados:

('SELECT', 'select')
('WHITESPACE', ' ')
('ID', 'id')
('COMMA', ',')
('WHITESPACE', ' ')
('ID', 'nome')
('COMMA', ',')
('WHITESPACE', ' ')
('ID', 'salary')
('WHITESPACE', ' ')
('FROM', 'from')
('WHITESPACE', ' ')
('ID', 'empregados')
('WHITESPACE', ' ')
('WHERE', 'where')
('WHITESPACE', ' ')
('ID', 'salary')
('WHITESPACE', ' ')
('GREATER_EQ', '>=')
('WHITESPACE', ' ')
('NUM', '820')

