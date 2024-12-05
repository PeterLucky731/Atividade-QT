import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from ex3 import Ui_MainWindow
import random   

class CountAposta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.avaliarAposta)

    def avaliarAposta(self):
        
        try:
            aposta = float(self.ui.aposta.text())
            numero0a100 = random.randint(0, 100)
            if aposta == numero0a100:
                QMessageBox.information(self, "Resultado", "Você ganhou!")
                #self.ui.result.setText("ganho")
            else:
                QMessageBox.information(self, "Resultado", "Você perdeu!")
                #self.ui.result.setText("perdeu")
        except:
            QMessageBox.information(self, "Erro", "Aposta inválida!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = CountAposta()
    janela.show()
    sys.exit(app.exec_())