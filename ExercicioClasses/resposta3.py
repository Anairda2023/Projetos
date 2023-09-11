class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valores(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornar_valores(self):
        return self.ladoA, self.ladoB

    def calcular_area(self):
        return self.ladoA * self.ladoB

    def calcular_perimetro(self):
        return 2 * (self.ladoA + self.ladoB)


def calcular_pisos_rodapes(local, medida_piso, medida_rodape):
    area_local = local.calcular_area()
    perimetro_local = local.calcular_perimetro()

    area_piso = medida_piso ** 2
    area_rodape = medida_rodape * perimetro_local

    quantidade_pisos = area_local / area_piso
    quantidade_rodapes = perimetro_local / medida_rodape

    return quantidade_pisos, quantidade_rodapes


ladoA = float(input("Informe a medida do lado A do local: "))
ladoB = float(input("Informe a medida do lado B do local: "))

local = Retangulo(ladoA, ladoB)

medida_piso = float(input("Informe a medida de um piso: "))
medida_rodape = float(input("Informe a medida de um rodapé: "))


quantidade_pisos, quantidade_rodapes = calcular_pisos_rodapes(local, medida_piso, medida_rodape)


print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes:.2f}")
