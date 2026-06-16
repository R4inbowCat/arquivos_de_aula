import csv
import definicoes as d
d.limpa()
d.cabecalho()

with open('turma.csv','r',encoding='utf-8') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        print(linha['nome'])


while True:
    print("1 - Cadastro")
    print("2 - Listar alunos")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        nome = input("Digite seu nome: ")
        nota = input("Digite sua nota: ")
        turma = input("Digite sua turma: ")
        with open('turm.csv','a',newline='',enconding='utf-8') as f:
            elif opcao == 2:
                print(alunos)
    else:
        break
