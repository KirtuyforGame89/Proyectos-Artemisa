#Webos 0.1 
print("¡Hola! Ingresar Nombre")
nombre = input("Escribe tu nombre: ")
print("Bienvenido,", nombre)
print("Este es mi primer preograma")
edad = 20 
#Webos 0.2 (% de propina )
print("===Calculo para La Mesera eoeoeoe===")
print()
#pedir los datos 
gente = input("Enumera las cabezas de la chavisa: ")
gente = int(gente)
print()
print("Muchos webones, espero no se hallan comido a la mesera tambien")
print()
print("¡Ahora! Cuanto comieron manada de muertos de hambre>")
cuenta = input("total del dinero por la comida $")
#texto a nimero decimal
cuenta = float(cuenta)
#establecer porcentaje
porciento = input("¿Cuanto sera el porcentaje de la mesera? (ej: 9, 11, 13): ")
porciento = float(porciento)
#operacion
propina = cuenta * (porciento / 100)
#cuenta + propina
Total_dineros = cuenta + propina
#entregar calculo 
print()
print(">>>>>>Resultado<<<<<<")
print("Cuanto tragste: $", cuenta)
print("Propina (", porciento, "%): $", propina)
print("TOTAL DINEROS: $", Total_dineros)
print()
print("¡¡¡¡¡La proxima dale webo al mesero, en esta economia no alcansa para propina!!!!")
