#imports
import turtle as trtl

# Create all necessary turtles 

#Create game board painter 
game_painter = trtl.Turtle()
game_painter.speed("fastest")
game_painter.pensize(5)
game_painter.penup()

#Create box writers
box1_writer = trtl.Turtle()
box1_writer.penup()
box1_writer.hideturtle()

box2_writer = trtl.Turtle()
box2_writer.penup()
box2_writer.hideturtle()

box3_writer = trtl.Turtle()
box3_writer.penup()
box3_writer.hideturtle()

box4_writer = trtl.Turtle()
box4_writer.penup()
box4_writer.hideturtle()

box5_writer = trtl.Turtle()
box5_writer.penup()
box5_writer.hideturtle()

box6_writer = trtl.Turtle()
box6_writer.penup()
box6_writer.hideturtle()

box7_writer = trtl.Turtle()
box7_writer.penup()
box7_writer.hideturtle()

box8_writer = trtl.Turtle()
box8_writer.penup()
box8_writer.hideturtle()

box9_writer = trtl.Turtle()
box9_writer.penup()
box9_writer.hideturtle()

#Create turtle that indicates player turns
turn_indicator = trtl.Turtle()
turn_indicator.shape("arrow")
turn_indicator.pencolor("blue")
turn_indicator.penup()
turn_indicator.goto(200, -150)

#Create turtle that writes result of game
result_writer = trtl.Turtle()
result_writer.penup()
result_writer.hideturtle()

# Initialize variables        

#Initialize variables for letter colors
x_color = "teal"
o_color = "orange"

#Initialize variables for drawing game board grid
x_pos = -100
y_pos = 0

#Initialize variables for box coordinates
left_column = -160
middle_column = -60
right_column = 37
top_row = 30
middle_row = -70
bottom_row = -174

#Initialize list for each turn during the game
turns = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

#Initialize variable to access indexes of the turns list
index = 0

#Initialize variables to check which letter each box has
#These are created so that if a player makes a move in a box, the corresponding variables will change and be used to check if the game is finished
box1 = "1"
box2 = "2"
box3 = "3"
box4 = "4"
box5 = "5"
box6 = "6"
box7 = "7"
box8 = "8"
box9 = "9"

#Initialize variables to help move turtle to indicate which player's turn it is
xturn_ypos = 20
oturn_ypos = -130

#Set up game environment

#Tells user to use the numbers displayed to play the game
print("During the game, click the number of the corresponding box to make your move there.")

#Write title of game
game_painter.goto(-195, 220)
game_painter.write("Tic Tac Toe", font=("Arial", 40, "normal"))

#Create game board
game_painter.goto(100, -200)
game_painter.setheading(180)
game_painter.pendown()
for i in range(4):
    game_painter.forward(300)
    game_painter.right(90)
for i in range(2):
    game_painter.setheading(270)
    game_painter.penup()
    game_painter.goto(x_pos, 100)
    game_painter.pendown()
    game_painter.forward(300)
    x_pos += 100
for i in range(2):
    game_painter.setheading(0)
    game_painter.penup()
    game_painter.goto(-200, y_pos)
    game_painter.pendown()
    game_painter.forward(300)
    y_pos -= 100
game_painter.hideturtle()

#Write numbers in game board
box1_writer.goto(left_column, top_row)
box1_writer.write("1", font=("Arial", 21, "normal"))
box2_writer.goto(middle_column, top_row)
box2_writer.write("2", font=("Arial", 21, "normal"))
box3_writer.goto(right_column, top_row)
box3_writer.write("3", font=("Arial", 21, "normal"))
box4_writer.goto(left_column, middle_row)
box4_writer.write("4", font=("Arial", 21, "normal"))
box5_writer.goto(middle_column, middle_row)
box5_writer.write("5", font=("Arial", 21, "normal"))
box6_writer.goto(right_column, middle_row)
box6_writer.write("6", font=("Arial", 21, "normal"))
box7_writer.goto(left_column, bottom_row)
box7_writer.write("7", font=("Arial", 21, "normal"))
box8_writer.goto(middle_column, bottom_row)
box8_writer.write("8", font=("Arial", 21, "normal"))
box9_writer.goto(right_column, bottom_row)
box9_writer.write("9", font=("Arial", 21, "normal"))

