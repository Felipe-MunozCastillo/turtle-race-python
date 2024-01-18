"""Importacion de modulos"""
from turtle import Turtle, Screen
import random


def define_colors(bet):
    """Funcion para asignar el color de la tortuga.
    Se ingresa un string con el nombre del color"""
    if bet == 'roja' or bet == 'rojo':
        bet = "red"
        return bet
    elif bet == "amarilla" or bet == "amarillo":
        bet = "yellow"
        return bet
    elif bet == "naranja" or bet == "naranjo":
        bet = "orange"
        return bet
    elif bet == "verde":
        bet = "green"
        return bet
    elif bet == "azul":
        bet = "blue"
        return bet
    elif bet == "purpura":
        bet = "purple"
        return bet
    else:
        return False


def create_turtles(bet, turtle_colors):
    """Funcion para la creacion de la tortuga escogida por el usuario y competidoras."""
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(user_bet)
    tim.goto(x=-230, y=-100)
    all_turtles.append(tim)

    turtle_colors.remove(bet)

    for iteration in range(len(turtle_colors)):
        create_a_turtle(-230, -100, iteration, colors[iteration])


def create_a_turtle(position_x, position_y, iteration, color):
    """Funcion para posicionar a las tortugas en la pantalla."""
    racer = Turtle(shape="turtle")
    racer.color(color)
    racer.penup()
    racer.goto(position_x, position_y + (iteration + 1) * 50)
    all_turtles.append(racer)


def reverse_colors(bet):
    """Funcion para traducir el color de la tortuga."""
    if bet == 'red':
        bet = "roja"
        return bet
    elif bet == "yellow":
        bet = "amarilla"
        return bet
    elif bet == "orange":
        bet = "naranja"
        return bet
    elif bet == "green":
        bet = "verde"
        return bet
    elif bet == "blue":
        bet = "azul"
        return bet
    elif bet == "purple":
        bet = "purpura"
        return bet
    else:
        return False


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = False
user_bet = screen.textinput(
    title="Has tu apuesta", prompt="¿Que tortuga ganará la carrera? Ingresa un color: ").lower()
user_bet = define_colors(user_bet)

while not user_bet:
    user_bet = screen.textinput(title="Has tu apuesta",
                                prompt="Lo siento, no tenemos de ese color. Escoge otro: ").lower()
    user_bet = define_colors(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

create_turtles(user_bet, colors)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                winning_color = reverse_colors(winning_color)
                print(f"¡Ganaste! La tortuga {winning_color} es la ganadora.")
            else:
                winning_color = reverse_colors(winning_color)
                print(f"¡Perdiste! La tortuga {winning_color} es la ganadora.")
                break
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()
