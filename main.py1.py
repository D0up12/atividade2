class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco


    def calcular_imposto(self):
        return self.preco * 0.10



class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca


    def desconto(self):
        return self.preco * 0.05



class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, marca, cilindrada):
        super().__init__(modelo, ano, preco)
        self.marca = marca
        self.cilindrada = cilindrada

    
    def calcular_imposto(self):
        return self.preco * 0.05



carro1 = Carro("OMEGA", 1995, 35000.0, "chevrolet")
moto1 = Moto("Falcon", 2005, 8000.0, "honda", 400)


print("=== CARRO ===")
print("Modelo:", carro1.modelo)
print("Marca:", carro1.marca)
print("Imposto:", carro1.calcular_imposto())
print("Desconto:", carro1.desconto())

print("\=== MOTO ===")
print("Modelo:", moto1.modelo)
print("Marca:", moto1.marca)
print("Cilindrada:", moto1.cilindrada)
print("Imposto:", moto1.calcular_imposto())