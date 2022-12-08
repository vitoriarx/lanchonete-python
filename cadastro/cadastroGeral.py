from insert.inserts import Inserts
dados = Inserts()
class CadastroGeral():
    def cadastroCliente(self):
        nome=input("Nome completo:")
        cpf=input("Cpf:")
        rg=input("RG:")
        idade=input("Idade:")
        telefone=input("Telefone:")
        email=input("Email:")
        sexo=input("Sexo:")
        cep=input("Cep:")
        senha=input("Senha:")

        dados.insertClient(nome,cpf,rg,idade,telefone,email,sexo,cep,senha)
    
    def cadastroComida(self):
        nome=input("Nome da refeição:")
        preco=input("Preço da refeição:")
        dados.insertCardapio(nome, preco)






