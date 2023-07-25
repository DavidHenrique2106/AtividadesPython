op=input("Digite a operação desejada -> (+), (-), (x) ou (/) ->  ")

num1=int(float(input("Digite um valor -> ")))
num2=int(float(input("Digite mais um valor -> ")))

soma = (num1+num2)
subt = (num1-num2)
mult = (num1*num2)
divs = (num1/num2)

if op == "+":
    print(f"Você escolheu a soma! Resultado foi de {soma}")

elif op == "-":
    print(f"Você escolheu a subtração! Resultado foi de {subt}")

elif op == "x":
    print(f"Você escolheu a subtração! Resultado foi de {mult}")

elif op == "/":
    print(f"Você escolheu a subtração! Resultado foi de {divs}")
