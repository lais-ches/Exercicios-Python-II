# AUTORA: LAÍS RODRIGUES

###
# Crie um professor de classe com atributos nome, idade e salário, onde o salário deve ter um método privado que não pode ser acessado fora da classe.

# a. Crie um método para acessar o método privado, onde é passada a identificação do usuário se ele pode ou não acessar.

class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
      
    def __salario(self):
        return f"O salário é R$ 5000,00"

    def autorizacao(self, nome):
        if nome == 'Lais':
            return self.__salario()

professor1 = Professor('Lais', '29').autorizacao('Lais')
print(professor1)