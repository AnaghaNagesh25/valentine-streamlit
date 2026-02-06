st.markdown("## 💕 Find Each Other 💕")

# --- Initialize game state ---
if "car1" not in st.session_state:
    st.session_state.car1 = [0, 0]      # You
    st.session_state.car2 = [4, 4]      # Him
    st.session_state.heart = [2, 2]
    st.session_state.won = False

GRID_SIZE = 5

def move(car, direction):
    if direction == "up" and car[0] > 0:
        car[0] -= 1
    elif direction == "down" and car[0] < GRID_SIZE - 1:
        car[0] += 1
    elif direction == "left" and car[1] > 0:
        car[1] -= 1
    elif direction == "right" and car[1] < GRID_SIZE - 1:
        car[1] += 1

# --- Grid display ---
grid_html = "<div style='display:grid;grid-template-columns:repeat(5,50px);gap:6px;justify-content:center;'>"

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        cell = ""
        if [i, j] == st.session_state.car1:
            cell = "🚗"
        elif [i, j] == st.session_state.car2:
            cell = "🚙"
        elif [i, j] == st.session_state.heart:
            cell = "💖"

        grid_html += f"""
        <div style="
            width:50px;
            height:50px;
            background:linear-gradient(145deg,#ffd6e8,#ffb6d5);
            border-radius:14px;
            box-shadow:inset 4px 4px 8px #ff9fc7,inset -4px -4px 8px #fff;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:26px;">
            {cell}
        </div>
        """

grid_html += "</div>"
st.markdown(grid_html, unsafe_allow_html=True)

st.markdown("### 💕 Move *You* (🚗)")
c1 = st.columns(4)
if c1[0].button("⬅️", key="c1l"): move(st.session_state.car1, "left")
if c1[1].button("⬆️", key="c1u"): move(st.session_state.car1, "up")
if c1[2].button("⬇️", key="c1d"): move(st.session_state.car1, "down")
if c1[3].button("➡️", key="c1r"): move(st.session_state.car1, "right")

st.markdown("### 💕 Move *Him* (🚙)")
c2 = st.columns(4)
if c2[0].button("⬅️", key="c2l"): move(st.session_state.car2, "left")
if c2[1].button("⬆️", key="c2u"): move(st.session_state.car2, "up")
if c2[2].button("⬇️", key="c2d"): move(st.session_state.car2, "down")
if c2[3].button("➡️", key="c2r"): move(st.session_state.car2, "right")

# --- Win condition ---
if (
    st.session_state.car1 == st.session_state.heart
    and st.session_state.car2 == st.session_state.heart
):
    st.session_state.won = True

if st.session_state.won:
    st.markdown("""
    <div style="
        margin-top:20px;
        padding:18px;
        background:linear-gradient(135deg,#ff8fcf,#ffc1e3);
        border-radius:20px;
        text-align:center;
        font-size:18px;
        box-shadow:0 10px 25px rgba(255,105,180,0.4);
        color:#5b0036;">
        💗 You always find each other.<br>
        No matter the path. No matter the storm. 💗
    </div>
    """, unsafe_allow_html=True)


