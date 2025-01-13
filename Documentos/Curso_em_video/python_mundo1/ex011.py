'''
Exercício Python 11: 
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
 a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
 pinta uma área de 2 metros quadrados.
'''


largura = float(input("Digite a largura:"))
altura = float(input("Digite a altura:"))

area = largura * altura

taxa_tinta = 2

quantidade_tinta = area / taxa_tinta

print(f"A área da parede é {area} metros quadrados")
print(f"A quantidade de tinta necessária é {quantidade_tinta} litros")


