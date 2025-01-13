'''
Exercício Python 12:
 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''


preco_produto = float(input("Qual o preço do porduto:"))

desconto = preco_produto * 0.05

novo_preço = preco_produto - desconto

print(f"Preço do produto é {preco_produto}R$ com o desconto fica {novo_preço}R$ ")