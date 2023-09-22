produto = input("Digite o nome do produto -> ")
quantidade = int(input("Digite a quantidade que você pegou -> "))
preço_unitário = int(input("Digite o valor do produto que você pegou -> "))
total = (quantidade * preço_unitário)

desconto1 = (total - total * 0.02)
desconto2 = (total - total * 0.03)
desconto3 = (total - total * 0.05)

if quantidade <= 5:
    print(f"Valor total -> {total}")
    print(f"Desconto de 2%")
    print(f"Valor final -> {desconto1}")

elif quantidade > 5 and quantidade <=10:
    print(f"Valor total -> {total}")
    print(f"Desconto de 3%")
    print(f"Valor final -> {desconto2}")
 
if quantidade > 10:
    print(f"Valor total -> {total}")
    print(f"Desconto de 5%")
    print(f"Valor final -> {desconto3}")