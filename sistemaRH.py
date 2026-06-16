import definicoes as d
d.limpa()
d.cabecalho()

class Funcionarios():
    def __init__ (self,nome, cpf, salbruto):
        self.nome = nome
        self.cpf = cpf
        if salbruto<1621:
            print("Salário menor do que o mínimo.")
            return
        else:
            self.salbruto = salbruto
    def info_funcionario(self):
        self.salliquido = self.salarioliquido()
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário Bruto: {self.salbruto}")
        print(f"Salário Líquido: {self.salliquido}")
    def salarioliquido(self):
        # Desconto IR
        if self.salbruto <= 5000:
            desconto_ir = 0
        elif self.salbruto <= 7500:
            desconto_ir = self.salbruto*0.075
        elif self.salbruto <= 8000:
            desconto_ir = self.salbruto*0.15
        elif self.salbruto <= 9500:
            desconto_ir = self.salbruto*0.225
        else:
            desconto_ir = self.salbruto*0.275
        # Desconto INSS
        if self.salbruto <= 1621:
            desconto_inss = self.salbruto*0.075
        elif self.salbruto <= 3000:
            desconto_inss = self.salbruto*0.09
        elif self.salbruto <= 5000:
            desconto_inss = self.salbruto*0.12
        else:
            desconto_inss = self.salbruto*0.14
        self.salliquido = self.salbruto-(desconto_inss+desconto_ir)
        return self.salliquido
    def receber_aumento(self,percentual):
        self.salbruto = self.salbruto+self.salbruto*(percentual/100)
        self.salarioliquido()

funcionario1 = Funcionarios("Sophia",11111111111,1621)
funcionario2 = Funcionarios("Melyssa",22222222222,6300)
funcionario1.info_funcionario()
funcionario2.info_funcionario()