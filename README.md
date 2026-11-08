# Sistema de Gestión de Estudiantes (SGE) básico

Aplicación por consola en Python para el curso **Algoritmos y Programación** (UCompensar).

## Funcionalidades
1. Agregar estudiantes (ID, nombre, edad, carrera y nota), con validación de cada dato.
2. Mostrar la lista completa, con total, sumatoria y promedio de notas, y los últimos registros.
3. Buscar un estudiante por ID.
4. Salir del sistema.

## Requisitos
- Python **3.10 o superior** (el programa usa `match-case`).

## Cómo ejecutarlo
```bash
python sge.py
```

## Archivos
- `sge.py`: código fuente del programa.
- `SGE_diagramas.drawio`: diagramas de flujo editables en [diagrams.net](https://app.diagrams.net) (6 páginas).

## Reglas de validación
- ID: entero positivo y sin repetirse.
- Nombre y carrera: no pueden quedar vacíos.
- Edad: entero de 15 años o más.
- Nota: número entre 0.0 y 5.0 (acepta punto o coma decimal). Aprueba con 3.0 o más.

## Autor
Fabian Ricardo Morales Martinez · Fundación Universitaria Compensar
