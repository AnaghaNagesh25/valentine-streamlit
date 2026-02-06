import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="For You, My Babyboy 💗", layout="wide")

# ------------------- GLOBAL PINK STYLE -------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background: linear-gradient(180deg,#ffd6eb,#ffb3d1);
}
h1,h2,h3,p {
    color:#5b0036;
}
</style>
""", unsafe_allow_html=True)

# ------------------- TITLE -------------------
st.markdown("<h1 style='text-align:center;'>For You, My Babyboy 💞</h1>", unsafe_allow_html=True)

# ------------------- POEM (UNCHANGED) -------------------
st.markdown("""
<div style="max-width:750px;margin:auto;padding:25px;
background:rgba(255,214,235,0.75);
border-radius:24px;
box-shadow:0 20px 40px rgba(255,105,180,0.35);">

<p>
We walked through storms that left no witnesses,<br>
winds that tried to rewrite who we were.
</p>

<p>
We learned how to stay soft<br>
in a world that asked us to harden.
</p>

<p>
Everything else bent.<br>
Everything else broke.
</p>

<p>
But our love —<br>
untouched, unpolluted —<br>
stood exactly where the storm gave up.
</p>

<p>
We didn’t rush the healing.<br>
We let time teach us gentleness again.
</p>

<p>
And now, in the quiet after the chaos,<br>
I don’t want a beginning that forgets the past.<br>
I want a forever that remembers<br>
what it took to arrive here.
</p>

<p>
If the world falls apart again,<br>
let it.
</p>

<p>
As long as it’s you and me,<br>
I will choose this love —<br>
again, again, and forever.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------- 3D ROTATING HEART (BIG) -------------------
components.html("""
<div style="display:flex;justify-content:center;">
<canvas id="heart" width="420" height="420"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45,1,0.1,1000);
const renderer = new THREE.WebGLRenderer({alpha:true,canvas:document.getElementById("heart")});
renderer.setSize(420,420);

const shape = new THREE.Shape();
shape.moveTo(0,0);
shape.bezierCurveTo(0,0,0,-3,-3,-3);
shape.bezierCurveTo(-6,-3,-6,3,-6,3);
shape.bezierCurveTo(-6,7,-3,9,0,12);
shape.bezierCurveTo(3,9,6,7,6,3);
shape.bezierCurveTo(6,3,6,-3,3,-3);
shape.bezierCurveTo(1,-3,0,0,0,0);

const geometry = new THREE.ExtrudeGeometry(shape,{depth:3,bevelEnabled:true,bevelSize:0.6});
const material = new THREE.MeshStandardMaterial({color:0xff5fa2});
const heart = new THREE.Mesh(geometry,material);
scene.add(heart);

const light = new THREE.PointLight(0xffffff,1);
light.position.set(10,10,10);
scene.add(light);

camera.position.z = 18;

function animate(){
    requestAnimationFrame(animate);
    heart.rotation.y += 0.01;
    heart.rotation.x += 0.005;
    renderer.render(scene,camera);
}
animate();
</script>
""", height=460)

st.markdown("---")

# ------------------- MINI DINO-STYLE LOVE GAME -------------------
st.markdown("## 💗 Run Toward Forever")

components.html("""
<canvas id="game" width="720" height="260"></canvas>
<br>
<div style="text-align:center;">
<button onclick="jumpGirl()">She jumps 💖</button>
<button onclick="jumpBoy()">He jumps 💙</button>
</div>

<style>
button{
background:#ff8fcf;
border:none;
padding:10px 18px;
margin:8px;
border-radius:18px;
font-weight:600;
color:#4b0f2b;
cursor:pointer;
}
</style>

<script>
const c = document.getElementById("game");
const ctx = c.getContext("2d");

const img = new Image();
img.src = "buhb.jpeg";

let g={x:80,y:170,v:0};
let b={x:160,y:170,v:0};
let grav=1.1;
let obs=[{x:500},{x:650}];
let heartX=820;
let won=false;

function jumpGirl(){ if(g.y>=170) g.v=-15; }
function jumpBoy(){ if(b.y>=170) b.v=-15; }

function drawChar(x,y){
 ctx.save();
 ctx.beginPath();
 ctx.arc(x+20,y+20,20,0,Math.PI*2);
 ctx.clip();
 ctx.drawImage(img,x,y,40,40);
 ctx.restore();
}

function loop(){
 ctx.clearRect(0,0,720,260);

 ctx.fillStyle="#ff8fcf";
 ctx.fillRect(0,210,720,50);

 g.y+=g.v; g.v+=grav;
 b.y+=b.v; b.v+=grav;
 if(g.y>170){g.y=170;g.v=0;}
 if(b.y>170){b.y=170;b.v=0;}

 obs.forEach(o=>o.x-=2);
 heartX-=2;

 ctx.fillStyle="#ff4fa3";
 obs.forEach(o=>ctx.fillRect(o.x,180,20,30));

 drawChar(g.x,g.y);
 drawChar(b.x,b.y);

 ctx.font="40px serif";
 ctx.fillText("💗",heartX,190);

 if(heartX<200 && !won){
   won=true;
   ctx.fillStyle="#5b0036";
   ctx.font="28px serif";
   ctx.fillText("Forever reached 💞",230,120);
 }
 requestAnimationFrame(loop);
}
loop();
</script>
""", height=360)

st.markdown("---")

# ------------------- PINK RESULT CARD -------------------
def pink_result(text):
    st.markdown(f"""
    <div style="
    background:#ffd6eb;
    padding:15px;
    border-radius:18px;
    box-shadow:0 10px 25px rgba(255,105,180,0.35);
    color:#5b0036;
    text-align:center;
    font-weight:600;">
    {text}
    </div>
    """, unsafe_allow_html=True)

# ------------------- FUN GAMES -------------------
st.markdown("## 💕 Little Valentine Games")

if st.button("🎲 Fate Dice"):
    pink_result(random.choice([
        "Even fate bent so we could meet.",
        "Every road led back to us.",
        "This love was written long before us.",
        "No matter the timeline — it’s you."
    ]))

if st.button("💌 Love Message"):
    pink_result(random.choice([
        "You are my calm after every storm.",
        "Still you. Still us.",
        "I’d choose you in every lifetime.",
        "My safest place is loving you."
    ]))

if st.button("♾️ FOREVER"):
    st.balloons()
    pink_result("Again. Again. And forever 💗")




