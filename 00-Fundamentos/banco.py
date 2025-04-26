from os import system


def deposito(saldo: float, transacoes: list) -> float:
    
    # Checagem da variável valor
    while True:
        print("Digite o valor a ser depositado (digite 0 para sair): R$", end="")
        
        valor = checarNumero()
        
        if valor < 0:
            print("Valor inválido. Tente novamente.")
            continue
        
        elif valor == 0:
            return saldo
        
        else:
            break

    saldo += valor
    transacoes.append(valor)
    
    return saldo
    

def saque(saldo: float, transacoes: list, saques: int) -> float:    
    MAX_VALOR_SAQUE = 500.00
    MAX_SAQUES_DIARIOS = 3
    
    # Checagem da variável valor
    while True:        
        print("Digite o valor a ser sacado (digite 0 para sair): R$", end="")
        
        valor = checarNumero()
        
        if valor < 0:
            print("Valor inválido. Tente novamente.")
            
        elif valor == 0:
            return saldo
        
        elif saques >= MAX_SAQUES_DIARIOS:
            print(f"Foi atingido o máximo número de saques diários de {MAX_SAQUES_DIARIOS} saques.\nTente novamente amanhã.")
            return saldo
        
        elif valor > MAX_VALOR_SAQUE:
            print(f"O valor máximo de saque é de {MAX_VALOR_SAQUE}")
            
        elif valor > saldo:
            print("Saldo insuficiente.")
            
        else:
            break
    
    saldo -= valor
    transacoes.append(valor * (-1))
    
    return saldo
    

def extrato(saldo: float, transacoes: list) -> None:
    for transacao in transacoes:
        if transacao > 0:
            print(f"Depósito: {"R$":>6}{transacao:,.2f}")
            
        else:
            print(f"Saque: {"R$":>9}{transacao * (-1):,.2f}")
            
    mostrarSaldo(saldo)


def mostrarSaldo(saldo: float) -> None:
    print(f"\nSaldo: {"R$":>9}{saldo:,.2f}")


def checarNumero() -> float:
    num = input()
    
    try:
        return float(num)
    except:
        return 0.00


def limparTerminal() -> None:
    system("cls||clear")


def main():
    saques = 0
    saldo = 0
    running = 1
    transacoes = []
    
    limparTerminal()
    
    while running:        
        print(f"""
{" Banco ".center(20, "-")}\n
[1] Depositar
[2] Sacar
[3] Ver extrato
[4] Sair
        """)
        print("-" * 20)
        
        mostrarSaldo(saldo)
        
        print("Selecione uma opção: ", end="")
        
        opcao = checarNumero()
        
        limparTerminal()
        
        mostrarSaldo(saldo)
        
        match opcao:
            case 1:
                saldo = deposito(saldo, transacoes)
            case 2:                
                if saldo <= 0:
                    print("Você não possui dinheiro para sacar.")
                    continue
                saldo_anterior = saldo
                saldo = saque(saldo, transacoes, saques)
                
                if saldo_anterior != saldo:
                    saques += 1
            case 3:
                limparTerminal()
                extrato(saldo, transacoes)
            case 4:
                limparTerminal()
                running = 0
            case _:
                limparTerminal()
                print("Opção inválida. Selecione novamente uma das opções abaixo: ")
            
    
if __name__ == "__main__":
    main()