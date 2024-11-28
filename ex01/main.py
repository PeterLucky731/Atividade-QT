import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from ex1 import Ui_MainWindow

class CountNota(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNovo.triggered.connect(self.novo)
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionSalvar.triggered.connect(self.salvar)
        self.ui.actionSair.triggered.connect(self.sair)
        
        self.ui.btn.clicked.connect(self.avaliarNota)

    def avaliarNota(self):
    
        try:
            nota = int(self.ui.nota.text())

            if (nota < 0 or nota > 100):
                self.ui.result.setText("Nota Inválida! Digite uma nota entre 0 e 100")
            elif (nota >= 90):
                self.ui.result.setText("Resultado da Avaliação: Excelente")
            elif (nota < 90 and nota >= 70):
                self.ui.result.setText("Resultado da Avaliação: Bom")
            elif (nota < 70 and nota >= 50):
                self.ui.result.setText("Resultado da Avaliação: Regular")
            elif (nota < 50):
                self.ui.result.setText("Resultado da Avaliação: Insuficiente")
                       
        except ValueError:
            self.ui.result.setText("Nota Inválida! Digite apenas números")

    def novo(self):
        self.ui.nota.clear()
        self.ui.result.setText("Resultado da Avaliação:")

    def abrir(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                content = file.read()
                self.ui.nota.setText(content) 

    def salvar(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.ui.nota.text()) 

    def sair(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = CountNota()
    janela.show()
    sys.exit(app.exec_())