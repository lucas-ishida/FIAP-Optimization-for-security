#Hospital
#Corona Virus
#Nome; Idade 15 < or > 60; Tem risco? (Prioritario); 
#segue na fila

nome = input("Qual seu nome?: ")
idade = int(input("Qual sua idade?"))
risco = input("Eh grupo de risco? (SIM ou NAO)")
risco_pad = risco.upper
if idade < 15 or idade > 60:
    print ("Realizar Exame Imediatamente")
elif risco_pad == "SIM":
    print ("Realizar Exame Imediatamente")
else:
    print ("Segue na Fila")
