import json
from unittest.mock import patch
from cadastro.cadastroGeral import CadastroGeral
from pedido.pedidos import Pedidos
cadastro = CadastroGeral()
pedido = Pedidos


print('''Olá, seja bem vindo a lanchonete Doce Delícia''')
while True:
    print('''================ Menu Inicial ===============''')
    print('''
    [1] Cadastrar Cliente
    [2] Fazer Pedido
    [3] Adicionar item ao cardapio
    [4] Gerar Sangria das vendas
    [5] Sair
    ''')
    escolha = int(input(":"))
    if(escolha == 1):
        cadastro.cadastroCliente()
    elif(escolha == 2):
        pedido.autenticator()
    elif(escolha == 3):
        cadastro.cadastroComida()
    elif(escolha == 4):
        path=r"C:\Users\Vitória\OneDrive\Documentos\Área de Trabalho\vitoriaTrabalho-master\data\san2gria.json"
        with open(path, encoding='utf-8') as jsonFile:
            user = json.load(jsonFile)
        
        impressao = open("impressaoSangria.txt","a")
        listWrite = list()
        
        Topo = ("======================== Sangria =========================  \n")
        listWrite.append(Topo)
        
        for valor in range(len(user)):
            nome=f"Nome Do Cliente   ------------------------ {str(user[valor]['nome_do_cliente'])} \n"
            pedidoCliente=f"Pedido_do_cliente ------------------------ {str(user[valor]['pedido_do_cliente'])} \n"
            valorCliente= f"Valor_pago  ------------------------------ {str(user[valor]['valor_pago']) } \n"
            troco= f"Troco   ------------------------ {str(user[valor]['troco'])} \n"
            data=  f"Data ------------------------------------- {str(user[valor]['data'])} \n"
            fim="================================================================================== \n" 
            
            listWrite.append(nome)
            listWrite.append(pedidoCliente)
            listWrite.append(valorCliente)
            listWrite.append(troco)
            listWrite.append(data)
            listWrite.append(fim)
        
        impressao.writelines(listWrite)
    elif(escolha == 5):
        break
    else:
        print("Escolha não corresponde aos valores indicados no menu por favor digitar o numero da opção")
