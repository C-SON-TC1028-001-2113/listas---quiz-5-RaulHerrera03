
def matriz(lista):
    diagonal = []
    for i in range(len(lista)):
        diagonal.append(lista[i][i])
    return (diagonal)

def main():
    lista = []
    a = int(input(''))
    b = int(input(''))
    if a==b :
        for i in range(a):
            lista.append([])
            for j in range(b):
                n = int(input())
                lista[i].append(n)
        resultado = matriz(lista)
        print(resultado)
    else:
        print('La matriz no es cuadrada')

if __name__=='__main__':
    main()
