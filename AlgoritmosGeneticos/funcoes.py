import random as rd

def gene_cb():
    """Gera um gene válido para o problema das caixas binárias
    
    Return:
    Um valor zero ou um.
    """
    lista = [0, 1]
    gene = rd.choice(lista)
    return gene

def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não binárias
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir
    
    Return:
        Um valor entre zero e o máximo.
    """
    gene = rd.randint(0, valor_max_caixa)
    return gene


def individuo_cb(n):
    """Gera um indivíduo para o problema das caixas binárias
    
    Args:
        n: número de genes do indivíduo
        
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for _ in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo

def individuo_cnb(n, valor_max_caixa):
    """Gera um indivíduo para o problema das caixas não binárias
    
    Args:
        n: número de genes do indivíduo
        valor_max_caixa: Valor máximo que a caixa pode assumir
        
    Return:
        Uma lista com n genes. Cada gene é um valor entre zero e o valor máximo dos genes.
    """
    individuo = []
    for _ in range(n):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

def populacao_cb(tamanho, n):
    """Cria uma população para o problema das caixas binárias
    
    Args:
        n: Número de genes de cada indivíduo
        tamanho: Número de Indivíduos
    
    Return:
        Uma lista contendo cada indivíduo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao

def populacao_cnb(tamanho, n, valor_max_caixa):
    """Cria uma população para o problema das caixas binárias
    
    Args:
        n: Número de genes de cada indivíduo
        tamanho: Número de Indivíduos
        valor_max_caixa: Valor máximo que a caixa pode assumir
    
    Return:
        Uma lista contendo cada indivíduo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n, valor_max_caixa))
    return populacao

def selecao_roleta_max(populacao, fitness):
    """ Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
        população: Lista com todos os indivíduos da população
        fitness: lista com valor da função objetivo dos indivíduos da população
        
    Return: 
        Um valor representando a soma dos genes dos indivíduos.
    """
    populacao_selecionada = rd.choices(populacao, weights=fitness, k = len(populacao))
    return populacao_selecionada
    
def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples
    
    Args:
        pai: uma lista representando um indivíduo
        mão: uma lista representando um indivíduo
    
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos
    """
    ponto_de_corte = rd.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2
    
def mutacao_cb(individuo):
    """Realiza a mutação de um gene na problema das caixas binárias
    
    Args:
        individuo: uma lista representando o individuo no problema das caixas binárias
        
    Return:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = rd.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo

def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene na problema das caixas binárias
    
    Args:
        individuo: uma lista representando o individuo no problema das caixas binárias
        valor_max_caixa: Valor máximo que a caixa pode assumir
        
    Return:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = rd.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo
    
def funcao_objetivo_cb(individuo):
    """Computa qual é a função objetivo do problema de caixas binárias
    
    Args:
        individuo: lista contendo os genes das caixas binárias
        
    Return:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo)

def funcao_objetivo_cnb(individuo):
    """Computa qual é a função objetivo do problema de caixas não binárias
    
    Args:
        individuo: lista contendo os genes das caixas não binárias
        
    Return:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo)

def funcao_objetivo_pop_cb(populacao):
    """ Calcula a função objetivo para todos os membros de uma população
    
    Args:
        população: Lista com todos os indivíduos da população
        
    Return:
        Lista contendo o fitness de cada indivíduo
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    """ Calcula a função objetivo para todos os membros de uma população
    
    Args:
        população: Lista com todos os indivíduos da população
        
    Return:
        Lista contendo o fitness de cada indivíduo
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cnb(individuo)
        fitness.append(fobj)
    return fitness

# problema descobrindo a senha

def caractere_para_numero_ds(caractere):
    """Cria uma função que converte um caractere para um número seguindo a relação estabelecida
    
    Args:
        caractere: o caractere que se deseja converter
        
    Return:
        O número correspondente
    
    Obs: Essa função não precisava existir, mas deixa o código bem explicado
    """
    return ord(caractere)

def numero_para_caractere_ds(numero):
    """Cria uma função que converte um número para um caracter seguindo a relação estabelecida
    
    Args:
        numero: o número que se deseja converter
        
    Return:
        O caractere correspondente
        
    Obs: Essa função não precisava existir, mas deixa o código bem explicado
    """
    return chr(numero)

