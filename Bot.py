import time

#Primera Función
def CheckearMensaje(entrada):
    """
    Recibe la entrada del usuario, crea dos listas paralelas que se corresponden de probabilidad y mensajes.
    Llama al método ProbabilidadDelMensaje() pasandole las palabras claves.
    Luego elije la respuesta con mayor probabilidad. En caso de no haberla, devuelve Incomprendido()
    En caso de haber dos, devuelve la más anterior.
    """
    probabilidad_mas_alta = []
    posible_respuesta = []
    # Acá se detallan todas las posibles respuestas
    posible_respuesta.append("Hola!")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["hola", "buenos", "dias", "hi", "hello", "buenas", "tardes", "noches"]))

    posible_respuesta.append("Yo muy bien! ¿Y tú?")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["que", "tal", "como", "esta", "estas", "anda"]))

    posible_respuesta.append("¡Me alegro mucho!")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["bien", "yo", "muy", "perfecto", "genial", "perfectamente", "me", "siento", "encuentro", "estoy"]))

    posible_respuesta.append("¡Adiós! No se olvide de descargar nuestra extensión!!!")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["adios", "chau", "bye", "nos", "vemos", "hasta", "pronto", "luego"]))

    posible_respuesta.append("Gracias a usted por visitarnos! No se olvide de descargar nuestra extensión...")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["te", "agradezco", "mucho", "muchas", "muchisimas", "de", "un", "millon", "mil", "gracias"]))
    
    posible_respuesta.append("TOTALMENTE! No dude en usarla cuando lo necesite!!")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["la", "su", "extension", "servicio", "es", "gratis", "gratuito", "este", "100%", "ciento"]))

    posible_respuesta.append("jajaja")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["que", "insistente", "cuanta", "insistencia", "pesado","molesto", "jajaja", "jaja", "ja"]))


    # Acá se preguntan cuestiones tecnicas
    posible_respuesta.append("Revise la configuracion del dispositivo en redes y bla bla bla")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["como", "puedo", "mejorar", "seguridad", "configuración", "configuracion"]))

    posible_respuesta.append("Por lo general, no.")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["son", "seguras", "las", "redes", "públicas", "publicas"]))

    posible_respuesta.append("Es recomendable usarlas cuando...")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["cuando", "usar", "una", "vpn"]))

    posible_respuesta.append("La pagina...")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["cuando", "que", "segura", "seguras", "pagina", "paginas", "páginas", "página"]))

    posible_respuesta.append("Una VPN sirve para ocultar su ranstro de...")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["para", "que", "qué", "vpn", "sirve", "una"]))
    #Como me doy cuenta?
    posible_respuesta.append("Usted debe fijarse si...")
    probabilidad_mas_alta.append(ProbabilidadDelMensaje(entrada, ["como", "me", "doy", "cuenta", "si", "una", "red", "es", "segura", "se", "fijo" ]))

    # Acá encontramos la mejor respuesta comparando probabilidades
    mejor_respuesta = max(probabilidad_mas_alta)
    mejor_respuesta = posible_respuesta[probabilidad_mas_alta.index(mejor_respuesta)]


    return "No te estoy entendiendo, dimelo de otra forma" if max(probabilidad_mas_alta) < 1 else mejor_respuesta

# Tercera Función
def ProbabilidadDelMensaje(entrada, palabras_claves=()):   
    """
    Distingue mediante un ciclo for las palabras claves.
    Calcula la probabilidad del mensaje a enviar (hay que hacerlas variables, no Strings, para la traduccion)
    """
    certeza_del_mensaje = 0

    for palabra in entrada:
        if palabra in palabras_claves:
            certeza_del_mensaje += 1

    porcentaje = float(certeza_del_mensaje) / float(len(palabras_claves))
    
    return int(porcentaje*100)




# LLenamos las variables para hablar también en inglés, u otros idiomas. 
# (luego cambiar por archivos o funciones o algo así)
Pregunta_inicial = "¿Qué duda necesita solucionar?"
HORA = int(time.strftime("%H"))

if HORA < 5 or HORA > 20:
    Saludo = "¡Buenas noches!"
elif HORA < 13:
    Saludo = "¡Buenos dias!"
else:
    Saludo = "¡Buenas tardes!"


# Saludo inicial
print(f"""
Sharky: {Saludo} {Pregunta_inicial} 
""")

# Bucle "infinito"
while True:

    #Dibuja la consola, pasa a CheckearMensaje la entrada del usuario, quitándole caracteres especiales y convertida en minusculas y en tupla (cada palabra un elemento)
    print("Sharky: ", CheckearMensaje(input("Diga algo: ").translate({ord(','): "",ord('?'): "",ord('¿'): "",ord('!'): "",ord('¡'): "",ord(')'): "",ord('('): "",ord('.'): "", ord(':'): "", ord(';'): ""}).lower().translate(str.maketrans('áéíóúü','aeiouu')).split()))

