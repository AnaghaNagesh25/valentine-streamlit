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


st.markdown("""# ---------------- SMALL SLIDING PUZZLE ----------------
st.markdown("### 🧩 Put Us Back Together")

img = Image.open("buhb.jpeg").resize((240,240))
tiles = np.array(img).reshape(3,80,3,80,3).swapaxes(1,2).reshape(-1,80,80,3)

if "puzzle" not in st.session_state:
    st.session_state.puzzle = list(range(9))
    random.shuffle(st.session_state.puzzle)

def move(direction):
    idx = st.session_state.puzzle.index(8)
    r, c = divmod(idx, 3)
    swaps = {
        "⬅️": (r, c+1),
        "➡️": (r, c-1),
        "⬆️": (r+1, c),
        "⬇️": (r-1, c)
    }
    if direction in swaps:
        nr, nc = swaps[direction]
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr*3 + nc
            st.session_state.puzzle[idx], st.session_state.puzzle[ni] = st.session_state.puzzle[ni], st.session_state.puzzle[idx]

cols = st.columns(3)
for i, tile in enumerate(st.session_state.puzzle):
    with cols[i%3]:
        if tile != 8:
            st.image(tiles[tile], use_container_width=True)
        else:
            st.write(" ")

ctrl = st.columns(4)
if ctrl[0].button("⬅️"): move("⬅️")
if ctrl[1].button("⬆️"): move("⬆️")
if ctrl[2].button("⬇️"): move("⬇️")
if ctrl[3].button("➡️"): move("➡️")

if st.session_state.puzzle == list(range(9)):
    st.success("You fixed us — perfectly 💗")

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
