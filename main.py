# Instalar la libreria: pip install nltk
# Descomentar la linea 5 y ejecutar para terminar de instalar
# Una vez instalada la libreria volver a comentar
import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt')

preguntas_y_respuestas = {
    "difultades Dificultades difucltades Difucltades": "Las dificultades en la gestión de los legajos internos incluyen limitaciones de escalabilidad, problemas de seguridad y rendimiento en la base de datos. Además, parte de la gestión se realiza a través de Onedrive, donde se almacenan imágenes de algunas características de los presos.",
    
    "base datos, Base, actualmente" : "Actualmente, la base de datos es un Access y un OneDrive en donde se almacenan las imagenes de los presos",
    
    "informacion gestion gestiona actualmente": """La información que se gestiona actualmente es:
                                                    *Carpeta médica
                                                    *Educación
                                                    *Carta de situación: Nombre, DNI, Numero de Loft o Lift y Juzgado al que pertenece
                                                    *Distintas oficinas judiciales
                                                    *Relaciones sociales, como por ejemplo las visitas
                                                    *Foto de los presos
                                                    *Senias particulares
                                                    """,
    
    "actualizaciones actualiza cada cuanto": "Todos los días se realizan actualizaciones de datos por la contínua entrada y salida de condenados y procesados.",
    
    "Seguridad seguridad confidencialidad medidas": "Actualmente unicamente pueden tener acceso los empleados que cumplan con los roles requeridos.",
    
    "areas dependencias": """Las areas/dependecias del Servicio Penitenciario son:
    *Oficinas de seguridad interna
    *Tratamiento
    *Judiciales
    *Sanidad
    *Social
    *Trabajo
    Cada área cuenta con disponibilidad de computadoras y cada uno se encarga de cargar los datos pertinentes a cada area
    Los datos obligatorios van a depender de cada área.
    """,
    
    "elementos, disponibilidad, dispositivo, dispositivos":"Cada área cuenta con disponibilidad de computadoras y cada uno se encarga de cargar los datos pertinentes a su area",
    "funcionalidades, requerimientos, requerimiento": 
    """Los mismos con lo que ya cuentan actualmente, que son: Visualización, Consulta.
    Se requiere que se agreguen alertas en casos específicos.
    También la base debe tener una actualización diaria, en lo posible, debido a que tienen muchos ingresos y egresos diarios.
    Dentro de la información importante a visualizar se encuentra: 
    *Quien es
    *legajo
    *Tiempo de condena
    *Tiempo cumplido
    *Tiempo de beneficio
    *Fase de liberación""",
    
    "codigo acceso para agregar descripciones":"Cada sector tiene un codigo de acceso y debe estar habilitado para agregar descripciones""",
    
    "niveles ": "Se tienen 4 niveles: Judiciales, Educación, Sanidad, Trabajo",
    
    "sectores sector ": """La idea es que cada nivel tenga su formulario
                La cárcel consta de varios sectores/niveles como: 
                *Judiciales
                *Educación
                *Sanidad
                *Trabajo
                Cada sector tiene un codigo de acceso y debe estar habilitado para agregar descripciones
                """,
    " se espera, impacto, idea, procesos": """Se espera obtener la Carta de situación
    La idea es que se vinculen datos o crucen entre internos. Los vinculos a tener en cuenta son: 
    * Relaciones entre internos.
    * Organigrama de visitas.
    * Alerta de persona ya registrada en visitas.
    * Cruzaba información entre internos. Esta utlima ya esta creada pero es obsoleta.
    """,
    "Lider, lider, coordinador, supervisor":" El  Gestor de Proyecto es Luis Gonzalez",
    "participantes, participante, alumnos, alumno, integrantes, integrante, carrera":"Los alumnos de 4to y 5to año de la carrera de Ingenieria en Sistemas de la Informacion de la Universidad de la Cuenca del Plata",
    "duracion, tiempo ejecucion": "El planeamiento se llevara a cabo durante el primer cuatrimestre a cargo de los alumnos de 5to año y el desarrollo de la base de datos se llevara a cabo en el segundo cuatrimestre a cargo de los alumnos de 4to año",
    "contexto, resumen":"La implementación de una base de datos para la gestión de legajos de internos en todas las dependencias del Servicio Penitenciario permite una gestión más eficiente de la información y contribuye a la construcción de ciudades y comunidades sostenibles.",
    "Objetivo, objetivo, proposito, Propositos":"Implementar una base de datos centralizada y segura para la gestión de los legajos de los internos del Servicio Penitenciario de la Provincia de Corrientes, garantizando el acceso y actualización de la información de manera remota y eficiente.",
    "tenes, funcion, finalidad":"""Tengo informacion acerca del proyecto Gestión Integral de Legajos de Internos en el Servicio Penitenciario de la Provincia de Corrientes.Puedo hablarte de los objetivos del proyecto, los participantes, fecha de realizacion y responder preguntas en base a la primera reunion realizada""",
    "Como estas como ":"Soy un bot, no tengo estado de animo",
    "creado":"Fui creado para contestar las preguntas que me hagas sobre la implementacion de una base de datos para el Servicio Penitenciario para tu trabajo práctico 2 de tu carrera",
    "sos, agente inteligente consideras":"Si me considero un agente inteligente",
    "Gracias":"De nada, ojala te recibas pronto, recorda que el titulo intermedio tambien vale",
    "notas":"En mi opinion de agente inteligente, mi voto es secreto",
    "Dale nota merecemos dale":"Un 10, Felicidades!!!!!",
    "nombre, llamas":"Mi nombre es Tobi, no te confundas con un perro soy un agente inteligente", 
    "chiste" :"El programador se quedó atascado en la ducha debido a las instrucciones del estado del champú:Hacer espuma, enjuagar, repetir",
    "Contame otro chiste otro Otro":"¿Qué es un terapeuta? 1024 Gigapeutas.",           
}
# Tokeniza las preguntas y respuestas
preguntas_tokenizadas = {
    pregunta: word_tokenize(pregunta.lower()) for pregunta in preguntas_y_respuestas
}
pregunta_usuario = "hola"

