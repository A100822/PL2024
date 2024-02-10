def dividirFaixaEtarias(idades):
    faixasEtarias = {}
    total_atletas = len(idades)
    for idade in idades:
        faixa_etaria = int(idade) // 5 * 5
        faixa = f"{faixa_etaria}-{faixa_etaria + 4}"
        if faixa in faixasEtarias:
            faixasEtarias[faixa] += 1
        else:
            faixasEtarias[faixa] = 1
    #percentagem de atletas em cada faixa etária
    for faixa, num_atletas in faixasEtarias.items():
        percentagem = (num_atletas / total_atletas) * 100
        faixasEtarias[faixa] = {"numero_de_atletas": num_atletas, "percentagem": percentagem}
    return faixasEtarias

with open('dataset.csv', 'r') as file:
    
    linhas = file.readlines()[1:]
    modalidades = set()
    aptos = []
    idades = []

    total_true = 0
    total_false = 0

    
    for linha in linhas:
        colunas = linha.strip().split(',')

        #modalidades desportivas
        modalidade = colunas[8]
        modalidades.add(modalidade.lower())

        #atletas aptos e inaptos
        apto = colunas[12]
        aptos.append(apto)

        if apto == "true":
            total_true += 1

        elif apto == "false":
            total_false += 1

        #idades dos atletas
        idade = colunas[5]
        idades.append(idade)


    #ordenação das modalidades
    modalidades = sorted(modalidades)
    print(modalidades)

    #percentagens de aptos e inaptos
    total = len(aptos)
    percentagem_true = (total_true / total) * 100
    percentagem_false = (total_false / total) * 100

    print(f"Percentagem de aptos para a prática desportiva: {percentagem_true:.2f}%")
    print(f"Percentagem de inaptos para a prática desportiva: {percentagem_false:.2f}%")

    #distribuição de atletas por escalão etário
    faixasEtarias = dividirFaixaEtarias(idades)
    for faixa, info in faixasEtarias.items():
        print(f"Faixa Etária [{faixa}]: número de atletas: {info['numero_de_atletas']} percentagem: {info['percentagem']:.2f}%")
