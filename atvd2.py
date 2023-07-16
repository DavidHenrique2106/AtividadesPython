salario=int(float(input("Digite seu salário -> ")))

aumento1 = salario + (salario*20)/100
aumento2 = salario + (salario*15)/100
aumento3 = salario + (salario*10)/100
aumento4 = salario + (salario*5)/100

if salario<=280:
    print(f"Seu salário aumentou 20% -> Seu salário era {salario} e agora é {aumento1}")

elif salario>281 == salario<700:
    print(f"Seu salário aumentou 15% -> Seu salário era {salario} e agora é {aumento2}")

elif salario>701 == salario<1500:
    print(f"Seu salário aumentou 10% -> Seu salário era de {salario} e agora é {aumento3}")

elif salario>=1501:
    print(f"Seu salário aumentou 5% -> Seu salário era de {salario} e agora é de {aumento4}")


