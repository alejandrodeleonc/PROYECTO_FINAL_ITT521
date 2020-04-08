from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
import time
from typing import List
from PROYECTO_FINAL.clases import Materia, Estudiante


def semestre_actual():
    today = date.today()
    mes = today.month
    annio = str(today.year)

    if mes == 1 or mes == 2 or mes == 3 or mes == 4 :
        return "ENERO "+ annio
    elif  mes == 5 or mes == 6 or mes == 7 or mes == 8:
        return "ABRIL "+ annio
    elif mes == 9 or mes == 10 or mes == 11 or mes == 12:
        return "SEPTIEMBRE "+ annio

    return None
def get_carrera(c):
    carrera = c.replace('Grado - ', '')
    return carrera
def get_indice(c):
    aux = c.replace('Nota Media: 2.0 obligatoria, ', '')
    indice = aux.replace(' real.', '')
    return indice
semestre = semestre_actual()

def get_estudiante(user:str, passsword:str):
    print("Recolectando datos desde Campus Solutions...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get("https://micampus.pucmm.edu.do/psp/cs92pro/?cmd=login&languageCd=ESP&")
    username = driver.find_element_by_id("userid")
    username.clear()
    username.send_keys(user)
    password = driver.find_element_by_name("pwd")
    password.clear()
    password.send_keys(passsword)
    driver.find_element_by_name("Submit").click()
    driver.get("https://micampus.pucmm.edu.do/psc/cs92pro/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_MY_ACAD.GBL?Page=SSS_MY_ACAD&Action=U")
    nombre_est= driver.find_element_by_id("win0divDERIVED_SSTSNAV_PERSON_NAME").text
    print("Nombre: "+nombre_est)
    carrera = get_carrera(driver.find_element_by_id("#ICSetFieldSSS_MY_ACAD.TREECNTRLFIELD1.S4").text)
    print("Matricula: "+ user)
    print("Carrera: "+carrera)
    driver.find_element_by_id("DERIVED_SSSACA2_SS_DEG_PROG_LINK$span").click()
    time.sleep(1)
    i = driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[11]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/div/span/ul/li[3]").text
    indice = get_indice(i)
    print("Indice acumulado: "+indice)
    driver.get("https://micampus.pucmm.edu.do/psc/cs92pro/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL?Page=SSR_SSENRL_GRADE&Action=A&ExactKeys=Y&ACAD_CAREER=GRDO&EMPLID=10128009&INSTITUTION=PUCMM&STRM=1740")
    time.sleep(1)
    driver.find_element_by_name("DERIVED_SSS_SCT_SSS_TERM_LINK").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[4]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[6]/td[2]/div/a/span/input").click()
    time.sleep(1)
    puntos_acumulados = driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[10]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[13]/td[4]/div/span").text
    time.sleep(1)
    #main_window.progressBar.setProperty("value", 60)
    print("Puntos acumulados: "+puntos_acumulados)
    creditos_acumulados = driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[10]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[14]/td[4]/div/span").text
    print("Creditos acumulados: "+ creditos_acumulados)
    creditos_encurso = driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[10]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[6]/td[2]/div/span").text
    print("Creditos en curso: "+creditos_encurso)
    rows = []
    rows = driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[8]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody").find_elements_by_tag_name("tr")
    time.sleep(1)
    cant_materias_encurso = len(rows)-1
    print(f"Cantidad de materias en curso: {cant_materias_encurso} ")
    materias: List[Materia] = []
    for i in range(0, (cant_materias_encurso)):
        m = f"CLASS_TBL_VW_DESCR${i}"
        c = f"win0divSTDNT_ENRL_SSV1_UNT_TAKEN${i}"
        nombre_materia = driver.find_element_by_id(m).text
        creditos = driver.find_element_by_id(c).text
        ma = Materia(nombre_materia, creditos)
        materias.append(ma)
    """for m in materias:
        print(m.nombre + " tiene " + m.creditos + " creditos")"""
    driver.close()
    estudiante = Estudiante(nombre_est, user, carrera, materias, indice, puntos_acumulados, creditos_acumulados,
                            creditos_encurso, cant_materias_encurso)
    return estudiante





