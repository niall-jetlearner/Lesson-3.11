from tkinter import * 
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0),('paper',1),('scissors',2)]

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text = "Computer Won!")
    computer_score_label.config(text = "Computer Score :" + str(computer_score))
    players_score_label.config(text = "Player Score :" + str(player_score))

def player_wins():
    global player_score, computer_score
    player_score += 1
    winner_label.config(text = "Player Won!")
    players_score_label.config(text = "Player Score :" + str(player_score))
    computer_score_label.config(text = "Computer Score :" + str(computer_score))

def tie():
    global computer_score, player_score
    winner_label.config(text = "Tie!")
    computer_score_label.config(text = "Computer Score :" + str(computer_score))
    players_score_label.config(text = "Player Score :" + str(player_score))

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)
    players_choice_label.config(text = "You've selected :" + player_input[0])
    computer_choice_label.config(text = "Computer selected :" + computer_input[0])

    if(player_input == computer_input):
        tie()

    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            computer_wins()
        elif(computer_input[1] == 2):
            player_wins()

    if(player_input[1] == 1):
        if(computer_input[1] == 0):
            player_wins()
        elif(computer_input[1] == 2):
            computer_wins()

    if(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_wins()
        elif(computer_input[1] == 1):
            player_wins()

def get_computer_choice():
    return random.choice(options)


game_window = Tk()
game_window.title("Rock Paper Scissors Game")

app_font = font.Font(size = 12)

game_title = Label(game_window, text = "Rock Paper Scissors", font = font.Font(size = 20), fg = 'grey')
game_title.pack()

winner_label = Label(game_window, text = "Player Won!!", fg = "green", font = font.Font(size = 14))
winner_label.pack()

frame = Frame(game_window)
frame.pack()

player_options = Label(frame, text = "Your Options :", font = font.Font(size = 15), fg = "grey")
player_options.grid(row = 0, column = 0, padx = 8, pady = 5)

rock_button = Button(frame, text = "Rock", bg = "pink", padx = 8, pady = 5, command = lambda: player_choice(options[0]))
rock_button.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_button = Button(frame, text = "Paper", bg = "silver", padx = 8, pady = 5, command = lambda: player_choice(options[1]))
paper_button.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_button = Button(frame, text = "Scissors", bg = "lightblue", padx = 8, pady = 5, command = lambda: player_choice(options[2]))
scissors_button.grid(row = 1, column = 3, padx = 8, pady = 5)

score = Label(frame, text = "Score :", font = font.Font(size = 15), fg = "grey")
score.grid(row = 2, column = 0, padx = 8, pady = 5)

players_choice_label = Label(frame, text = "Player chose : ---", font = font.Font(size = 12))
players_choice_label.grid(row = 3, column = 1, padx = 8, pady = 5)

players_score_label = Label(frame, text = "Player score : ---", font = font.Font(size = 12))
players_score_label.grid(row = 3, column = 2, padx = 8, pady = 5)

computer_choice_label = Label(frame, text = "Computer chose : ---", font = font.Font(size = 12))
computer_choice_label.grid(row = 4, column = 1, padx = 8, pady = 5)

computer_score_label = Label(frame, text = "Computer score : ---", font = font.Font(size = 12))
computer_score_label.grid(row = 4, column = 2, padx = 8, pady = 5)

game_window.geometry('700x300')
game_window.mainloop()