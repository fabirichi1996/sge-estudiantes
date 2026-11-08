"""
Sistema de Gestión de Estudiantes (SGE) básico
Aplicación por consola desarrollada para el curso Algoritmos y Programación (UCompensar).

Funcionalidades: agregar estudiantes, mostrarlos, buscarlos por ID y salir.
Requiere Python 3.10 o superior (usa la sentencia match-case).
"""

# ----------------------------------------------------------------------
# Constantes: evitan "números mágicos" y permiten cambiar las reglas
# del sistema en un solo lugar.
# ----------------------------------------------------------------------
EDAD_MINIMA = 15            # la edad debe ser mayor a 14
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_APROBATORIA = 3.0
NOTA_SOBRESALIENTE = 4.5
MAX_ULTIMOS = 3             # cuántos registros recientes se muestran al final de la lista


# ----------------------------------------------------------------------
# Funciones de lectura con validación (patrón "repetir hasta que sea válido")
# ----------------------------------------------------------------------
def leer_entero(mensaje, minimo=None):
    """Pide un número entero y repite la pregunta hasta que sea válido."""
    while True:
        texto = input(mensaje)
        try:
            valor = int(texto)
        except ValueError:
            print("Error: ingrese un número entero.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def leer_texto_no_vacio(mensaje, mensaje_error):
    """Pide un texto y repite la pregunta mientras el usuario deje el campo vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print(mensaje_error)


def leer_nota():
    """Pide una nota entre 0.0 y 5.0. Acepta punto o coma como separador decimal."""
    while True:
        texto = input("Ingrese la nota (0.0 a 5.0): ").strip().replace(",", ".")
        try:
            nota = float(texto)
        except ValueError:
            print("Error: ingrese un valor numérico.")
            continue
        # Se escribe como rango positivo para que también rechace valores como "nan".
        if not (NOTA_MINIMA <= nota <= NOTA_MAXIMA):
            print("Error: la nota debe estar entre 0.0 y 5.0.")
            continue
        return nota


# ----------------------------------------------------------------------
# Funciones de apoyo
# ----------------------------------------------------------------------
def id_ya_registrado(ids, id_nuevo):
    """Devuelve True si el ID ya está en la lista (usa una bandera y un for con break)."""
    id_repetido = False
    for id_existente in ids:
        if id_existente == id_nuevo:
            id_repetido = True
            break  # no hace falta seguir recorriendo la lista
    return id_repetido


def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por ID")
    print("4. Salir")


def mostrar_estudiante(id_est, nombre, edad, carrera, nota):
    """Imprime los datos de un estudiante y su resultado según la nota."""
    print("\nID:", id_est)
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Carrera:", carrera)
    print("Nota:", nota)
    if nota >= NOTA_APROBATORIA:
        if nota >= NOTA_SOBRESALIENTE:      # decisión anidada
            print("Resultado: Aprobó (sobresaliente)")
        else:
            print("Resultado: Aprobó")
    else:
        print("Resultado: Perdió")


# ----------------------------------------------------------------------
# Funcionalidades del menú
# ----------------------------------------------------------------------
def agregar_estudiante(ids, nombres, edades, carreras, notas):
    """Registra un estudiante. Devuelve True si se agregó y False si no."""
    print("\n--- Registro de estudiante ---")
    id_nuevo = leer_entero("Ingrese el ID (número positivo): ", 1)

    if id_ya_registrado(ids, id_nuevo):
        print("El ID del estudiante ya se encuentra en el sistema.")
        return False

    nombre = leer_texto_no_vacio("Ingrese el nombre completo: ",
                                 "El nombre no puede estar vacío.")
    edad = leer_entero(f"Ingrese la edad (mínimo {EDAD_MINIMA} años): ", EDAD_MINIMA)
    carrera = leer_texto_no_vacio("Ingrese la carrera que estudia: ",
                                  "La carrera no puede estar vacía.")
    nota = leer_nota()

    # Las cinco listas son paralelas: la misma posición pertenece al mismo estudiante.
    ids.append(id_nuevo)
    nombres.append(nombre)
    edades.append(edad)
    carreras.append(carrera)
    notas.append(nota)
    return True


def mostrar_estudiantes(ids, nombres, edades, carreras, notas, contador):
    """Muestra todos los estudiantes, la sumatoria y el promedio de las notas."""
    print("\n--- Lista de estudiantes ---")
    if contador == 0:
        print("No hay estudiantes registrados.")
        return

    sumatoria = 0
    for i in range(contador):                      # iteración ascendente
        mostrar_estudiante(ids[i], nombres[i], edades[i], carreras[i], notas[i])
        sumatoria += notas[i]                      # variable acumuladora

    promedio = sumatoria / contador
    print("\nTotal de estudiantes:", contador)
    print(f"Sumatoria de las notas: {sumatoria:.2f}")
    print(f"Promedio de las notas: {promedio:.2f}")

    print("\nÚltimos registros (del más reciente al más antiguo):")
    limite = max(contador - MAX_ULTIMOS, 0)
    for i in range(contador - 1, limite - 1, -1):  # iteración descendente
        print(f"  {ids[i]} - {nombres[i]}")


def buscar_estudiante(ids, nombres, edades, carreras, notas, contador):
    """Busca un estudiante por ID y muestra sus datos si existe."""
    print("\n--- Búsqueda por ID ---")
    id_buscar = leer_entero("Ingrese el ID que desea buscar: ")

    encontrado = False                             # bandera de la búsqueda
    for i in range(contador):
        if ids[i] == id_buscar:
            encontrado = True
            mostrar_estudiante(ids[i], nombres[i], edades[i], carreras[i], notas[i])
            break

    if not encontrado:
        print("ID no encontrado.")


# ----------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------
def main():
    # Estructura de datos: cinco listas paralelas.
    ids = []
    nombres = []
    edades = []
    carreras = []
    notas = []

    contador = 0               # variable de conteo: total de estudiantes
    bandera_salir = False      # bandera que controla el ciclo del menú

    print("===== Sistema de Gestión de Estudiantes (SGE) =====")

    while bandera_salir == False:
        mostrar_menu()

        try:
            opcion = int(input("Elija la opción: "))
        except ValueError:
            print("Error, ingrese una opción válida.")
            continue

        match opcion:
            case 1:
                if agregar_estudiante(ids, nombres, edades, carreras, notas):
                    contador += 1
                    print("\nEstudiante ingresado correctamente.")
                    print("Total de estudiantes ingresados:", contador)
            case 2:
                mostrar_estudiantes(ids, nombres, edades, carreras, notas, contador)
            case 3:
                buscar_estudiante(ids, nombres, edades, carreras, notas, contador)
            case 4:
                bandera_salir = True
                print("Programa finalizado.")
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma interrumpido por el usuario.")
