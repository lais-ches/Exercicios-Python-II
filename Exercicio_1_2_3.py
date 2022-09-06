# AUTORA: LAÍS RODRIGUES

###
# 1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma classe onde teremos o retorno do documento, o retorno do nome e verificação de tipo de pessoa, 
# onde um método irá receber como parâmetro “F” ou “N” para trazer fumante ou não fumante. Feito isso, crie uma instância e retorne esses valores.

class Pessoa:
    def __init__(self, documento, nome, idade, fumante):
        self.documento = documento
        self.nome = nome
        self.idade = idade
        self.fumante = fumante
        
    
    def eh_fumante(self):
        if self.fumante == "F":
            return f"é fumante"
        return f"não é fumante"

    def descricao(self):
        return f"{self.nome} tem {self.idade} anos de idade,  {self.eh_fumante()} e seu documento é {self.documento}."

pessoa1 = Pessoa('cpf', 'Lais', '29', 'N')
print(pessoa1.descricao())


###
# 2 Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método exclusivo para a classe e acesse-o.

class PessoaFisica(Pessoa):
    def __init__(self, documento, nome, idade, fumante, cpf):
        self.cpf = cpf

        super().__init__(documento, nome, idade, fumante)

    def descricao(self):
        return super().descricao() + f" de número {self.cpf}."

PF = PessoaFisica('cpf', 'Lais', '29', 'N', '123.456.789-00')
print(PF.descricao())


###
# 3 Escreva uma classe “PessoaJurica” e herde Pessoa, agora modificando o comportamento, retorne o cnpj. Crie uma instância e acesse os dados

class PessoaJuridica(Pessoa):
    def __init__(self, documento, nome, idade, fumante, cnpj):
        self.cnpj = cnpj

        super().__init__(documento, nome, idade, fumante)

    def descricao(self):
        return super().descricao() + f" de número {self.cnpj}."

PJ = PessoaFisica('cnpj', 'Lais', '29', 'N', '12.456.789/0001-00')
print(PJ.descricao())