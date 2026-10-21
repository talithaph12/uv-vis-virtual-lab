import os
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Virtual UV-Vis Laboratory | V3",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
  .block-container {padding-top: 1.2rem; padding-bottom: 1.5rem;}
  .hero {padding: 1.25rem 1.4rem; border-radius: 18px;
         background: linear-gradient(120deg,#e5f7f4,#f3f7fb);
         border: 1px solid #d7ebe8; margin-bottom: 1rem;}
  .hero h1 {margin:0; color:#123f46; font-size:2rem;}
  .hero p {margin:.4rem 0 0 0; color:#47646b;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Panel praktikum")
    page = st.radio("Pilih modul", ["Laboratorium 3D", "Panduan penggunaan", "Tentang simulasi"])
    st.divider()
    st.caption("Tahap 3 • Model instrumen, komponen interaktif, dan pembacaan simulasi")
    st.caption("Model edukasi terinspirasi UV-1800; bukan perangkat atau perangkat lunak resmi Shimadzu.")

if page == "Laboratorium 3D":
    st.markdown("""
    <div class="hero">
      <h1>Virtual UV-Vis Laboratory</h1>
      <p>Model 3D interaktif • penjelasan bagian alat • simulasi blanko, sampel, dan spektrum</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("Cara pakai: klik bagian alat untuk membaca fungsinya. Gunakan tab Kontrol untuk membuka kompartemen dan menjalankan simulasi pengukuran.")
    html_path = Path(__file__).parent / "assets" / "uv1800_lab.html"
    if not html_path.exists():
        st.error(f"File model tidak ditemukan: {html_path}. Pastikan assets/uv1800_lab.html ikut diunggah ke GitHub.")
    else:
        html = html_path.read_text(encoding="utf-8")
        components.html(html, height=1450, scrolling=True)

elif page == "Panduan penggunaan":
    st.title("Panduan penggunaan")
    st.markdown("""
    1. **Jelajahi model:** seret mouse untuk memutar, gunakan scroll untuk zoom, lalu klik bagian alat untuk membaca penjelasan.
    2. **Buka kompartemen:** pilih tab Kontrol, kemudian tekan *Buka kompartemen*.
    3. **Masukkan kuvet:** tekan *Masukkan kuvet*. Kuvet hanya dapat dipasang saat kompartemen terbuka.
    4. **Tutup kompartemen:** tutup sebelum melakukan pengukuran.
    5. **Blanko:** pilih Blanko lalu tekan *Jalankan pembacaan blanko* untuk menetapkan referensi simulasi.
    6. **Sampel:** pilih Sampel, masukkan konsentrasi demonstrasi, lalu tekan *Ukur sampel*.
    7. **Spektrum:** jalankan pemindaian untuk melihat kurva absorbansi terhadap panjang gelombang.

    **Catatan ilmiah:** nilai absorbansi, transmitansi, dan spektrum dihasilkan oleh model matematis edukasi. Aplikasi tidak terhubung ke instrumen fisik.
    """)
elif page == "Tentang simulasi":
    st.title("Tentang simulasi")
    st.markdown("""
    Aplikasi ini merupakan rekonstruksi edukasi berbasis Three.js yang terinspirasi dari bentuk umum spektrofotometer UV-Vis Shimadzu UV-1800.

    **Batasan:** geometri bukan CAD resmi, tampilan tidak dimaksudkan untuk identifikasi komponen internal secara servis, dan pembacaan bukan data eksperimen nyata. Proses optik ditampilkan sebagai ilustrasi untuk membantu memahami alur sumber cahaya → pemilih panjang gelombang → kuvet → detektor → pembacaan.
    """)
