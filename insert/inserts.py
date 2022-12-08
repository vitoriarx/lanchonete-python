import json
from os import path
import datetime
class Inserts():
    def insertClient(self, nome,cpf,rg,idade,telefone,email,sexo,cep,senha):

 
        filename = r"C:\Users\Vitória\OneDrive\Documentos\Área de Trabalho\vitoriaTrabalho-master\data\clientes.json"
        listObj = []
        
        
        # Lendo o arquivo json
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome":nome,
            "cpf": cpf,
            "rg":rg,
            "idade": idade,
            "telefone": telefone,
            "email":email,
            "sexo": sexo,
            "cep": cep,
            "senha":senha


            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
        print('Usuario cadastrado Com sucesso')
    
    def insertCardapio(self,nomeDoPrato,preco):
        filename = r"C:\Users\Vitória\OneDrive\Documentos\Área de Trabalho\vitoriaTrabalho-master\data\comidas.json"
        listObj = []
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome_do_prato":nomeDoPrato,
            "preco": preco,
            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        
        print('Pedido Inserido no Menu!')
    
    def sangria(self,nomeCliente,pedidoCliente,valorPago,troco):
        filename = r"C:\Users\Vitória\OneDrive\Documentos\Área de Trabalho\vitoriaTrabalho-master\data\sangria.json"
        listObj = []
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append({
            "nome_do_cliente":nomeCliente,
            "pedido_do_cliente": pedidoCliente,
            "valor_pago": valorPago,
            "troco": troco,
            "data": str(datetime.datetime.now())
            })
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        