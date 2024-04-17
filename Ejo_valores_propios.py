import numpy as np

def calcular_valores_propios(matriz):
    valores_propios, vectores_propios = np.linalg.eig(matriz)
    return valores_propios

if __name__ == "__main__":
    matriz_ejemplo = np.array([[4, -2, 1],
                               [1, 1, 2],
                               [3, 6, 7]])

    valores_propios = calcular_valores_propios(matriz_ejemplo)
    
    print("Valores propios de la matriz:")
    for i, valor in enumerate(valores_propios):
        print(f"Valor propio {i + 1}: {valor}")