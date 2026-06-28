import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout
from PySide6.QtCore import Qt, Slot


class AplikasiKita(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inisialisasi_interface()

    def inisialisasi_interface(self) -> None:
        self.setWindowTitle("Aplikasi Kita")
        self.setGeometry(300, 300, 500, 400)

        self.layout_tumpukan: QStackedLayout = QStackedLayout()
        
        self.halaman_beranda: QWidget = QWidget()
        label_beranda: QLabel = QLabel("Selamat datang di beranda kita", self.halaman_beranda)
        label_beranda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_beranda: QVBoxLayout = QVBoxLayout()
        layout_beranda.addWidget(label_beranda)
        self.halaman_beranda.setLayout(layout_beranda)

        self.halaman_profil: QWidget = QWidget()
        label_profil: QLabel = QLabel("Halaman Profil", self.halaman_profil)
        label_profil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_profil: QVBoxLayout = QVBoxLayout()
        layout_profil.addWidget(label_profil)
        self.halaman_profil.setLayout(layout_profil)

        self.layout_tumpukan.addWidget(self.halaman_beranda)
        self.layout_tumpukan.addWidget(self.halaman_profil)

        self.tombol_beranda: QPushButton = QPushButton("Beranda", self)
        self.tombol_beranda.clicked.connect(lambda: self.ganti_halaman(0))
        self.tombol_profil: QPushButton = QPushButton("Profil", self)
        self.tombol_profil.clicked.connect(lambda: self.ganti_halaman(1))

        self.layout_tombol: QHBoxLayout = QHBoxLayout()
        self.layout_tombol.addWidget(self.tombol_beranda)
        self.layout_tombol.addWidget(self.tombol_profil)
        self.layout_tombol.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layout_utama: QVBoxLayout = QVBoxLayout()
        self.layout_utama.addLayout(self.layout_tombol)
        self.layout_utama.addLayout(self.layout_tumpukan)

        self.setLayout(self.layout_utama)

    @Slot()
    def ganti_halaman(self, index_halaman: int) -> None:
        self.layout_tumpukan.setCurrentIndex(index_halaman)

if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiKita = AplikasiKita()
    jendela.show()

    sys.exit(aplikasi.exec())
