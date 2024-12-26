def calculadora(divisor,dividendo,operacao):
    if (operacao == 1):
        return divisor + dividendo;
    elif (operacao == 2):
        return divisor - dividendo;
    elif (operacao == 3):
        return divisor * dividendo;
    elif (operacao == 4):
        return dividendo / divisor;

resultado = calculadora(10,20,1);
print(f"O resultado: {resultado}");

resultado = calculadora(10,20,2);
print(f"O resultado: {resultado}");

resultado = calculadora(10,20,3);
print(f"O resultado: {resultado}");

resultado = calculadora(10,20,4);
print(f"O resultado: {resultado}");