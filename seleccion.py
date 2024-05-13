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

def mostrar_preguntas():
    while True:
        print("-----------------------------------------------")
        print("Programa de Preguntas y Respuestas")
        print("-----------------------------------------------")
        print("Seleccione una pregunta:")
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
        else:
            print("Entrada inválida. Por favor, ingrese un número válido.")

mostrar_preguntas()
