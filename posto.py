gasolina =4.02
etanol = 3.24

combustivel = input("Digite G para gasolina ou E para Etanol -> ")
litros = int(float(input("Digite quantos litros você abasteceu -> " )))

if combustivel == 'g' and litros <20:
    print(f"Valor original -> {litros * gasolina} \n")
    print(f"Valor do desconto -> {litros * gasolina * 3 / 100} \n")
    print(f"Valor final -> {litros * gasolina - litros * gasolina * 3 / 100 } \n")

elif combustivel == 'g' and litros >= 20:
    print(f"Valor original -> {litros * gasolina} \n")
    print(f"Valor do desconto -> {litros * gasolina * 5 / 100} \n")
    print(f"Valor final -> {litros * gasolina - litros * gasolina * 5 / 100 } \n")

elif combustivel == 'e' and litros < 20:
    print(f"Valor original -> {litros * etanol} \n")
    print(f"Valor do desconto -> {litros * etanol * 4 / 100} \n")
    print(f"Valor final -> {litros * etanol - litros * etanol * 4 / 100 } \n")

elif combustivel == 'e' and litros >= 20:
    print(f"Valor original -> {litros * etanol} \n")
    print(f"Valor do desconto -> {litros * etanol * 6 / 100} \n")
    print(f"Valor final -> {litros * etanol - litros * etanol * 6 / 100 } \n")

else:
    print("Combustível inválido!!!!")

