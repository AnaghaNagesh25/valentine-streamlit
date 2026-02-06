import streamlit as st
import base64
import random
from streamlit.components.v1 import html

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For You, My Babyboy 💖",
    page_icon="💗",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align:center;'>for you, my babyboy 💕</h1>",
    unsafe_allow_html=True
)

# ---------------- LOAD IMAGE ----------------
with open("buhb.jpeg", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()

image_src = f"data:image/jpeg;base64,{encoded_image}"

# ---------------- POEM ----------------
poem = """
We walked through storms that left no witnesses,  
winds that tried to rewrite who we were.  

We learned the language of silence,  
the weight of staying when leaving felt easier.  

Everything else bent.  
Everything else broke.  

But our love —  
untouched, unpolluted — stayed standing  
where the storm gave up.  

We did not rush the healing.  
We let the cracks teach us tenderness again.  

And now, in this quiet after the chaos,  
I don’t want a beginning that forgets the past.  
I want a forever that remembers  
what it took to arrive here.  

If the world falls apart again,  
let it.  

As long as it’s you and me,  
I will choose this love —  
again, and again, and forever.
"""

with st.expander("🖤 A Poem For Us"):
    st.markdown(f"<p style='font-size:18px; line-height:1.7'>{poem}</p>", unsafe_allow_html=True)

# ---------------- 3D SCENE ----------------
html_scene = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
  overflow: hidden;
  background: linear-gradient(-45deg, #ffd6e8, #fbb1c8, #fde2e4, #f8cdda);
  background-size: 400% 400%;
  animation: bg 18s ease infinite;
}

@keyframes bg {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>
</head>

<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>

<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(40, window.innerWidth/window.innerHeight, 0.1, 100);
camera.position.z = 10;

const renderer = new THREE.WebGLRenderer({ antialias:true, alpha:true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

scene.add(new THREE.AmbientLight(0xffffff, 0.9));

const light = new THREE.PointLight(0xff9ecb, 1.5);
light.position.set(5,6,6);
scene.add(light);

// Heart
const heartShape = new THREE.Shape();
heartShape.moveTo(0,2);
heartShape.bezierCurveTo(0,2,-3,-1,-3,-3);
heartShape.bezierCurveTo(-3,-6,0,-7,0,-4);
heartShape.bezierCurveTo(0,-7,3,-6,3,-3);
heartShape.bezierCurveTo(3,-1,0,2,0,2);

const heartGeo = new THREE.ExtrudeGeometry(heartShape, {
  depth: 1,
  bevelEnabled: true,
  bevelThickness: 0.6,
  bevelSize: 0.45,
  bevelSegments: 30
});

const texture = new THREE.TextureLoader().load("__IMG__");

const heartMat = new THREE.MeshPhongMaterial({
  map: texture,
  emissive: 0xff7aa2,
  emissiveIntensity: 0.4,
  shininess: 100
});

const heart = new THREE.Mesh(heartGeo, heartMat);
heart.scale.set(0.22,0.22,0.22);
heart.rotation.x = Math.PI;
scene.add(heart);

// Floating photo
const planeGeo = new THREE.PlaneGeometry(2.2,2.8);
const planeMat = new THREE.MeshBasicMaterial({
  map: texture,
  transparent: true,
  opacity: 0.9
});
const memory = new THREE.Mesh(planeGeo, planeMat);
memory.position.set(3.2,0,-1);
scene.add(memory);

// Swan curves
function swan(x){
  const curve = new THREE.CatmullRomCurve3([
    new THREE.Vector3(0,0,0),
    new THREE.Vector3(0.6,1.4,0),
    new THREE.Vector3(1.2,2.4,0),
    new THREE.Vector3(0.8,3.2,0)
  ]);
  const pts = curve.getPoints(50);
  const geo = new THREE.BufferGeometry().setFromPoints(pts);
  const mat = new THREE.LineBasicMaterial({ color: 0xffffff });
  const line = new THREE.Line(geo, mat);
  line.position.set(x,-2,-2);
  return line;
}

scene.add(swan(-4));
scene.add(swan(4));

function animate(){
  requestAnimationFrame(animate);
  heart.rotation.y += 0.01;
  memory.rotation.y -= 0.005;
  renderer.render(scene,camera);
}
animate();

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth/window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
</script>
</body>
</html>
"""

html(html_scene.replace("__IMG__", image_src), height=600)

# ---------------- GAMES ----------------
st.markdown("## 💘 Valentine Games")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💌 Love Message"):
        msgs = [
            "You are my safest place.",
            "I choose you, every lifetime.",
            "Still you. Always you.",
            "My calm after every storm."
        ]
        st.success(random.choice(msgs))

with col2:
    if st.button("🎲 Fate Dice"):
        st.info(random.choice([
            "Cuddle night incoming 💕",
            "Movie + snacks date 🍿",
            "Long hug, no talking 🤍",
            "Soft love, no rush 🖤"
        ]))

with col3:
    if st.button("💖 Forever Button"):
        st.balloons()
        st.markdown("### It’s always you. 🌙")


