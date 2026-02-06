import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="For You 💕", layout="wide")

st.markdown(
    "<h1 style='text-align:center; color:#c94f7c;'>I made this for you 💗</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>A tiny 3D world, just us ✨</p>",
    unsafe_allow_html=True
)

# Load image
with open("buhb.jpeg", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

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
  loader.load("data:image/jpeg;base64,{encoded}", texture => {{
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
