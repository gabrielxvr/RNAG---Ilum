def funcao_objetivo_cb(individuo):
    """Computa qual é a função objetivo do problema de caixas binárias
    
    Args:
        individuo: lista contendo os genes das caixas binárias
        
    Return:
        Um valor representando a soma dos genes do indivíduo.
    """
    return sum(individuo) 
