# Dada a lista temperaturas = [22, 19, 25, 30, 18, 27], use list comprehension para criar temperaturas_altas, contendo apenas as temperaturas maiores que 24.

temperaturas = [22, 19, 25, 30, 18, 27]

temperaturas_altas = [t for t in temperaturas if t > 24]

print(temperaturas_altas)