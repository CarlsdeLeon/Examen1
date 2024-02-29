class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamannio = 0

    def esta_vacia(self):
        return self.primero is None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        self.tamannio += 1

    def eliminar_elemento(self, valor):
        if self.esta_vacia():
            print('La lista esta vacia')
            return
        if self.primero.dato == valor:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            if self.primero == self.primero.siguiente:
                self.primero = None
                self.tamannio -= 1
            else:
                actual.siguiente = self.primero.siguiente
        else:
            actual = self.primero
            prev = None
            self.tamannio -= 1
            while True:
                if actual.dato == valor:
                    prev.siguiente = actual.siguiente
                    break
                prev = actual
                actual = actual.siguiente
                if actual == self.primero:
                    break

    def buscar_elemento(self, dato):
        if self.esta_vacia():
            print('La lista esta vacia')
            return False
        actual = self.primero
        while True:
            if actual.dato == dato:
                print(f'El elemento {dato} esta en la lista.')
                return True
            actual = actual.siguiente
            if actual == self.primero:
                print(f'El elemento {dato} no esta en la lista.')
                return False

    def seleccionar(self, dato):
        if self.esta_vacia():
            print('La lista esta vacia')
            return False
        actual = self.primero
        for i in range(dato):
            actual = actual.siguiente
        return actual.dato


    def mostrar_lista(self):
        if self.esta_vacia():
            print('La lista esta vacia')
            return
        actual = self.primero
        while True:
            print(actual.dato, end=' + ')
            actual = actual.siguiente
            if actual == self.primero:
                print( end='0')
                break
        print()

    def rotar(self, k):
        if self.primero is None:
            return

        if k > 0:
            for _ in range(k):
                self.ultimo = self.primero
                self.primero = self.primero.siguiente
        elif k < 0:
            for _ in range(k * -1):
                nodo_anterior = None
                nodo_actual = self.primero
                while nodo_actual.siguiente != self.primero:
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.siguiente
                self.primero = nodo_actual
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual

    def editar_elemento(self, dato_buscar, dato_nuevo):
        if self.esta_vacia():
            print('La lista esta vacia.')
            return
        actual = self.primero
        while True:
            if actual.dato == dato_buscar:
                actual.dato = dato_nuevo
                return
            actual = actual.siguiente
            if actual == self.primero:
                print(f'El elemento {dato_buscar} no esta en la lista')
                return

