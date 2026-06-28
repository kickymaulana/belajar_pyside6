import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot
from random import choice


class AplikasiKita:
    def __init__(self) -> None:
        loader: QUiLoader = QUiLoader()
        self.ui: QMainWindow = loader.load("latihan.ui")
        self.ui.setWindowTitle("Aplikasi PySide6 Pertama")
        self.inisialisasi_interface()
    def inisialisasi_interface(self) -> None:
        self.btn_halo: QPushButton = self.ui.btn_halo
        self.label_utama: QLabel = self.ui.label_utama
        self.btn_halo.clicked.connect(self.saat_tombol_ditekan)
    @Slot()
    def saat_tombol_ditekan(self) -> None:
        nama: list[str] = ["kicky", "yildi", "dedi", "ricky"]
        self.label_utama.setText(choice(nama))
        print("label diganti")
if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiKita = AplikasiKita()
    jendela.ui.show()

    sys.exit(aplikasi.exec())