#Set up indicator beside the game board to indicate player turns
turn_indicator.pencolor(o_color)
turn_indicator.write("Player O's Turn", font=("Arial", 25, "normal"))
turn_indicator.goto(200, 0)
turn_indicator.pencolor(x_color)
turn_indicator.write("Player X's Turn", font=("Arial", 25, "normal"))
turn_indicator.goto(150, 20)
turn_indicator.pencolor("black")

#Adjust coordinates of writers to write letters, since the letters will be larger in size compared to the numbers
box1_writer.goto(left_column-10, top_row-10)
box2_writer.goto(middle_column-10, top_row-10)
box3_writer.goto(right_column-10, top_row-10)
box4_writer.goto(left_column-11, middle_row-10)
box5_writer.goto(middle_column-10, middle_row-10)
box6_writer.goto(right_column-10, middle_row-10)
box7_writer.goto(left_column-10, bottom_row-10)
box8_writer.goto(middle_column-10, bottom_row-10)
box9_writer.goto(right_column-10, bottom_row-10)

# Define necessary functions for game

#Stops game and writes who won
def game_won(winner):
   #Clears the indicator after the game is finished
   turn_indicator.clear() 
   turn_indicator.hideturtle()
   if box1 == "1":
    box1_writer.clear()
   if box2 == "2":
    box2_writer.clear()
   if box3 == "3":
    box3_writer.clear()
   if box4 == "4":
    box4_writer.clear()
   if box5 == "5":
    box5_writer.clear()
   if box6 == "6":
    box6_writer.clear()
   if  box7 == "7":
    box7_writer.clear()
   if box8 == "8":
    box8_writer.clear()
   if box9 == "9":
    box9_writer.clear()
   result_writer.goto(-185, 130)
   #Checks which player won in order to write result in the corresponding color
   if (index % 2 == 0): 
    result_writer.pencolor(x_color)
   else:
    result_writer.pencolor(o_color) 
   result_writer.write("Player " + winner + " wins!", font=("Arial", 30, "normal"))

#Stops game and writes that game is tied
def game_tied():
   #Clears the indicator after the game is finished
   turn_indicator.clear() 
   turn_indicator.hideturtle()
   result_writer.goto(-207, 130)
   result_writer.write("The game is tied!", font=("Arial", 30, "normal"))

#Function to check win
def check_win():
    global index
    #Checks if one player won the game by comparing if boxes are equal
    if (box1 == box2 and box1 == box3) or (box4 == box5 and box4 == box6) or (box7 == box8 and box7 == box9) or (box1 == box4 and box1 == box7) or (box2 == box5 and box2 == box8) or (box3 == box6 and box3 == box9) or (box1 == box5 and box1 == box9) or (box3 == box5 and box3 == box7):
        game_won(turns[index])
    #If game is not won yet, checks if all boxes are filled up to indicate that the game is tied
    elif (box1 != "1" and box2 != "2" and box3 != "3" and box4 != "4" and box5 != "5" and box6 != "6" and box7 != "7" and box8 != "8" and box9 != "9"):
        game_tied()
    #Continues the game
    else:
        if (index % 2 == 0):    
            turn_indicator.goto(150, oturn_ypos)
        else:
            turn_indicator.goto(150, xturn_ypos)
    index += 1

#For each of the functions below that are for pressing a number: 
#Once that number is pressed, the specific box writer for that box clears the number, 
#then writes the letter of the player in a larger size and in the corresponding color
#The variable for each box is then also changed to the letter of the player, in order to later check when the game is finished

