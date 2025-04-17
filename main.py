import streamlit as st

st.set_page_config(page_title="Roleplay Configurator", layout="centered")

st.title("🎭 Streamlit Roleplay Configuration")

# 1. Input for 'prompt'
prompt = st.text_input("📝 Prompt", value="You are a friendly customer service agent")

# 2. Dropdown for 'roleplay_type'
roleplay_type = st.selectbox("🧑‍💼 Roleplay Type", options=["Customer", "Sales"])

# 3. Dropdown for 'voice_id'
voice_id = st.selectbox("🗣️ Voice ID", options=[
    "en-US-AndrewMultilingualNeural",
    "en-US-EmmaMultilingualNeural",
    "en-US-EchoTurboMultilingualNeural"
])

# 4. Dropdown for 'difficulty_level'
difficulty_level = st.selectbox("📊 Difficulty Level", options=["Easy", "Medium", "Hard"])

# 5. Session time - hardcoded
session_time = 10

# 6. Input for 'avatar_name'
avatar_name = st.text_input("🧑 Avatar Name", value="John")

# 7. user_id - hardcoded
user_id = "streamlit"

# 8. frontend_desc - hardcoded
frontend_desc = "This is a streamlit roleplay"

# Display the collected data
if st.button("Submit"):
    config = {
        "prompt": prompt,
        "roleplay_type": roleplay_type,
        "voice_id": voice_id,
        "difficulty_level": difficulty_level,
        "session_time": session_time,
        "avatar_name": avatar_name,
        "user_id": user_id,
        "frontend_desc": frontend_desc
    }

    st.subheader("🧾 Configuration Summary")
    st.json(config)
