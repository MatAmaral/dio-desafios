# codigo_a_ser_testado/calculadora.py

def calcular(operacao, a, b):
    """
    Executa uma operação matemática simples.

    Args:
        operacao (str): A operação a ser realizada ('soma', 'subtracao', 'multiplicacao', 'divisao').
        a (int or float): O primeiro número.
        b (int or float): O segundo número.

    Returns:
        int or float: O resultado da operação.

    Raises:
        ValueError: Se a operação for inválida.
        TypeError: Se as entradas não forem números.
        ZeroDivisionError: Se houver tentativa de divisão por zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Entradas 'a' e 'b' devem ser numéricas.")

    if operacao == 'soma':
        return a + b
    elif operacao == 'subtracao':
        return a - b
    elif operacao == 'multiplicacao':
        return a * b
    elif operacao == 'divisao':
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return a / b
    else:
        raise ValueError(f"Operação '{operacao}' desconhecida.")