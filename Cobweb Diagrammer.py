"""
Written by Colby Simpson
A cobweb diagram maker for investigating the behaviour of the logistic map
"""


import Tkinter as tk
import turtle


def logistic_map(r, x_range):

    """
    :param r: The growth rate parameter of the logistic map
    :param x_range: For the logistic map, this will be an ordered list of numbers in [0,1] acting as interpolation points
    :return: An ordered list of numbers representing the values of the logistic map at the interpolation points
    """
    if isinstance(x_range, list):
       y_range = [r*x*(1-x) for x in x_range]
    elif isinstance(x_range, float):
        y_range = r*x_range*(1-x_range)
    else:
        y_range = 'Uh oh'
    return y_range


def linspace(lower, upper, num_steps):
    """
    :param lower: The lower bound of the interval
    :param upper: The upper bound of the interval
    :param num_steps: The number of steps to take across the inteval
    :return: A list of (steps) evenly spaced points between the values of (lower) and (upper)
    """
    step_size = (upper-lower) * 1.0 / num_steps
    return [lower + i*step_size for i in range(num_steps)]


def cobweb(turt, r, num_it, initial_value):
    # Clear the screen
    turt.clear()
    turt.speed(0)
    # Draw the line y = x in blue
    turt.penup()
    turt.goto(0,0)
    turt.color('blue')
    turt.pendown()
    turt.goto(1, 1)

    # Draw the logistic map
    turt.penup()
    turt.goto(0,0)
    turt.pendown()
    turt.color('purple')

    # Draw the polynomial map, for the time being, the logistic map
    turtle_x_range = linspace(0, 1, 100)
    turtle_y_range = logistic_map(r, turtle_x_range)

    for i in range( len( turtle_x_range ) ):
        turt.goto( turtle_x_range[i], turtle_y_range[i] )

    # Begin iteration of the map from our seed value
    turt.penup()
    x_current = initial_value
    turt.goto(x_current, 0)
    turt.color('red')
    turt.pendown()
    # i think it would be cool to see the cobweb being drawn
    turt.speed(5)

    for i in range(num_it):
        x_new = logistic_map( r, x_current )
        turt.goto( x_current, x_new )
        turt.goto( x_new, x_new )
        x_current = x_new

root = tk.Tk()  # Defines the main application window
root.title('Cobweb Plotter')  # Puts a title along the top bar of the window

r = tk.DoubleVar()
num_it = tk.IntVar()
initial_value = tk.DoubleVar()

# Entry boxes for the r and num_it parameters
growth_entry = tk.Entry(root, textvariable = r, bd = 5)
growth_entry.grid(row=0, column=1)
iter_entry = tk.Entry(root, textvariable = num_it, bd = 5)
iter_entry.grid(row=0, column=3)
init_entry = tk.Entry(root, textvariable = initial_value, bd = 5)
init_entry.grid(row=0, column=5)

# Labels for entry boxes
growth_label = tk.Label(root, text = 'Growth Parameter')
growth_label.grid(row=0, column=0)
iter_label = tk.Label(root, text = 'Number of Iterations')
iter_label.grid(row = 0, column=2)
init_label = tk.Label(root, text = 'Initial Value')
init_label.grid(row=0, column=4)

# Where the magic happens
woodland = tk.Canvas(width = 860, height = 860, bg = 'white')
woodland.grid(row=1, columnspan = 7)

franklin = turtle.RawTurtle(woodland)
screen = franklin.getscreen()
screen.setworldcoordinates(0,0,1,1)

# Releases the spiders
b = tk.Button(root, text = "Let's Go", command = lambda: cobweb(franklin, r.get(), num_it.get(), initial_value.get()))
# The lambda: makes it so the cobweb function is only evaluated once the button is pressed
b.grid(row=0, column=7)

root.mainloop()