def senha_aleatoria_ds(n, caracteres):
    """Gera uma senha aleatória de tamanho n
    
    Args:
        n: número de genes ou tamanho da senha
        caracteres: caracteres disponíveis para a senha
    Return
        Lista contendo cada caractere da senha
    """
    senha = []
    for _ in range(n):
        caractere = rd.choice(caracteres)
        senha.append(caractere)
    return senha

def caractere_para_numero_individuo_ds(individuo_car):
    """Converte todos os genes de um indivíduo de caracteres para números
    
    Args:
        individuo_car: indivíduo com genes em caracteres
        
    Return:
        individuo com genes em números
    """
    individuo_num = []
    for i in individuo_car:
        j = caractere_para_numero_ds(i)
        individuo_num.append(j)
    return individuo_num

def numero_para_caractere_individuo_ds(individuo_num):
    """Converte todos os genes de um indivíduo de números para caracteres
    
    Args:
        individuo_num: indivíduo com genes em números
        
    Return:
        individuo com genes em caracteres
    """
    individuo_car = []
    for i in individuo_num:
        j = numero_para_caractere_ds(i)
        individuo_car.append(j)
    return individuo_car

def gene_ds(caracteres):
    """Gera um gene válido para o problema descobrindo a senha
    
    Args:
        caracteres: caracteres disponíveis para a senha
    
    Return:
        O número correspondente a um caractere disponível para a senha
    """
    gene = caractere_para_numero_ds(rd.choice(caracteres))
    return gene

def individuo_ds(n, caracteres):
    """Gera um indivíduo para o problema descobrindo a senha
    
    Args:
        n: número de genes do indivíduo
        caracteres: caracteres disponíveis para a senha
        
    Return:
        Uma lista com n genes. Cada gene é o número correspondente a um caractere.
    """
    individuo = []
    for _ in range(n):
        gene = gene_ds(caracteres)
        individuo.append(gene)
    return individuo

def populacao_ds(tamanho, n, caracteres):
    """Cria uma população para o problema descobrindo a senha
    
    Args:
        n: Número de genes de cada indivíduo
        tamanho: Número de Indivíduos
        caracteres: caracteres disponíveis para a senha
    
    Return:
        Uma lista contendo cada indivíduo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_ds(n, caracteres))
    return populacao


def funcao_objetivo_ds(individuo, senha):
    """Computa qual é a função objetivo do problema "descobrindo a senha"
    
    Args:
        individuo: lista contendo os genes das caixas não binárias
        senha: a senha verdadeira
        
    Return:
        Um valor representando a soma dos erros do indivíduo
        
    Obs:
        Eu escolhi usar o erro "não quadrado" para aumentar a diversidade
    """
    fitness = 0
    senha_num = caractere_para_numero_individuo_ds(senha)
    for i in range(len(individuo)):
        fitness = fitness + abs(individuo[i] - senha_num[i])
    return fitness

def funcao_objetivo_pop_ds(populacao, senha):
    """ Calcula a função objetivo para todos os membros de uma população
    
    Args:
        população: Lista com todos os indivíduos da população
        senha: a senha verdadeira
        
    Return:
        Lista contendo o fitness de cada indivíduo
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_ds(individuo, senha)
        fitness.append(fobj)
    return fitness

def selecao_por_torneio_ds(populacao_total, chance_de_participar, senha):
    """Seleciona uma parcela da população para competir e coloca o valor do vencedor no lugar dos demais
    
    Args:
        população: Lista com todos os indivíduos da população
        taxa_de_competicao: chance de um individuo participar da competição
        
    Return:
        Lista após as alterações feitas pelo torneio 
    """
    index = []
    """solução antiga: melhor_fit = 1e20 # não gostei dessa solução, mas não pensei em nada melhor """
    melhor_fit = float("inf")
    for i in range(len(populacao_total)):
        if rd.random() < chance_de_participar:
            individuo = populacao_total[i]
            fobj = funcao_objetivo_ds(individuo, senha)
            if fobj < melhor_fit:
                melhor_fit = fobj
                indice_melhor_fit = i
            index.append(i)
    
    populacao_selecionada = populacao_total
    
    for j in index:
        populacao_selecionada[j] = populacao_total[indice_melhor_fit]
    
    return populacao_selecionada

