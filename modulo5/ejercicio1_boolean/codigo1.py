# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?

print("Puede salir hoy solo si tiene 18 años o más Y si tiene permiso")
edad = input("cuantos años tienes")
edad = int(edad)
if (edad >= 18) and tiene_permiso:
    print("puede salir")
else:
    print("no puede salir")





# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
es_finde = input("es fin de semana? (si/no)")
if es_finde or tiene_permiso:
    print("andar en las calles, puedes salir")
else:
    print("no puedes salir, solo puedes estar en casa")



# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
print("no tiene permiso")




# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea.
# para andar con permisos debe tener 21 an
if (edad >= 21) and tiene_permiso:
        print("puede conducir")






