n1=int(input("Digite o valor de N1 -> "))
n2=int(input("Digite o valor de N2 -> "))
n3=int(input("Digite o valor de N3 -> "))

if n1 > n2 and n1 > n3 and n2 > n3:
    print("A ordem é -> N1, N2 e N3")

elif n1 > n2 and n1> n3 and n3> n2:
    print("A ordem é -> N1, N3 e N2")

elif n2 > n1 and n2 > n3 and n1 > n3:
    print("A ordem é -> N2,N1 e N3")
    
elif n2 > n1 and n2 > n3 and n3 > n1:
    print("A ordem é -> N2, N3 e N1")

elif n3 > n2 and n3 > n1 and n2 > n1:
    print("A ordem é -> N3, N2 e N1")

elif n3 > n2 and n3 > n1 and n1 > n2:
    print("A ordem é -> N3, N1 e N2")