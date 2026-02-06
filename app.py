import streamlit as st
import streamlit.components.v1 as components
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For You 💕",
    page_icon="💗",
    layout="wide"
)

# ---------------- TITLE ----------------
st.markdown(
    """
    <h1 style='text-align:center; color:#c94f7c;'>
        I made this for you 💗
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center; font-size:18px; color:#7a3b4d;'>
    A little pink world, with all my love ✨
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- POEM CARD ----------------
st.markdown(
    """
    <div style="
        max-width:700px;
        margin: 30px auto;
        background: rgba(255, 214, 232, 0.6);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        font-size: 18px;
        color: #5b2b3a;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    ">
    In a world that moves too fast,<br>
    you slow my heart down.<br><br>

    In days that feel too loud,<br>
    you feel like calm.<br><br>

    If love were a place,<br>
    it would look a lot like you 🤍
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD IMAGE ----------------
with open("buhb.jpeg", "rb") as f:
    encoded_image = base64.b64encode(f.read()).decode()

# ---------------- 3D ANIMATION ----------------
html_3d = f"""
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
    50,
    window.innerWidth / window.innerHeight,
    0.1,
    100
  );

  const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);

  scene.add(new THREE.AmbientLight(0xffffff, 1));
  const light = new THREE.PointLight(0xffffff, 0.8);
  light.position.set(5,5,5);
  scene.add(light);

  const loader = new THREE.TextureLoader();
  loader.load("data:image/jpeg;base64,{encoded_image}", texture => {{
    const geometry = new THREE.PlaneGeometry(4, 5.5);
    const material = new THREE.MeshBasicMaterial({{
      map: texture,
      transparent: true
    }});

    const couple = new THREE.Mesh(geometry, material);
    scene.add(couple);

    function animate() {{
      requestAnimationFrame(animate);
      const t = Date.now() * 0.001;
      couple.position.y = Math.sin(t) * 0.15;
      couple.rotation.y = Math.sin(t * 0.5) * 0.15;
      camera.position.x = Math.sin(t * 0.3) * 0.4;
      camera.lookAt(0, 0, 0);
      renderer.render(scene, camera);
    }}
    animate();
  }});

  camera.position.z = 7;

  window.addEventListener("resize", () => {{
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  }});
</script>

</body>
</html>
"""

components.html(html_3d, height=600)

# ---------------- VALENTINE GAME ----------------
st.markdown("---")

st.markdown(
    "<h2 style='text-align:center; color:#c94f7c;'>💘 Catch My Heart 💘</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Click the hearts and collect love ✨</p>",
    unsafe_allow_html=True
)

if "love_score" not in st.session_state:
    st.session_state.love_score = 0

messages = [
    "You make everything softer 💕",
    "You’re my favorite feeling 🌷",
    "You feel like home 🏡",
    "I’d choose you every lifetime ♾️",
    "You already have my heart 💗"
]

cols = st.columns(5)
for col in cols:
    with col:
        if st.button("💗"):
            st.session_state.love_score += 1
            if st.session_state.love_score <= len(messages):
                st.toast(messages[st.session_state.love_score - 1])

st.markdown(
    f"<h3 style='text-align:center;'>Love Score: {st.session_state.love_score} 💞</h3>",
    unsafe_allow_html=True
)

if st.session_state.love_score >= 5:
    st.markdown(
        """
        <div style="
            background: rgba(255, 214, 232, 0.6);
            padding: 30px;
            border-radius: 25px;
            text-align: center;
            margin-top: 30px;
            font-size: 18px;
            color: #5b2b3a;
        ">
        🦄✨ <br><br>
        You win.<br><br>
        Not the game —<br>
        my heart 💗<br><br>
        Happy Valentine’s 🤍
        </div>
        """,
        unsafe_allow_html=True
    )
