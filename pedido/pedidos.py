import json
from common.commons import Common
from cadastro.cadastroGeral import CadastroGeral
from insert.inserts import Inserts


salva = Inserts()
cadastro = CadastroGeral()
common = Common()



class Pedidos():
    def autenticator():
        user=input("Digite o nome do Cliente:")
        if(common.verificadorUser(user)):
            with open( r"C:\Users\Vitória\OneDrive\Documentos\Área de Trabalho\vitoriaTrabalho-master\data\comidas.json", encoding='utf-8') as jsonFile:
                escolha = json.load(jsonFile)
            
            print("==================== Cardapio =====================")
            for pedido in range(len(escolha)):
                print(f"[{pedido}]      {escolha[pedido]['nome_do_prato']} ---------------------- R$ {escolha[pedido]['preco']}")
            

            pedidoCliente = int(input(":"))
            valorPago = float(input("Digita valor pago:"))
            troco = valorPago - float(escolha[pedidoCliente]['preco'])
            print(f"Troco Do Cliente:{troco}")
            salva.sangria(user,pedidoCliente,valorPago,troco)

        else:
            print("Usuario ainda não cadastrado!")
            cadastro.cadastroCliente()