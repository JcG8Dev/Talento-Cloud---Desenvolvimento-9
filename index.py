# Algoritimo para imprimir o número de andares de um prédio exceto o número 13

# Utilizando for para imprimir em ordem crescente
for andar in range(1, 21):
    if andar != 13:
        print(andar)

# Utilizando for para imprimir em ordem decrescente
for andar in range(20, 0, -1):
    if andar != 13:
        print(andar)

# Utilizando while para imprimir em ordem crescente
andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1

# Utilizando while para imprimir em ordem decrescente
andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1
