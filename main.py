import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

# 1. Setiap aplikasi PySide6 HARUS memiliki satu objek QApplication
app = QApplication(sys.argv)

# 2. membuat main window (jendela utama)
window = QMainWindow()
window.setWindowTitle("Aplikasi Pertama PySide6")
window.resize(400, 200)  # lebar 400px tinggi 200px

# 3. membuat konten dalam jendela
# karea QMainWindow butuh satu "Central Widget", kita buat penampung dulu
central_widget = QWidget()
window.setCentralWidget(central_widget)

# membuat layout vertical (menyusun komponen dari atas ke bawah)
layout = QVBoxLayout()

# membuat komponen (Widget)
label_halo = QLabel("Halo, Selamat data di PySide6!")
tombol_klik = QPushButton("Klik aku")

# memasukan komponen ke dalam layout
layout.addWidget(label_halo)
layout.addWidget(tombol_klik)

# pasang layout ke central widget
central_widget.setLayout(layout)

# 4. tampilkan jendela ke layar
window.show()

# 5. jalankan event loop aplikasi agar program tidak langsung tertutup
sys.exit(app.exec())

