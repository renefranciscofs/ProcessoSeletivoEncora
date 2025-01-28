def makeChange(n):
    """
    A função abaixo irá calcular todas as formas de representar 'n' centavos
    utilizando um número infinito de 'quarters' (25 centavos), 'dimes' (10 centavos), 'nickels' (5 centavos) e 'pennies' (1 centavo).
    Cada combinação será representada como uma lista ['quarters', 'dimes, ' nickels', 'pennies'].
    Essa função funcionará da seguinte forma:
    - Iterará todas as possibilidade de 'quarters' (de 0 para a maior possível).
    - A partir do número de 'quarters', iterará todas as possibilidades de 'dimes'.
    - Para cada combinação de 'quarters' e 'dimes', iterará a possibilidade do número de 'nickels'.
    - Calculará o restante para ser representado em 'pennies'.
    - Se o restante do valor não for negativo, adicionar a combinação para o set de resultado.
    - Retornará o set com todas as combinações válidas.
    """
    result = set() # Set para armazenar as combinações únicas

    # Iteração de todas as possibilidades de 'quarters'abs
    for quarters in range(n // 25 + 1):
        # Iteração para todas as possibilidade de 'dimes'
        for dimes in range((n - quarters * 25) // 10 + 1):
            # Iteração para todas as possibilidades de 'nickels'
            for nickels in range((n- quarters * 25 - dimes * 10) // 5 + 1):
                # Calcular o valor remanescente a ser representado por 'pennies'
                pennies = n - (quarters * 25 + dimes * 10 + nickels * 5)
                # Verificando se o valor remanescente não é negativo
                if pennies >= 0:
                    # Adicionando a combinação ao set de resultado como uma tupla
                    result.add((quarters, dimes, nickels, pennies))

    return [list(combination) for combination in result]
