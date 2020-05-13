import math

valorA = float(input("Entre com os valores de A: "))
valorB = float(input("Entre com os valores de B: "))
valorC = float(input("Entre com os valores de C: "))              

delta = (valorB**2) - 4*(valorA)*(valorC)
raizdelta = math.sqrt(delta)
x1 = (-(valorB)+(raizdelta))/(2*(valorA))
x2 = (-(valorB)-(raizdelta))/(2*(valorA))
x0 = (-(valorB))/(2*(valorA))
               
if delta > 0:
    print("Existem duas raízes reais, são elas")
    print("X1=", float(x1))
    print("X2=", float(x2))

elif delta == 0:
    print("Existe apenas uma raíz real, que é: ")
    print("X=", float(x0))

else:
    print("Não existe raíz real")



               
