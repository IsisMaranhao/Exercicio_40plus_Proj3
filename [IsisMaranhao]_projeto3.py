def rio(matrix, linha, coluna):

    tamanho = 1

    if linha+1 < len(matrix) and matrix[linha+1][coluna] == 1:
        matrix[linha+1][coluna] = 2
        tamanho += rio(matrix, linha+1, coluna)
    
    if linha-1 >= 0 and matrix[linha-1][coluna] == 1:
        matrix[linha-1][coluna] = 2
        tamanho += rio(matrix, linha-1, coluna)

    if coluna+1 < len(matrix[0]) and matrix[linha][coluna+1] == 1:
        matrix[linha][coluna+1] = 2
        tamanho += rio(matrix, linha, coluna+1)

    if coluna-1 >= 0 and matrix[linha][coluna-1] == 1:
        matrix[linha][coluna-1] = 2
        tamanho += rio(matrix, linha, coluna-1)
    
    return tamanho

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

def obter_tamanho(matrix):
    linhas = len(matrix)
    colunas = len(matrix[0])
    
    return linhas, colunas

print(obter_tamanho(matrix))

tamanho_rios = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (matrix[i][j] == 1):
            matrix[i][j] = 2
            tamanho_rios.append(rio(matrix,i,j))

print(tamanho_rios)