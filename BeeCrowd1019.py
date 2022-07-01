# Ler um valor inteiro
temp_total = int(input())

# Calcualr horas, minutos e segundos
quantidade_segundos = [3600, 60, 1]
resultado = [ ]

for alvo in quantidade_segundos:
    qtd = int(temp_total / alvo)
    resultado.append(str(qtd))
    temp_total -= qtd * alvo

# Imprimir o resultado
print(":".join(resultado))