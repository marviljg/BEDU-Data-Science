sueldo = float(input("¿Sueldo del empleado?: "))
ventas_anuales_totales = float(
    input("¿Total de ventas anuales del empleado?: "))
bono = 0

if ventas_anuales_totales > 1000000:
    bono = 0.2
elif ventas_anuales_totales > 700000:
    bono = 0.15
elif ventas_anuales_totales > 400000:
    bono = 0.1
elif ventas_anuales_totales > 100000:
    bono = 0.05
else:
    bono = 0.01

print(
    f"Felicidades, tu sueldo es {sueldo}; tu bono es de {bono}; y el total de sueldo con el bono incluido es de {sueldo+ventas_anuales_totales*bono}")

'''
NOTAS:
* La función input() siempre retornara el valor en forma de string. Debe de convertirse
  al tipo de dato correcto a utilizar
'''
