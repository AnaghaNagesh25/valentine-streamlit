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

# ---------------- SMALL SLIDING PUZZLE ----------------
st.markdown("## 💕 Find Each Other 💕")

# --- Initialize game state ---
if "car1" not in st.session_state:
    st.session_state.car1 = [0, 0]      # You
    st.session_state.car2 = [4, 4]      # Him
    st.session_state.heart = [2, 2]
    st.session_state.won = False

GRID_SIZE = 5

def move(car, direction):
    if direction == "up" and car[0] > 0:
        car[0] -= 1
    elif direction == "down" and car[0] < GRID_SIZE - 1:
        car[0] += 1
    elif direction == "left" and car[1] > 0:
        car[1] -= 1
    elif direction == "right" and car[1] < GRID_SIZE - 1:
        car[1] += 1

# --- Grid display ---
grid_html = "<div style='display:grid;grid-template-columns:repeat(5,50px);gap:6px;justify-content:center;'>"

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        cell = ""
        if [i, j] == st.session_state.car1:
            cell = "🚗"
        elif [i, j] == st.session_state.car2:
            cell = "🚙"
        elif [i, j] == st.session_state.heart:
            cell = "💖"

        grid_html += f"""
        <div style="
            width:50px;
            height:50px;
            background:linear-gradient(145deg,#ffd6e8,#ffb6d5);
            border-radius:14px;
            box-shadow:inset 4px 4px 8px #ff9fc7,inset -4px -4px 8px #fff;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:26px;">
            {cell}
        </div>
        """

grid_html += "</div>"
st.markdown(grid_html, unsafe_allow_html=True)

st.markdown("### 💕 Move *You* (🚗)")
c1 = st.columns(4)
if c1[0].button("⬅️", key="c1l"): move(st.session_state.car1, "left")
if c1[1].button("⬆️", key="c1u"): move(st.session_state.car1, "up")
if c1[2].button("⬇️", key="c1d"): move(st.session_state.car1, "down")
if c1[3].button("➡️", key="c1r"): move(st.session_state.car1, "right")

st.markdown("### 💕 Move *Him* (🚙)")
c2 = st.columns(4)
if c2[0].button("⬅️", key="c2l"): move(st.session_state.car2, "left")
if c2[1].button("⬆️", key="c2u"): move(st.session_state.car2, "up")
if c2[2].button("⬇️", key="c2d"): move(st.session_state.car2, "down")
if c2[3].button("➡️", key="c2r"): move(st.session_state.car2, "right")

# --- Win condition ---
if (
    st.session_state.car1 == st.session_state.heart
    and st.session_state.car2 == st.session_state.heart
):
    st.session_state.won = True

if st.session_state.won:
    st.markdown("""
    <div style="
        margin-top:20px;
        padding:18px;
        background:linear-gradient(135deg,#ff8fcf,#ffc1e3);
        border-radius:20px;
        text-align:center;
        font-size:18px;
        box-shadow:0 10px 25px rgba(255,105,180,0.4);
        color:#5b0036;">
        💗 You always find each other.<br>
        No matter the path. No matter the storm. 💗
    </div>
    """, unsafe_allow_html=True)

# ---------------- FUN GAMES ----------------
st.markdown("### 💘 Valentine Games")

# Fate Dice
with st.container():
    st.markdown("<div class='game'>", unsafe_allow_html=True)
    if st.button("🎲 Roll the Fate Dice", key="dice"):
        st.success(random.choice([
            "We were always meant to find each other.",
            "Every road led back to us.",
            "Even fate knew we’d choose love.",
            "This connection was written long before us."
        ]))
    st.markdown("</div>", unsafe_allow_html=True)

# Love Message Generator
with st.container():
    st.markdown("<div class='game'>", unsafe_allow_html=True)
    if st.button("💌 Generate a Love Message", key="love_msg"):
        st.success(random.choice([
            "You are my calm after every storm.",
            "Still you. Still us.",
            "I feel safest when I’m choosing you.",
            "Every version of forever looks like you."
        ]))
    st.markdown("</div>", unsafe_allow_html=True)

# Forever Button + Balloons
with st.container():
    st.markdown("<div class='game'>", unsafe_allow_html=True)
    if st.button("💍 FOREVER", key="forever"):
        st.balloons()
        st.success("Locked in. No matter what. Forever 💗")
    st.markdown("</div>", unsafe_allow_html=True)


