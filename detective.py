# hacer una pregunta al candidato  

actividad = input( "¿Cómo te gustaría pasar la noche?\n(A) leyendo un libro\n(B) asistiendo a una fiesta\n" )

# imprimir qué actividad eligien

print(f"Elegiste {actividad}")

if actividad == "A":
    print( "Muy buena eleccion!" )
elif actividad == "B":
    print( "Parece divertido!" )
else:
    print("Debes escribir A o B, digamos que te gusta leer.")
    
# hacer una SEGUNDA pregunta al candidato
trabajo = input( "¿Cuál es el trabajo de tus sueños?\n(A) Ser un Programdor\n(B) Dirigir un negocio\n" )
if trabajo == "A":
    print( "Programador¡buena elección!" )
elif trabajo =="B":
    print( "¿Dirigir tu propio negocio? ¡Suena divertido y Ariesgardo!")
else:
    print("Por favor escribe A o B")
    trabajo = "A"

# hacer una TERCERA  pregunta al candidato
value = input( "¿Qué es más importante para ti?\n(A) El dinero\n(B) El amor\n" )
if value == "A":
    print( "Dinero es unos de lo grande placeres de la vida!" )
elif value =="B":
    print( "El Amor buena elecion espero nio de defrauden!" )
else:
    print("Debes escirbir A o B")
    value = "A"

# hacer una Cuarta  pregunta al candidato
genero = input( "¿Cual es su genero de musica favorito?\n(B) Reggeaton\n(A) Salsa\n" )
if genero == "A":
    print( "te gusta el perreo salvaje por lo visto!" )
elif genero =="B":
    print( "Eres un gran bailador!" )
else:
    print("Debes escribir A o B")
    genero = "A"

# ask the candidate a fifth question
forma_de_viajar= input( "¿Cuál es tu forma favorita de viajar?\n(A) Conducir\n(B) Copiloto\n" )
if forma_de_viajar== "A":
    print( "Te gusta tener el control!" )
elif forma_de_viajar=="B":
    print( "Dormilon!" )
else:
    print("Debes escribir A o B")
    forma_de_viajar= "A"

# imprime las eleciones del candidato
print( f"Primero Elegiste {actividad}, Luego {trabajo}, Luego {value}, Luego {genero}, Luego {forma_de_viajar}.")


# crear algunas variables para Las puntuaciones 

sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# actualizar las variables de puntuación en función de la elección de la actividad
if actividad == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    indy_like = indy_like + 1

# ctualizar las variables de puntuación según la elección del trabajo
if trabajo == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    cam_like = cam_like - 1
else:
    sam_like = sam_like - 1
    kai_like = kai_like + 2
    indy_like = indy_like + 1

# actualizar las variables de puntuación en función de la elección del valor
if value == "A":
    sam_like = sam_like - 1
    kai_like = kai_like + 1
else:
    sam_like = sam_like + 2
    cam_like = cam_like + 2
    indy_like = indy_like + 1

# actualizar las variables de puntuación en función de la elección de la genero musical
if genero == "A":
    cam_like = cam_like + 2
    sam_like = sam_like + 2
else:
    kai_like = kai_like + 1
    indy_like = indy_like + 2

# actualizar las variables de puntuación en función de la elección de viaje
if forma_de_viajar == "A":
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    indy_like = indy_like - 1
else:
    sam_like = sam_like + 1
    cam_like = cam_like + 1
    kai_like = kai_like - 1

#  imprimir los resultados en función de la puntuación
if sam_like >= 3:
    print( "Eres más como Sam el de ojos agudo" )
elif cam_like >= 3:
    print( "Eres más como Curious Cam" )
elif kai_like >= 3:
    print( "Eres más como Keen Kai") 
else:
    print( "¡Eres más como Inquisitive Indy" )
    