import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from ex2 import Ui_MainWindow

class CountIdade(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.avaliarIdade)

    def avaliarIdade(self):

        try:
            idade = int(self.ui.idade.text())

            if (idade < 18):
                self.ui.result.setText("Menor de idade")
            else:
                self.ui.result.setText("Maior de idade")
        except ValueError:
            self.ui.result.setText("Idade inválida! Digite apenas números!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = CountIdade()
    janela.show()
    sys.exit(app.exec_())