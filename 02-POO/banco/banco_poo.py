from os import system

class Usuario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def criar_conta(self, agencia, numero_conta):
        conta = ContaBancaria(agencia, numero_conta, self)
        self.contas.append(conta)
        return conta

class ContaBancaria:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0

    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0.0
        self.transacoes = []
        self.saques_realizados = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(('Depósito', valor))
            return True
        return False

    def sacar(self, valor):
        if valor <= 0:
            return False
        if self.saques_realizados >= self.LIMITE_SAQUES:
            print(f"Limite diário de {self.LIMITE_SAQUES} saques atingido.")
            return False
        if valor > self.LIMITE_VALOR_SAQUE:
            print(f"O valor máximo de saque é R$ {self.LIMITE_VALOR_SAQUE:.2f}")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.transacoes.append(('Saque', valor))
        self.saques_realizados += 1
        return True

    def extrato(self):
        print("Extrato:")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for tipo, valor in self.transacoes:
                sinal = '-' if tipo == 'Saque' else '+'
                print(f"{tipo}: {sinal}R$ {valor:,.2f}")
        print(f"Saldo atual: R$ {self.saldo:,.2f}")

def limpar_terminal():
    system("cls||clear")

def checar_numero(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            return valor if valor >= 0 else -1
        except:
            return -1

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def selecionar_usuario(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return None
    print("Usuários cadastrados:")
    for i, usuario in enumerate(usuarios, 1):
        print(f"[{i}] {usuario.nome} - CPF: {usuario.cpf}")
    idx = input("Selecione o número do usuário: ").strip()
    if idx.isdigit() and 1 <= int(idx) <= len(usuarios):
        return usuarios[int(idx)-1]
    print("Usuário inválido.")
    return None

def listar_contas_usuario(usuario):
    if not usuario.contas:
        print("Nenhuma conta para este usuário.")
        return []
    for conta in usuario.contas:
        print(f"Agência: {conta.agencia} | Conta: {conta.numero_conta}")
    return usuario.contas

def selecionar_conta_usuario(usuario):
    contas = listar_contas_usuario(usuario)
    if not contas:
        return None
    numero = input("Digite o número da conta que deseja acessar: ").strip()
    for conta in contas:
        if str(conta.numero_conta) == numero:
            print(f"Conta {numero} selecionada.")
            return conta
    print("Conta não encontrada.")
    return None

def menu_conta(conta):
    while True:
        print(f"""
--- Conta {conta.numero_conta} | Agência {conta.agencia} ---
[1] Depositar
[2] Sacar
[3] Ver extrato
[4] Voltar para o menu do usuário
        """)
        print(f"\nSaldo: {'R$':>9}{conta.saldo:,.2f}")
        opcao = input("Selecione uma opção: ").strip()
        limpar_terminal()
        if opcao == "1":
            valor = checar_numero("Valor do depósito: R$ ")
            if valor > 0:
                conta.depositar(valor)
                print("Depósito realizado!")
            else:
                print("Valor inválido!")
        elif opcao == "2":
            valor = checar_numero("Valor do saque: R$ ")
            if conta.sacar(valor):
                print("Saque realizado!")
            else:
                print("Falha ao sacar!")
        elif opcao == "3":
            conta.extrato()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 1
    running = True

    while running:
        print(f"""
{" Banco ".center(30, "-")}
[1] Selecionar usuário
[2] Cadastrar usuário
[3] Sair
        """)
        opcao = input("Selecione uma opção: ").strip()
        limpar_terminal()
        if opcao == "1":
            usuario = selecionar_usuario(usuarios)
            if not usuario:
                continue
            while True:
                print(f"""
--- Usuário: {usuario.nome} ---
[1] Criar conta
[2] Selecionar conta
[3] Voltar para o menu principal
                """)
                op_u = input("Selecione uma opção: ").strip()
                limpar_terminal()
                if op_u == "1":
                    conta = usuario.criar_conta(AGENCIA, numero_conta)
                    contas.append(conta)
                    print(f"Conta criada! Agência: {AGENCIA} Conta: {numero_conta}")
                    numero_conta += 1
                elif op_u == "2":
                    conta = selecionar_conta_usuario(usuario)
                    if conta:
                        menu_conta(conta)
                elif op_u == "3":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "2":
            cpf = input("Informe o CPF (somente números): ").strip()
            cpf = "".join(filter(str.isdigit, cpf))
            if filtrar_usuario(cpf, usuarios):
                print("Já existe usuário com esse CPF!")
                continue
            nome = input("Informe o nome completo: ").strip()
            nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
            endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ").strip()
            usuarios.append(Usuario(nome, nascimento, cpf, endereco))
            print("Usuário cadastrado com sucesso!")
        elif opcao == "3":
            running = False
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()