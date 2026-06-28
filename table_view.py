import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QStyledItemDelegate, QPushButton, QStyleOptionViewItem
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPainter
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QModelIndex, QRect

# 1. MEMBUAT KELAS DELEGATE (Kustom Komponen untuk Tombol)
class TombolAksiDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    # Fungsi untuk menggambar (paint) tombol di dalam sel tabel
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        # Buat tombol tiruan secara visual di dalam koordinat sel
        rect_tombol: QRect = option.rect.adjusted(5, 2, -5, -2) # Beri padding sedikit
        
        # Gambar kotak tombol (Warna biru khas tombol Edit)
        painter.fillRect(rect_tombol, Qt.GlobalColor.blue)
        
        # Tulis teks di dalam tombol
        painter.setPen(Qt.GlobalColor.white)
        painter.drawText(rect_tombol, Qt.AlignmentFlag.AlignCenter, "Edit")

class AplikasiKita:
    def __init__(self) -> None:
        loader: QUiLoader = QUiLoader()
        self.ui: QMainWindow = loader.load("table_view.ui")
        self.ui.setWindowTitle("QTableView dengan Tombol Edit")
        self.inisialisasi_interface()
        self.muat_data_ke_tabel()

    def inisialisasi_interface(self) -> None:
        self.tabel_karyawan: QTableView = self.ui.tabel_karyawan
        
        # Menghubungkan event klik pada sel tabel
        self.tabel_karyawan.clicked.connect(self.saat_tabel_diklik)

    def muat_data_ke_tabel(self) -> None:
        # Data JSON simulasi dari API Laravel
        list_karyawan: list[dict[str, str]] = [
            {"nik": "MARK-001", "nama": "Kicky Maulana", "jabatan": "IT Supervisor"},
            {"nik": "MARK-002", "nama": "Dedi", "jabatan": "IT Programmer"},
            {"nik": "MARK-003", "nama": "Yildiz", "jabatan": "Graphic Designer"},
            {"nik": "MARK-004", "nama": "Ricky", "jabatan": "IT Manager"}
        ]

        # Membuat Model dengan 4 kolom (Kolom ke-4 untuk Aksi)
        self.model_data: QStandardItemModel = QStandardItemModel(len(list_karyawan), 4)
        self.model_data.setHorizontalHeaderLabels(["NIK", "Nama Lengkap", "Jabatan", "Aksi"])

        for index_baris, karyawan in enumerate(list_karyawan):
            self.model_data.setItem(index_baris, 0, QStandardItem(karyawan["nik"]))
            self.model_data.setItem(index_baris, 1, QStandardItem(karyawan["nama"]))
            self.model_data.setItem(index_baris, 2, QStandardItem(karyawan["jabatan"]))
            
            # Kolom aksi diisi string kosong saja karena nanti digambar oleh Delegate
            self.model_data.setItem(index_baris, 3, QStandardItem(""))

        self.tabel_karyawan.setModel(self.model_data)

        # 2. PASANG DELEGATE TOMBOL KE KOLOM INDEKS 3 (KOLOM KE-4)
        delegate_tombol = TombolAksiDelegate(self.tabel_karyawan)
        self.tabel_karyawan.setItemDelegateForColumn(3, delegate_tombol)

    # 3. MENANGANI EVENT KLIK PADA TOMBOL
    def saat_tabel_diklik(self, index: QModelIndex) -> None:
        # Pastikan yang diklik adalah kolom Aksi (indeks ke-3)
        if index.column() == 3:
            baris: int = index.row()
            
            # Mengambil data NIK dari kolom 0 di baris yang sama
            nik: str = self.model_data.item(baris, 0).text()
            nama: str = self.model_data.item(baris, 1).text()
            
            print(f"Aksi Edit dipicu untuk NIK: {nik} - Nama: {nama}")
            # Di sini nanti tempat Anda memunculkan form edit atau dialog baru


if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiKita = AplikasiKita()
    jendela.ui.show()
    sys.exit(aplikasi.exec())