#Changes box 1 to letter of player
def press1():
    global box1
    global index
    while box1 == "1":
        box1_writer.clear()
        if (index % 2 == 0):
            box1_writer.pencolor(x_color)
        else:
            box1_writer.pencolor(o_color)
        box1_writer.write(turns[index], font=("Arial", 40, "normal"))
        box1 = turns[index]
        check_win()

#Changes box 2 to letter of player
def press2():
    global box2
    global index
    while box2 == "2":
        box2_writer.clear()
        if (index % 2 == 0):
            box2_writer.pencolor(x_color)
        else:
            box2_writer.pencolor(o_color)
        box2_writer.write(turns[index], font=("Arial", 40, "normal"))
        box2 = turns[index]
        check_win()

#Changes box 3 to letter of player
def press3():
    global box3
    global index
    while box3 == "3":
        box3_writer.clear()
        if (index % 2 == 0):
            box3_writer.pencolor(x_color)
        else:
            box3_writer.pencolor(o_color)
        box3_writer.write(turns[index], font=("Arial", 40, "normal"))
        box3 = turns[index]
        check_win()

#Changes box 4 to letter of player
def press4():
    global box4
    global index
    while box4 == "4":
        box4_writer.clear()
        if (index % 2 == 0):
            box4_writer.pencolor(x_color)
        else:
            box4_writer.pencolor(o_color)
        box4_writer.write(turns[index], font=("Arial", 40, "normal"))
        box4 = turns[index]
        check_win()

#Changes box 5 to letter of player
def press5():
    global box5
    global index
    while box5 == "5":
        box5_writer.clear()
        if (index % 2 == 0):
            box5_writer.pencolor(x_color)
        else:
            box5_writer.pencolor(o_color)
        box5_writer.write(turns[index], font=("Arial", 40, "normal"))
        box5 = turns[index]
        check_win()

#Changes box 6 to letter of player
def press6():
    global box6
    global index
    while box6 == "6":
        box6_writer.clear()
        if (index % 2 == 0):
            box6_writer.pencolor(x_color)
        else:
            box6_writer.pencolor(o_color)
        box6_writer.write(turns[index], font=("Arial", 40, "normal"))
        box6 = turns[index]
        check_win()

#Changes box 7 to letter of player
def press7():
    global box7
    global index
    while box7 == "7":
        box7_writer.clear()
        if (index % 2 == 0):
            box7_writer.pencolor(x_color)
        else:
            box7_writer.pencolor(o_color)
        box7_writer.write(turns[index], font=("Arial", 40, "normal"))
        box7 = turns[index]
        check_win()

#Changes box 8 to letter of player
def press8():
    global box8
    global index
    while box8 == "8":
        box8_writer.clear()
        if (index % 2 == 0):
            box8_writer.pencolor(x_color)
        else:
            box8_writer.pencolor(o_color)
        box8_writer.write(turns[index], font=("Arial", 40, "normal"))
        box8 = turns[index]
        check_win()

#Changes box 9 to letter of player
def press9():
    global box9
    global index
    while box9 == "9":
        box9_writer.clear()
        if (index % 2 == 0):
            box9_writer.pencolor(x_color)
        else:
            box9_writer.pencolor(o_color)
        box9_writer.write(turns[index], font=("Arial", 40, "normal"))
        box9 = turns[index]
        check_win()


wn = trtl.Screen()
#The background color of the game is set
wn.bgcolor("grey")

#For each number pressed, run the function that corresponds with that number 
wn.onkeypress(press1, 1)
wn.onkeypress(press2, 2)
wn.onkeypress(press3, 3)
wn.onkeypress(press4, 4)
wn.onkeypress(press5, 5)
wn.onkeypress(press6, 6)
wn.onkeypress(press7, 7)
wn.onkeypress(press8, 8)
wn.onkeypress(press9, 9)

#Listen for the keys if pressed
wn.listen()

#Mainloop
wn.mainloop()
