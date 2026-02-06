import streamlit as st
import base64
import random

st.set_page_config(page_title="For You, My Babyboy 💗", layout="wide")

# ---------- LOAD IMAGE ----------
def load_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = load_image_base64("buhb.jpeg")

# ---------- STYLES ----------
st.markdown("""
<style>
html, body {
    background: linear-gradient(180deg, #ffd6e8, #ffeef6);
    overflow-x: hidden;
    font-family: 'Georgia', serif;
}

.title {
    text-align: center;
    font-size: 3rem;
    color: #7a1c4b;
    margin-top: 20px;
}

.poem {
    max-width: 800px;
    margin: auto;
    padding: 30px;
    background: rgba(255, 255, 255, 0.65);
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(255,105,180,0.25);
    font-size: 1.1rem;
    line-height: 1.8;
    color: #3a0f25;
}

.game-box {
    background: rgba(255,255,255,0.75);
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0 15px 30px rgba(255,105,180,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='title'>For You, My Babyboy 💗</div>", unsafe_allow_html=True)

# ---------- 3D HEART + SWANS ----------
st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body style="margin:0; overflow:hidden;">

<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer({alpha:true});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Lights
const light = new THREE.PointLight(0xffffff, 1.2);
light.position.set(5,5,5);
scene.add(light);

// Heart Shape
const heartShape = new THREE.Shape();
heartShape.moveTo(0, 0);
heartShape.bezierCurveTo(0, 0, -1.5, -1.5, -3, 0);
heartShape.bezierCurveTo(-4.5, 2.5, -2, 5, 0, 6);
heartShape.bezierCurveTo(2, 5, 4.5, 2.5, 3, 0);
heartShape.bezierCurveTo(1.5, -1.5, 0, 0, 0, 0);

const heartGeometry = new THREE.ExtrudeGeometry(heartShape, {
    depth: 0.6,
    bevelEnabled: true,
    bevelThickness: 0.2,
    bevelSize: 0.2,
    bevelSegments: 10
});

const textureLoader = new THREE.TextureLoader();
const photoTexture = textureLoader.load("data:image/jpeg;base64,{{IMG}}");

const heartMaterial = new THREE.MeshStandardMaterial({
    map: photoTexture,
    metalness: 0.3,
    roughness: 0.4
});

const heart = new THREE.Mesh(heartGeometry, heartMaterial);
heart.scale.set(0.4,0.4,0.4);
scene.add(heart);

// Swan shapes (abstract elegant curves)
function createSwan(xStart) {
    const curve = new THREE.CatmullRomCurve3([
        new THREE.Vector3(xStart, 0, 0),
        new THREE.Vector3(xStart/2, 0.8, 0),
        new THREE.Vector3(0, 0.3, 0)
    ]);

    const tube = new THREE.TubeGeometry(curve, 50, 0.05, 8, false);
    const mat = new THREE.MeshStandardMaterial({color: 0xffffff});
    const swan = new THREE.Mesh(tube, mat);
    scene.add(swan);
    return swan;
}

const swanLeft = createSwan(-4);
const swanRight = createSwan(4);

function animate() {
    requestAnimationFrame(animate);

    heart.rotation.y += 0.01;
    heart.rotation.x += 0.005;

    swanLeft.position.x += 0.01;
    swanRight.position.x -= 0.01;

    renderer.render(scene, camera);
}
animate();
</script>

</body>
</html>
""".replace("{{IMG}}", img_base64), height=600)

# ---------- POEM ----------
st.markdown("""
<div class="poem">
We walked through storms that never asked permission.<br>
The kind that carved silence into our bones,<br>
the kind that taught us how to survive before we learned how to hope.<br><br>

There were nights love felt heavy,<br>
days it felt fragile,<br>
moments where staying was the bravest thing we could do.<br><br>

Everything else bent.<br>
Everything else broke.<br>
But not us.<br><br>

Because what we built was never loud.<br>
It was steady.<br>
Chosen.<br>
Earned.<br><br>

Now, standing where the storm can’t reach,<br>
I don’t want a love that forgets the past.<br>
I want one that survived it.<br><br>

If the world asks us to begin again,<br>
I will — every time —<br>
as long as it’s with you.
</div>
""", unsafe_allow_html=True)

# ---------- GAMES ----------
st.markdown("### 💘 Valentine Games")

with st.container():
    st.markdown("<div class='game-box'>", unsafe_allow_html=True)
    if st.button("💖 Tap for Love"):
        st.success(random.choice([
            "You are my safest place.",
            "I choose you, always.",
            "Still you. Still us.",
            "Forever starts here."
        ]))
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='game-box'>", unsafe_allow_html=True)
    answer = st.radio("What survives everything?", ["Time", "Fear", "Love"])
    if answer == "Love":
        st.success("Correct. It was always us 💗")
    st.markdown("</div>", unsafe_allow_html=True)


