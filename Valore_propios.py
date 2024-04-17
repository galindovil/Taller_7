import numpy as np

def pedir_matriz():
    print("Al ingresar el numero de filas y columnas, se debe recordar que la matriz debe ser cuadrada:")
    filas = int(input("Ingresa el número de filas de la matriz: "))
    columnas = int(input("Ingresa el número de columnas de la matriz: "))

    matriz = np.zeros((filas, columnas))
    
    print("Ingresa los elementos de la matriz:")
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = float(input(f"Elemento [{i + 1},{j + 1}]: "))
    
    return matriz

def calcular_valores_y_vectores_propios(matriz):
    if matriz.shape[0] != matriz.shape[1]:
        raise ValueError("La matriz no es cuadrada")

    valores_propios, vectores_propios = np.linalg.eig(matriz)
    return valores_propios, vectores_propios

if __name__ == "__main__":
    matriz_usuario = pedir_matriz()

    try:
        valores_propios, vectores_propios = calcular_valores_y_vectores_propios(matriz_usuario)

        print("\nValores propios de la matriz:")
        for i, valor in enumerate(valores_propios):
            print(f"Valor propio {i + 1}: {valor}")

        print("\nVectores propios de la matriz:")
        for i, vector in enumerate(vectores_propios.T):
            print(f"Vector propio {i + 1}:", vector)
    except ValueError as e:
        print("Error:", e)