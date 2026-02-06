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
    background:
        radial-gradient(circle at 15% 25%, #ffd6eb 0%, transparent 35%),
        radial-gradient(circle at 85% 35%, #ffc1dc 0%, transparent 40%),
        radial-gradient(circle at 50% 85%, #ffb3d1 0%, transparent 45%),
        linear-gradient(180deg, #ffe6f2, #ffd1e8);
    background-size: 300% 300%;
    animation: bgFloat 18s ease infinite;
    font-family: 'Georgia', serif;
}

@keyframes bgFloat {
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
    background: rgba(255, 240, 248, 0.88);
    padding: 28px;
    border-radius: 24px;
    box-shadow: 0 25px 45px rgba(255,105,180,0.3);
    margin: 25px auto;
    max-width: 900px;
}

.game {
    background: rgba(255,240,248,0.92);
    padding: 22px;
    border-radius: 20px;
    box-shadow: 0 15px 30px rgba(255,105,180,0.3);
    margin-bottom: 22px;
}

button {
    background-color: #ff9acb !important;
    color: #4b0f2b !important;
    border-radius: 14px !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>For You, My Babyboy 💗</div>", unsafe_allow_html=True)
def pink_result(text):
    st.markdown(f"""
    <div style="
        background:#ffd6eb;
        color:#5b0036;
        padding:14px;
        border-radius:14px;
        margin-top:10px;
        box-shadow:0 10px 25px rgba(255,105,180,0.3);
        font-weight:600;
        text-align:center;">
        {text}
    </div>
    """, unsafe_allow_html=True)


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

scene.add(new THREE.AmbientLight(0xffffff, 0.9));
const light = new THREE.PointLight(0xffffff, 1.6);
light.position.set(5,5,5);
scene.add(light);

// Heart
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
        new THREE.Vector3(x/2,1.3,0),
        new THREE.Vector3(0,0.4,0)
    ]);
    const g = new THREE.TubeGeometry(curve,60,0.06,8,false);
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
    swanL.position.x += 0.012;
    swanR.position.x -= 0.012;
    renderer.render(scene,camera);
}
animate();
</script>
</body>
</html>
""".replace("{{IMG}}", img_b64), height=600)

# ---------------- POEM (UNCHANGED) ----------------
st.markdown("""
<div class="card">
We walked through storms that left no witnesses,<br>
winds that tried to rewrite who we were.<br><br>

We learned how to stay soft<br>
in a world that asked us to harden.<br><br>

Everything else bent.<br>
Everything else broke.<br><br>

But our love —<br>
untouched, unpolluted —<br>
stood exactly where the storm gave up.<br><br>

We didn’t rush the healing.<br>
We let time teach us gentleness again.<br><br>

And now, in the quiet after the chaos,<br>
I don’t want a beginning that forgets the past.<br>
I want a forever that remembers<br>
what it took to arrive here.<br><br>

If the world falls apart again,<br>
let it.<br><br>

As long as it’s you and me,<br>
I will choose this love —<br>
again, again, and forever.
</div>
""", unsafe_allow_html=True)

import streamlit as st
import random

st.set_page_config(page_title="Tiny Love Car Game", layout="centered")

# ---------- STYLES ----------
st.markdown("""
<style>
body { background:#ffe6f2; }
.game-wrap { width:260px; margin:auto; }
.grid { display:grid; grid-template-columns:repeat(5, 44px); grid-gap:6px; }
.tile {
  width:44px; height:44px; border-radius:10px;
  background:linear-gradient(145deg,#ff9acb,#ff6fb3);
  box-shadow:6px 6px 12px rgba(0,0,0,.18), -4px -4px 10px rgba(255,255,255,.6);
  display:flex; align-items:center; justify-content:center; font-size:20px;
}
.road { background:linear-gradient(145deg,#ffd1e8,#ffb6da); }
.heart { background:linear-gradient(145deg,#ff4f9a,#ff86bf); color:white; }
.msg { background:#ffd1e8; padding:10px; border-radius:14px; text-align:center; color:#7a1c4b; font-weight:600; margin-top:8px; }
.controls { display:flex; gap:6px; justify-content:center; margin-top:8px; }
</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "p1" not in st.session_state:
    st.session_state.p1 = [0, 2]
    st.session_state.p2 = [4, 2]
    st.session_state.heart = [2, 2]

# ---------- HELPERS ----------
def move(player, dx, dy):
    p = st.session_state.p1 if player == 1 else st.session_state.p2
    nx, ny = p[0] + dx, p[1] + dy
    if 0 <= nx < 5 and 0 <= ny < 5:
        p[0], p[1] = nx, ny

# ---------- UI ----------
st.markdown("<div class='game-wrap'>", unsafe_allow_html=True)
st.markdown("### 🚗💗 Tiny Love Car Game")

# GRID
st.markdown("<div class='grid'>", unsafe_allow_html=True)
for y in range(5):
    for x in range(5):
        icon = ""
        cls = "tile road"
        if [x, y] == st.session_state.heart:
            icon = "💗"
            cls = "tile heart"
        if [x, y] == st.session_state.p1:
            icon = "🚗"
        if [x, y] == st.session_state.p2:
            icon = "🚙"
        st.markdown(f"<div class='{cls}'>{icon}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# CONTROLS
st.markdown("<div class='controls'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.button("⬆️", on_click=move, args=(1, 0, -1))
    st.button("⬅️", on_click=move, args=(1, -1, 0))
    st.button("➡️", on_click=move, args=(1, 1, 0))
    st.button("⬇️", on_click=move, args=(1, 0, 1))
with col2:
    st.button("⬆️ ", on_click=move, args=(2, 0, -1))
    st.button("⬅️ ", on_click=move, args=(2, -1, 0))
    st.button("➡️ ", on_click=move, args=(2, 1, 0))
    st.button("⬇️ ", on_click=move, args=(2, 0, 1))
st.markdown("</div>", unsafe_allow_html=True)

# WIN
if st.session_state.p1 == st.session_state.heart and st.session_state.p2 == st.session_state.heart:
    st.markdown("<div class='msg'>Two paths. One heart. 💞</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)



# ---------------- FUN GAMES ----------------
st.markdown("### 💘 Valentine Games")

# Fate Dice
if st.button("🎲 Roll the Fate Dice", key="dice"):
    pink_result(random.choice([
        "We were always meant to find each other.",
        "Every road led back to us.",
        "Even fate knew we’d choose love.",
        "This connection was written long before us."
    ]))

# Love Message
if st.button("💌 Generate a Love Message", key="love_msg"):
    pink_result(random.choice([
        "You are my calm after every storm.",
        "Still you. Still us.",
        "I feel safest when I’m choosing you.",
        "Every version of forever looks like you."
    ]))

# Forever
if st.button("💍 FOREVER", key="forever"):
    st.balloons()
    pink_result("Locked in. No matter what. Forever 💗")
