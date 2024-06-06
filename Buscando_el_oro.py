
AmountInputs = int(input());

PrincipioBolsa = []
FinalBolsa = []

material = "";

for i in range(AmountInputs):
    material = input()

    if(material.lower() == 'oro'):
        FinalBolsa.append(material)
    else:
        PrincipioBolsa.append(material)

Bolsa = PrincipioBolsa + FinalBolsa

for objetos in Bolsa:
    print(objetos)
