# Importamos las funciones de nuestros propios módulos
import utils
import operaciones

def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n" + "=" * 40)
    print("   Gestión de Datos de Países - TPI")
    print("=" * 40)
    print("1. Buscar país por nombre")
    print("2. Filtrar países (por continente, población o superficie)")
    print("3. Ordenar países (por nombre, población o superficie)")
    print("4. Mostrar estadísticas")
    print("5. Recargar datos (Volver a leer el CSV)")
    print("6. Salir")
    print("=" * 40)

def main():
    """
    Función principal del programa.
    """
    # Nombre del archivo CSV base [cite: 97]
    archivo_csv = "paises.csv" 
    
    # Carga inicial de datos
    lista_paises = utils.cargar_datos_csv(archivo_csv)
    
    if not lista_paises:
        print("No se pudo iniciar el programa. Verifique el archivo CSV.")
        return

    while True:
        mostrar_menu()
        opcion = utils.obtener_opcion_menu()

        if opcion == 1:
            # --- Búsqueda por nombre  ---
            nombre = utils.obtener_texto("Ingrese el nombre (parcial o exacto) del país: ")
            resultados = operaciones.buscar_por_nombre(lista_paises, nombre)
            utils.mostrar_paises(resultados)

        elif opcion == 2:
            # --- Menú de Filtros  ---
            print("Seleccione un criterio de filtro:")
            print("  a) Por Continente [cite: 52]")
            print("  b) Por Rango de Población [cite: 53]")
            print("  c) Por Rango de Superficie [cite: 54]")
            sub_opcion = input("Opción (a, b, c): ").lower()

            resultados = []
            if sub_opcion == 'a':
                continente = utils.obtener_texto("Ingrese el nombre del continente: ")
                resultados = operaciones.filtrar_por_continente(lista_paises, continente)
            elif sub_opcion == 'b':
                min_pob, max_pob = utils.obtener_rango_numerico("población")
                resultados = operaciones.filtrar_por_rango_poblacion(lista_paises, min_pob, max_pob)
            elif sub_opcion == 'c':
                min_sup, max_sup = utils.obtener_rango_numerico("superficie")
                resultados = operaciones.filtrar_por_rango_superficie(lista_paises, min_sup, max_sup)
            else:
                print("Error: Opción de filtro no válida.") # [cite: 69]
                
            utils.mostrar_paises(resultados)

        elif opcion == 3:
            # --- Ordenamiento  ---
            print("Seleccione un criterio de ordenamiento:")
            print("  a) Nombre [cite: 56]")
            print("  b) Población [cite: 57]")
            print("  c) Superficie [cite: 58]")
            criterio_op = input("Opción (a, b, c): ").lower()
            
            criterio_str = ""
            if criterio_op == 'a':
                criterio_str = "nombre"
            elif criterio_op == 'b':
                criterio_str = "poblacion"
            elif criterio_op == 'c':
                criterio_str = "superficie"
            else:
                print("Error: Criterio no válido.")
                continue

            orden = input("Orden (asc/desc): ").lower()
            descendente = (orden == 'desc') # [cite: 58]
            
            resultados = operaciones.ordenar_paises(lista_paises, criterio_str, descendente)
            utils.mostrar_paises(resultados)

        elif opcion == 4:
            # --- Estadísticas  ---
            operaciones.calcular_estadisticas(lista_paises)

        elif opcion == 5:
            # --- Recargar datos ---
            print("Recargando datos desde el archivo...")
            lista_paises = utils.cargar_datos_csv(archivo_csv)

        elif opcion == 6:
            # --- Salir ---
            print("Saliendo del programa. ¡Hasta luego!")
            break

# Punto de entrada del programa
if __name__ == "__main__":
    main()