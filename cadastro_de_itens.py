import csv
import definicoes as d
d.limpa()
d.cabecalho()

estrutura = ['nome','preco','quantidade']
def cadastro_produto(nome,preco,quantidade):
    with open('estoque.csv','a',newline='') as estoque:
        produto = {'nome':nome,'preco':preco,'quantidade':quantidade}
        escritor = csv.DictWriter(estoque,fieldnames=estrutura)
        escritor.writerow(produto)

def listar_produtos():
    with open('estoque.csv','r') as estoque:
        leitor = csv.DictReader(estoque)
        for itens in leitor:
            print(f"Nome: {itens['nome']} | Preço: {itens['preco']} | Quantidade: {itens['quantidade']}")

def modificar_preco(nome,novo_preco):
    produtos = []
    with open('estoque.csv','r') as estoque:
        leitor = csv.DictReader(estoque)
        for item in leitor:
            if nome == item['nome']:
                item['preco'] = novo_preco
                produtos.append(item)

    with open('estoque.csv','w',newline='',encoding = 'utf-8') as estoque:
       escritor = csv.DictWriter(estoque,fieldnames=estrutura)
       escritor.writeheader()
       escritor.writerow(produtos)

modificar_preco('Pipoca Doce','10')