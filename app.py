import streamlit as st
import streamlit.components.v1 as components
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="My Valentine 💗",
    page_icon="💖",
    layout="wide"
)

# ---------------- TITLE ----------------
st.markdown("""
<h1 style="text-align:center; color:#c94f7c;">
Hey you 💕
</h1>
<p style="text-align:center; font-size:18px; color:#7a3b4d;">
I built a tiny universe for us
</p>
""", unsafe_allow_html=True)

# ---------------- POEM ----------------
st.markdown("""
<div style="
max-width:750px;
margin: 30px auto;
background: rgba(255, 214, 232, 0.65);
padding: 35px;
border-radius: 30px;
text-align: center;
font-size: 18px;
color: #5b2b3a;
line-height:1.6;
box-shadow: 0 15px 40px rgba(0,0,0,0.08);
">

I don’t love you loudly —  
I love you **deeply**.  

In the way my day feels unfinished  
until I tell you about it.  

In the way your name feels  
like something I’ll always know.  

You’re my comfort,  
my excitement,  
my favorite person to come home to.  

And if I had to choose again —  
it would still be you 💗  

</div>
""", unsafe_allow_html=True)

# ---------------- LOAD IMAGE ----------------
with open("buhb.jpeg", "rb") as f:
    encoded_image = base64.b64encode(f.read()).decode()

# ---------------- 3D HEART ----------------
html_heart = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
  margin: 0;
  overflow: hidden;
  background: linear-gradient(#fde2e4, #fadadd);
}}
</style>
</head>

<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>

<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  45,
  window.innerWidth / window.innerHeight,
  0.1,
  100
);
camera.position.z = 7;

const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Lights
scene.add(new THREE.AmbientLight(0xffffff, 0.9));
const light = new THREE.PointLight(0xffffff, 1);
light.position.set(5, 5, 5);
scene.add(light);

// Heart Shape
const heartShape = new THREE.Shape();
heartShape.moveTo(0, 0);
heartShape.bezierCurveTo(0, 0, -2, 2, -2, 4);
heartShape.bezierCurveTo(-2, 6, 0, 7.5, 0, 9);
heartShape.bezierCurveTo(0, 7.5, 2, 6, 2, 4);
heartShape.bezierCurveTo(2, 2, 0, 0, 0, 0);

const geometry = new THREE.ExtrudeGeometry(heartShape, {{
  depth: 0.6,
  bevelEnabled: true,
  bevelThickness: 0.3,
  bevelSize: 0.3,
  bevelSegments: 20
}});

const texture = new THREE.TextureLoader().load(
  "data:image/jpeg;base64,{encoded_image}"
);

const material = new THREE.MeshStandardMaterial({{
  map: texture,
  metalness: 0.2,
  roughness: 0.4
}});

const heart = new THREE.Mesh(geometry, material);
heart.scale.set(0.25, 0.25, 0.25);
heart.rotation.x = Math.PI;
scene.add(heart);

// Animation
function animate() {{
  requestAnimationFrame(animate);
  heart.rotation.y += 0.01;
  heart.position.y = Math.sin(Date.now() * 0.002) * 0.15;
  renderer.render(scene, camera);
}}
animate();

// Resize
window.addEventListener("resize", () => {{
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}});
</script>
</body>
</html>
"""

components.html(html_heart, height=650)

# ---------------- GAME 1 ----------------
st.markdown("---")
st.markdown("<h2 style='text-align:center; color:#c94f7c;'>💗 Love Meter 💗</h2>", unsafe_allow_html=True)

if "love" not in st.session_state:
    st.session_state.love = 0

messages = [
    "You make me smile without trying 🥰",
    "You feel like home 💞",
    "I trust you with my heart 💗",
    "You’re my person 🌷",
    "Okay wow I’m very in love 💘"
]

cols = st.columns(5)
for col in cols:
    with col:
        if st.button("💖"):
            st.session_state.love += 1
            if st.session_state.love <= len(messages):
                st.toast(messages[st.session_state.love - 1])

st.markdown(
    f"<h3 style='text-align:center;'>Love Level: {st.session_state.love}/5 💕</h3>",
    unsafe_allow_html=True
)

# ---------------- FINAL NOTE ----------------
st.markdown("""
<div style="
margin:40px auto;
max-width:600px;
background: rgba(255, 214, 232, 0.6);
padding: 30px;
border-radius: 25px;
text-align:center;
color:#5b2b3a;
font-size:18px;
">
You don’t need to win a game.  
You already have my heart 🤍  
</div>
""", unsafe_allow_html=True)

