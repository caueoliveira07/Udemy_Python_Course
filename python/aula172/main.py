"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Cliente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from banco import Banco
import pessoas
import contas
from abc import ABC, abstractmethod


class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo=0):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def depositar(self, valor_para_deposito):
        self.saldo += valor_para_deposito

    def sacar(self, valor_para_saque):
        raise NotImplementedError(
            "Método sacar deve ser implementado nas subclasses.")


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo=0, limite=0):
        super().__init__(agencia, numero_da_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        saldo_total = self.saldo + self.limite
        if valor <= saldo_total:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                self.saldo = 0
                self.limite -= (valor - self.saldo)
            print("Saque de", valor, "realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")


class ContaPoupanca(Conta):
    def sacar(self, valor_para_saque):
        if self.saldo >= valor_para_saque:
            self.saldo -= valor_para_saque
            print(f'Saque de {valor_para_saque} realizado com sucesso.')
        else:
            print('Saldo insuficiente para o saque.')


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def autenticar_cliente(self, cliente, agencia):
        if cliente in self.clientes and cliente.conta.agencia == agencia:
            return True
        else:
            return False

    def autenticar_conta(self, conta, agencia):
        if conta in self.contas and conta.agencia == agencia:
            return True
        else:
            return False


banco = Banco()

conta1 = ContaPoupanca(agencia="1234", numero_da_conta="0001")
conta1.depositar(1000)

conta2 = ContaCorrente(agencia="1234", numero_da_conta="0002", limite=500)
conta2.depositar(2000)

cliente1 = Cliente(nome="João", idade=30, conta=conta1)
cliente2 = Cliente(nome="Maria", idade=25, conta=conta2)

banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

agencia_autenticacao = "1234"

if banco.autenticar_cliente(cliente1, agencia_autenticacao):
    cliente1.conta.sacar(500)
else:
    print("Cliente não autenticado.")

if banco.autenticar_conta(conta2, agencia_autenticacao):
    conta2.sacar(3000)
else:
    print("Conta não autenticada.")


# Resolução do professor

# c1 = pessoas.Cliente('Luiz', 30)
# cc1 = contas.ContaCorrente(111, 222, 0, 0)
# c1.conta = cc1
# c2 = pessoas.Cliente('Maria', 18)
# cp1 = contas.ContaPoupanca(112, 223, 100)
# c2.conta = cp1
# banco = Banco()
# banco.clientes.extend([c1, c2])
# banco.contas.extend([cc1, cp1])
# banco.agencias.extend([111, 222])

# if banco.autenticar(c1, cc1):
#     cc1.depositar(10)
#     c1.conta.depositar(100)
#     print(c1.conta)
