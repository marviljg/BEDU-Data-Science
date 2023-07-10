mi_informacion = ["Jose", "pepe", "la pizza", "los chayotes",
                  "dedicarme a la industria tecnologica en un pueblo tranquilo de Cánada"]

# Las triples comillas generan varias lineas de código
print(f'''
¡Hola! Mi nombre es {mi_informacion[0]}. Todos me dicen {mi_informacion[1]}.
Mi comida favorita es {mi_informacion[2]}. Y la comida que más detesto son los {mi_informacion[3]}.
Mi trabajo ideal sería {mi_informacion[4]}.
¡Gracias, chau!
''')

info_0 = ["de los muchos existentes y que quedan por existir"]
info_1 = ["encontrar sentido, proposito y felicidad en sus vidas"]
info_2 = ["podran senirse verdaderamente humanos, podran empezar a ser empáticos con la vida, el mundo y los otros"]
info_3 = ["aceptar que cada uno de nosotros, como individuos, no es nada comparada con la grandeza de lograr un sueño conjunto"]
info_4 = ["trato de esforzarme un poco, mejorar cada día y ayudar a sacar lo mejor de otros en ellos mismos"]

info_faltante = [info_0, info_1, info_2, info_3, info_4]

print(f'''
Algún día los {info_faltante[0]} lograrán su objetivo. Su objetivo de {info_faltante[1]}.
Ese día, los humanos {info_faltante[2]} y tendrán que {info_faltante[3]}.
Por esa razón yo todos los días {info_faltante[4]}.
''')

respuestas = [0.58, 9, 2, 3, 37, 5, 75, 4]

print(f'''
1. Los humanos tenemos {respuestas[2]} ojos en la cara.
2. Un humano adulto tiene {respuestas[4]} dientes dentro de su boca.
3. Un feto tarda {respuestas[1]} meses en gestarse antes de nacer.
4. La expectativa de vida en México es de alrededor de {respuestas[-2]} años.
5. Las horas de sueño al día recomendadas para adultos jóvenes son entre {respuestas[2]+respuestas[-3]} y {respuestas[-7]}.
6. El récord actual de velocidad en 100 metros (09/05/2020) fue establecido por Usain Bolt y es de {respuestas[0]+respuestas[1]}
''')

'''
La diferencia entre () y [] es, que la primera es una tupla (inmutable). La segunda, una lista.
tupla = (algo)
lista = [otra cosa]
podeos acceder a elementos de una lista de fin a principio, con valores negativos, empezando en el indice -1
'''
