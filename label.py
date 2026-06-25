import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt, Slot
from random import choice


class ApikasiKita(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inisialisasi_interface()

    def inisialisasi_interface(self) -> None:
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle("Aplikasi PySide6 Pertama")

        self.label_utama: QLabel = QLabel("Wello apa kabar", self)
        self.label_utama.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_utama.setStyleSheet("""
                                       font-size: 18px;
                                       font-weight: bold;
                                       color: #2c3e50;
                                       padding: 20px;
                                       """)

        self.tombol_aksi: QPushButton = QPushButton("Klik untuk ganti si label", self)
        self.tombol_aksi.setStyleSheet("""
                                       font-size: 16px;
                                       background-color: #3494db;
                                       color: white;
                                       border-radius: 8px;
                                       padding: 10px;
                                       """)
        self.tombol_aksi.clicked.connect(self.saat_tombol_ditekan)

        self.layout_utama: QVBoxLayout = QVBoxLayout()
        self.layout_utama.addWidget(self.label_utama)
        self.layout_utama.addWidget(self.tombol_aksi)
        self.setLayout(self.layout_utama)

    @Slot()
    def saat_tombol_ditekan(self) -> None:
        nama: list[str] = [
            "amba",
            "arief",
            "arfy",
            "nongpal",
            "namad",
            "mochie",
            "vinz",
        ]
        self.label_utama.setText(choice(nama))
        print("label diganti!")


if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: ApikasiKita = ApikasiKita()
    jendela.show()

    sys.exit(aplikasi.exec())
