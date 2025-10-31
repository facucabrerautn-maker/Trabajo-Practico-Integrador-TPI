def buscar_por_nombre(paises, nombre):
    """
    Busca países por nombre (coincidencia parcial o exacta).
    """
    nombre_buscado = nombre.lower()
    resultados = []
    for pais in paises:
        if nombre_buscado in pais['nombre'].lower():
            resultados.append(pais)
    return resultados

def filtrar_por_continente(paises, continente):
    """
    Filtra la lista de países por un continente específico[cite: 52].
    """
    continente_buscado = continente.lower()
    resultados = [
        pais for pais in paises 
        if pais['continente'].lower() == continente_buscado
    ]
    return resultados

def filtrar_por_rango_poblacion(paises, min_pob, max_pob):
    """
    Filtra la lista de países por un rango de población[cite: 53].
    """
    resultados = [
        pais for pais in paises 
        if min_pob <= pais['poblacion'] <= max_pob
    ]
    return resultados

def filtrar_por_rango_superficie(paises, min_sup, max_sup):
    """
    Filtra la lista de países por un rango de superficie[cite: 54].
    """
    resultados = [
        pais for pais in paises 
        if min_sup <= pais['superficie'] <= max_sup
    ]
    return resultados

def ordenar_paises(paises, criterio, descendente=False):
    """
    Ordena la lista de países por nombre, población o superficie [cite: 55-58].
    """
    if criterio not in ['nombre', 'poblacion', 'superficie']:
        print("Error: Criterio de ordenamiento no válido.")
        return paises # Retorna la lista sin ordenar

    # Usamos una función lambda para definir la clave de ordenamiento
    try:
        lista_ordenada = sorted(paises, key=lambda x: x[criterio], reverse=descendente)
        return lista_ordenada
    except TypeError:
        print(f"Error al ordenar por {criterio}. Verifique los tipos de datos.")
        return paises

def calcular_estadisticas(paises):
    """
    Calcula y muestra las estadísticas solicitadas.
    """
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    # 1. País con mayor y menor población [cite: 61]
    pais_max_pob = max(paises, key=lambda x: x['poblacion'])
    pais_min_pob = min(paises, key=lambda x: x['poblacion'])

    # 2. Promedio de población y superficie [cite: 62, 63]
    total_poblacion = sum(p['poblacion'] for p in paises)
    total_superficie = sum(p['superficie'] for p in paises)
    num_paises = len(paises)
    
    promedio_poblacion = total_poblacion / num_paises
    promedio_superficie = total_superficie / num_paises

    # 3. Cantidad de países por continente [cite: 65]
    conteo_continentes = {} # Usamos un diccionario [cite: 13]
    for pais in paises:
        continente = pais['continente']
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    # Impresión de resultados
    print("\n--- Estadísticas Globales ---")
    print(f"País con Mayor Población: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:,})")
    print(f"País con Menor Población: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:,})")
    print("-" * 30)
    print(f"Promedio de Población:   {promedio_poblacion:,.2f} habitantes")
    print(f"Promedio de Superficie:  {promedio_superficie:,.2f} km²")
    print("-" * 30)
    print("Cantidad de países por Continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad} país(es)")