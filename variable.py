class Variable:
    def __init__(self, cantidad, grado):
        self.cantidad = cantidad
        self.grado = grado

    def __str__(self):
        return f'{self.cantidad}X^{self.grado}'