import turtle
from time import sleep


def draw_table(players, bids, scores):
    """
    Draw a table of players using the turtle module.
    """
    turtle.clearscreen()
    screen = turtle.Screen()
    screen.setup(width=1000, height=600)
    screen.title("Player Table")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    

    cell_width = 200
    cell_height = 50
    start_x = -400
    start_y = 250

    def draw_cell(x, y, width, height, text):
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(0)
        for _ in range(2):
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)
        pen.penup()
        pen.goto(x + width / 2, y - height / 2)
        pen.write(text, align="center", font=("Arial", 12, "normal"))

    headers = ["names", "words", "scores"]
    for i, header in enumerate(headers):   
        draw_cell(start_x + i * cell_width, start_y, cell_width, cell_height, header)

    for i, player in enumerate(players):  
        draw_cell(start_x, start_y - (i + 1) * cell_height, cell_width, cell_height, player)
    
    for i, bid in enumerate(bids):
        draw_cell(start_x + cell_width, start_y - (i + 1) * cell_height, cell_width, cell_height, bid)

    for i, score in enumerate(scores):
        draw_cell(start_x + cell_width * 2, start_y - (i + 1) * cell_height, cell_width, cell_height, score)
        
    sleep(5)