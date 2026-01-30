# 1° - Enunciado: Um matematico precisa saber quantos numeros primos existem dentro uma certa quantidade de numeros. O matematico sem saber linguagem de programação e tendo pesquisado sobre python, pede para que ajude com essa tarefa.

# 2° - Utilizando Python, deve ser criado uma janela para input da distancia de numeros que se quer verificar a quantidade de primos dentro. Lembrando que os numeros primos são todos que só podem ser divididos por si proprios e 1.

rangeNum = int(input("Insira até qual numero natural deseja verificar a quantidade de numeros primos:"))

quantNum = 1
quantNumPri = 0
numPri = []

for num in range(2, rangeNum + 1):
    quantNum += 1
    numDiv = 2
    
    for rangeTest in range(2, num + 1):
        if ((num+1)/2) <= rangeTest: break
        if numDiv >= 3: break
        if (num % rangeTest) == 0: numDiv += 1
            
    if numDiv == 2:
        quantNumPri += 1
        numPri.append(num)

print(f"Há {quantNumPri} número(s) primo(s) dentro de {quantNum} primeiro(s) número(s) natural(is). E são: {numPri}.")
