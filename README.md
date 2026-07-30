# 🥗 NutriScale SPPG - Platform Analisis & Perencanaan Gizi Presisi

**NutriScale SPPG** adalah aplikasi web interaktif berbasis Python & Streamlit yang dirancang khusus untuk memenuhi kebutuhan Ahli Gizi di **Satuan Pelayanan Pemenuhan Gizi (SPPG)**. Aplikasi ini mempermudah perhitungan berat kotor/bersih bahan makanan, analisis nilai gizi makro, pencatatan log harian, hingga pengelolaan 1.200+ data bahan makanan berdasarkan **Tabel Komposisi Pangan Indonesia (TKPI)**.

---

## ✨ Fitur Utama

- **📝 Input Menu Harian & Autocomplete Bahan**:
  - Pencarian pintar kata kunci bahan baku dari database TKPI.
  - Perhitungan **% BDD (Bagian Dapat Dimakan)** & Berat Bersih secara otomatis.
  - **Edit Berat Kotor Interaktif (✏️)** langsung di tabel untuk penyesuaian porsi gizi target secara *real-time*.
- **📊 Laporan & Rekapitulasi Gizi Harian**:
  - Filter laporan berdasarkan rentang tanggal penyajian.
  - Akumulasi total gramasi & zat gizi makro (Energi, Protein, Lemak, Karbohidrat).
  - Visualisasi grafik asupan energi harian dan opsi **Unduh Laporan (CSV / Excel)**.
- **📚 Kelola & Update Database Bahan Pangan**:
  - Manajemen 1.200+ data bahan makanan TKPI/DKBM.
  - Penambahan bahan pangan kustom secara manual.
  - Pengeditan langsung nilai gizi per 100g & % BDD.
- **📱 Akses Multi-Platform (PWA Ready)**:
  - Tampilan responsif dengan tema **Full Blue SPPG**.
  - Dapat di-install di Laptop/Desktop (Chrome/Edge) maupun HP (Android & iOS).

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman**: Python 3.10+
* **Framework Frontend**: Streamlit
* **Database**: SQLite3
* **Pengolahan Data**: Pandas, OpenPyXL

---

## 🚀 Cara Menjalankan Aplikasi Secara Lokal

### 1. Clone Repositori
```bash
git clone [https://github.com/rayrachman/nutriscale.git](https://github.com/rayrachman/nutriscale.git)
cd nutriscale
### 2. Install Dependensi
Bash
pip install -r requirements.txt
### 3. Inisialisasi Database
Bash
python database.py
### 4. Jalankan Aplikasi Streamlit
Bash
streamlit run app.py
Aplikasi akan otomatis terbuka di browser Anda pada alamat http://localhost:8501.

## 📦 File Requirements (requirements.txt)
Pastikan Anda memiliki berkas requirements.txt berisi:

Plaintext
streamlit
pandas
openpyxl

## 👨‍💻 Kredit & Pengembang
Dikembangkan oleh @rayrachman Project NutriScale - Solusi Teknologi Digitalisasi Layanan Gizi SPPG.
