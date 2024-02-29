# Manifest TPC3

## Autor: 

**Nome:** Maya Gomes

**ID:** A100822

## Enunciado Somador on/off : 
Pretende-se um programa que some todas as sequências de dígitos que encontre num texto.

**Objetivo do tpc:** Criar um programa em que:
- se aparecer "on" (com qualquer combinação de maiuscualas e minusculas) o programa passa a somar os inteiros que encontrar;
- se encontrar "off" (com qualquer combinação de maiuscualas e minusculas) o programa deixa de somar
- se encontrar "=" o programa imprime o somatorio da soma: "Soma = XX"

## Etapas:
Foram criadas quatro expressões regulares:
- `re.search(r'ON', linha, re.IGNORECASE)`:  Esta expressão regular procura pela string 'ON' (em letras maiúsculas ou minúsculas) na linha atual.
- `re.sub(r'.*?ON', '', linha, flags=re.IGNORECASE)`:  Esta expressão regular procura por qualquer sequência de caracteres (.*?) seguida de um 'ON' (em letras maiúsculas ou minúsculas), e substitui essa parte da linha por uma string vazia, removendo-a. Assim, não teremos em conta esses elementos na soma.
- `re.search(r'OFF', linha, re.IGNORECASE)`: Esta expressão regular procura pela string 'OFF' (em letras maiúsculas ou minúsculas) na linha atual.
- `re.findall(r'\d+', linha)`: Esta expressão regular encontra todas as ocorrências de um ou mais dígitos (\d+) na linha atual.

Para além disso, sempre que é encontrado um "=" programa imprime a soma total dos números encontrados até o momento. A soma acumulada até o momento é armazenada na variável `soma_total`.

## Resultados:
(exemplo da aula teórica)
soma=12
soma=32

