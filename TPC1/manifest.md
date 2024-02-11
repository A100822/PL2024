# Manifest TPC1


**Objetivo:** Ler o dataset fornecido, processá-lo e criar resultados.

## Etapas: 
Numa primeira fase abre-se o ficheiro "dataset.csv" em modo de leitura e lê-se todas as linhas do mesmo, excluindo a primeira linha (que contém os cabeçalhos). De seguida, armazena-se as diversas linhas numa lista chamada "linhas".
Extrai-se as colunas da linha atual dividindo-a usando o "split(',')".

**Modalidades desportivas:**
Armazena-se a modalidade desportiva de cada linha (atravês de um ciclo for) no conjunto denominado "modalidades". Depois do ciclo, as modalidades são ordenadas alfabeticamente, sem esquecer de passar tudo para minusculas com o "lower()".

**Atletas aptos e inaptos:**
Armazena-se o valor da coluna "resultados", de forma a perceber se o atleta é apto (true) ou inapto (false), no conjunto denominado "aptos". Para além disso, atualiza-se os contadores "total_true" e "total_false" com base no valor do resultado de cada atleta. De seguida, calcula-se as percentagens de atletas aptos e inaptos em relação ao número total de atletas.

**Distribuição de atletas por escalão etário:**
Numa primeira fase, elaborou-se a função "dividirFaixaEtarias", função que recebe uma lista de idades e retorna um dicionário que contém todas as faixas etárias, o número de atletas em cada uma e a respetiva percentagem associada.
Assim, armazena-se a idade de cada atleta numa lista denominada "idades" e aplica-se a função referida anteriormente. 



## Resultados:
**Resultados das modalidades desportivas:**
                ['andebol', 'atletismo', 'badminton', 'basquetebol', 'btt', 'ciclismo', 'danã§a', 'equitaã§ã£o', 'esgrima', 'futebol', 'karatã©', 'orientaã§ã£o', 'parapente', 'patinagem', 'triatlo']
**Resultados das percentagem de atletas aptos e inaptos:**
                Percentagem de aptos para a prática desportiva: 54.00%
                Percentagem de inaptos para a prática desportiva: 46.00%

**Resultados da distribuição dos atletas por escalão etário:**
                Faixa Etária [25-29]: número de atletas: 102 percentagem: 34.00%
                Faixa Etária [30-34]: número de atletas: 104 percentagem: 34.67%
                Faixa Etária [20-24]: número de atletas: 80 percentagem: 26.67%
                Faixa Etária [35-39]: número de atletas: 14 percentagem: 4.67%