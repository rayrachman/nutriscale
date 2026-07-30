# calculator.py

def konversi_berat(berat_input: float, bdd: float, tipe_input: str = "kotor"):
    """
    tipe_input: 'kotor' (diubah ke bersih) atau 'bersih' (diubah ke kotor)
    """
    if bdd <= 0:
        bdd = 100.0
        
    if tipe_input == "kotor":
        berat_kotor = berat_input
        berat_bersih = berat_input * (bdd / 100.0)
    else:
        berat_bersih = berat_input
        berat_kotor = berat_input / (bdd / 100.0)
        
    return round(berat_kotor, 1), round(berat_bersih, 1)

def analisis_menu(daftar_bahan_terpilih: list, target_kebutuhan: dict):
    total_kalori = 0.0
    total_protein = 0.0
    total_lemak = 0.0
    total_karbo = 0.0
    
    rincian_menu = []
    
    for item in daftar_bahan_terpilih:
        bdd = item.get('bdd', 100.0)
        tipe_input = item.get('tipe_input', 'kotor')
        berat_val = item.get('berat_gram', 100.0)
        
        berat_kotor, berat_bersih = konversi_berat(berat_val, bdd, tipe_input)
        
        # Kandungan gizi selalu dihitung dari BERAT BERSIH
        faktor = berat_bersih / 100.0
        
        kal = item['kalori'] * faktor
        prot = item['protein'] * faktor
        lem = item['lemak'] * faktor
        karb = item['karbohidrat'] * faktor
        
        total_kalori += kal
        total_protein += prot
        total_lemak += lem
        total_karbo += karb
        
        rincian_menu.append({
            "nama": item['nama'],
            "bdd_pct": bdd,
            "berat_kotor_g": berat_kotor,
            "berat_bersih_g": berat_bersih,
            "kalori": round(kal, 1),
            "protein": round(prot, 1),
            "lemak": round(lem, 1),
            "karbo": round(karb, 1)
        })
        
    pct_kalori = (total_kalori / target_kebutuhan['target_kalori']) * 100 if target_kebutuhan['target_kalori'] > 0 else 0
    pct_protein = (total_protein / target_kebutuhan['target_protein']) * 100 if target_kebutuhan['target_protein'] > 0 else 0
    pct_lemak = (total_lemak / target_kebutuhan['target_lemak']) * 100 if target_kebutuhan['target_lemak'] > 0 else 0
    pct_karbo = (total_karbo / target_kebutuhan['target_karbo']) * 100 if target_kebutuhan['target_karbo'] > 0 else 0
    
    return {
        "rincian_menu": rincian_menu,
        "total_asupan": {
            "kalori": round(total_kalori, 1),
            "protein": round(total_protein, 1),
            "lemak": round(total_lemak, 1),
            "karbo": round(total_karbo, 1)
        },
        "persentase_akg": {
            "kalori_pct": round(pct_kalori, 1),
            "protein_pct": round(pct_protein, 1),
            "lemak_pct": round(pct_lemak, 1),
            "karbo_pct": round(pct_karbo, 1)
        }
    }