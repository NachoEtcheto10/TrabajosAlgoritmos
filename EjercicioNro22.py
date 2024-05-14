def usar_la_fuerza(mochila, objetos_sacados=0):
    if not mochila:
        return False, objetos_sacados
    
    objeto = mochila.pop(0)
    objetos_sacados += 1
    
    if objeto == "sable_de_luz":
        return True, objetos_sacados
    
    return usar_la_fuerza(mochila, objetos_sacados)

mochila = ["libro", "comida", "ropa", "sable_de_luz", "botiquín"]
encontrado, objetos_sacados = usar_la_fuerza(mochila)
if encontrado:
    print("¡El Jedi encontró un sable de luz después de sacar", objetos_sacados, "objetos!")
else:
    print("El Jedi no encontró un sable de luz en la mochila.")