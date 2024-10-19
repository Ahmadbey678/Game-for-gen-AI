import streamlit as st
import random

# Initialize scores and game states for both games
if 'rps_user_score' not in st.session_state:
    st.session_state.rps_user_score = 0
if 'rps_computer_score' not in st.session_state:
    st.session_state.rps_computer_score = 0
if 'tic_tac_toe_board' not in st.session_state:
    st.session_state.tic_tac_toe_board = [' '] * 9
if 'tic_tac_toe_turn' not in st.session_state:
    st.session_state.tic_tac_toe_turn = 'X'
if 'tic_tac_toe_winner' not in st.session_state:
    st.session_state.tic_tac_toe_winner = None

# Page config
st.set_page_config(page_title="Fun Game Corner", page_icon="🎮", layout="centered")

# Function to determine winner for Rock, Paper, Scissors
def determine_winner_rps(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw! 🤝"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win! 🎉"
    else:
        return "Computer wins! 😢"

# Function to check the winner for Tic Tac Toe
def check_winner_ttt(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return "Draw"
    return None

# Reset Tic Tac Toe game
def reset_tic_tac_toe():
    st.session_state.tic_tac_toe_board = [' '] * 9
    st.session_state.tic_tac_toe_turn = 'X'
    st.session_state.tic_tac_toe_winner = None

# Sidebar for game selection
game_choice = st.sidebar.radio("Choose a game:", ['Tic Tac Toe', 'Rock, Paper, Scissors'], index=0)

# --------- Rock Paper Scissors Game ---------
if game_choice == 'Rock, Paper, Scissors':
    st.markdown("<h1 style='color: darkblue; text-align: center;'>Rock, Paper, Scissors</h1>", unsafe_allow_html=True)
    choices = {'Rock': '✊', 'Paper': '🖐', 'Scissors': '✌'}
    
    user_choice = st.selectbox('Choose your move:', list(choices.keys()), format_func=lambda x: f"{x} {choices[x]}")
    computer_choice = random.choice(list(choices.keys()))

    if st.button('Play Rock Paper Scissors'):
        result = determine_winner_rps(user_choice, computer_choice)
        
        if result == "You win! 🎉":
            st.session_state.rps_user_score += 1
            st.markdown(f"<h3 style='color: green;'>{result}</h3>", unsafe_allow_html=True)
        elif result == "Computer wins! 😢":
            st.session_state.rps_computer_score += 1
            st.markdown(f"<h3 style='color: red;'>{result}</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color: orange;'>{result}</h3>", unsafe_allow_html=True)
        
        st.write(f"**Your choice:** {choices[user_choice]}")
        st.write(f"**Computer's choice:** {choices[computer_choice]}")
    
    # Display scores
    st.markdown(f"<h4>Your Score: {st.session_state.rps_user_score} 💪</h4>")
    st.markdown(f"<h4>Computer's Score: {st.session_state.rps_computer_score} 🤖</h4>")
    
    # Reset button for scores
    if st.button('Reset RPS Scores'):
        st.session_state.rps_user_score = 0
        st.session_state.rps_computer_score = 0
        st.success("Rock Paper Scissors scores reset!")

# --------- Tic Tac Toe Game ---------
elif game_choice == 'Tic Tac Toe':
    st.markdown("<h1 style='color: darkgreen; text-align: center;'>Tic Tac Toe</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Player X vs Player O. Take turns to win!</p>", unsafe_allow_html=True)

    # Tic Tac Toe Board UI
    board = st.session_state.tic_tac_toe_board
    turn = st.session_state.tic_tac_toe_turn
    winner = st.session_state.tic_tac_toe_winner

    # Display the 3x3 grid as interactive buttons
    cols = [st.columns(3) for _ in range(3)]
    for i in range(9):
        row = i // 3
        col = i % 3
        if cols[row][col].button(board[i], key=i, disabled=board[i] != ' ' or winner is not None):
            board[i] = turn
            st.session_state.tic_tac_toe_turn = 'O' if turn == 'X' else 'X'
            st.session_state.tic_tac_toe_winner = check_winner_ttt(board)

    # Check for a winner or draw
    winner = st.session_state.tic_tac_toe_winner
    if winner:
        if winner == "Draw":
            st.markdown("<h3 style='color: orange; text-align: center;'>It's a Draw! 🤝</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color: green; text-align: center;'>Player {winner} wins! 🎉</h3>", unsafe_allow_html=True)

    # Reset button for Tic Tac Toe
    if st.button('Reset Tic Tac Toe'):
        reset_tic_tac_toe()
        st.success("Tic Tac Toe board reset!")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose your game wisely and have fun!</p>", unsafe_allow_html=True)
