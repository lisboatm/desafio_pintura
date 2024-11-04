def calcular_operacoes(n, m, r, c, imagem_desejada):
    imagem = [[0] * m for _ in range(n)]  # Inicializa a matriz com 0 (branco)
    operacoes = 0
    # Matriz auxiliar para controlar as inversões
    inversoes = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            # Calcula o estado atual do pixel considerando as inversões
            if i > 0:
                inversoes[i][j] += inversoes[i - 1][j]
            if j > 0:
                inversoes[i][j] += inversoes[i][j - 1]
            if i > 0 and j > 0:
                inversoes[i][j] -= inversoes[i - 1][j - 1]

            # Estado atual do pixel
            atual = (imagem[i][j] + inversoes[i][j]) % 2
            
            if atual != imagem_desejada[i][j]:
                if i + r <= n and j + c <= m:  # Verifica se a operação cabe na matriz
                    operacoes += 1
                    # Inverte a matriz na área r x c
                    inversoes[i][j] += 1
                    if i + r < n:
                        inversoes[i + r][j] -= 1
                    if j + c < m:
                        inversoes[i][j + c] -= 1
                    if i + r < n and j + c < m:
                        inversoes[i + r][j + c] += 1
                else:
                    return -1  # Não é possível inverter

    return operacoes

# Leitura dos casos de teste
while True:
    n, m, r, c = map(int, input().split())
    if n == 0 and m == 0 and r == 0 and c == 0:
        break
    
    imagem_desejada = [list(map(int, list(input().strip()))) for _ in range(n)]
    resultado = calcular_operacoes(n, m, r, c, imagem_desejada)
    print(resultado)
