'''
Crie um programa que pergunte a idade do usuário
e em seguida informe se este usuário é menor de
idade ou maior de idade.
'''

idade = int(input("Informe a sua idade:"))

#lógica do op ternário: ( se for falso, se for verdadeiro )[teste condicional]
#resultado = ("menor de idade", "maior de idade")[idade >= 18]

resultado = "maior de idade" if idade >= 18 else "menor de idade"
print("Você é ", resultado)