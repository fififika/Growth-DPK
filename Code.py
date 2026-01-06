import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
# Menyesuaikan dengan format file Anda (menggunakan sep=None untuk deteksi otomatis)
file_input = 'Growth_DPK.csv'
kolom = ['wilayah', 'cabang', 'nama', 'segment', 'open_cif', 'saldo_lama', 'saldo_baru']

try:
    df = pd.read_csv(file_input, encoding='utf-16', names=kolom, sep=None, engine='python', header=None)
    
    # 2. PEMBERSIHAN DATA (CLEANING)
    for col in ['saldo_lama', 'saldo_baru']:
        # Hapus titik ribuan, ganti koma jadi titik desimal
        df[col] = df[col].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Hapus data yang saldonya kosong dan hitung selisih (Growth)
    df = df.dropna(subset=['saldo_baru', 'saldo_lama']).copy()
    df['selisih'] = df['saldo_baru'] - df['saldo_lama']

    # 3. ANALISIS DATA ======================================================================================
    # A. Saldo Posisi per Cabang *******************************************************************
    cabang_terbesar = df.groupby('cabang')['saldo_baru'].sum().sort_values(ascending=False).reset_index()

    # B. Top 20 Loser (Penurunan saldo terdalam) ************************************************************
    top_20_loser = df.sort_values(by='selisih', ascending=True).head(20)

    # C. Top 20 Gainer (Kenaikan saldo tertinggi) ***********************************************************
    top_20_gainer = df.sort_values(by='selisih', ascending=False).head(20)

    # D. Saldo Poisi per Segment ****************************************************************************
    segment_posisi = df.groupby('segment')['saldo_baru'].sum().sort_values(ascending=False).reset_index()

    # 4. EXPORT HASIL KE CSV ================================================================================
    cabang_terbesar.to_csv('1_Posisi_Saldo_Cabang.csv', index=False, sep=';')
    top_20_loser.to_csv('2_Top_20_Loser.csv', index=False, sep=';')
    top_20_gainer.to_csv('3_Top_20_Gainer.csv', index=False, sep=';')
    print("✅ File CSV berhasil dibuat.")

    # 5. VISUALISASI GRAFIK
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(15, 10))

    # Grafik : Distribusi Saldo per Segment
    plt.subplot(1, 1, 1)
    sns.barplot(data=segment_posisi, x='saldo_baru', y='segment', hue='segment', palette='Blues', legend=False)
    plt.title('Total Saldo Baru Berdasarkan Segment')

    plt.tight_layout()
    plt.savefig('Analisis_DPK_Visual.png')
    plt.show()
    print("✅ Grafik berhasil disimpan sebagai 'Analisis_DPK_Visual.png'.")

except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")