def mutacao_ds(individuo, caracteres):
    """Realiza a mutação de um gene no problema descobrindo a senha
    
    Args:
        individuo: uma lista representando o individuo no problema das caixas binárias
        caracteres: caracteres disponíveis para a senha
        
    Return:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = rd.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_ds(caracteres)
    return individuo
    
# função de Himmelblau

def intervalo_com_passo(lim_inf, lim_sup, passo):
    """ Cria uma lista com um intervalo e com um passo que será a diferença entre os elementos dessa lista
    
    Args:
        lim_inf: limite inferior
        lim_sup: limite superior
        passo: diferença entre os elementos sequentes da lista
        
    Return:
        Uma lista com valores númericos em um intervalo
    """
    lista_ip = []
    a = int(lim_inf/passo)
    b = int(lim_sup/passo)
    
    for i in range(a, b):
        j = round(i*passo, 3)
        lista_ip.append(j)
        
    return lista_ip


def gene_fh(dominio_x_y):
    """ Função que gera, a partir do domínio de x e y, um gene
    
    Args:
        dominio_x_y: valores possíveis para x

    Return:
        Um valor pertencente ao domínio de x e y
        
    Obs:
        Vamos trabalhar apenas com domínios iguais para x e y
    """
    gene = rd.choice(dominio_x_y)
    return gene

def individuo_fh(n, dominio_x_y):
    """ Função que gera a partir de um número de genes um domínio, um indivíduo
    
    Args:
        n: número de genes
        dominio_x_y: valores possíveis para x e y
        
    Return:
        Um indivíduo possível para o problema
    """
    individuo = []
    for _ in range(n):
        gene = gene_fh(dominio_x_y)
        individuo.append(gene)
    return individuo

def populacao_fh(tamanho, n, dominio_x_y):
    """ Função que gera uma população de indivíduos
    
    Args:
        n: Número de genes de cada indivíduo
        tamanho: Número de Indivíduos
        dominio_x_y: valores possíveis para x e y
    
    Return:
        Uma lista contendo cada indivíduo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_fh(n, dominio_x_y))
    return populacao

def funcao_objetivo_fh(individuo):
    """Computa qual é a função objetivo do problema de caixas não binárias
    
    Args:
        individuo: lista contendo os genes das caixas não binárias
        
    Return:
        O valor da função de função de Himmelblau no ponto de x e y correspondentes ao gene
    """
    x = individuo[0]
    y = individuo[1]
    
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def funcao_objetivo_pop_fh(populacao):
    """ Calcula a função objetivo para todos os membros de uma população
    
    Args:
        população: Lista com todos os indivíduos da população
        
    Return:
        Lista contendo o fitness de cada indivíduo
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_fh(individuo)
        fitness.append(fobj)
    return fitness

def selecao_por_torneio_fh(populacao_total, chance_de_participar):
    """Seleciona uma parcela da população para competir e coloca o valor do vencedor no lugar dos demais
    
    Args:
        população: Lista com todos os indivíduos da população
        taxa_de_competicao: chance de um individuo participar da competição
        
    Return:
        Lista após as alterações feitas pelo torneio 
    """
    index = []
    """solução antiga: melhor_fit = 1e20 # não gostei dessa solução, mas não pensei em nada melhor """
    melhor_fit = float("inf")
    for i in range(len(populacao_total)):
        if rd.random() < chance_de_participar:
            individuo = populacao_total[i]
            fobj = funcao_objetivo_fh(individuo)
            if fobj < melhor_fit:
                melhor_fit = fobj
                indice_melhor_fit = i
            index.append(i)
    
    populacao_selecionada = populacao_total
    
    for j in index:
        populacao_selecionada[j] = populacao_total[indice_melhor_fit]
    
    return populacao_selecionada

def mutacao_fh(individuo, dominio_x_y):
    """Realiza a mutação de um gene na problema da função de Himmelblau
    
    Args:
        individuo: uma lista representando o individuo no problema das caixas binárias
        dominio_x_y: valores possíveis para x
        
    Return:
        Um indivíduo com um gene mutado.
    """
    gene_a_ser_mutado = rd.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_fh(dominio_x_y)
    return individuo

