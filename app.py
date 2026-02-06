import streamlit as st
import streamlit.components.v1 as components
import base64
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For You 💗",
    page_icon="💖",
    layout="wide"
)

# ---------------- TITLE ----------------
st.markdown("""
<h1 style="text-align:center; color:#c94f7c;">
For you, my babyboy 💗
</h1>
<p style="text-align:center; font-size:18px; color:#6b2c3e;">
after everything — still us
</p>
""", unsafe_allow_html=True)

# ---------------- DARK ROMANTIC POEM ----------------
st.markdown("""
<div style="
max-width:760px;
margin: 35px auto;
background: linear-gradient(145deg, rgba(255,214,232,0.7), rgba(240,180,200,0.5));
padding: 40px;
border-radius: 30px;
text-align: center;
font-size: 18px;
color: #4a1f2c;
line-height:1.75;
box-shadow: 0 20px 50px rgba(0,0,0,0.12);
">

We walked through storms  
that rewired our bones.  
The kind that leave no scars you can point to,  
only quieter hearts  
and stronger hands.  

There were moments  
we didn’t feel whole.  
Moments we learned how to survive  
before we learned how to hope again.  

But even when everything else fractured,  
our love stayed untouched —  
not innocent,  
but **pure in the way truth survives fire**.  

We didn’t rush the healing.  
We let the darkness teach us  
how to be gentle again.  
How to choose softness  
without losing strength.  

Now, standing in this calm,  
I don’t want a love that forgets the past.  
I want a forever that honors it.  

If the world breaks again,  
let it.  

As long as we remain —  
chosen, steady, unafraid —  
I will rebuild  
every lifetime  
with you. 🤍  

</div>
""", unsafe_allow_html=True)

# ---------------- LOAD IMAGE ----------------
with open("buhb.jpeg", "rb") as f:
    encoded_image = base64.b64encode(f.read()).decode()

# ---------------- 3D HEART WITH IMAGE ----------------
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
const camera = new THREE.PerspectiveCamera(40, window.innerWidth/window.innerHeight, 0.1, 100);
camera.position.z = 9;

const renderer = new THREE.WebGLRenderer({{ antialias:true, alpha:true }});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// lights
scene.add(new THREE.AmbientLight(0xffffff, 0.85));
const light = new THREE.PointLight(0xff8fab, 1.4);
light.position.set(5,6,6);
scene.add(light);

// heart shape
const heartShape = new THREE.Shape();
heartShape.moveTo(0, 2);
heartShape.bezierCurveTo(0, 2, -3, -1, -3, -3);
heartShape.bezierCurveTo(-3, -6, 0, -7, 0, -4);
heartShape.bezierCurveTo(0, -7, 3, -6, 3, -3);
heartShape.bezierCurveTo(3, -1, 0, 2, 0, 2);

const geometry = new THREE.ExtrudeGeometry(heartShape, {{
  depth: 1,
  bevelEnabled: true,
  bevelThickness: 0.6,
  bevelSize: 0.45,
  bevelSegments: 35
}});

const texture = new THREE.TextureLoader().load(
  "data:image/jpeg;base64,{encoded_image}"
);

const material = new THREE.MeshPhongMaterial({{
  map: texture,
  emissive: 0xff7aa2,
  emissiveIntensity: 0.4,
  shininess: 90,
  side: THREE.DoubleSide
}});

const heart = new THREE.Mesh(geometry, material);
heart.scale.set(0.22, 0.22, 0.22);
heart.rotation.x = Math.PI;
scene.add(heart);

// animate
function animate() {{
  requestAnimationFrame(animate);
  heart.rotation.y += 0.005;
  heart.position.y = Math.sin(Date.now() * 0.002) * 0.12;
  renderer.render(scene, camera);
}}
animate();

// resize
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

# ---------------- GAME 1: LOVE METER ----------------
st.markdown("---")
st.markdown("<h2 style='text-align:center; color:#c94f7c;'>💗 Love Meter</h2>", unsafe_allow_html=True)

if "love" not in st.session_state:
    st.session_state.love = 0

love_msgs = [
    "You feel like safety 🖤",
    "I trust you with my heart 💞",
    "You’re my constant 💗",
    "I choose you — always 💘",
    "This is forever energy ♾️"
]

cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        if st.button("💖", key=f"love_{i}"):
            st.session_state.love = min(5, st.session_state.love + 1)
            st.toast(love_msgs[st.session_state.love - 1])

st.markdown(
    f"<h3 style='text-align:center;'>Love Level: {st.session_state.love}/5 💕</h3>",
    unsafe_allow_html=True
)

# ---------------- GAME 2: COMPLIMENT ----------------
st.markdown("---")
st.markdown("<h2 style='text-align:center; color:#c94f7c;'>🖤 Press for a Truth</h2>", unsafe_allow_html=True)

truths = [
    "You are safe to love",
    "You are deeply wanted",
    "You are chosen without hesitation",
    "You are stronger than your past",
    "You are my home"
]

if st.button("✨ Tell me ✨"):
    st.success(random.choice(truths))

# ---------------- FINAL MESSAGE ----------------
st.markdown("""
<div style="
margin:45px auto;
max-width:620px;
background: rgba(255, 214, 232, 0.6);
padding: 35px;
border-radius: 25px;
text-align:center;
color:#4a1f2c;
font-size:18px;
">
After everything —  
it’s still you.  

And it will always be you 🤍  
</div>
""", unsafe_allow_html=True)

