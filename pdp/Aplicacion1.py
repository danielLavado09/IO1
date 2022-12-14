from stochasticdp import StochasticDP

# Número de etapas
number_of_stages = 4

# Lista de estados
states = [0, 1]

# Lista de decisiones
decisions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Inicializar programa
dp = StochasticDP(number_of_stages, states, decisions, minimize=True)

# Probabilidades de transición y contribuciones del estado n = 0
for t in range(number_of_stages - 1):
    for x in decisions:
        dp.probability[1, 0, t, x] = 0
        dp.contribution[1, 0, t, x] = 0
        dp.probability[0, 0, t, x] = 1
        dp.contribution[0, 0, t, x] = 0

# Probabilidades de transición y contribuciones del estado n = 1
for t in range(number_of_stages - 1):
    for x in decisions:
        if x > 0:
            K = 5
        else:
            K = 0
        dp.probability[0, 1, t, x] = 1 - (1/2)**x
        dp.contribution[0, 1, t, x] = K + x
        dp.probability[1, 1, t, x] = (1/2)**x
        dp.contribution[1, 1, t, x] = K + x

# Condiciones iniciales
dp.boundary[0] = 0
dp.boundary[1] = 64

# Resolver 
value, policy = dp.solve()
print(value)