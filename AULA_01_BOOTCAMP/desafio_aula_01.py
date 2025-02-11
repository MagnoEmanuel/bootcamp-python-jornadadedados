#Variáveis
from numpy.lib.user_array import container

nome_usuario = (input("Digite o seu nome: "))

salario_usuario = float(input("Digite o seu salário: R$ "))

bonus_usuario = float(input("Digite o seu multiplicador de bônus: "))

constante_bonus = 1000

#Cálculo do KPI de Bônus

valor_do_bonus = constante_bonus + salario_usuario * bonus_usuario
formato = "R$ {:,.2f}".format(valor_do_bonus).replace(".", "X").replace(",", ".").replace("X", ",")

#Quanto, em porcentagem, recebeu de bônus

porcentagem_bonus = round((salario_usuario / valor_do_bonus) * 100)

#Código

print(f"""Bônus recebido por {nome_usuario} é de: {formato}
Percentual de bônus foi de: {porcentagem_bonus}%
""")