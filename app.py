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
after every storm — still us
</p>
""", unsafe_allow_html=True)

# ---------------- POEM ----------------
st.markdown("""
<div style="
max-width:780px;
margin: 35px auto;
background: linear-gradient(145deg, rgba(255,214,232,0.7), rgba(240,180,200,0.55));
padding: 40px;
border-radius: 32px;
text-align: center;
font-size: 18px;
color: #4a1f2c;
line-height:1.75;
box-shadow: 0 20px 50px rgba(0,0,0,0.15);
">

We walked through storms  
that changed the way we breathe.  
The kind that teaches your heart  
how to survive before it learns how to hope.  

There were moments  
we weren’t soft.  
Moments we held on quietly,  
not knowing if the light would return.  

But everything else bent.  
Everything else cracked.  
Everything else asked something of us.  

And our love —  
it stayed untouched.  

Not innocent.  
Not fragile.  
But **pure in the way truth survives fire**.  

We didn’t rush the healing.  
We let the dark teach us  
how to be gentle again.  

Now, standing in the calm,  
I don’t want a love that forgets the past.  
I want a forever that honors it.  

If the world breaks again,  
let it.  

As long as we remain —  
chosen, steady, unafraid —  
I will rebuild  
every lifetime  
with you 🤍  

</div>
""", unsafe_allow_html=True)

# ---------------- LOAD IMAGE ----------------
with open("buhb.jpeg", "rb") as f:
    encoded_image = base64.b64encode(f.read()).decode()

# ---------------- 3D PINTEREST SCENE ----------------
html_scene = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
  margin: 0;
  overflow: hidden;
  background: linear-gradient(-45deg, #ffd6e8, #fbb1c8, #fde2e4, #f8cdda);
  background-size: 400% 400%;
  animation: gradientBG 18s ease infinite;
}}

@keyframes gradientBG {{
  0% {{ background-position: 0% 50%; }}
  50% {{ background-position: 100% 50%; }}
  100% {{ background-position: 0% 50%; }}
}}
</style>
</head>

<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>

<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, window.innerWidth/window.innerHeight, 0.1, 100);
camera.position.z = 11;

const renderer = new THREE.WebGLRenderer({{ antialias:true, alpha:true }});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Lights
scene.add(new THREE.AmbientLight(0xffffff, 0.9));
const pinkLight = new THREE.PointLight(0xff9ecb, 1.6);
pinkLight.position.set(5,6,6);
scene.add(pinkLight);

// ---------------- HEART ----------------
const heartShape = new THREE.Shape();
heartShape.moveTo(0, 2);
heartShape.bezierCurveTo(0, 2, -3, -1, -3, -3);
heartShape.bezierCurveTo(-3, -6, 0, -7, 0, -4);
heartShape.bezierCurveTo(0, -7, 3, -6, 3, -3);
heartShape.bezierCurveTo(3, -1, 0, 2, 0, 2);

const heartGeometry = new THREE.ExtrudeGeometry(heartShape, {{
  depth: 1,
  bevelEnabled: true,
  bevelThickness: 0.6,
  bevelSize: 0.45,
  bevelSegments: 35
}});

const texture = new THREE.TextureLoader().load(
  "data:image/jpeg;base64,{encoded_image}"
);

const heartMaterial = new THREE.MeshPhongMaterial({{
  map: texture,
  emissive: 0xff7aa2,
  emissiveIntensity: 0.45,
  shininess: 100,
  side: THREE.DoubleSide
}});

const heart = new THREE.Mesh(heartGeometry, heartMaterial);
heart.scale.set(0.22, 0.22, 0.22);
heart.rotation.x = Math.PI;
scene.add(heart);

// ---------------- FLOATING PHOTO MEMORY ----------------
const memoryGeo = new THREE.PlaneGeometry(2.2, 2.8);
const memoryMat = new THREE.MeshBasicMaterial({{
  map: texture,
  transparent: true,
  opacity: 0.85
}});
const memory = new THREE.Mesh(memoryGeo, memoryMat);
memory.position.set(3.5, 0, -1);
scene.add(memory);

// ---------------- SWAN-LIKE CURVES ----------------
function createSwan(xPos) {{
  const curve = new THREE.CatmullRomCurve3([
    new THREE.Vector3(0, 0, 0),
    new THREE.Vector3(0.6, 1.2, 0),
    new THREE.Vector3(1.2, 2.4, 0),
    new THREE.Vector3(0.8, 3.2, 0)
  ]);

  const points = curve.getPoints(60);
  const geo = new THREE.BufferGeometry().setFromPoints(points);
  const mat = new THREE.LineBasicMaterial({{ color: 0xffffff }});
  const swan = new THREE.Line(geo, mat);
  swan.position.set(xPos, -2, -2);
  return swan;
}

const swanLeft = createSwan(-4);
const swanRight = createSwan(4);
scene.add(swanLeft);
scene.add(swanRight);

// ---------------- FLOATING PARTICLES ----------------
const particles = [];
const pGeo = new THREE.SphereGeometry(0.05, 8, 8);
const pMat = new THREE.MeshBasicMaterial({{ color: 0xffc0cb }});

for (let i = 0; i < 60; i++) {{
  const p = new THREE.Mesh(pGeo, pMat);
  p.position.set(
    (Math.random() - 0.5) * 10,
    (Math.random() - 0.5) * 6,
    (Math.random() - 0.5) * 4
  );
  particles.push(p);
  scene.add(p);
}}

// ---------------- ANIMATION ----------------
function animate() {{
  requestAnimationFrame(animate);

  heart.rotation.y += 0.005;
  heart.position.y = Math.sin(Date.now()*0.002) * 0.15;

  memory.position.y = Math.sin(Date.now()*0.0015) * 0.25;
  memory.rotation.y += 0.002;

  swanLeft.rotation.y += 0.003;
  swanRight.rotation.y -= 0.003;

  particles.forEach(p => {{
    p.position.y += 0.01;
    if (p.position.y > 4) p.position.y = -4;
  }});

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

components.html(html_scene, height=700)

# ---------------- GAME: LOVE METER ----------------
st.markdown("---")
st.markdown("<h2 style='text-align:center; color:#c94f7c;'>💗 Love Meter</h2>", unsafe_allow_html=True)

if "love" not in st.session_state:
    st.session_state.love = 0

messages = [
    "You feel like safety 🖤",
    "I trust you completely 💞",
    "You’re my constant 💗",
    "I choose you — always 💘",
    "This is forever ♾️"
]

cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        if st.button("💖", key=f"love_{i}"):
            st.session_state.love = min(5, st.session_state.love + 1)
            st.toast(messages[st.session_state.love - 1])

st.markdown(
    f"<h3 style='text-align:center;'>Love Level: {st.session_state.love}/5 💕</h3>",
    unsafe_allow_html=True
)

# ---------------- FINAL MESSAGE ----------------
st.markdown("""
<div style="
margin:45px auto;
max-width:620px;
background: rgba(255, 214, 232, 0.6);
padding: 35px;
border-radius: 28px;
text-align:center;
color:#4a1f2c;
font-size:18px;
">
No matter how many storms come,  
this stays.  

You and me.  
Forever 🤍  
</div>
""", unsafe_allow_html=True)

