import streamlit.components.v1 as components

components.html("""
<!DOCTYPE html>
<html>
<head>
  <style>
    body { margin:0; background:transparent; overflow:hidden; }
  </style>
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.z = 6;

const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// 💗 Heart
const heartShape = new THREE.Shape();
heartShape.moveTo(0,0);
heartShape.bezierCurveTo(0,0,-1.5,-1.5,-3,0);
heartShape.bezierCurveTo(-4.5,2,0,4,0,6);
heartShape.bezierCurveTo(0,4,4.5,2,3,0);
heartShape.bezierCurveTo(1.5,-1.5,0,0,0,0);

const heartGeo = new THREE.ExtrudeGeometry(heartShape,{
  depth:0.6,
  bevelEnabled:true,
  bevelThickness:0.2,
  bevelSize:0.2
});

const heartMat = new THREE.MeshStandardMaterial({
  color:0xff6fae,
  metalness:0.6,
  roughness:0.2
});

const heart = new THREE.Mesh(heartGeo, heartMat);
heart.scale.set(0.25,0.25,0.25);
scene.add(heart);

// 🪽 Wings
function createWing(side){
  const wingGeo = new THREE.PlaneGeometry(3,2,12,12);
  const wingMat = new THREE.MeshStandardMaterial({
    color:0xffc1dc,
    side:THREE.DoubleSide,
    transparent:true,
    opacity:0.85
  });
  const wing = new THREE.Mesh(wingGeo, wingMat);
  wing.position.x = side * 2.2;
  wing.rotation.y = side * Math.PI/6;
  return wing;
}

const leftWing = createWing(-1);
const rightWing = createWing(1);
scene.add(leftWing);
scene.add(rightWing);

// 💡 Light
const light = new THREE.PointLight(0xffffff,1.5);
light.position.set(5,5,5);
scene.add(light);

const ambient = new THREE.AmbientLight(0xffb6d9,1);
scene.add(ambient);

let t = 0;
function animate(){
  requestAnimationFrame(animate);
  t += 0.03;
  heart.rotation.y += 0.01;

  leftWing.rotation.z = Math.sin(t)*0.2;
  rightWing.rotation.z = -Math.sin(t)*0.2;

  renderer.render(scene,camera);
}
animate();
</script>

