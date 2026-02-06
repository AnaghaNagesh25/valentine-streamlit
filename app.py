import streamlit.components.v1 as components

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
canvas {
  background: linear-gradient(#ffd1ea, #ff9fcf);
  border-radius: 20px;
  box-shadow: 0 15px 30px rgba(255,105,180,0.4);
}
button {
  background:#ff6fae;
  border:none;
  padding:12px 20px;
  border-radius:20px;
  color:white;
  font-size:16px;
  cursor:pointer;
}
</style>
</head>
<body>

<h2 style="color:#5b0036;text-align:center;">
Run Toward Forever 💗
</h2>

<canvas id="game" width="600" height="200"></canvas>
<br><br>
<div style="text-align:center;">
<button onclick="jump()">JUMP 💕</button>
</div>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let y = 140;
let vy = 0;
let gravity = 1.2;
let grounded = true;
let heartX = 550;
let gameWon = false;

const playerImg = new Image();
playerImg.src = "buhb.jpeg";

const heartImg = new Image();
heartImg.src = "https://i.imgur.com/Qp5ZQ9M.png"; // glossy heart

function jump(){
  if(grounded){
    vy = -15;
    grounded = false;
  }
}

function drawHeart(){
  ctx.save();
  ctx.translate(heartX, 120);
  ctx.scale(1.6,1.6);
  ctx.shadowColor = "#ff4fa3";
  ctx.shadowBlur = 20;
  ctx.drawImage(heartImg, -30, -30, 60, 60);
  ctx.restore();
}

function update(){
  ctx.clearRect(0,0,canvas.width,canvas.height);

  // Player physics
  y += vy;
  vy += gravity;
  if(y >= 140){
    y = 140;
    vy = 0;
    grounded = true;
  }

  // Ground
  ctx.fillStyle = "#ff8fcf";
  ctx.fillRect(0,170,600,30);

  // Player
  ctx.drawImage(playerImg, 50, y, 40, 40);

  // Heart movement
  if(!gameWon){
    heartX -= 2;
  }

  drawHeart();

  // Win condition
  if(heartX < 90){
    gameWon = true;
    ctx.fillStyle = "#5b0036";
    ctx.font = "20px serif";
    ctx.fillText("You made it to forever 💗", 180, 90);
  }

  requestAnimationFrame(update);
}

update();
</script>

</body>
</html>
""", height=360)

