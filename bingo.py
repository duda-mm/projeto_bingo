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
            
#verifica se tds os números foram marcados na cartela do bingo
def verificar_vitoria(cartela):
    for linha in cartela['numeros']:
        for num in linha:
            if num not in cartela['num_marcados']:
                return False
    return True
    
#exibir a cartela
def exibir_cartela(cartela):
    print(f'\n🃏 Cartela do jogador {cartela['jogador']}') #nome do jogador
    for linha in cartela["numeros"]:
        print(' '.join(
            f"[ {n:02} ]" if n in cartela['num_marcados'] else f" {n:02} "
            for n in linha
        ))
#sortear numeros sem os repetir
def sortear_numero(numeros_sorteados, ultimo_numero):
    while True:
        numero = random.randint(1,ultimo_numero)
        if numero not in numeros_sorteados:
