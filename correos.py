import smtplib

from string import Template
from PROYECTO_FINAL.clases import Estudiante, Materia
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PROYECTO_FINAL.scrapper import semestre_actual

#LISTA_CONTACTOS = "contactos.txt"
ARCHIVO_PLANTILLA = "PLANTILLA_CORREO.txt"

MI_CORREO = 'estimadordeindice@gmail.com'
PASSWORD = 'estima123'

MTA_HOST = 'smtp.gmail.com'
MTA_PORT = 587  # SSL: 465, TLS: 587


def lee_plantilla(filename):
    """
    Returna un objeto Template que encapsula el contenido de filename
    """

    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return Template(contenido)


def envia(est: Estudiante, materias: Materia, indice_seme, puntos_acu, creditos_acu, indice_acu):
    nombre = est.nombre
    correo = str(est.correo)
    message_template = lee_plantilla(ARCHIVO_PLANTILLA)

    # crea sesión SMTP
    s = smtplib.SMTP(host=MTA_HOST, port=MTA_PORT)
    s.starttls()
    s.set_debuglevel(1)  # esto se debería de remover en un ambiente real
    s.login(MI_CORREO, PASSWORD)

    msj = MIMEMultipart()  # create a message

    # agrega el nombre de la persona en el mensaje de la plantilla
    mensaje = message_template.substitute(NOMBRE_PERSONA=nombre.title(), INDICE_SEMESTRAL= str(indice_seme),
                                          PUNTOS_ACUMULADO= str(puntos_acu), CREDITOS_SEMESTRAL= str(est.creditos_cursando),
                                          CREDITOS_ACUMULADO=str(creditos_acu))

    # Imprime el mensaje
    print(mensaje)

    # asigna parámetros al correo
    msj['From'] = MI_CORREO
    msj['To'] = correo
    msj['Subject'] = "Estimacion de indice del semestre " + semestre_actual()

    # agrega mensaje al cuerpo del correo
    for m in materias:
        tex = m.nombre + "con una " + m.calficacion
        msj.attach(MIMEText(mensaje, tex))



    # envía mensaje usando sesión creada anteriormente
    s.send_message(msj)
    del msj

    # Termina la sesión SMTP y cierra la conexión
    s.quit()