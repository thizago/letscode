p0 = float(input('Entre com a posição inicial: '))
v0 = float(input('Entre com a velocidade inicial do Projetil: '))
t = float(input('Entre com o instante de tempo :'))
g = 9.797645
pt = (p0 + (v0 * t) + (g * (t ** 2)) / 2

print('O projétil estará na posição' , pt, 'no instante', t)
