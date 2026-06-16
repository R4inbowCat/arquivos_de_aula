class Carro():
    motor = 1
    rodas = 4
    buzina = 1
    farolete = 2
    chave = 0
    def __init__(self,marca,modelo,peso,comprimento):
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.comprimento = comprimento
        self.Buzinar()
    def Buzinar(self):
        if(self.chave == 1):
            print(f"{self.marca} {self.modelo} disse: Bibi!")
        else:
            print(f"{self.marca} {self.modelo} está desligado!")

    def Inserir_chave(self):
        self.chave = 1

carro1 = Carro("Mitsubishi","Triton",1000,3.5)
carro1.Inserir_chave()
carro1.Buzinar()