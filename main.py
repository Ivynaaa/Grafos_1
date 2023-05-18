grafo_mat = [[0, 0, 0, 0],
             [0, 0, 1, 1],
             [0, 1, 0, 1],
             [0, 1, 1, 0]]
grafo_lista = [[],
               [2, 3],
               [1, 3],
               [1, 2]]

# verf se 1 é vizinho de 3
# if grafo_mat[1][3]==1: #O(1)
#     print('sim')
# else:
#     print('nao')
# ou
# eh_vizinho=grafo_mat[1][3]==1
# print(eh_vizinho)
# ou
print(grafo_mat[1][3] == 1)  # O(1)

# 1 é ligado a 3
# eh_vizinho=False
# for vizinho in grafo_lista[1]: #O(N)
#     if vizinho==3:
#         eh_vizinho=True
#         break
# print(eh_vizinho)
# ou
print(3 in grafo_lista[1])

# 2 funções que recebem 2 nós e informa se
# são vizinhos usando mat_adj e outra list_adj


def vizinho_matriz(no1, no2, grafo_mat):
    return grafo_mat[no1][no2] == 1


def vizinho_lista(no1, no2, grafo_lista):
    return no2 in grafo_lista[no1]


print(vizinho_matriz(1, 3, grafo_mat))
print(vizinho_lista(1, 3, grafo_lista))

grafoh_lista = {"Bia": [],
                'Caio': ["Alex"],
                'Liz': ["Caio", "Alex"],
                'Alex': ['Liz']}
