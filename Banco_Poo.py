import random

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, numero, usuario):
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.saques_totais = 3

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    
    def saque(self, valor):
        if self.saques_totais > 0:
            if valor > 0 and valor <= 500:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saques_totais -= 1
                    print(f"Saque de R${valor:.2f} realizado com sucesso.")
                else:
                    print("Saldo insuficiente para realizar a operação saque.")
            else:
                print("Valor de saque inválido, seu limite é R$ 500,00/dia.")
        else:
            print("Limite diário de saques atingido.")

    def extrato(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

def cadastrar_usuario(usuarios):
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
    cpf = input("Digite o CPF: ")
    endereco = {
        "logradouro": input("Digite o logradouro: "),
        "numero": input("Digite o número: "),
        "bairro": input("Digite o bairro: "),
        "cidade": input("Digite a cidade: "),
        "estado": input("Digite a sigla do estado: ")
    }
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios[cpf] = usuario
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(usuarios, contas):
    cpf = input("Digite o CPF do usuário: ")
    if cpf in usuarios:
        numero_conta = gerar_numero_conta(contas)
        conta = Conta(numero_conta, usuarios[cpf])
        contas[numero_conta] = conta
        print(f"Conta cadastrada com sucesso para o usuário {usuarios[cpf].nome}. Número da conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Cadastre o usuário antes de criar uma conta.")

def gerar_numero_conta(contas):
    numero_conta = random.randint(1000, 9999)
    while numero_conta in contas:
        numero_conta = random.randint(1000, 9999)
    return numero_conta

def verificar_contas_criadas(contas):
    if contas:
        print("Contas criadas:")
        for conta in contas.values():
            print(f"Conta nº: {conta.numero}, CPF do titular: {conta.usuario.cpf}")
    else:
        print("Nenhuma conta criada até o momento.")

def main():
    usuarios = {}
    contas = {}
    
    while True:
        print("\nMenu Principal:")
        print("C - Cadastrar usuário")
        print("A - Cadastrar conta")
        print("D - Depósito")
        print("S - Saque")
        print("E - Extrato")
        print("V - Verificar contas criadas")
        print("Q - Sair")

        operacao = input("Digite a operação desejada: ").upper()

        if operacao == "C":
            cadastrar_usuario(usuarios)
        elif operacao == "A":
            cadastrar_conta(usuarios, contas)
        elif operacao == "D":
            numero_conta = int(input("Digite o número da conta: "))
            if numero_conta in contas:
                valor = float(input("Digite o valor do depósito: "))
                contas[numero_conta].deposito(valor)
            else:
                print("Conta não encontrada.")
        elif operacao == "S":
            numero_conta = int(input("Digite o número da conta: "))
            if numero_conta in contas:
                valor = float(input("Digite o valor do saque: "))
                contas[numero_conta].saque(valor)
            else:
                print("Conta não encontrada.")
        elif operacao == "E":
            numero_conta = int(input("Digite o número da conta: "))
            if numero_conta in contas:
                contas[numero_conta].extrato()
            else:
                print("Conta não encontrada.")
        elif operacao == "V":
            verificar_contas_criadas(contas)
        elif operacao == "Q":
            print("Obrigado por utilizar nossos serviços, o banco agradece ;)")
            break
        else:
            print("Operação inválida.")

if __name__ == "__main__":
    main()
