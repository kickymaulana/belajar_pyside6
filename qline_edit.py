import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot

class AplikasiKita:
    def __init__(self) -> None:
        loader: QUiLoader = QUiLoader()
        self.ui: QMainWindow = loader.load("latihan.ui")
        self.ui.setWindowTitle("Belajar input PySide6")
        self.inisialisasi_interface()
    def inisialisasi_interface(self) -> None:
        self.btn_halo: QPushButton = self.ui.btn_halo
        self.label_utama: QLabel = self.ui.label_utama
        self.input_nama: QLineEdit = self.ui.input_nama
        self.btn_halo.clicked.connect(self.saat_tombol_ditekan)
    @Slot()
    def saat_tombol_ditekan(self) -> None:
        nama_inputan: str = self.input_nama.text()
        if nama_inputan.strip() == "":
            self.label_utama.setText("Tolong isi dulu namanya bos")
        else:
            self.label_utama.setText(f"Halo, Selamat datang {nama_inputan}")
            print(f"User menginput {nama_inputan}")

if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiKita = AplikasiKita()
    jendela.ui.show()
    sys.exit(aplikasi.exec())
