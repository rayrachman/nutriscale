# 🥗 NutriScale SPPG — Platform Analisis & Perencanaan Gizi Presisi
NutriScale SPPG adalah aplikasi web interaktif berbasis Python dan Streamlit yang dirancang khusus untuk memenuhi kebutuhan Ahli Gizi di Satuan Pelayanan Pemenuhan Gizi (SPPG).

Aplikasi ini mempermudah perhitungan berat kotor/bersih bahan makanan, analisis nilai gizi makro, pencatatan log harian, hingga pengelolaan 1.200+ data bahan makanan berdasarkan Tabel Komposisi Pangan Indonesia (TKPI).

## ✨ Fitur Utama
📝 Input Menu Harian & Autocomplete Bahan
Pencarian Cerdas: Autocomplete kata kunci bahan baku langsung dari database TKPI.

Kalkulasi Otomatis: Perhitungan % BDD (Bagian Dapat Dimakan) dan Berat Bersih secara presisi.

Penyuntingan Interaktif (✏️): Ubah Berat Kotor langsung di dalam tabel untuk penyesuaian porsi target gizi secara real-time.

## 📊 Laporan & Rekapitulasi Gizi Harian
Filter Tanggal: Penyaringan laporan berbasis rentang tanggal penyajian.

Akumulasi Makronutrisi: Rekap total gramasi dan nilai gizi makro (Energi, Protein, Lemak, Karbohidrat).

Visualisasi & Ekspor: Grafik tren asupan energi harian serta opsi ekspor laporan ke format CSV dan Excel.

## 📚 Kelola Database Bahan Pangan
Master Data TKPI/DKBM: Akses dan kelola 1.200+ basis data pangan Indonesia.

Bahan Kustom: Fitur penambahan bahan pangan baru secara manual.

Editor Nilai Gizi: Pembaruan nilai gizi per 100g dan % BDD secara dinamis.

## 📱 Akses Multi-Platform (PWA Ready)
Desain Responsif: Tampilan modern dengan tema Full Blue SPPG.

Lintas Perangkat: Dapat diinstal sebagai aplikasi di Laptop/Desktop (Chrome/Edge) maupun ponsel pintar (Android & iOS).

## 🛠️ Teknologi & Pustaka
Bahasa Pemrograman: Python 3.10+

Framework Frontend: Streamlit

Database: SQLite3

Pengolahan & Ekspor Data: Pandas, OpenPyXL

## 📁 Struktur Direktori Proyek
Plaintext
nutriscale/
├── app.py              # Berkas utama aplikasi Streamlit
├── database.py         # Skrip inisialisasi & manajemen database SQLite3
├── requirements.txt    # Daftar dependensi modul Python
└── README.md           # Dokumentasi proyek

## 🚀 Cara Menjalankan Aplikasi Secara Lokal
### 1. Clone Repositori
```bash
git clone [https://github.com/rayrachman/nutriscale.git](https://github.com/rayrachman/nutriscale.git)
cd nutriscale

### 2. Buat & Aktifkan Virtual Environment (Disarankan)
Linux / macOS:
Bash
python3 -m venv venv
source venv/bin/activate
Windows:
Bash
python -m venv venv
venv\Scripts\activate

### 3. Install Dependensi
Bash
pip install -r requirements.txt

### 4. Inisialisasi Database
Bash
python database.py

### 5. Jalankan Aplikasi
Bash
streamlit run app.py

### 💡 Informasi: Aplikasi akan otomatis terbuka di peramban web Anda pada alamat http://localhost:8501.

## 📦 Berkas Dependensi (requirements.txt)
Daftar modul yang dibutuhkan untuk menjalankan proyek ini:

Plaintext
streamlit
pandas
openpyxl

## 👨‍💻 Kredit & Pengembang
Pengembang Utama: @rayrachman

Proyek: NutriScale — Solusi Teknologi Digitalisasi Layanan Gizi SPPG.
