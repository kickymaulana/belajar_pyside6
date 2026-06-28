import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot
from random import choice

class AplikasiKita: # Tidak perlu inherit QMainWindow di sini karena kita pakai loader direktori
    def __init__(self) -> None:
        loader: QUiLoader = QUiLoader()
        
        # Memuat UI. Jendela asli Qt Designer dimuat langsung ke self.ui
        self.ui: QMainWindow = loader.load("latihan.ui")
        
        self.inisialisasi_interface()

    def inisialisasi_interface(self) -> None:
        self.ui.setWindowTitle("Aplikasi PySide6 Pertama")

        # Akses komponen langsung dari objek self.ui
        self.btn_halo: QPushButton = self.ui.btn_halo
        self.label_utama: QLabel = self.ui.label_utama

        self.btn_halo.clicked.connect(self.saat_tombol_ditekan)

    @Slot()
    def saat_tombol_ditekan(self) -> None:
        nama: list[str] = ["amba", "arief", "arfy", "nongpal", "namad", "mochie", "vinz"]
        self.label_utama.setText(choice(nama))
        print("label diganti!")


if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    
    # Inisialisasi class
    main_app: AplikasiKita = AplikasiKita()
    
    # Tampilkan jendela ui-nya langsung
    main_app.ui.show()

    # sys.exit memastikan terminal mendapat sinyal exit code (0) saat windows ditutup
    sys.exit(aplikasi.exec())
