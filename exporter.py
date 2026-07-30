# exporter.py

import io
import pandas as pd
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def export_to_excel(data_pasien: dict, rincian_menu: list, total_asupan: dict, target_akg: dict) -> io.BytesIO:
    """
    Menghasilkan file Excel (.xlsx) dalam bentuk BytesIO buffer (siap di-download di Streamlit).
    """
    output = io.BytesIO()
    
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Sheet 1: Profil Pasien & Ringkasan Target
        df_pasien = pd.DataFrame([data_pasien])
        df_pasien.to_excel(writer, sheet_name='Profil & Target', index=False)
        
        # Sheet 2: Tabel Menu Harian
        df_menu = pd.DataFrame(rincian_menu)
        
        # Tambahkan Baris Total
        baris_total = {
            "nama": "TOTAL ASUPAN",
            "berat_g": df_menu['berat_g'].sum() if not df_menu.empty else 0,
            "kalori": total_asupan['kalori'],
            "protein": total_asupan['protein'],
            "lemak": total_asupan['lemak'],
            "karbo": total_asupan['karbo']
        }
        df_menu_final = pd.concat([df_menu, pd.DataFrame([baris_total])], ignore_index=True)
        df_menu_final.to_excel(writer, sheet_name='Rincian Menu', index=False)

    output.seek(0)
    return output


def export_to_word(data_pasien: dict, rincian_menu: list, total_asupan: dict, persentase_akg: dict) -> io.BytesIO:
    """
    Menghasilkan dokumen Laporan Word (.docx) dalam bentuk BytesIO buffer.
    """
    doc = Document()
    
    # Judul Laporan
    title = doc.add_heading('LAPORAN PERENCANAAN MENU GIZI (SPPG)', level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Section 1: Profil Klien
    doc.add_heading('1. Profil Klien & Target AKG', level=1)
    p = doc.add_paragraph()
    p.add_run(f"Nama Klien     : {data_pasien.get('Nama', '-')}\n").bold = True
    p.add_run(f"Usia           : {data_pasien.get('Usia', '-')} Tahun\n")
    p.add_run(f"Jenis Kelamin  : {data_pasien.get('Jenis Kelamin', '-')}\n")
    p.add_run(f"BB / TB        : {data_pasien.get('Berat Badan (kg)', '-')} kg / {data_pasien.get('Tinggi Badan (cm)', '-')} cm\n")
    p.add_run(f"Target Kalori  : {data_pasien.get('Target Kalori (kcal)', '-')} kcal/hari\n")
    
    # Section 2: Tabel Rincian Menu
    doc.add_heading('2. Rincian Menu Makanan', level=1)
    
    table = doc.add_table(rows=1, cols=6)
    table.style = 'Table Grid'
    
    # Header Tabel
    hdr_cells = table.rows[0].cells
    headers = ['Nama Bahan', 'Berat (g)', 'Kalori (kcal)', 'Protein (g)', 'Lemak (g)', 'Karbo (g)']
    for i, header_text in enumerate(headers):
        hdr_cells[i].text = header_text
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        
    # Isi Data Menu
    for item in rincian_menu:
        row_cells = table.add_row().cells
        row_cells[0].text = str(item['nama'])
        row_cells[1].text = str(item['berat_g'])
        row_cells[2].text = str(item['kalori'])
        row_cells[3].text = str(item['protein'])
        row_cells[4].text = str(item['lemak'])
        row_cells[5].text = str(item['karbo'])
        
    # Section 3: Evaluasi AKG
    doc.add_heading('3. Evaluasi Pemenuhan Nutrisi', level=1)
    p_eval = doc.add_paragraph()
    p_eval.add_run(f"• Total Kalori: {total_asupan['kalori']} kcal ({persentase_akg['kalori_pct']}% Target)\n")
    p_eval.add_run(f"• Total Protein: {total_asupan['protein']} g ({persentase_akg['protein_pct']}% Target)\n")
    p_eval.add_run(f"• Total Lemak: {total_asupan['lemak']} g ({persentase_akg['lemak_pct']}% Target)\n")
    p_eval.add_run(f"• Total Karbohidrat: {total_asupan['karbo']} g ({persentase_akg['karbo_pct']}% Target)\n")
    
    # Output Buffer
    output = io.BytesIO()
    doc.save(output)
    output.seek(0)
    return output