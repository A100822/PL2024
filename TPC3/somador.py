import re

def processa(nome_ficheiro):
    soma_total = 0
    soma_ativa = False

    with open(nome_ficheiro, 'r') as ficheiro:
        for linha in ficheiro:
            if re.search(r'ON', linha, re.IGNORECASE):
                soma_ativa = True
                linha = re.sub(r'.*?ON', '', linha, flags=re.IGNORECASE)
            elif re.search(r'OFF', linha, re.IGNORECASE):
                soma_ativa = False

            if soma_ativa:
                numeros = re.findall(r'\d+', linha)
                for numero in numeros:
                    soma_total += int(numero)

            if "=" in linha:
                print("Soma =", soma_total)

def main():
    nome_ficheiro = "teste.txt"
    processa(nome_ficheiro)

if __name__ == "__main__":
    main()