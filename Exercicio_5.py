# AUTORA: LAÍS RODRIGUES

###
# Escreva uma classe “Quadrado”, crie dois métodos que retornem a área do quadrado e o perímetro, não crie a instância nesse exercício.

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (self.lado**2)

    def perimetro(self):
        return (self.lado*4)