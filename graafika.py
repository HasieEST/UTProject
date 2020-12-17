import turtle

background = turtle.Screen()
background.bgcolor("grey")
background.addshape("backk.gif")


card_1 = turtle.Turtle()
card_2 = turtle.Turtle()
card_3 = turtle.Turtle()
card_4 = turtle.Turtle()
card_5 = turtle.Turtle()
card_6 = turtle.Turtle()
card_7 = turtle.Turtle()
card_8 = turtle.Turtle()
card_9 = turtle.Turtle()
card_10 = turtle.Turtle()
card_11 = turtle.Turtle()
card_12 = turtle.Turtle()
card_13 = turtle.Turtle()
card_14 = turtle.Turtle()
card_15 = turtle.Turtle()


def mänguala(pliiats):         
    pliiats.pensize(5)
    pliiats.color("black")
    pliiats.goto(220,205)
    pliiats.begin_fill()
    pliiats.pendown()
    pliiats.goto(220,-205)
    pliiats.right(90)
    pliiats.circle(-15,90)
    pliiats.goto(-205,-220)
    pliiats.circle(-15,90)
    pliiats.goto(-220,205)
    pliiats.circle(-15,90)
    pliiats.goto(205,220)
    pliiats.circle(-15,90)
    pliiats.color("#432616")
    pliiats.end_fill()
    
    
    pliiats.color("black")
    pliiats.penup()
    pliiats.goto(205,200)
    pliiats.pensize(3)
    pliiats.begin_fill()
    pliiats.pendown()
    pliiats.goto(205,-200)
    pliiats.circle(-5,90)
    pliiats.goto(-200,-205)
    pliiats.circle(-5,90)
    pliiats.goto(-205,200)
    pliiats.circle(-5,90)
    pliiats.goto(200,205)
    pliiats.circle(-5,90)
    pliiats.color("darkgreen")
    pliiats.end_fill()
    pliiats.penup()
    pliiats.goto(0,0)
    
    pakk = turtle.Turtle()
    pakk.penup()
    pakk.setheading(90)
    pakk.shape("backk.gif")





cards_on_table = []
card_turtles = [card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,card_11,card_12,card_13,card_14,card_15]

def reset_turtles():
    global cards_on_table
    cards_on_table = []
    for turtle in card_turtles:
        turtle.hideturtle()
        turtle.penup()
        turtle.setheading(90)
        turtle.goto(0,0)

def create_card_image(hand, player):
    if player == "player":
        table_position = -1.25
    elif player == "player2":
        table_position = -0.5
    elif player == "dealer":
        table_position = 1
    for card in hand:
        if card in cards_on_table:
          continue
    else:
        background.addshape(card[2])
        card_turtles[(len(cards_on_table))].showturtle()
        card_turtles[(len(cards_on_table))].shape(card[2])
        card_turtles[(len(cards_on_table))].goto(-130+(65*(len(hand)-1)),(130*table_position))
        cards_on_table.append(card)
