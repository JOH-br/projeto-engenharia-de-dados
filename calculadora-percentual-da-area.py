# 1° - Enunciado: O plano diretor de desenvolvimento urbano de uma cidade determina qual é o percentual máximo de área destinado para garagem em relação à área total do terreno da casa, dependendo da localização desse terreno na cidade. Uma empresa de arquitetura está com vários contratos e necessita calcular rapidamente esse percentual, antes de iniciar os projetos. Faça um programa que recebe as medidas do terreno e da garagem e calcula o percentual de ocupação da área da garagem em relação ao terreno.

# 2° - Primeiro precisamos receber e calcular a area da garagem, pedindo que o usuario insira a largura e a profundidade da garegem; Segundo precisamos e receber e calcular a area do terreno, pedindo que o usurario insira a largura e a profundidade do terreno; Terceiro inviaremos o resultado do calculo do percentual oculpado da garegem dentro do terreno.

AreaGaragem = 
 float(input("Insira a largura da garagem, em metros: "))*
 float(input("Insira a profundidade da garagem, em metros: "))

AreaTerreno = 
 float(input("Insira a largura do terreno, em metros: "))*
 float(input("Insira a profundidade do terreno, em metros: "))

print("A area percentual da ocupação  da garegem em relação ao terreno é: "+
      str(100*AreaGaragem/AreaTerreno)+"%")
