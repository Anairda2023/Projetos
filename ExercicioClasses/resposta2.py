class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudelado(self, novolado):
        self.lado = novolado
    def retornarlado(self):
        return self.lado
    def area(self):
        return self.lado ** 2
definicao_do_quadrado = Quadrado(2)

print("O Valor do lado é", definicao_do_quadrado.retornarlado())
print("O Valor da área é", definicao_do_quadrado.area())

definicao_do_quadrado.mudelado(4)

print("O Valor do novo lado é", definicao_do_quadrado.retornarlado())
print("O Valor da nova área é", definicao_do_quadrado.area())
