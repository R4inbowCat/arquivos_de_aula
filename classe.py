import definicoes as d
d.limpa()
d.cabecalho()

class Pessoa():
    def __init__ (self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.Vida()
    def Envelhecer(self,nova_idade):
        if nova_idade<1:
            print("Envelhecimento não permitido.")
        else:
            self.idade += nova_idade
    def Engordar(self,ganho_peso):
        if ganho_peso<1:
            print("Engorda não foi permitida.")
        else:
            self.peso += ganho_peso
    def Emagrecer(self,perde_peso):
        if perde_peso<1:
            print("Emagrecimento não permitido.")
        else:
            self.peso -= perde_peso
    def Crescer(self,nova_altura):
        if nova_altura<1:
            print("Crescimento não permitido.")
        else:
            self.altura += nova_altura
    def Vida(self):
        print(f"{self.nome} possui {self.idade} anos, {self.peso} quilos e {self.altura} metros.")


class Quadrado():
    def __init__ (self,lado):
        self.lado = lado
    def Mudar_lado(self,novo_lado):
        self.lado = novo_lado
    def Calcular_area(self):
        area = self.lado*self.lado
        print(f"A área do quadrado é de {area} cm.")
    def Mostrar_lado(self):
        print(f"O quadrado possui {self.lado} cm de lado.")


class Conta_corrente():
    saldo = 0
    def __init__ (self,num_de_conta,nome):
        self.num_de_contas = num_de_conta
        self.nome = nome
    def Alterar_nome(self,novo_nome):
        self.nome = novo_nome
    def Depositar(self,deposito):
        if deposito<0:
            print("Depósito inválido.")
        else:
            self.saldo += deposito
    def Sacar(self,saque):
        if saque<0:
            print("Saque inválido.")
        else:
            self.saldo -= saque