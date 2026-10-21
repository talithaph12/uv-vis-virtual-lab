import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Virtual UV-Vis Laboratory",
    page_icon="🧪",
    layout="wide",
)

st.markdown("""
<style>
    .block-container {padding-top: 1.4rem; padding-bottom: 2rem;}
    .hero {
        padding: 1.2rem 1.4rem;
        border: 1px solid rgba(120, 140, 150, .25);
        border-radius: 18px;
        background: linear-gradient(135deg, rgba(219,244,241,.75), rgba(246,250,250,.7));
        margin-bottom: 1rem;
    }
    .hero h1 { margin: 0 0 .35rem 0; }
    .muted { color: #53636b; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🧪 Virtual UV-Vis Laboratory</h1>
  <div class="muted">Laboratorium virtual untuk mengenal instrumen UV-Vis secara interaktif.</div>
</div>
""", unsafe_allow_html=True)

st.info(
    "Tahap 1: eksplorasi model 3D. Model ini merupakan ilustrasi edukasi yang "
    "terinspirasi dari bentuk luar Shimadzu UV-1800, bukan replika teknis resmi."
)

tab_model, tab_guide = st.tabs(["🔎 Eksplorasi Model 3D", "📘 Petunjuk Penggunaan"])

with tab_model:
    left, right = st.columns([3, 1], gap="large")
    with left:
        html = r"""
<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  html, body { margin:0; width:100%; height:100%; overflow:hidden; font-family:Arial,sans-serif; background:#eef4f5; }
  #stage { position:relative; width:100%; height:540px; }
  canvas { display:block; width:100%; height:100%; }
  #hint { position:absolute; top:12px; left:12px; background:rgba(255,255,255,.92); padding:9px 12px; border-radius:10px; font-size:12px; color:#33434a; box-shadow:0 2px 10px #00000010; }
  #label { position:absolute; left:12px; bottom:12px; max-width:78%; background:rgba(255,255,255,.96); padding:12px 14px; border-radius:12px; color:#26363c; box-shadow:0 2px 12px #00000012; font-size:13px; line-height:1.45; }
  #label strong { display:block; font-size:15px; margin-bottom:3px; }
  #reset { position:absolute; top:12px; right:12px; border:1px solid #d0dcdf; border-radius:9px; padding:8px 10px; background:white; cursor:pointer; color:#26363c; }
  #reset:hover { background:#f7fbfb; }
</style>
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/"
  }
}
</script>
</head>
<body>
<div id="stage">
  <div id="hint">Drag: putar alat · Scroll: zoom · Klik bagian untuk mengenalinya</div>
  <button id="reset">Atur ulang tampilan</button>
  <div id="label"><strong>Model UV-Vis</strong>Pilih layar, tombol, casing, atau kompartemen sampel pada model.</div>
</div>
<script type="module">
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const stage = document.getElementById('stage');
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xeef4f5);
const camera = new THREE.PerspectiveCamera(42, stage.clientWidth/stage.clientHeight, 0.1, 100);
camera.position.set(5.6, 4.1, 7.3);

const renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(stage.clientWidth, stage.clientHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
stage.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.target.set(0, 1.05, 0);
controls.minDistance = 4;
controls.maxDistance = 13;

scene.add(new THREE.HemisphereLight(0xffffff, 0x9aaab0, 2.0));
const keyLight = new THREE.DirectionalLight(0xffffff, 2.2);
keyLight.position.set(4, 8, 5);
scene.add(keyLight);

const floor = new THREE.Mesh(
  new THREE.PlaneGeometry(200,200),
  new THREE.MeshStandardMaterial({color:0xe4ecee, roughness:0.95})
);
floor.rotation.x = -Math.PI/2;
floor.position.y = -0.03;
scene.add(floor);

const model = new THREE.Group();
scene.add(model);
const clickable = [];
const material = (color, roughness=0.55, metalness=0.05) =>
  new THREE.MeshStandardMaterial({color, roughness, metalness});

function part(name, description, size, position, color, options={}) {
  const mesh = new THREE.Mesh(
    new THREE.BoxGeometry(size[0],size[1],size[2]),
    material(color, options.roughness ?? 0.55, options.metalness ?? 0.05)
  );
  mesh.position.set(...position);
  mesh.castShadow = true;
  mesh.receiveShadow = true;
  mesh.userData = {name, description, original: color};
  model.add(mesh);
  clickable.push(mesh);
  return mesh;
}

// Approximate outer casing proportions; all geometry is illustrative.
part('Badan utama',
  'Casing utama melindungi sistem optik dan elektronik instrumen. Bentuk serta dimensinya disederhanakan untuk pembelajaran.',
  [4.25,1.65,2.45],[0,0.94,0],0xf6f7f6,{roughness:0.42});
part('Panel atas',
  'Panel bagian atas merupakan bagian luar penutup instrumen. Pada alat nyata, sistem optik berada di dalam ruang tertutup.',
  [4.05,0.16,2.28],[0,1.84,0],0xe5e9e8);
part('Panel depan bawah',
  'Panel depan menjadi area antarmuka pengguna dan akses ke bagian instrumen tertentu.',
  [4.05,0.52,0.08],[0,0.64,1.24],0xdce2e1);
part('Layar',
  'Layar digunakan untuk menampilkan informasi pengukuran dan pengaturan instrumen. Tampilan pada model ini hanya ilustrasi.',
  [1.18,0.63,0.09],[-1.16,1.23,1.31],0x173b4b,{roughness:0.22,metalness:0.15});
part('Bingkai layar',
  'Bingkai mengelilingi area layar pada panel depan.',
  [1.32,0.77,0.07],[-1.16,1.23,1.27],0xabb8b8);
part('Tombol pengoperasian',
  'Tombol-tombol pada instrumen digunakan untuk mengoperasikan menu dan pengaturan. Tombol pada model belum merepresentasikan tata letak resmi secara persis.',
  [0.42,0.17,0.1],[0.15,1.15,1.31],0x4d7f87);
part('Tombol fungsi',
  'Tombol fungsi tambahan digambarkan sebagai elemen antarmuka. Pada instrumen nyata, fungsi tombol mengikuti menu dan konfigurasi alat.',
  [0.34,0.13,0.1],[0.73,1.1,1.31],0x7c999c);
part('Kompartemen sampel',
  'Kompartemen sampel adalah area tempat kuvet diletakkan saat pengukuran. Posisi dan bentuk pintu pada model ini disederhanakan.',
  [1.02,0.73,0.12],[1.48,1.13,1.29],0xc5cecc);
part('Pintu kompartemen',
  'Pintu kompartemen menutup area tempat sampel agar pengukuran dilakukan dalam kondisi yang sesuai.',
  [0.86,0.55,0.08],[1.48,1.13,1.37],0xe8eceb);
part('Kaki instrumen',
  'Kaki menopang badan instrumen. Kaki pada model dibuat sederhana untuk memperjelas bentuk keseluruhan.',
  [0.52,0.16,0.55],[-1.55,0.08,-0.82],0x56666a);
part('Kaki instrumen',
  'Kaki menopang badan instrumen.',
  [0.52,0.16,0.55],[1.55,0.08,-0.82],0x56666a);
part('Kaki instrumen',
  'Kaki menopang badan instrumen.',
  [0.52,0.16,0.55],[-1.55,0.08,0.82],0x56666a);
part('Kaki instrumen',
  'Kaki menopang badan instrumen.',
  [0.52,0.16,0.55],[1.55,0.08,0.82],0x56666a);

// Decorative status light
const led = new THREE.Mesh(new THREE.SphereGeometry(0.055,20,16), material(0x3e9c88,0.25));
led.position.set(1.03,1.13,1.37);
model.add(led);

const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
const label = document.getElementById('label');
let selected = null;
const defaultCamera = camera.position.clone();

function selectPart(mesh) {
  if (selected && selected.material && selected.material.emissive) {
    selected.material.emissive.setHex(0x000000);
  }
  selected = mesh;
  if (selected.material.emissive) selected.material.emissive.setHex(0x203b40);
  label.innerHTML = '<strong>' + mesh.userData.name + '</strong>' + mesh.userData.description;
}
renderer.domElement.addEventListener('pointerdown', (event) => {
  const rect = renderer.domElement.getBoundingClientRect();
  pointer.x = ((event.clientX-rect.left)/rect.width)*2-1;
  pointer.y = -((event.clientY-rect.top)/rect.height)*2+1;
  raycaster.setFromCamera(pointer,camera);
  const hits = raycaster.intersectObjects(clickable,false);
  if (hits.length) selectPart(hits[0].object);
});
document.getElementById('reset').addEventListener('click', () => {
  camera.position.copy(defaultCamera);
  controls.target.set(0,1.05,0);
  controls.update();
  label.innerHTML = '<strong>Model UV-Vis</strong>Pilih layar, tombol, casing, atau kompartemen sampel pada model.';
  if (selected && selected.material.emissive) selected.material.emissive.setHex(0x000000);
  selected = null;
});

function resize() {
  const w=stage.clientWidth, h=stage.clientHeight;
  camera.aspect=w/h;
  camera.updateProjectionMatrix();
  renderer.setSize(w,h);
}
window.addEventListener('resize',resize);
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene,camera);
}
animate();
</script>
</body>
</html>
"""
        components.html(html, height=560, scrolling=False)
    with right:
        st.subheader("Kontrol model")
        st.markdown("""
        - **Putar:** klik lalu geser mouse.
        - **Zoom:** gunakan scroll mouse atau gerakan pinch pada layar sentuh.
        - **Pilih bagian:** klik casing, layar, tombol, atau kompartemen sampel.
        - **Reset:** kembalikan sudut pandang awal.
        """)
        st.caption("Catatan: Three.js dimuat dari CDN, sehingga browser memerlukan koneksi internet.")
        st.markdown("**Tahap berikutnya**")
        st.markdown("1. Memperhalus bentuk alat.")
        st.markdown("2. Menambahkan penjelasan komponen.")
        st.markdown("3. Membuat simulasi pengukuran.")
        st.markdown("4. Menambahkan perhitungan kadar dan grafik.")

with tab_guide:
    st.subheader("Cara menjalankan proyek")
    st.markdown("""
    1. Unduh ZIP proyek ini lalu ekstrak ke komputer.
    2. Buat repository baru di GitHub dengan nama `uv-vis-virtual-lab`.
    3. Unggah file `app.py`, `requirements.txt`, dan `README.md` ke repository.
    4. Buka Streamlit Community Cloud dan hubungkan akun GitHub untuk menerbitkan aplikasi.
    5. Pilih repository tersebut dan tetapkan `app.py` sebagai file utama.

    Untuk sekarang, model ini adalah **prototipe tahap pertama**. Kita belum memasukkan perhitungan kadar karena fokus awalnya memastikan model 3D tampil dan dapat berinteraksi.
    """)
    st.markdown("[Dokumentasi Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)")
    st.markdown("[Panduan resmi Three.js](https://threejs.org/manual/)")

st.divider()
st.caption("Proyek pembelajaran. Model bukan produk resmi atau replika teknis tersertifikasi dari Shimadzu.")
