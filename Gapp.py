import streamlit as st
import random

# Set up persistent score tracking
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0

# Define the game choices with emojis
choices = {'Rock': '✊', 'Paper': '🖐', 'Scissors': '✌'}
user_score = st.session_state.user_score
computer_score = st.session_state.computer_score

# Page configuration with title and emojis
st.set_page_config(page_title="Rock, Paper, Scissors", page_icon="✊🖐✌", layout="centered")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw! 🤝"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win! 🎉"
    else:
        return "Computer wins! 😢"

# Add colorful title
st.markdown("<h1 style='color: darkblue; text-align: center;'>Rock, Paper, Scissors Game</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: darkgreen; text-align: center;'>Choose wisely and beat the computer!</h2>", unsafe_allow_html=True)

# User choice selection with emojis
user_choice = st.selectbox(
    'Make your choice:',
    list(choices.keys()),
    format_func=lambda x: f"{x} {choices[x]}",
    help="Choose Rock, Paper, or Scissors!"
)

# Computer randomly chooses a move
computer_choice = random.choice(list(choices.keys()))

# Add play button and handle game logic
if st.button('Play'):
    result = determine_winner(user_choice, computer_choice)
    
    # Display colorful result with emojis
    if result == "You win! 🎉":
        st.markdown(f"<h3 style='color: green;'>{result}</h3>", unsafe_allow_html=True)
        st.session_state.user_score += 1
    elif result == "Computer wins! 😢":
        st.markdown(f"<h3 style='color: red;'>{result}</h3>", unsafe_allow_html=True)
        st.session_state.computer_score += 1
    else:
        st.markdown(f"<h3 style='color: orange;'>{result}</h3>", unsafe_allow_html=True)
    
    # Display choices with emojis
    st.write(f"**Your choice:** {choices[user_choice]} {user_choice}")
    st.write(f"**Computer's choice:** {choices[computer_choice]} {computer_choice}")
    
# Display current scores
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>Current Scores</h3>", unsafe_allow_html=True)
st.markdown(f"<h4 style='color: blue;'>Your Score: {st.session_state.user_score} 💪</h4>", unsafe_allow_html=True)
st.markdown(f"<h4 style='color: red;'>Computer's Score: {st.session_state.computer_score} 🤖</h4>", unsafe_allow_html=True)

# Add a reset button for resetting the scores
if st.button('Reset Scores'):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Scores have been reset!")

# Add a footer for fun
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>Built with ❤️ by Ahmad Bey</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>Rock ✊, Paper 🖐, Scissors ✌ - Let the battle continue!</p>", unsafe_allow_html=True)