def gene_fh2():
    """ Função que gera um gene
    
    Args:

    Return:
        Um valor entre -9 e 9
        
    """
    gene = rd.randint(-9, 10)
    return gene

def individuo_fh2(n):
    """ Função que gera a partir de um número de genes um domínio, um indivíduo
    
    Args:
        n: número de genes
        
    Return:
        Um indivíduo possível para o problema
    """
    individuo = []
    for _ in range(n):
        gene = gene_fh2()
        individuo.append(gene)
    return individuo

def populacao_fh2(tamanho, n):
    """ Função que gera uma população de indivíduos
    
    Args:
        n: Número de genes de cada indivíduo
        tamanho: Número de Indivíduos
    
    Return:
        Uma lista contendo cada indivíduo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_fh2(n))
    return populacao


# NOVIDADE
def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist

def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (rd.random(), rd.random())

    return cidades

def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    rd.shuffle(nomes)
    return nomes

def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao

def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = rd.randint(0, len(pai) - 2)
    corte2 = rd.randint(corte1, len(pai) - 1)
    
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
            
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
            
    return filho1, filho2

def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    Args:
      individuo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    
    indices = list(range(len(individuo)))
    lista_sorteada = rd.sample(indices, k=2)
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo

def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0
    
    for posicao in range(len(individuo) - 1):
        
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
        
    #calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
    
    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso
    
    return distancia
    
    # preencher o código

    return distancia

def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = rd.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

# Problema da mochila

def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    "vamos preencher aqui"
    
    valor_total =0
    peso_total = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]
            
            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item

    return valor_total, peso_total

def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """
    
    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila

def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado

# liga ternária

def computa_peso_lt(individuo):
    """Computa o peso do indivíduo
    
    Args:
        individuo: um indivíduo válido para a liga ternária
    
    Return:
        Um valor correspondente ao peso do indivíduo
    """
    
    peso = 0
    for cromossomo in individuo:
        peso += cromossomo[1]
        
    return peso

def computa_preco_lt(individuo, preco):
    """Computa o preco de um indivíduo
    
    Args:
        individuo: um indivíduo válido para a liga ternária
        preco: dicionário contendo o preço de cada elemento
        
    Return:
        preço da liga ternária
    """
    preco_liga = 0
    for cromossomo in individuo:
        elemento = cromossomo[0]
        massa = cromossomo[1]
        preco_elemento = preco[elemento]
        preco_liga += massa*preco_elemento/1000
        
    return preco_liga

def individuo_lt(n_elementos, massa_maxima, preco):
    """função que gera indivíduos viáveis, nesse caso, indivíduos em que os genes de massa somem n g.
    
    Args:
        n_elementos: número de elementos utilizados na liga
        massa_maxima: limite de massa da liga
        preco: dicionário contendo o preço de cada elemento
        
    return:
        Um indivíduo em que os genes de massa somam n g
    """
    
    elementos = list(preco.keys())
    
    individuo = []
    
    for _ in range(n_elementos):
        gene_elemento = rd.choice(elementos)
        gene_massa = 0
        cromossomo = [gene_elemento, gene_massa]
        individuo.append(cromossomo)    
    
    peso = computa_peso_lt(individuo)
    
    while peso != massa_maxima:
        ind = rd.randint(0, n_elementos - 1)
        individuo[ind][1] = 0
        peso = computa_peso_lt(individuo)
        val = rd.randint(1, massa_maxima - peso)
        individuo[ind][1] = val
        peso = computa_peso_lt(individuo)
    
    return individuo

def populacao_lt(n_elementos, massa_maxima, preco, n_individuos):
    """Cria uma população de indivíduos viáveis para o problema da liga ternária
    
    Args:
        n_elementos: número de elementos utilizados na liga
        massa_maxima: limite de massa da liga
        preco: dicionário contendo o preço de cada elemento
        n_individuos: Tamanho da população
        
    Return:
        Uma população da liga ternária
    """
    
    populacao = []
    
    for _ in range(n_individuos):
        populacao.append(individuo_lt(n_elementos, massa_maxima, preco))
        
    return populacao
        