import turtle, random
from turtle import Turtle, Screen

def forward(player):
    inc = random.randint(0,15)
    player.fd(inc)



screen = Screen()
screen.setup(width=500, height=400)
user_bet=turtle.textinput(title="make your bet", prompt="which turtle will win the race")
print(user_bet)

colors = ["red", "orange", "yellow", "blue", "purple", "wheat"]


player=[]
for count in range(0,6):
    plyr = Turtle(shape = "turtle")
    plyr.color(colors[count])
    plyr.penup()
    plyr.color(colors[count])
    plyr.goto(x=-230, y=((count*50)-100))
    player.append(plyr)

max=0
winner = ""
while max <200:
    for plyr1 in player:
        forward(plyr1)
    for plyr2 in player:
        if max < plyr2.xcor():
            max=plyr2.xcor()
            winner=plyr2.pencolor()

print(f"The winner is {winner}")
if user_bet == winner:
    print("you win!")
else:
    print("you lose!")
print(f"Your choice was {user_bet}")
screen.exitonclick()