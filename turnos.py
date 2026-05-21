# Lista donde se almacenan los turnos
turnos = []

# Número inicial del turno
numero_turno = 1

# Función para mostrar el menú
def mostrar_menu():
    print("\n===== SISTEMA DE TURNOS =====")
    print("1. Sacar turno")
    print("2. Llamar siguiente turno")
    print("3. Ver turnos pendientes")
    print("4. Salir")

# Función para registrar un nuevo turno
def sacar_turno():
    global numero_turno

    nombre = input("Ingrese el nombre del estudiante: ").strip()

    # Validación básica
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    # Crear turno
    turno = {
        "numero": numero_turno,
        "nombre": nombre
    }

    # Guardar turno en la lista
    turnos.append(turno)

    print(f"Turno asignado: {numero_turno} - {nombre}")

    numero_turno += 1

# Función para atender el siguiente turno
def llamar_siguiente():
    if len(turnos) == 0:
        print("No hay turnos pendientes.")
        return

    turno_actual = turnos.pop(0)

    print("\nAtendiendo turno:")
    print(f"Turno #{turno_actual['numero']}")
    print(f"Estudiante: {turno_actual['nombre']}")

# Función para mostrar turnos pendientes
def mostrar_turnos():
    if len(turnos) == 0:
        print("No hay turnos pendientes.")
        return

    print("\n===== TURNOS PENDIENTES =====")

    for turno in turnos:
        print(f"#{turno['numero']} - {turno['nombre']}")

# Programa principal
while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        sacar_turno()

    elif opcion == "2":
        llamar_siguiente()

    elif opcion == "3":
        mostrar_turnos()

    elif opcion == "4":
        print("Sistema finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")