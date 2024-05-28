episodio_V = ["Luke Skywalker", "Han Solo", "Leia Organa", "Darth Vader", "Yoda"]
episodio_VII = ["Han Solo", "Leia Organa", "Luke Skywalker", "Rey", "Finn", "Kylo Ren"]


stack_V = episodio_V[::-1]
stack_VII = episodio_VII[::-1]


set_V = set()
set_interseccion = set()


while stack_V:
    personaje = stack_V.pop()
    set_V.add(personaje)


while stack_VII:
    personaje = stack_VII.pop()
    if personaje in set_V:
        set_interseccion.add(personaje)


interseccion = list(set_interseccion)
print("Personajes que aparecen en ambos episodios:", interseccion)