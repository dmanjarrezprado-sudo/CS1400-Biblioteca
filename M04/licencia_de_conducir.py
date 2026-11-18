
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""
# M04 Tarea de Sentencias: Programa de Licencia de Conducir

print("--- EVALUADOR DE CONDICIONES PARA CONDUCIR ---")

# 1. Entrada de datos
edad = int(input("Por favor, introduce tu edad: "))

# Solicitud de 3 condiciones adicionales (comportamientos extremos/cómicos)
olvido_lentes = input("¿Olvidaste los lentes en la cocina? (si/no): ").strip().lower()
conducir_dormido = input("¿Estás intentando conducir completamente dormido? (si/no): ").strip().lower()
perro_volante = input("¿Dejaste que el perro tome el volante? (si/no): ").strip().lower()

# Convertir las respuestas de texto a valores booleanos (True/False)
tiene_lentes_en_cocina = olvido_lentes == "si"
esta_dormido = conducir_dormido == "si"
perro_manejando = perro_volante == "si"

# 2. Sentencias de control y operadores lógicos (AND, OR, NOT)
# Una persona NO puede conducir si es menor de edad OR si cumple alguna de las imprudencias graves
if edad < 18 or tiene_lentes_en_cocina or esta_dormido or perro_manejando:
    
    # Salida clara y personalizada según la situación
    print("\n[!!!] ¡DETÉNTE! Debes entregar las llaves inmediatamente.")
    
    if edad < 18:
        print("- Motivo: Aún no tienes la edad legal mínima para conducir.")
    if tiene_lentes_en_cocina:
        print("- Motivo: Tu abuela dice que sin lentes vas a confundir un semáforo con un árbol de Navidad.")
    if esta_dormido:
        print("- Motivo: El carro no tiene piloto automático espiritual. ¡A dormir a la cama!")
    if perro_manejando:
        print("- Motivo: Firulais conduce muy bien en los videojuegos, pero no en la vida real.")

else:
    # Si es mayor de edad AND NOT tiene ninguna de las imprudencias anteriores
    print("\n[✔] ¡Todo en orden! Estás en condiciones de conducir. Buen viaje y maneja con cuidado.")