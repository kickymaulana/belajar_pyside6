import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Slot

class AplikasiSimpel(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.base_url: str = "http://localhost/laravel_api/public/api/users?limit=10"

        self.url_sebelumnya = None
        self.url_berikutnya = None

        self.inisialisasi_interface()

    def inisialisasi_interface(self) -> None:
        self.setWindowTitle("Belajar Table PySide6 - Tanpa No Urut")
        self.setGeometry(300, 300, 550, 350)

        self.table_users: QTableWidget = QTableWidget(self)
        self.table_users.setColumnCount(2)
        self.table_users.setHorizontalHeaderLabels(["Nama", "Email"])
        self.table_users.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.tombol_prev: QPushButton = QPushButton("Sebelum", self)
        self.tombol_next: QPushButton = QPushButton("Berikut", self)

        self.tombol_prev.clicked.connect(self.muat_prev)
        self.tombol_next.clicked.connect(self.muat_next)

        layout_tombol: QHBoxLayout = QHBoxLayout()
        layout_tombol.addWidget(self.tombol_prev)
        layout_tombol.addWidget(self.tombol_next)
        
        layout_utama: QVBoxLayout = QVBoxLayout()
        layout_utama.addWidget(self.table_users)
        layout_utama.addLayout(layout_tombol)

        self.setLayout(layout_utama)

        self.ambil_data(self.base_url)

    def ambil_data(self, url_target: str) -> None:
        if not url_target:
            return
        try:
            headers = {
                "Accept": "application/json"
            }
            respons = requests.get(url_target, headers=headers)

            if respons.status_code == 200:
                data_json = respons.json()
                daftar_user = data_json.get("data", [])

                links = data_json.get("links", {})
                self.url_sebelumnya = links.get("prev")
                self.url_berikutnya = links.get("next")

                self.tombol_prev.setEnabled(self.url_sebelumnya is not None)
                self.tombol_next.setEnabled(self.url_berikutnya is not None)

                self.table_users.setRowCount(len(daftar_user))
                self.table_users.verticalHeader().setVisible(False)

                for baris, user in enumerate(daftar_user):

                    self.table_users.setItem(baris, 0, QTableWidgetItem(user.get("name")))
                    self.table_users.setItem(baris, 1, QTableWidgetItem(user.get("email")))

        except Exception as e:
            print(f"Error: {e}")

    @Slot()
    def muat_prev(self) -> None:
        self.ambil_data(self.url_sebelumnya)

    @Slot()
    def muat_next(self) -> None:
        self.ambil_data(self.url_berikutnya)


if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiSimpel = AplikasiSimpel()
    jendela.show()
    sys.exit(aplikasi.exec())
