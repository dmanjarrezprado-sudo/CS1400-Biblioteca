# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable "nombre" dentro de los paréntesis?
# r/ parametro.
# 2. ¿Qué le falta al código para ser completamente reutilizable?
# r/retornar un valor para que pueda ser reutilizable en otras partes del programa.


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    return numero % 2 == 0

# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
# r/ def    
# 4. Escribe los nombres de las dos funciones definidas arriba.
# r/ calcular_descuento y es_par.
# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
# r/funciona y reconoce el valor de 100 como precio y le aplica el descuento por defecto del 10%.
# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
# r/calcula el precio final aplicando un descuento del 20% al precio de 200.


# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")


compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Escribe el pseudocódigo de las funciones en la Parte 2.
def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    return numero % 2 == 0

# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito del programa. Tu compañera(o) te debe explicar lo siguiente. Lleguen a un acuerdo para agregar lo esencial como comentarios.
# r/ La función calcular_descuento calcula el precio final de un producto aplicando un descuento basado en un porcentaje dado.
# 9. Cambia las funciones para que acepten decimales en el precio.
# r/ Ya aceptan decimales, no es necesario hacer cambios adicionales.

# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)

# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
# r / La variable 'resultado' guarda el valor None porque la función mostrar_bienvenida() no tiene una declaración return, solo imprime el texto.
# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
# r /  para que la función devuelva el valor calculado del precio final, permitiendo que se pueda almacenar en las variables compra_1 y compra_2.
# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
# r / NameError.
# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# r / las variables establecidas solo funciona mientras se esta usanso el programa.
# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
# r / la funcion imprime el precio final, pero no devulve ningun valor.
# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
# r / calcular_descuento(precio=100, porcentaje=15)
# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.
# r / ya se agrego un docstring en cada funcion.