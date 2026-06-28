import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot

class AplikasiKita:
    def __init__(self) -> None:
        loader: QUiLoader = QUiLoader()
        self.ui: QMainWindow = loader.load("latihan.ui")
        self.ui.setWindowTitle("Latihan QComboBox")
        self.inisialisasi_interface()
    def inisialisasi_interface(self) -> None:
        self.btn_halo: QPushButton = self.ui.btn_halo
        self.label_utama: QLabel = self.ui.label_utama
        self.input_nama: QLineEdit = self.ui.input_nama
        self.combo_jabatan: QComboBox = self.ui.combo_jabatan
        self.combo_jabatan.clear()
        self.combo_jabatan.addItems(["It Manager", "IT Supervisor", "Qc Manager"])
        self.btn_halo.clicked.connect(self.saat_tombol_ditekan)
    @Slot()
    def saat_tombol_ditekan(self) -> None:
        nama_inputan: str = self.input_nama.text()
        jabatan_terpilih: str = self.combo_jabatan.currentText()

        if nama_inputan.strip() == "":
            self.label_utama.setText("isi dulu namanya")
        else:
            self.label_utama.setText(f"Selamat datang {nama_inputan} ({jabatan_terpilih})")
            print(f"Data di proses {nama_inputan} {jabatan_terpilih}")
if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiKita = AplikasiKita()
    jendela.ui.show()
    sys.exit(aplikasi.exec())
