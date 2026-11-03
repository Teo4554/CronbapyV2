# ==============================================================================
# CONFIGURACIÓN VISUAL (CÓDIGOS ANSI PARA COLOR EN PYTHON PURO)
# ==============================================================================
# Definimos variables cortas para limpiar el texto y aplicar estilos visuales en la CLI
RESET = "\033[0m"       # Restablece el color por defecto de la terminal
BOLD  = "\033[1m"       # Texto en negrita para resaltar encabezados
CYAN  = "\033[36m"      # Cian para datos del sistema o informativos
GREEN = "\033[32m"      # Verde para procesos exitosos o resultados finales
YELLOW= "\033[33m"      # Amarillo para entradas de datos (inputs)
MAGENTA= "\033[35m"     # Magenta para separadores estéticos o títulos
RED   = "\033[31m"      # Rojo para advertencias o errores de validación

# ==============================================================================
# ENTRADA DE DATOS INICIALES
# ==============================================================================
# Imprime el banner principal con el título de la herramienta usando negrita y cian
print(f"\n{BOLD}{CYAN}======================================================{RESET}")
print(f"{BOLD}{CYAN}     CALCULADORA DE CONSISTENCIA: ALFA DE CRONBACH    {RESET}")
print(f"{BOLD}{CYAN}======================================================{RESET}\n")

# Solicita la muestra asegurando que el input tenga un color amarillo para destacar la acción del usuario
N = int(input(f"{YELLOW}▶ Ingrese la muestra (Número de participantes): {RESET}"))

# Lista de palabras ordinales para guiar de forma humana la entrada de puntajes individuales
orden = ["primer", "segundo", "tercer", "cuarto", "quinto", "sexto", "septimo", "octavo", "noveno", "decimo", "undecimo", "decimo segundo", "decimotercer"] 

# Inicializa las estructuras globales que actuarán como bases de datos en memoria
allresultados = []  # Almacenará las listas de puntajes (Matriz bidimensional)
allvarianzas = []   # Almacenará el flotante de la varianza calculado para cada ítem
K = 0               # Contador incremental para registrar cuántos ítems válidos procesó el usuario

# Solicita confirmación de arranque usando el formato UX de resaltado
opcion = input(f"\n{YELLOW}¿Desea empezar a calcular ítems? (s/n): {RESET}")

# Validación básica inicial en caso de que ingresen caracteres no contemplados
if not "s" in opcion and not "n" in opcion:
    print(f"{RED}⚠ Entrada no reconocida. El programa continuará si detecta una 's'.{RESET}")
        
# ==============================================================================
# BUCLE PRINCIPAL: PROCESAMIENTO DINÁMICO DE ÍTEMS
# ==============================================================================
# El bucle correrá de forma indefinida mientras el usuario confirme con una 's' o 'S'
while opcion.lower() == "s":
    # Incrementa el contador de ítems al iniciar la vuelta para usar el número real actual
    K += 1
    
    # Imprime un encabezado dinámico para denotar en qué sección del cuestionario se encuentra el usuario
    print(f"\n{BOLD}{MAGENTA} ┌────────────────────────────────────────┐{RESET}")
    print(f"{BOLD}{MAGENTA} │            PROCESANDO ÍTEM {K:02d}          │{RESET}")
    print(f"{BOLD}{MAGENTA} └────────────────────────────────────────┘{RESET}\n")
    
    # Lista temporal para capturar los puntajes puros del ítem en la vuelta actual
    resultados = []
    
    # Bucle acotado a la muestra (N) para solicitar ordenadamente la nota de cada participante
    for i in range(N):
        puntaje = int(input(f"  {CYAN}├─►{RESET} Ingrese el {BOLD}{orden[i]}{RESET} puntaje: "))
        resultados.append(puntaje)
        
    # Operación matemática básica para obtener el promedio del ítem actual
    promedio = sum(resultados) / len(resultados)

    # Lista vacía para guardar las diferencias brutas respecto a la media aritmética
    bases = []
    # Itera sobre los puntajes del ítem para restarle el promedio de forma individual
    for puntaje in resultados:
        diferencia = puntaje - promedio
        bases.append(diferencia)
        
    # Lista vacía para guardar los valores absolutos de las distancias elevadas al cuadrado
    cuadrado = []
    # Itera sobre las diferencias para calcular su potencia por multiplicación directa
    for diferencia in bases:
        posresta = diferencia * diferencia
        cuadrado.append(posresta)
        
    # Calcula la varianza muestral dividiendo la sumatoria de cuadrados entre los grados de libertad (N-1)
    varianza = sum(cuadrado) / (N - 1)
    
    # Registra de manera permanente los datos del ítem actual en las cajas globales antes del reinicio
    allresultados.append(resultados)
    allvarianzas.append(varianza)
        
    # Cierre visual del bloque del ítem mostrando el dato clave calculado de manera limpia con 4 decimales
    print(f"\n  {GREEN}✔ Ítem {K:02d} procesado con éxito.{RESET}")
    print(f"  {BOLD}Varianza obtenida para este ítem:{RESET} {GREEN}{varianza:.4f}{RESET}")
    print(f"{MAGENTA} ──────────────────────────────────────────{RESET}")
    
    # Pregunta de control de flujo en la CLI para decidir si se itera o se rompe el ciclo principal
    opcion = input(f"\n{YELLOW}¿Quiere calcular la varianza de otro ítem? (s/n): {RESET}")

