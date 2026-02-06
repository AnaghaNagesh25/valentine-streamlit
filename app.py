import streamlit as st
import base64
import random
from PIL import Image
import numpy as np

st.set_page_config(page_title="For You, My Babyboy 💗", layout="wide")

# ---------------- LOAD IMAGE ----------------
def load_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_b64 = load_base64("buhb.jpeg")

# ---------------- STYLES ----------------
st.markdown("""
<style>
html, body {
    background: radial-gradient(circle at top, #ffd6eb, #ffc0d9, #ffb3d1);
    background-size: 400% 400%;
    animation: bgMove 15s ease infinite;
    font-family: 'Georgia', serif;
}

@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.title {
    text-align: center;
    font-size: 3rem;
    color: #7a1c4b;
    margin: 20px 0;
}

.card {
    background: rgba(255,255,255,0.75);
    padding: 25px;
    border-radius: 22px;
    box-shadow: 0 20px 40px rgba(255,105,180,0.25);
    margin: 20px auto;
    max-width: 900px;
}

.game {
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(255,105,180,0.2);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>For You, My Babyboy 💗</div>", unsafe_allow_html=True)

# ---------------- 3D HEART + SWANS ----------------
st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body style="margin:0; overflow:hidden;">
<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(70, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.z = 6;

const renderer = new THREE.WebGLRenderer({alpha:true});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Lights
scene.add(new THREE.AmbientLight(0xffffff, 0.9));
const light = new THREE.PointLight(0xffffff, 1.5);
light.position.set(5,5,5);
scene.add(light);

// Heart shape
const shape = new THREE.Shape();
shape.moveTo(0,0);
shape.bezierCurveTo(0,0,-2,-2,-4,0);
shape.bezierCurveTo(-6,3,-3,6,0,7);
shape.bezierCurveTo(3,6,6,3,4,0);
shape.bezierCurveTo(2,-2,0,0,0,0);

const geo = new THREE.ExtrudeGeometry(shape,{
    depth:0.8,
    bevelEnabled:true,
    bevelThickness:0.3,
    bevelSize:0.3,
    bevelSegments:10
});

const texture = new THREE.TextureLoader().load("data:image/jpeg;base64,{{IMG}}");
const mat = new THREE.MeshStandardMaterial({map:texture, roughness:0.35, metalness:0.3});
const heart = new THREE.Mesh(geo, mat);
heart.scale.set(0.45,0.45,0.45);
scene.add(heart);

// Swan curves
function swan(x) {
    const curve = new THREE.CatmullRomCurve3([
        new THREE.Vector3(x,0,0),
        new THREE.Vector3(x/2,1.2,0),
        new THREE.Vector3(0,0.4,0)
    ]);
    const g = new THREE.TubeGeometry(curve,50,0.06,8,false);
    const m = new THREE.MeshStandardMaterial({color:0xffffff});
    const s = new THREE.Mesh(g,m);
    scene.add(s);
    return s;
}

const swanL = swan(-5);
const swanR = swan(5);

function animate(){
    requestAnimationFrame(animate);
    heart.rotation.y += 0.01;
    heart.rotation.x += 0.005;
    swanL.position.x += 0.015;
    swanR.position.x -= 0.015;
    renderer.render(scene,camera);
}
animate();
</script>
</body>
</html>
""".replace("{{IMG}}", img_b64), height=600)

# ---------------- POEM ----------------
st.markdown("""
<div class="card">
We survived storms that rewrote us.<br>
Not loudly — but deeply.<br><br>

Everything else bent, broke, or disappeared.<br>
But our love stayed untouched —<br>
not because it was easy,<br>
but because it was chosen.<br><br>

We didn’t rush the healing.<br>
We learned how to be gentle again.<br>
How to trust the light when it returned.<br><br>

If the world asks us to begin again,<br>
I will — every lifetime —<br>
as long as it’s with you.
</div>
""", unsafe_allow_html=True)

# ---------------- PUZZLE GAME ----------------
st.markdown("### 🧩 Piece Us Back Together")

img = Image.open("buhb.jpeg").resize((300,300))
tiles = np.array(img).reshape(3,100,3,100,3).swapaxes(1,2).reshape(-1,100,100,3)

if "order" not in st.session_state:
    st.session_state.order = list(range(9))
    random.shuffle(st.session_state.order)

cols = st.columns(3)
for i, idx in enumerate(st.session_state.order):
    with cols[i%3]:
        st.image(tiles[idx], use_container_width=True)
        if st.button("💗", key=f"swap{i}"):
            j = random.randint(0,8)
            st.session_state.order[i], st.session_state.order[j] = st.session_state.order[j], st.session_state.order[i]

if st.session_state.order == list(range(9)):
    st.success("You fixed us — just like always 💞")

# ---------------- FUN GAMES ----------------
st.markdown("### 💘 Little Valentine Games")

with st.container():
    st.markdown("<div class='game'>", unsafe_allow_html=True)
    if st.button("💌 Tap for a Love Note", key="note"):
        st.success(random.choice([
            "Still you. Still us.",
            "My safest place.",
            "I’d choose you again.",
            "Forever feels right with you."
        ]))
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='game'>", unsafe_allow_html=True)
    ans = st.radio("What survives every storm?", ["Fear", "Time", "Us"], key="quiz")
    if ans == "Us":
        st.success("Always us 💗")
    st.markdown("</div>", unsafe_allow_html=True)

