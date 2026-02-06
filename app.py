st.markdown("---")

st.markdown(
    "<h2 style='text-align:center; color:#c94f7c;'>💘 Catch My Heart 💘</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Click the hearts to collect love points ✨</p>",
    unsafe_allow_html=True
)

# Initialize score
if "love_score" not in st.session_state:
    st.session_state.love_score = 0

messages = [
    "You make my days softer 💕",
    "I smile every time I think of you 🌷",
    "You feel like home 🏡",
    "I’d choose you every lifetime ♾️",
    "You already won my heart 💗"
]

cols = st.columns(5)

for i, col in enumerate(cols):
    with col:
        if st.button("💗"):
            st.session_state.love_score += 1
            if st.session_state.love_score <= len(messages):
                st.toast(messages[st.session_state.love_score - 1])

st.markdown(
    f"<h3 style='text-align:center;'>Love Score: {st.session_state.love_score} 💞</h3>",
    unsafe_allow_html=True
)

# Win condition
if st.session_state.love_score >= 5:
    st.markdown(
        """
        <div style="
            background: rgba(255, 214, 232, 0.6);
            padding: 25px;
            border-radius: 20px;
            text-align: center;
            margin-top: 20px;
        ">
        <h2>🦄 You unlocked the secret 💖</h2>
        <p>
        If love were a game,<br>
        you’d already be winning.<br><br>
        Happy Valentine’s, my favorite person 💕
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