# ==============================================================================
# PROCESAMIENTO POST-BUCLE: SUMATORIAS Y MATRICES TOTALES
# ==============================================================================
# Resumen técnico limpio con los metadatos recolectados en la sesión (Útil para control del investigador)
print(f"\n\n{BOLD}{CYAN}======================================================{RESET}")
print(f"{BOLD}{CYAN}          RESUMEN DE RECOLECCIÓN DE DATOS             {RESET}")
print(f"{BOLD}{CYAN}======================================================{RESET}")
print(f" {CYAN}•{RESET} {BOLD}Total de ítems registrados (K):{RESET} {GREEN}{K}{RESET}")
print(f" {CYAN}•{RESET} {BOLD}Varianzas individuales guardadas:{RESET} {allvarianzas}")
print(f" {CYAN}•{RESET} {BOLD}Matriz completa de respuestas:{RESET} {allresultados}\n")

# Inicializa la lista que contendrá las puntuaciones totales brutas ordenadas por participante
totalesfinales = []

# Suma de las varianzas de los ítems a través de una llamada nativa directa
sumatoriavaritem = sum(allvarianzas)

# Bucle para realizar la suma vertical indexando el participante 'i' a través de todas las sublistas
for i in range(N):  
    suma_participante = 0 # Variable acumuladora local por participante
    for item in allresultados:  
        suma_participante += item[i]  # Suma el puntaje del participante en la columna correspondiente
    totalesfinales.append(suma_participante) # Guarda el resultado total consolidado del sujeto

# Suma total absoluta de todos los datos recopilados (Sirve como paso intermedio para la media)
sumatoriafinales = sum(totalesfinales)

# Obtiene la media aritmética global de las puntuaciones sumadas
promediofinales = sumatoriafinales / len(totalesfinales)

# Lista vacía para procesar las desviaciones globales de los totales consolidados
restafinales = []
# Recorre los totales de cada sujeto para restarles la media global
for puntaje in totalesfinales:
    restafinales.append(puntaje - promediofinales)

# Lista vacía para acumular el valor cuadrático de las desviaciones globales
cuadradofinales = []
# Eleva al cuadrado cada desviación individual de la lista global
for diferencia in restafinales:
    cuadradofinales.append(diferencia * diferencia)
    
# Calcula la varianza de los puntajes totales acumulados dividiendo entre el tamaño muestral corregido (N-1)
varianzadesumatoriadeitem = sum(cuadradofinales) / (N - 1)

# ==============================================================================
# FÓRMULA FINAL Y DESPLIEGUE DE MÉTRICAS CLI
# ==============================================================================
# Aplica la ecuación matemática del Alfa de Cronbach usando agrupaciones de prioridad estrictas
a = (K / (K - 1)) * (1 - (sumatoriavaritem / varianzadesumatoriadeitem))

# Despliegue UX definitivo: Tarjeta de resultados limpia, jerarquizada y con colores semánticos
print(f"{BOLD}{GREEN}======================================================{RESET}")
print(f"{BOLD}{GREEN}                 CÓMPUTO ESTADÍSTICO FINAL            {RESET}")
print(f"{BOLD}{GREEN}======================================================{RESET}")
print(f"  {BOLD}Sumatoria de varianzas por ítem (∑ Si²):{RESET} {sumatoriavaritem:.4f}")
print(f"  {BOLD}Varianza de puntuaciones totales (St²):{RESET}  {varianzadesumatoriadeitem:.4f}")
print(f" ──────────────────────────────────────────────────────")
print(f"  {BOLD}{GREEN}▶ CONFIABILIDAD ALFA DE CRONBACH (α):{RESET}   {BOLD}{GREEN}{a:.4f}{RESET}")
print(f"{BOLD}{GREEN}======================================================{RESET}\n")
