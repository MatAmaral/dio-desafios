from os import system

def limpar_terminal():
    system("cls||clear")

def checar_numero():
    num = input()
    try:
        return float(num)
    except:
        return 0.00

def mostrar_saldo(saldo):
    print(f"\nSaldo: {'R$':>9}{saldo:,.2f}")

def deposito(conta):
    saldo = conta["saldo"]
    transacoes = conta["transacoes"]
    while True:
        print("Digite o valor a ser depositado (digite 0 para sair): R$", end="")
        valor = checar_numero()
        if valor < 0:
            print("Valor inválido. Tente novamente.")
            continue
        elif valor == 0:
            return
        else:
            break
    saldo += valor
    transacoes.append(valor)
    conta["saldo"] = saldo

def saque(conta):
    saldo = conta["saldo"]
    transacoes = conta["transacoes"]
    saques = conta["saques"]
    MAX_VALOR_SAQUE = 500.00
    MAX_SAQUES_DIARIOS = 3
    while True:
        print("Digite o valor a ser sacado (digite 0 para sair): R$", end="")
        valor = checar_numero()
        if valor < 0:
            print("Valor inválido. Tente novamente.")
        elif valor == 0:
            return
        elif saques >= MAX_SAQUES_DIARIOS:
            print(f"Foi atingido o máximo número de saques diários de {MAX_SAQUES_DIARIOS} saques.\nTente novamente amanhã.")
            return
        elif valor > MAX_VALOR_SAQUE:
            print(f"O valor máximo de saque é de {MAX_VALOR_SAQUE}")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            break
    saldo -= valor
    transacoes.append(valor * (-1))
    conta["saldo"] = saldo
    conta["saques"] += 1

def extrato(conta):
    saldo = conta["saldo"]
    transacoes = conta["transacoes"]
    for transacao in transacoes:
        if transacao > 0:
            print(f"Depósito: {'R$':>6}{transacao:,.2f}")
        else:
            print(f"Saque: {'R$':>9}{-transacao:,.2f}")
    mostrar_saldo(saldo)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    cpf = "".join(filter(str.isdigit, cpf))
    if filtrar_usuario(cpf, usuarios):
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ").strip()
    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(agencia, numero_conta, usuario, contas):
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "transacoes": [],
        "saques": 0
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia} Conta: {numero_conta}")

def listar_contas_usuario(usuario, contas):
    contas_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == usuario["cpf"]]
    for conta in contas_usuario:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']}")
    return contas_usuario

def selecionar_usuario(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return None
    print("Usuários cadastrados:")
    for i, usuario in enumerate(usuarios, 1):
        print(f"[{i}] {usuario['nome']} - CPF: {usuario['cpf']}")
    idx = input("Selecione o número do usuário: ").strip()
    if idx.isdigit() and 1 <= int(idx) <= len(usuarios):
        return usuarios[int(idx)-1]
    print("Usuário inválido.")
    return None

def selecionar_conta_usuario(usuario, contas):
    contas_usuario = listar_contas_usuario(usuario, contas)
    if not contas_usuario:
        print("Nenhuma conta para este usuário.")
        return None
    numero = input("Digite o número da conta que deseja acessar: ").strip()
    for conta in contas_usuario:
        if str(conta["numero_conta"]) == numero:
            print(f"Conta {numero} selecionada.")
            return conta
    print("Conta não encontrada.")
    return None

def menu_conta(conta):
    while True:
        print(f"""
--- Conta {conta['numero_conta']} | Agência {conta['agencia']} ---
[1] Depositar
[2] Sacar
[3] Ver extrato
[4] Voltar para o menu do usuário
        """)
        mostrar_saldo(conta["saldo"])
        opcao = input("Selecione uma opção: ").strip()
        limpar_terminal()
        if opcao == "1":
            deposito(conta)
        elif opcao == "2":
            saque(conta)
        elif opcao == "3":
            extrato(conta)
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
--- Usuário: {usuario['nome']} ---
[1] Criar conta
[2] Selecionar conta
[3] Voltar para o menu principal
                """)
                op_u = input("Selecione uma opção: ").strip()
                limpar_terminal()
                if op_u == "1":
                    cadastrar_conta(AGENCIA, numero_conta, usuario, contas)
                    numero_conta += 1
                elif op_u == "2":
                    conta = selecionar_conta_usuario(usuario, contas)
                    if conta:
                        menu_conta(conta)
                elif op_u == "3":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "2":
            cadastrar_usuario(usuarios)
        elif opcao == "3":
            running = False
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()