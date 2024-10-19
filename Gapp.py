import streamlit as st
import random

# Define choices and scores
choices = ['Rock', 'Paper', 'Scissors']
user_score = 0
computer_score = 0

# Set page configuration for a fun title and layout
st.set_page_config(page_title="Rock, Paper, Scissors", page_icon="✊🖐✌", layout="centered")

# Define function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Add colorful title
st.markdown("<h1 style='color: darkblue; text-align: center;'>Rock, Paper, Scissors</h1>", unsafe_allow_html=True)

# Display game instructions
st.markdown("<p style='text-align: center;'>Choose Rock, Paper, or Scissors and try to beat the computer!</p>", unsafe_allow_html=True)

# Add a colorful select box for the user's choice
user_choice = st.selectbox(
    'Make your choice:', 
    choices, 
    index=0, 
    help="Choose Rock, Paper, or Scissors!"
)

# Let the computer randomly select a choice
computer_choice = random.choice(choices)

# Add a play button
if st.button('Play'):
    result = determine_winner(user_choice, computer_choice)

    # Display colorful result message
    if result == "You win!":
        st.markdown(f"<h3 style='color: green;'>{result}</h3>", unsafe_allow_html=True)
    elif result == "Computer wins!":
        st.markdown(f"<h3 style='color: red;'>{result}</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color: orange;'>{result}</h3>", unsafe_allow_html=True)
    
    # Display user and computer choices
    st.write(f"Your choice: {user_choice}")
    st.write(f"Computer's choice: {computer_choice}")
    
    # Update scores based on result
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

# Display scores
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>Current Scores</h3>", unsafe_allow_html=True)
st.write(f"**Your Score:** {user_score}")
st.write(f"**Computer's Score:** {computer_score}")

# Add a reset button to reset the scores
if st.button('Reset Scores'):
    user_score = 0
    computer_score = 0
    st.success("Scores have been reset!")

# Add a footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px;'>Built with ❤️ using Python and Streamlit</p>", unsafe_allow_html=True)