preguntas = [
    "¿Cuáles son las principales dificultades que enfrenta actualmente el personal penitenciario en la gestión de los legajos de internos?",
    "¿Cuál es la frecuencia de actualización de los datos en los legajos de los internos?",
    "¿Qué requisitos de seguridad y confidencialidad deben cumplir los datos de los legajos de los internos?",
    "¿Qué dependencias del Servicio Penitenciario se encuentran activas y qué dispositivos tecnológicos poseen?",
    "¿Qué funcionalidades específicas esperan obtener del sistema de gestión de legajos de internos?",
    "¿Qué nivel de accesibilidad y control se requiere sobre la información de los legajos de los internos?",
    "¿Cómo esperan que la implementación de esta base de datos impacte en la eficiencia y en los procesos de la gestión penitenciaria?"
]

respuestas = [
    "Las dificultades en la gestión de los legajos internos incluyen limitaciones de escalabilidad, problemas de seguridad y rendimiento en la base de datos. Además, parte de la gestión se realiza a través de Onedrive, donde se almacenan imágenes de algunas características de los presos.",
    "Todos los días se realizan actualizaciones de datos por la contínua entrada y salida de condenados y procesados.",
    "Actualmente unicamente pueden tener acceso los empleados que cumplan con los roles requeridos.",
    "Oficinas de seguridad interna, Tratamiento, Judiciales, Sanidad, Social, Trabajo. Cada área cuenta con disponibilidad de computadoras y cada uno carga datos pertinentes a sus áreas.",
    "Los mismos que ya cuentan actualmente, que son: Visualización, Consulta. Y se requiere que se agreguen alertas en casos específicos que quedamos en definir. También la base de tener una actualización diaria, en lo posible, debido a que tienen muchos ingresos y egresos diarios.",
    "SI, la idea es que cada nivel tenga su formulario. La cárcel consta de varios sectores/niveles como: Judiciales, Educación, Sanidad, Trabajo. Cada sector debe estar habilitado para agregar descripciones. Código de acceso a cada sector.",
    "Se espera obtener la Carta de situación. La idea es que se vinculen datos o crucen entre internos. Vínculos a tener en cuenta: Vincular vínculos entre internos. Organigrama de visitas. Alerta de persona ya registrada en visitas. Cruzaba información entre internos(YA CREADA) OBSOLETA."
]




