import streamlit as st
import random

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #4CAF50;
    }
    .stMarkdown h1 {
        color: #4CAF50;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 20px;
    }
    .stMarkdown h2 {
        color: #333;
        text-align: center;
        font-size: 2rem;
    }
    .stMarkdown h3 {
        color: #4CAF50;
        text-align: center;
        font-size: 1.5rem;
    }
    .stSuccess {
        color: #4CAF50;
        font-size: 1.2rem;
        text-align: center;
    }
    .stError {
        color: #ff4444;
        font-size: 1.2rem;
        text-align: center;
    }
    .stSidebar {
        background-color: #4CAF50;
        color: white;
        padding: 20px;
        border-radius: 10px;
    }
    .stSidebar h1 {
        color: white;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and Description
st.title("🎮 Number Guessing Game 🎮")
st.markdown("Welcome to the Number Guessing Game! Guess the correct number and win. 🏆")

# Difficulty Levels with colorful buttons
st.markdown("### 🎯 Select Difficulty Level")
difficulty = st.radio(
    "",
    ["Easy", "Medium", "Hard"],
    index=0,
    horizontal=True,
    key="difficulty",
    help="Choose your difficulty level."
)

# Set number range based on difficulty
if difficulty == "Easy":
    number_range = (1, 50)
elif difficulty == "Medium":
    number_range = (1, 100)
else:
    number_range = (1, 200)

# Initialize session state
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(number_range[0], number_range[1])
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# Input for user's guess
st.markdown("### 🔢 Enter Your Guess")
user_guess = st.number_input(
    "",
    min_value=number_range[0],
    max_value=number_range[1],
    step=1,
    key="user_guess",
    help="Enter your guess here."
)

# Check the guess
if st.button("🚀 Submit Guess", key="submit_guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.target_number:
        st.error("📉 Too Low! Try a higher number.")
    elif user_guess > st.session_state.target_number:
        st.error("📈 Too High! Try a lower number.")
    else:
        st.success(f"🎉 Correct! You guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.score += 1
        st.balloons()  # Celebration effect
        st.session_state.target_number = random.randint(number_range[0], number_range[1])
        st.session_state.attempts = 0

# Display score
st.markdown(f"### 🏅 Your Score: **{st.session_state.score}**")

# Leaderboard
st.sidebar.markdown("### 🏆 Leaderboard 🏆")
if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []
if st.session_state.score > 0:
    st.session_state.leaderboard.append(st.session_state.score)
st.sidebar.write("Top Scores:")
st.sidebar.write(sorted(st.session_state.leaderboard, reverse=True)[:5])

# Theme Toggle
st.sidebar.markdown("### 🎨 Choose Theme")
theme = st.sidebar.selectbox("", ["Light", "Dark"], key="theme")
if theme == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #4CAF50;
        }
        .stSidebar {
            background-color: #333;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")