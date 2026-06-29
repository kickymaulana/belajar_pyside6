import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QStyledItemDelegate, QPushButton, QStyleOptionViewItem
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPainter
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QModelIndex, QRect
class TombolAksiDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        rect_tombol: QRect = option.rect.adjusted(5, 2, -5, -2)
        painter.fillRect(rect_tombol, Qt.GlobalColor.blue)
        painter.setPen(Qt.GlobalColor.white)
        painter.drawText(rect_tombol, Qt.AlignmentFlag.AlignCenter, "Edit")
class AplikasiKita:
    def __init__(self) -> None:
        loader: QUiLoader = QUiLoader()
        self.ui: QMainWindow = loader.load("table_view.ui")
        self.ui.setWindowTitle("Belajar table view")
        self.inisialisasi_interface()
        self.muat_data_ke_table()
    def inisialisasi_interface(self) -> None:
        self.table_karyawan: QTableView = self.ui.table_karyawan
        self.table_karyawan.verticalHeader().setVisible(False)
        self.table_karyawan.clicked.connect(self.saat_tombol_diklik)
    def muat_data_ke_table(self) -> None:
        list_karyawan: list[dict[str, str]] = [
                {"nik": "123456789012346", "nama": "Kicky Maulana", "jabatan": "Programmer"},
                {"nik": "123456789012341", "nama": "Dedi Maulana", "jabatan": "Programmer"},
                {"nik": "123456789012342", "nama": "Yildiz Maulana", "jabatan": "Programmer"},
                ]
        self.model_data: QStandardItemModel = QStandardItemModel(len(list_karyawan), 4)
        self.model_data.setHorizontalHeaderLabels(["Nik", "Nama LENGKAP", "Jabatan", "Aksi"])
        for index_baris, karyawan in enumerate(list_karyawan):
            self.model_data.setItem(index_baris, 0, QStandardItem(karyawan["nik"]))
            self.model_data.setItem(index_baris, 1, QStandardItem(karyawan["nama"]))
            self.model_data.setItem(index_baris, 2, QStandardItem(karyawan["jabatan"]))
            self.model_data.setItem(index_baris, 3, QStandardItem(""))
        self.table_karyawan.setModel(self.model_data)
        delegate_tombol = TombolAksiDelegate(self.table_karyawan)
        self.table_karyawan.setItemDelegateForColumn(3, delegate_tombol)
    def saat_tombol_diklik(self, index: QModelIndex) -> None:
        if index.column() == 3:
            baris: int = index.row()
            nik: str = self.model_data.item(baris, 0).text()
            nama: str = self.model_data.item(baris, 1).text()
            print(f"Aksi Edit dipicu untuk nik: {nik} nama: {nama}")
if __name__ == "__main__":
    aplikasi: QApplication = QApplication(sys.argv)
    jendela: AplikasiKita = AplikasiKita()
    jendela.ui.show()
    sys.exit(aplikasi.exec())
