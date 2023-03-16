import random as rd

def gene_cb():
    """Gera um gene válido para o problema das caixas binárias
    
    Return:
    Um valor zero ou um.
    """
    lista = [0, 1]
    gene = rd.choice(lista)
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
    
def funcao_objetivo_cb(individuo):
    """Computa qual é a função objetivo do problema de caixas binárias
    
    Args:
        individuo: lista contendo os genes das caixas binárias
        
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