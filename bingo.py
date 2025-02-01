import random

#gerar a cartela
def gerar_cartela(jogador, linhas, colunas, intervalos):
    cartela=[]
    for _ in range(linhas):
        linha = [random.choice(range(intervalos[i][0], intervalos[i][1]+1)) for i in range (colunas)]
        cartela.append(linha)
    return{
        'jogador':jogador,
        'numeros': cartela,
        'num_marcados':set()
    }

#marcar o número q foi sorteado
def marcar_numero(cartela, numero):
    for linha in cartela['numeros']:
        if numero in linha:
            cartela['num_marcados'].add(numero)
def verificar_vitorai
