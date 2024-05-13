# Instalar la libreria: pip install nltk
# Descomentar la linea 5 y ejecutar para terminar de instalar
# Una vez instalada la libreria volver a comentar
import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt')

preguntas_y_respuestas = {
    "¿principales dificultades que enfrenta actualmente el personal penitenciario en la gestión de los legajos de internos?dificultades dificultad  gestion limitaciones  Desafíos principales, obstáculos principales, problemas principales  Encara actualmente, afronta en la actualidad, lidia actualmente Empleados carcelarios, funcionarios de prisiones, agentes penitenciarios Administración de expedientes de reclusos, manejo de archivos de presos, control de registros de internos ": "Las dificultades en la gestión de los legajos internos incluyen limitaciones de escalabilidad, problemas de seguridad y rendimiento en la base de datos. Además, parte de la gestión se realiza a través de Onedrive, donde se almacenan imágenes de algunas características de los presos.",
    
    "¿ actualidad  donde  guarda  informacion?  tipo base datos caracteristica imagenes guarda En qué lugar se guarda actualmente la informacion y qué tipo de base de datos se utiliza? Y qué características tienen las imágenes almacenadas? Cuál es la ubicación actual de la información y cuál es el formato de base de datos que se emplea? Podrías describir las características de las imágenes almacenadas? En qué ubicación se almacena actualmente la información y cuál es el tipo de base de datos utilizado? ¿Y podrías detallar las características de las imágenes que se guardan? Donde estan los datos de los presos? " : "Es un Access y hay un OneDrive que es donde se almacenan las imagenes",
    
    "¿Qué tipo  tipos  de informacion gestionan actualmente  legajos  internos?   informacion maneja  penitenciaria Informacion sobre Penitenciaria Informacion  Servicio Penitenciario  informacion gestiona actualmente tipo informacion gestiona actualmente ¿Qué tipo de tipos de información gestionan actualmente los legajos internos? ¿Qué información maneja la penitenciaría? Qué información sobre la Penitenciaria gestiona el Servicio Penitenciario? Qué información gestiona actualmente? Qué tipo de información gestiona actualmente la penitenciaría? Qué información de los presos internos hay existen?": """La información que se gestiona actualmente es:
                                                    *Carpeta médica
                                                    *Educación
                                                    *Carta de situación: Nombre, DNI, Numero de Loft o Lift y Juzgado al que pertenece
                                                    *Distintas oficinas judiciales
                                                    *Relaciones sociales, como por ejemplo las visitas
                                                    *Foto de los presos
                                                    *Senias particulares
                                                    """,
    
    "¿Con qué frecuencia se actualizan los datos de los legajos internos?, Cuál es la frecuencia de actualización de los datos en los legajos de internos, Con qué regularidad se actualizan los datos de los registros de los internos, Cuántas veces se actualizan diariamente los datos de los legajos de internos, Cada cuánto se renuevan los registros de los presos en la base de datos frecuencia, Se actualiza la base de datos, actualizacion, datos, legajos internos": "Todos los días se realizan actualizaciones de datos por la contínua entrada y salida de condenados y procesados.",
    
    "¿Cuáles son los requisitos de seguridad y confidencialidad que deben cumplirse para los datos de los legajos internos?, Qué medidas de seguridad y confidencialidad deben seguirse para los datos de los legajos internos, Cómo se implementa la seguridad y confidencialidad en la base de datos de los legajos internos, Cuál es el tipo de seguridad en la base de datos de los legajos internos, Qué medidas se toman para garantizar la seguridad de los datos en los legajos internos, seguridad, confidencialidad, seguiridad": "Actualmente unicamente pueden tener acceso los empleados que cumplan con los roles requeridos.",
    
    "¿Que areas o dependencias componentes el servicio penitenciario?, areas, dependencias, servicio penitenciario, componen": """Las areas/dependecias del Servicio Penitenciario son:
    *Oficinas de seguridad interna
    *Tratamiento
    *Judiciales
    *Sanidad
    *Social
    *Trabajo
    Cada área cuenta con disponibilidad de computadoras y cada uno se encarga de cargar los datos pertinentes a cada area
    Los datos obligatorios van a depender de cada área.
    """,
    "¿Con que tecnologia cuenta cada area del servicio penitenciario?, Que tecnologia tiene cada area, Con que tecnologia cuenta cada area, de que se encarga cada area":"Cada área cuenta con disponibilidad de computadoras y cada uno se encarga de cargar los datos pertinentes a su area",
    "¿ funcionalidades específicas esperan obtener  sistema de gestión  legajos  internos? Qué funcionalidades específicas esperan obtener del sistema de gestión de legajos internos? Cuáles son los requisitos que deben cumplir las funcionalidades de una base de datos específica para los usuarios funcionalidades requerimientos cumplir base de datos especificas usuario usuarios": 
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
    
    "¿Cada sector tiene un codigo de acceso? codigo de acceso para agregar descripciones? Sectores con codigos Códigos de acceso código de acceso descripciones":"Cada sector tiene un codigo de acceso y debe estar habilitado para agregar descripciones""",
    
    "¿Cuantos niveles conforman la penitenciaria?, Cuantos niveles tiene, cuales eran los niveles, que niveles conforman, que niveles tiene": "Se tienen 4 niveles: Judiciales, Educación, Sanidad, Trabajo",
    
    "¿ Que sectores tiene la penitenciaria carcel?, Cuantos sectores tiene la penitenciaria?, sectores sector de accesibilidad  control  requiere sobre  información   legajos   internos? Existe existe cada sector sectores tiene algo especial codigo acceso nivel control seguridad accesibilidad controles cuales penitenciaria": """La idea es que cada nivel tenga su formulario
                La cárcel consta de varios sectores/niveles como: 
                *Judiciales
                *Educación
                *Sanidad
                *Trabajo
                Cada sector tiene un codigo de acceso y debe estar habilitado para agregar descripciones
                """,
    "¿Que procesos impactarian de manera eficiente en la gestion? Que vinculos se tendrian que tener en cuenta? esperan implementación  impacto impactos base de datos impacte eficiencia procesos gestión penitenciaria carcel servicio penitenciario? espera luego base datos implementación impacte eficiencia procesos cree o proceso carga lectura datos Como sería el proceso de carga y lectura de datos?": """Se espera obtener la Carta de situación
    La idea es que se vinculen datos o crucen entre internos. Los vinculos a tener en cuenta son: 
    * Relaciones entre internos.
    * Organigrama de visitas.
    * Alerta de persona ya registrada en visitas.
    * Cruzaba información entre internos. Esta utlima ya esta creada pero es obsoleta.
    """,
    "¿Quien coordina el proyecto, supervisa el progreso del proyecto y asegura que los entregables se completen a tiempo y dentro del presupuesto?":" El  Gestor de Proyecto es Luis Gonzalez",
    "¿Quienes participan   proyecto? Cuales son los participantes del trabajo? cuales son los participantes del proyecto? Quienes quienes participan proyecto":"Los alumnos de 4to y 5to año de la carrera de Ingenieria en Sistemas de la Informacion de la Universidad de la Cuenca del Plata",
    "¿Cual duracion  proyecto? Duracion duracion proyecto": "El planeamiento se llevara a cabo durante el primer cuatrimestre a cargo de los alumnos de 5to año y el desarrollo de la base de datos se llevara a cabo en el segundo cuatrimestre a cargo de los alumnos de 4to año",
    " podes dar  resumen  contexto del proyecto?Contexto Resumen resumen proyecto":"La implementación de una base de datos para la gestión de legajos de internos en todas las dependencias del Servicio Penitenciario permite una gestión más eficiente de la información y contribuye a la construcción de ciudades y comunidades sostenibles.",
    "¿Cual   objetivo  proyecto? Objetivo objetivo proposito":"Implementar una base de datos centralizada y segura para la gestión de los legajos de los internos del Servicio Penitenciario de la Provincia de Corrientes, garantizando el acceso y actualización de la información de manera remota y eficiente.",
    "¿informacion tenes manejas?  tenes informacion?Podes contarme podes Informacion informacion tenes contame para  fuiste creado?":"""Tengo informacion acerca del proyecto Gestión Integral de Legajos de Internos en el Servicio Penitenciario de la Provincia de Corrientes.Puedo hablarte de los objetivos del proyecto, los participantes, fecha de realizacion y responder preguntas en base a la primera reunion realizada""",
    "Como estas hoy?estas como ":"Soy un bot, no tengo estado de animo",
    " puedes hacer?  hacer puedes¿Para  fuiste creado?creado para otra respuesta":"Fui creado para contestar las preguntas que me hagas sobre la implementacion de una base de datos para el Servicio Penitenciario para tu trabajo práctico 2 de tu carrera",
    "¿Que sos?, sos un agente inteligente?":"Si soy un agente inteligente",
    "Gracias amigo gracias muchas gracias":"De nada, ojala te recibas pronto, recorda que el titulo intermedio tambien vale",
    "Que nota crees  merecemos? nota merecemos merecer calificacion":"En mi opinion de agente inteligente, mi voto es secreto",
    "Dale nota merecemos?dale":"Un 10, Felicidades!!!!!",
    "¿Cual nombre? Tenes nombre tienes nombre cual como te llamas":"Mi nombre es Tobi, no te confundas con un perro soy un agente inteligente", 
    "Contame  chiste Chiste contas chistes? tenes chistes para contar?" :"El programador se quedó atascado en la ducha debido a las instrucciones del estado del champú:Hacer espuma, enjuagar, repetir",
    "Contame otro chiste otro Otro":"¿Qué es un terapeuta? 1024 Gigapeutas.",           
}
# Tokeniza las preguntas y respuestas
preguntas_tokenizadas = {
    pregunta: word_tokenize(pregunta.lower()) for pregunta in preguntas_y_respuestas
}
pregunta_usuario = "hola"


class __main__:

    def obtener_respuesta(pregunta_usuario):
        pregunta_usuario_tokenizada = word_tokenize(pregunta_usuario.lower())
        max_coincidencias = 0
        mejor_pregunta = None

        for pregunta, tokens in preguntas_tokenizadas.items():
            coincidencias = sum(
                1 for token in pregunta_usuario_tokenizada if token in tokens
            )
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_pregunta = pregunta

        if mejor_pregunta is not None:
            return preguntas_y_respuestas[mejor_pregunta]
        else:
            return "Lo siento, no tengo información sobre esa pregunta."

    # Ejemplo de uso
    nombre = input("Hola soy un bot de consultas, como te llamas: ")
    print(f"Hola {nombre}, mucho gusto")
    while pregunta_usuario != "No" or pregunta_usuario != "no":
        pregunta_usuario = input("Hazme una pregunta: ")
        print(obtener_respuesta(pregunta_usuario))
        print("-------------------------------------------------")
        print("Te puedo ayudar en algo mas?")
