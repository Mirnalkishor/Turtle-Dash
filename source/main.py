import random
import turtle
import time

WIDTH, HEIGHT = 700, 700
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'pink', 'purple', 'cyan', 'brown']

def get_number_of_racers():
    while True:
        racers = input("Enter number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Please input within the range (2-10)")
            continue

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(turtles):
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return turtles.index(racer)

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game!")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

turtles = create_turtles(colors)
winner_index = race(turtles)
winner_color = colors[winner_index]

print(f"The winner is the turtle with color {winner_color}!")


time.sleep(5)
