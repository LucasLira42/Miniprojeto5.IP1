from pessoa import Pessoa
from indices import taxa_mensal_rendimento
from indices import gastos

def inserir_pessoa(pessoas,nome,salario,patrimonio):  
    nova_pessoa = Pessoa(nome,salario,patrimonio,0)
    pessoas.append(nova_pessoa)
    

def digitar_dados_pessoa(pessoas):
    nome = input("digite aqui seu nome: ")
    salario = float(input("digite aqui o seu salário: "))
    patrimonio = float(input("digite aqui o seu patrimônio: "))

    inserir_pessoa(pessoas,nome,salario,patrimonio)

def mostrar_dados_pessoa(pessoa):
    print(f"{pessoa.nome:<20}, salário {pessoa.salario:<10.2f}, patrimonio: {pessoa.patrimonio:<13.2f} ")

def mostrar_dados_pessoas(pessoas):
    for i in pessoas: mostrar_dados_pessoa(i)

def simular_recebimentos(pessoa,taxa_mensal_rendimento):
    rendimento_mensal_passivo = taxa_mensal_rendimento * pessoa.patrimonio
    pessoa.conta_corrente = rendimento_mensal_passivo + pessoa.salario

def simular_gastos(pessoa,gastos):
    moradia = max(gastos["moradia"][0], gastos["moradia"][1] * pessoa.salario)

    if pessoa.conta_corrente > 0:
        pessoa.conta_corrente  = pessoa.conta_corrente  - moradia
    else:
        pessoa.conta_corrente  = pessoa.conta_corrente  - gastos["moradia"][0]
     

    alimentacao = max(gastos["alimentacao"][0], gastos["alimentacao"][1] * pessoa.salario)

    if pessoa.conta_corrente > 0:
        pessoa.conta_corrente  = pessoa.conta_corrente  - alimentacao
    else:
        pessoa.conta_corrente  = pessoa.conta_corrente  - gastos["alimentacao"][0]


    transporte = max(gastos["transporte"][0] , gastos["transporte"][1] * pessoa.salario)

    if pessoa.conta_corrente > 0:
        pessoa.conta_corrente  = pessoa.conta_corrente  - transporte
    else:
        pessoa.conta_corrente  = pessoa.conta_corrente  - gastos["transporte"[0]]

    educacao = max(gastos["educacao"][0] , gastos["educacao"][1] * pessoa.salario)

    if pessoa.conta_corrente > 0:
        pessoa.conta_corrente  = pessoa.conta_corrente  - educacao
    else:
        pessoa.conta_corrente  = pessoa.conta_corrente  - gastos["educacao"][0] 

    saude= max(gastos["saude"][0], gastos["saude"][1] * pessoa.salario)

    if pessoa.conta_corrente > 0:
        pessoa.conta_corrente  = pessoa.conta_corrente  - saude
    else:
        pessoa.conta_corrente  = pessoa.conta_corrente  - gastos["saude"][0]               

    pessoa.patrimonio = pessoa.patrimonio + pessoa.conta_corrente 
    pessoa.conta_corrente  = 0
    
        #eu tenho que colocar para cada chave do dicionário de gastos? 

def simular_mes_populacao(pessoas, taxa_mensal_rendimento,gastos):
    
    for i in pessoas: 
     simular_recebimentos(i,taxa_mensal_rendimento) 
     simular_gastos(i,gastos) 




    

 




