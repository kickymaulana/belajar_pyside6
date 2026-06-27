import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Slot

class AplikasiSimpel(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # URL & Token Laravel kamu
        self.base_url: str = "http://localhost/laravel_api/public/api/users?limit=2"
        self.token: str = "Bearer 1|GTaxCcsNorLVn34Cek0KEGDxR8qm6sXqO9WAoqsZ6387c3f5"
        
        # Variabel penampung link page selanjutnya/sebelumnya
        self.url_sebelumnya = None
        self.url_berikutnya = None
        
        self.inisialisasi_interface()

    def inisialisasi_interface(self) -> None:
        self.setWindowTitle("Belajar Tabel PySide6 Simpel")
        self.setGeometry(300, 300, 500, 350)

        # 1. BIKIN TABEL & SETTING AGAR TIDAK BISA DIEDIT LANGSUNG
        self.tabel_users: QTableWidget = QTableWidget(self)
        self.tabel_users.setColumnCount(2) # Cukup 2 kolom dulu (Nama & Email) biar simpel
        self.tabel_users.setHorizontalHeaderLabels(["Nama", "Email"])
        
        # Opsi Kunci: Ini yang membuat tabel TIDAK BISA double-click edit (Read-Only)
        self.tabel_users.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        # 2. BIKIN TOMBOL PAGINATION
        self.tombol_prev: QPushButton = QPushButton("⬅ Sebelum", self)
        self.tombol_next: QPushButton = QPushButton("Berikut ➡", self)
        
        self.tombol_prev.clicked.connect(self.muat_prev)
        self.tombol_next.clicked.connect(self.muat_next)

        # 3. SUSUN LAYOUT
        layout_tombol: QHBoxLayout = QHBoxLayout()
        layout_tombol.addWidget(self.tombol_prev)
        layout_tombol.addWidget(self.tombol_next)

        layout_utama: QVBoxLayout = QVBoxLayout()
        layout_utama.addWidget(self.tabel_users) # Tabel di atas
        layout_utama.addLayout(layout_tombol)     # Tombol di bawah
        
        self.setLayout(layout_utama)

        # Jalankan fungsi ambil data pertama kali dibuka
        self.ambil_data(self.base_url)

    # --- FUNGSI UTAMA AMBIL DATA ---
    def ambil_data(self, url_target: str) -> None:
        if not url_target:
            return

        try:
            headers = {
                "Accept": "application/json",
                # "Authorization": self.token
            }
            respons = requests.get(url_target, headers=headers)
            
            if respons.status_code == 200:
                data_json = respons.json()
                daftar_user = data_json.get("data", [])
                
                # Simpan link navigasi dari Laravel
                links = data_json.get("links", {})
                self.url_sebelumnya = links.get("prev")
                self.url_berikutnya = links.get("next")

                # Aktifkan atau matikan tombol secara otomatis
                self.tombol_prev.setEnabled(self.url_sebelumnya is not None)
                self.tombol_next.setEnabled(self.url_berikutnya is not None)

                # Set jumlah baris tabel sesuai total data yang diterima dari API
                self.tabel_users.setRowCount(len(daftar_user))

                # Masukkan data ke dalam kotak-kotak tabel
                for baris, user in enumerate(daftar_user):
                    self.tabel_users.setItem(baris, 0, QTableWidgetItem(user.get("name")))
                    self.tabel_users.setItem(baris, 1, QTableWidgetItem(user.get("email")))
                    
        except Exception as e:
            print(f"Error: {e}")

    # --- SLOT TOMBOL NAVIGASI ---
    @Slot()
    def muat_prev(self) -> None:
        self.ambil_data(self.url_sebelumnya)

    @Slot()
    def muat_next(self) -> None:
        self.ambil_data(self.url_berikutnya)

if __name__ == "__main__":
    aplikasi = QApplication(sys.argv)
    jendela = AplikasiSimpel()
    jendela.show()
    sys.exit(aplikasi.exec())
