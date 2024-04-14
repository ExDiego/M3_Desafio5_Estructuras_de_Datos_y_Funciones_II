def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def calcular_productoria(lista):
    productoria = 1
    for num in lista:
        productoria *= num
    return productoria

def controlar_calculos(**kwargs):
    for key, value in kwargs.items():
        if key.startswith('fact_'):
            numero = int(value)
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es {resultado}")
        elif key.startswith('prod_'):
            lista = value
            resultado = calcular_productoria(lista)
            print(f"La productoria de {lista} es {resultado}")

def main():
    controlar_calculos(fact_1 = 5, prod_1 = [3, 6, 4, 2, 8], fact_2 = 6)

if __name__ == "__main__":
    main()