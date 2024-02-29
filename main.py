from listaCircular import ListaCircular
from variable import Variable

listaA = ListaCircular()
listaB = ListaCircular()
listaC = ListaCircular()

def operar(num): #aqui se realiza la operacion
    listaC = ListaCircular()
    if listaA.tamannio == listaB.tamannio:
        print('entro')
        for i in range(listaA.tamannio):
            actualA = listaA.seleccionar(i)
            actualB = listaB.seleccionar(i)
            actualC = actualA.cantidad + (actualB.cantidad * num)
            listaC.agregar_elemento(Variable(actualC, actualA.grado))
        listaC.mostrar_lista()
    elif listaA.tamannio > listaB.tamannio: #aqui es cuando A es mayor a B
        tamannio_extra = listaA.tamannio - listaB.tamannio
        for i in range(tamannio_extra):
            actualA = listaA.seleccionar(i)
            listaC.agregar_elemento(Variable(actualA.cantidad, actualA.grado))
        for i in range(listaB.tamannio):
            actualA = listaA.seleccionar(i + tamannio_extra)
            actualB = listaB.seleccionar(i)
            actualC = actualA.cantidad + (actualB.cantidad * num)
            listaC.agregar_elemento(Variable(actualC, actualA.grado))
        listaC.mostrar_lista()
    elif listaA.tamannio < listaB.tamannio: #aqui cuando B es mayor a A
        tamannio_extra = listaB.tamannio - listaA.tamannio
        for i in range(tamannio_extra):
            actualB = listaB.seleccionar(i)
            listaC.agregar_elemento(Variable(actualB.cantidad * num, actualB.grado)) #ya que es A - B los resultados de 0 - B daran - B
        for i in range(listaA.tamannio):
            actualA = listaA.seleccionar(i)
            actualB = listaB.seleccionar(i + tamannio_extra)
            actualC = actualA.cantidad + (actualB.cantidad * num)
            listaC.agregar_elemento(Variable(actualC, actualA.grado))
        listaC.mostrar_lista()




def evaluar(lista, num):
    sumatoria = 0
    actualimp = ''
    for i in range(num + 1):
        actual = lista.seleccionar(i)
        sumatoria += actual.cantidad * (num ** actual.grado)
        actualimp = actualimp + '+ ' + str(actual.cantidad) + f'({str(num)})^{str(actual.grado)}'
    print(actualimp, '+ 0')
    print('Resultado:', sumatoria)
def main():
    while True:

        select = input('Menu\n'
                       '1.Ingresar componentes a un polinomio\n'
                       '2.Adición y sustracción\n'
                       '3.Evaluar polinomio\n'
                       '4.Cerrar programa\n'
                       '|:')

        print('A =')
        listaA.mostrar_lista()
        print('B =')
        listaB.mostrar_lista()

        if select == '1':
            select = input('1.Ingresar en polinomio A\n'
                           '2.Ingresar en polinomio B\n'
                           '|:')
            if select == '1':
                num = int(input('Ingrese el numero a agregar (solo enteros): '))
                listaA.agregar_elemento(Variable(num, listaA.tamannio))
                listaA.rotar(-1) #como se guarda a la derecha lo roto una vez a la derecha para que se guarde en el iniico
                listaA.mostrar_lista()
            elif select == '2':
                num = int(input('Ingrese el numero a agregar (solo enteros): '))
                listaB.agregar_elemento(Variable(num, listaB.tamannio))
                listaB.rotar(-1)
                listaB.mostrar_lista()
            else:
                print('Dato invalido')

        elif select == '2':
            select = input('1.Sumar listas\n'
                           '2.Restar listas\n'
                           '|:')
            if select == '1':
                operar(1)
            elif select == '2':
                operar(-1) #el menos es para que cuando se opere reste en lugar de sumar
            else:
                print('DAto invalido')
        elif select == '3':
            select = input('1.Evaluar listaA\n'
                           '2.Evaluar listaB\n'
                           '|:')
            if select == '1': #aqui se realizan las evaluaciones
                num = int(input('Ingrese con que numero desea evaluar (solo enteros): '))
                evaluar(listaA, num)
            elif select == '2':
                num = int(input('Ingrese con que numero desea evaluar (solo enteros): '))
                evaluar(listaB, num)
            else:
                print('Dato invalido')
        elif select == '4':
            break
        else:
            print('Invalido')


main()
