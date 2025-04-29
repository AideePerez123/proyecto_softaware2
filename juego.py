import random

def comparar_resultado(opcion_humano, opcion_maquina):
        if opcion_humano == opcion_maquina:
            resultado = 0
            return resultado
        elif (opcion_humano == 'piedra' and opcion_maquina == 'tijera') or (opcion_humano == 'tijera' and opcion_maquina == 'papel') or (opcion_humano == 'papel' and opcion_maquina == 'piedra'):
            resultado = 1
            return resultado
            
        else:
            resultado = -1
            return resultado

opcion_ingresada = input('Ingrese las opciones (piedra papel tijera ): ').lower().strip()
opciones_humano = opcion_ingresada.split()




opciones = ['piedra', 'papel', 'tijera']
opciones_maquina = []
for i in range(3):
    opcion = random.choice(opciones)
    opciones_maquina.append(opcion)


puntos_humano = 0
puntos_maquina = 0
for i in range(3):
    resultado = comparar_resultado(opciones_humano[i], opciones_maquina[i])
    if resultado == 1:
        puntos_humano = puntos_humano + 1
    elif resultado == -1:
        puntos_maquina = puntos_maquina + 1

print('El programa elige:', opciones_maquina)
    





print('Punteo:', puntos_humano, '--', puntos_maquina)

if puntos_humano > puntos_maquina:
    print('GANADOR: Humano')
elif puntos_maquina > puntos_humano:
    print('GANADOR: Programa')
else:
    print('RESULTADO: Empate')