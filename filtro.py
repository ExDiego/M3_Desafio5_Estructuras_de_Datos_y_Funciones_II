import sys

umbral = float(sys.argv[1])

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(umbral, comparacion='mayor'):
    productos_filtrados = {}
    for producto, precio in precios.items():
        if comparacion == 'mayor':
            if precio > umbral:
                productos_filtrados[producto] = precio
        elif comparacion == 'menor':
            if precio < umbral:
                productos_filtrados[producto] = precio
        else:
            print("Lo sentimos, no es una operación válida")
            return
    return productos_filtrados

def main():
    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        productos = filtrar_productos(umbral)
        print("Los productos mayores al umbral son:", ', '.join(productos.keys()))
    elif len(sys.argv) == 3:
        umbral = int(sys.argv[1])
        comparacion = sys.argv[2]
        if comparacion == 'mayor' or comparacion == 'menor':
            productos = filtrar_productos(umbral, comparacion)
            if comparacion == 'mayor':
                print("Los productos mayores al umbral son:", ', '.join(productos.keys()))
            else:
                print("Los productos menores al umbral son:", ', '.join(productos.keys()))
        else:
            print("Lo sentimos, no es una operación válida")
    else:
        print("Uso: python filtro.py <umbral> [mayor|menor]")

if __name__ == "__main__":
    main()