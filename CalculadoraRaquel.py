# calculadora Pyhton

print("\n***********Calculadora Raquel*************")

def add(x, y):
    return x + y

def add(x, y):
    return x - y

def add(x, y):
    return x * y

def add(x, y):
    return x * y

def add(x, y):
    return x / y

print("/Selecione o número para a operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\nDigite sua opção (1/2/3/4): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")
    
elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")
    
elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")
    
else:
    print("\nOpção inválida!")
    
    
       
        