import csv

def cargar_datos_csv(ruta_archivo):
    """
    Carga los datos de países desde un archivo CSV.
    Convierte los datos a los tipos correctos (listas de diccionarios)[cite: 13, 19].
    Realiza validaciones de formato[cite: 67].
    """
    paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as file:
            # Lee el CSV como una lista de diccionarios [cite: 13, 19]
            lector_csv = csv.DictReader(file)
            
            linea = 1
            for fila in lector_csv:
                linea += 1
                try:
                    # Validación de tipos de datos
                    pais = {
                        "nombre": fila['nombre'].strip(),
                        "poblacion": int(fila['poblacion']),
                        "superficie": int(fila['superficie']),
                        "continente": fila['continente'].strip()
                    }
                    
                    # Validación de contenido
                    if not pais["nombre"] or not pais["continente"] or pais["poblacion"] < 0 or pais["superficie"] < 0:
                        print(f"Advertencia (Línea {linea}): Registro con datos inválidos omitido: {fila}")
                        continue
                        
                    paises.append(pais)
                    
                except ValueError:
                    # Control de errores de formato en CSV [cite: 67]
                    print(f"Error de formato (Línea {linea}): 'poblacion' o 'superficie' no son numéricos. Fila omitida.")
                except KeyError:
                    print(f"Error (Línea {linea}): Faltan columnas esperadas. Fila omitida.")

        if paises:
            print(f"--- Se cargaron {len(paises)} países exitosamente ---")
        else:
            print("--- No se cargaron datos. El archivo podría estar vacío o tener formato incorrecto ---")
            
        return paises

    except FileNotFoundError:
        print(f"Error Crítico: No se encontró el archivo en la ruta: {ruta_archivo}")
        return []
    except Exception as e:
        print(f"Error Crítico inesperado al leer el archivo: {e}")
        return []

def mostrar_paises(lista_paises):
    """
    Imprime una lista de países en un formato legible.
    """
    if not lista_paises:
        print("No se encontraron países que coincidan con los criterios.")
        return

    print("\n--- Resultados ---")
    print(f"{'Nombre':<30} | {'Continente':<15} | {'Población':>15} | {'Superficie (km²)':>18}")
    print("-" * 81)
    
    for pais in lista_paises:
        # Formateo para alinear números a la derecha y texto a la izquierda
        print(f"{pais['nombre']:<30} | {pais['continente']:<15} | {pais['poblacion']:>15,} | {pais['superficie']:>18,}")
    print(f"\nTotal de países mostrados: {len(lista_paises)}")

def obtener_opcion_menu():
    """
    Solicita al usuario una opción del menú y valida que sea un número.
    """
    while True:
        opcion = input("\nIngrese una opción (1-6): ")
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            return int(opcion)
        else:
            print("Error: Opción no válida. Intente nuevamente.") # [cite: 69]

def obtener_texto(mensaje):
    """
    Solicita un texto no vacío al usuario.
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("Error: La entrada no puede estar vacía.") # [cite: 68]

def obtener_rango_numerico(tipo):
    """
    Solicita un rango (mínimo y máximo) para población o superficie.
    """
    while True:
        try:
            min_val = int(input(f"Ingrese {tipo} mínima (0 para omitir): "))
            max_val = int(input(f"Ingrese {tipo} máxima (0 para omitir): "))
            
            if min_val < 0 or max_val < 0:
                print("Error: Los valores no pueden ser negativos.")
                continue

            # Si el máximo es 0, lo tratamos como "sin límite"
            if max_val == 0:
                max_val = float('inf') # Infinito

            if min_val > max_val:
                print("Error: El valor mínimo no puede ser mayor que el máximo.")
                continue
                
            return min_val, max_val
        except ValueError:
            print("Error: Debe ingresar un número válido.") # [cite: 68]