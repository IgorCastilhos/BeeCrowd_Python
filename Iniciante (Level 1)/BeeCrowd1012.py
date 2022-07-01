A, B, C = map(float, input().split())

r1 = (A * C) / 2
r2 = C**2 * 3.14159
r3 = ((A + B) * C) / 2
r4 = B**2
r5 = A * B

print("TRIANGULO: {:.3f}".format(r1))
print("CIRCULO: {:.3F}".format(r2))
print("TRAPEZIO: {:.3F}".format(r3))
print("QUADRADO: {:.3F}".format(r4))
print("RETANGULO: {:.3F}".format(r5))