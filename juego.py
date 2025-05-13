import random
import sys

historial_usuario = []

def validar_entradas(opciones_humano):
    opciones_validas = ['piedra', 'papel', 'tijera']
    if len(opciones_humano) != 3:
        print('Debe de ingresar exactamente tres opciones: ')
    for opcion in opciones_humano:
        if opcion not in opciones_validas:
            print(f'La opcion no es invalida: {opcion}')

def comparar_resultado(opcion_humano, opcion_maquina):
    if opcion_humano == opcion_maquina:
        return 0
    elif (opcion_humano == 'piedra' and opcion_maquina == 'tijera') or \
         (opcion_humano == 'tijera' and opcion_maquina == 'papel') or \
         (opcion_humano == 'papel' and opcion_maquina == 'piedra'):
        return 1
    else:
        return -1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    opciones_humano = [opcion.lower().strip() for opcion in sys.argv[1:4]]
    try:
        validar_entradas(opciones_humano)
    except ValueError as e:
        print(f'ERROR: {e}')
        sys.exit(1)

    historial_usuario.extend(opciones_humano)

    opciones = ['piedra', 'papel', 'tijera']
    opciones_maquina = [random.choice(opciones) for _ in range(3)]

    puntos_humano = 0
    puntos_maquina = 0
    for i in range(3):
        resultado = comparar_resultado(opciones_humano[i], opciones_maquina[i])
        if resultado == 1:
            puntos_humano += 1
        elif resultado == -1:
            puntos_maquina += 1

    print('El programa eligió:', opciones_maquina)
    print('Historial del usuario:', historial_usuario)
    print('Punteo:', puntos_humano, '--', puntos_maquina)

    if puntos_humano > puntos_maquina:
        print('GANADOR: Humano')
    elif puntos_maquina > puntos_humano:
        print('GANADOR: Programa')
    else:
        print('RESULTADO: Empate')
