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

