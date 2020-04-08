from PROYECTO_FINAL.l import*
from PROYECTO_FINAL.scrapper import *
from PROYECTO_FINAL.clases import Estudiante, Materia
from PROYECTO_FINAL.ventana_principall import*





def main():
    """materias: List[Materia] = []
    mat = Materia("Materia 1", "3")
    materias.append(mat)
    matt = Materia("Materia 2", "5")
    materias.append(matt)
    mattt = Materia("Materia 3", "6")
    materias.append(mattt)

    est =  Estudiante("Alejandro De Leon", "20160338", "Ingenieria Telematica",materias, "2.2", "401.000", "180.000", "26.000", 3)
    app = QApplication([])
    window = QMainWindow()
    main_window = Ui_MainWindow_main_prin()
    main_window.setupUi_main_prin(window, est)
    window.show()
    app.exec_()"""

    app = QApplication([])
    window = QMainWindow()
    main_window = Ui_MainWindow_login()
    main_window.setupUi(window)
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()