class __main__:
    def obtener_respuesta(pregunta_usuario):
        pregunta_usuario = pregunta_usuario.lower()
        max_coincidencias = 0
        mejor_pregunta = None

        def contar_coincidencias(pregunta_usuario, pregunta):
            coincidencias = sum(1 for i in range(len(pregunta_usuario) - 3) if pregunta_usuario[i:i+4] in pregunta)
            return coincidencias

        for pregunta in preguntas_y_respuestas.keys():
            coincidencias = contar_coincidencias(pregunta_usuario, pregunta.lower())
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_pregunta = pregunta

        if mejor_pregunta is not None:
            return preguntas_y_respuestas[mejor_pregunta]
        else:
            return "Lo siento, aún no tengo información sobre eso."

    nombre = input("Hola soy un bot de consultas, como te llamas: ")
    print(f"Hola {nombre}, mucho gusto")
    print("Soy un bot de consultas y tengo integradas las respuestas a estas preguntas ")
    while pregunta_usuario != "No" or pregunta_usuario != "no":
        print("---------------------------------------------------------------")
        for i, pregunta in enumerate(preguntas, 1):
            print(f"{i}. {pregunta}")
        print("---------------------------------------------------------------")
        print("Si la pregunta no esta en la lista, seleccione 12")
        seleccion = input("Ingrese el número de la pregunta: ")
        if seleccion == '12':
            pregunta_usuario = input("Hazme una pregunta: ")
            print(obtener_respuesta(pregunta_usuario))
            print("-------------------------------------------------")
            pregunta_usuario = input("Te puedo ayudar en algo mas? (si - no): ")
            if pregunta_usuario == "No" or pregunta_usuario == "no":
                print("Nos vemos pronto, que tengas buen dia C:")
                exit()
        elif seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(preguntas):
                print(respuestas[seleccion - 1])
                pregunta_usuario = input("Te puedo ayudar en algo mas? (si - no): ")
                if pregunta_usuario == "No" or pregunta_usuario == "no":
                    print("Nos vemos pronto")
                    exit()
            else:
                print("Selección inválida. Por favor, ingrese un número válido.")
                pregunta_usuario = input("Te puedo ayudar en algo mas? (si - no): ")
                if pregunta_usuario == "No" or pregunta_usuario == "no":
                    print("Nos vemos pronto")
                    exit()


""" 
        for i, pregunta in enumerate(preguntas, 1):
            print(f"{i}. {pregunta}")
        seleccion = input("Ingrese el número de la pregunta (o ingrese '10' para salir): ")
        if seleccion == '10':
            print("Saliendo del programa...")
            exit()  # Sale del programa si se ingresa '10'
        elif seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(preguntas):
                print(respuestas[seleccion - 1])
            else:
                print("Selección inválida. Por favor, ingrese un número válido.")
 """

"""     # Ejemplo de uso
    nombre = input("Hola soy un bot de consultas, como te llamas: ")
    print(f"Hola {nombre}, mucho gusto")
    while pregunta_usuario != "No" or pregunta_usuario != "no":
        print("Soy un bot de consultar y tengo integradas las respuestas a estas preguntas ")
        print("---------------------------------------------------------------")
        for i, pregunta in enumerate(preguntas, 1):
            print(f"{i}. {pregunta}")
        print("---------------------------------------------------------------")
        print("Si la pregunta no esta en la lista, seleccione 12")
        seleccion = input("Ingrese el número de la pregunta: ")
        if seleccion == '12':
            pregunta_usuario = input("Hazme una pregunta: ")
            print(obtener_respuesta(pregunta_usuario))
            print("-------------------------------------------------")
            print("Te puedo ayudar en algo mas?")
 """