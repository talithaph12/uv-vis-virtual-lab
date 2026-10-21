import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Virtual UV-Vis Laboratory",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
  .block-container {padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1500px;}
  .hero {padding: 1.25rem 1.5rem; border-radius: 18px; background: linear-gradient(120deg,#e8f7f4,#f3f7fb); border: 1px solid #d6e9e6; margin-bottom: 1rem;}
  .hero h1 {margin: 0; color: #153d43; font-size: 2rem;}
  .hero p {margin: .4rem 0 0 0; color: #365b60;}
  .small-note {color: #667085; font-size: .88rem;}
  div[data-testid="stMetric"] {border: 1px solid #e6eaf0; padding: 12px; border-radius: 12px;}
</style>
<div class="hero">
  <h1>🧪 Virtual UV-Vis Laboratory</h1>
  <p>Laboratorium virtual interaktif — model edukasi yang terinspirasi dari Shimadzu UV-1800.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Panel praktikum")
    page = st.radio(
        "Pilih modul",
        ["Laboratorium 3D", "Panduan penggunaan", "Tentang simulasi"],
        index=0
    )
    st.divider()
    st.caption("Tahap 2 • Model instrumen dan komputer virtual")
    st.caption("Model edukasi, bukan perangkat atau perangkat lunak resmi Shimadzu.")

if page == "Laboratorium 3D":
    st.subheader("Instrumen dan workstation")
    st.write("Putar model dengan menyeret mouse, gunakan scroll untuk zoom, lalu gunakan kontrol untuk membuka kompartemen dan menjalankan simulasi.")
    html_path = os.path.join(os.path.dirname(__file__), "assets", "uv1800_lab.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    components.html(html, height=1200, scrolling=False)
    st.markdown(
        '<p class="small-note">Petunjuk: gunakan tombol “Buka kompartemen”, “Masukkan kuvet”, “Tutup kompartemen”, dan “Ukur sampel” di dalam simulasi. '
        'Hasil numerik merupakan data demonstrasi, bukan pengukuran instrumen sungguhan.</p>',
        unsafe_allow_html=True
    )

elif page == "Panduan penggunaan":
    st.subheader("Alur kerja praktikum virtual")
    steps = [
        ("1. Persiapan", "Pastikan model instrumen dan workstation terlihat. Kenali panel depan, layar, kompartemen kuvet, serta perangkat lunak virtual."),
        ("2. Buka kompartemen", "Klik tombol untuk membuka tutup kompartemen. Model memperlihatkan dudukan kuvet di bagian dalam."),
        ("3. Masukkan kuvet", "Klik tombol memasukkan kuvet. Kuvet demonstrasi akan muncul pada dudukannya."),
        ("4. Tutup kompartemen", "Tutup kembali kompartemen sebelum pengukuran dimulai."),
        ("5. Atur pengukuran", "Gunakan panel komputer virtual untuk memilih panjang gelombang dan mode pengukuran."),
        ("6. Jalankan simulasi", "Klik Ukur Sampel untuk menampilkan hasil demonstrasi pada layar perangkat lunak dan panel instrumen."),
    ]
    for title, desc in steps:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.write(desc)
    st.info("Dalam penggunaan nyata, prosedur blanko, pemilihan panjang gelombang, penanganan kuvet, dan keselamatan harus mengikuti SOP laboratorium serta manual instrumen.")

else:
    st.subheader("Tentang simulator")
    st.write("""
    Aplikasi ini merupakan media pembelajaran untuk membantu mahasiswa mengenali bentuk instrumen UV-Vis dan memahami urutan kerja analisis secara visual.

    **Batasan versi ini**
    - Bentuk instrumen adalah model 3D perkiraan yang dibuat dari geometri dasar.
    - Komputer dan antarmuka pengukuran adalah tampilan perangkat lunak fiktif untuk pendidikan.
    - Nilai absorbansi/transmitansi yang tampil adalah nilai simulasi.
    - Belum ada koneksi fisik ke spektrofotometer atau komunikasi dengan perangkat keras.
    """)
    st.write("Pengembangan berikutnya dapat menambahkan simulasi blanko dan sampel, hukum Beer-Lambert, kurva kalibrasi, regresi linear, dan perhitungan kadar.")
