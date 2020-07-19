objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0
contador=0

while abs(respuesta**2 - objetivo)> epsilon and respuesta <= objetivo:
    respuesta += paso
    contador +=1

if abs(respuesta**2-objetivo)>= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    print(f'Se requirieron {contador} iteraciones')