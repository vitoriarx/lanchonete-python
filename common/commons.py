import json
class Common():
    def verificadorUser(self,nomeCompleto):
        filename = r"C:\Users\Vitória\OneDrive\Documentos\Área de Trabalho\vitoriaTrabalho-master\data\clientes.json"
        with open(filename, encoding='utf-8') as jsonFile:
            user = json.load(jsonFile)
        
        for valor in range(len(user)):
            if(user[valor]['nome'] == nomeCompleto):
                return True