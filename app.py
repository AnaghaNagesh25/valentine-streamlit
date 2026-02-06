import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="For You My Babyboy 💗", layout="wide")

# ---------- GLOBAL PINK STYLE ----------
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #ffd1e8, #ff9fcf);
}
h1, h2, h3, p {
    color: #5b0036;
    text-align: center;
}
button {
    background-color: #ff8fcf !important;
    color: white !important;
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1>For You, My Babyboy 💕</h1>", unsafe_allow_html=True)

# ---------- POEM ----------
st.markdown("""
<div style="max-width:700px;margin:auto;padding:25px;
background:rgba(255,255,255,0.6);
border-radius:25px;
box-shadow:0 15px 40px rgba(255,105,180,0.4);">
<p>
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
</p>
</div>
""", unsafe_allow_html=True)

# ---------- 3D HEART WITH WINGS ----------
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>body{margin:0;overflow:hidden;}</style>
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.z = 6;

const renderer = new THREE.WebGLRenderer({ alpha:true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Heart
const shape = new THREE.Shape();
shape.moveTo(0,0);
shape.bezierCurveTo(0,0,-1.5,-1.5,-3,0);
shape.bezierCurveTo(-4.5,2,0,4,0,6);
shape.bezierCurveTo(0,4,4.5,2,3,0);
shape.bezierCurveTo(1.5,-1.5,0,0,0,0);

const geo = new THREE.ExtrudeGeometry(shape,{depth:0.6,bevelEnabled:true});
const mat = new THREE.MeshStandardMaterial({color:0xff6fae,metalness:0.6,roughness:0.2});
const heart = new THREE.Mesh(geo,mat);
heart.scale.set(0.25,0.25,0.25);
scene.add(heart);

// Wings
function wing(x){
  const g = new THREE.PlaneGeometry(3,2,12,12);
  const m = new THREE.MeshStandardMaterial({color:0xffc1dc,side:THREE.DoubleSide,transparent:true,opacity:0.9});
  const w = new THREE.Mesh(g,m);
  w.position.x = x;
  w.rotation.y = x>0 ? -0.5 : 0.5;
  return w;
}
const left = wing(-2.3);
const right = wing(2.3);
scene.add(left); scene.add(right);

// Light
scene.add(new THREE.AmbientLight(0xffb6d9,1.2));
const l = new THREE.PointLight(0xffffff,1.5);
l.position.set(5,5,5); scene.add(l);

let t=0;
function animate(){
  requestAnimationFrame(animate);
  t+=0.03;
  heart.rotation.y+=0.01;
  left.rotation.z=Math.sin(t)*0.25;
  right.rotation.z=-Math.sin(t)*0.25;
  renderer.render(scene,camera);
}
animate();
</script>
</body>
</html>
""", height=420)

# ---------- LOVE DINO GAME (STREAMLIT SAFE) ----------
st.markdown("## 💕 Run Toward Forever")

if "dino" not in st.session_state:
    st.session_state.dino = 0
    st.session_state.heart_pos = 6
    st.session_state.over = False

cols = st.columns(8)
for i in range(8):
    if i == st.session_state.dino:
        cols[i].image("buhb.jpeg", width=60)
    elif i == st.session_state.heart_pos:
        cols[i].markdown("💖")
    else:
        cols[i].markdown(" ")

if not st.session_state.over:
    if st.button("➡️ Jump Toward Love"):
        st.session_state.dino += 1
        if st.session_state.dino >= st.session_state.heart_pos:
            st.session_state.over = True

if st.session_state.over:
    st.success("💗 You always reach each other 💗")

# ---------- FUN GAMES ----------
st.markdown("## 🎲 Fate Dice")
if st.button("Roll the Dice of Fate"):
    st.markdown(f"💞 Destiny says: **{random.choice(['Forever','Always','Unbreakable','Written in Stars'])}**")

st.markdown("## 💌 Love Message")
if st.button("Reveal Love"):
    st.markdown("💗 You are my safest place and my wildest dream.")

st.markdown("## ♾️ Forever")
if st.button("FOREVER"):
    st.balloons()

