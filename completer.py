import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QCompleter
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot, Qt

class AplikasiKita:
    def __init__(self) -> None:
        loader: QUiLoader = QUiLoader()
        self.ui: QMainWindow = loader.load("latihan.ui")
        self.ui.setWindowTitle("Completer")
        self.inisialisasi_interface()
    def inisialisasi_interface(self) -> None:
        self.btn_halo: QPushButton = self.ui.btn_halo
        self.label_utama: QLabel = self.ui.label_utama
        self.input_nama: QLineEdit = self.ui.input_nama
        self.combo_jabatan: QComboBox = self.ui.combo_jabatan
        self.combo_jabatan.setEditable(True)
        completer: QCompleter = QCompleter(self.combo_jabatan.model(), self.combo_jabatan)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.combo_jabatan.setCompleter(completer)
        self.combo_jabatan.clear()
        list_jabatan: list[dict[str, str]] = [
                {"id": "1", "nama": "Supervisor IT"},
                {"id": "2", "nama": "Programmer Handal"},
                {"id": "3", "nama": "Tukang Suruh"},
                ]
        for item in list_jabatan:
            self.combo_jabatan.addItem(item["nama"], item["id"])
        self.btn_halo.clicked.connect(self.saat_tombol_ditekan)
    @Slot()
    def saat_tombol_ditekan(self) -> None:
        nama_inputan: str = self.input_nama.text()
        text_jabatan: str = self.combo_jabatan.currentText()
        id_jabatan: str = self.combo_jabatan.currentData()
        if nama_inputan.strip() == "":
            self.label_utama.setText("Isi dulu namanya")
        else:
            self.label_utama.setText(f"Selamat datang {nama_inputan} { text_jabatan}")
            print(f"id nya adlalah {id_jabatan}")
if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiKita = AplikasiKita()
    jendela.ui.show()
    sys.exit(aplikasi.exec())
