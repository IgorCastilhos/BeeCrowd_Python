nome = str(input())
salario = float(input())
vendas = float(input())
comissao = 0.15 * vendas
salariofinal = salario + comissao

print("TOTAL = R$ %.2f"%salariofinal);