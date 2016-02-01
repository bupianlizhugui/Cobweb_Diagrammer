import turtle

#2Do
# 1) Set up a GUI to accept user inputs for the initial value of iteration, and the growth parameter
# 2) Add support for more than just the logistic map


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


if __name__ == '__main__':
    #master = Tk()
    #canvas_width = 960
    #canvas_height = 960
    #window = Canvas(master, width = canvas_width, height = canvas_height)
    #window.pack()
    #woodland = turtle.TurtleScreen(window)
    woodland = turtle.Screen()
    woodland.setworldcoordinates(0, 0, 1, 1)
    franklin = turtle.Turtle()
    # Forget tying your shoes Franklin, its time to go fast
    franklin.speed(0)


    # This will be the seed for the iteration of the cobweb plotter
    initial_val = 0.25
    r = 3.2



    # Draw x and y axes
    franklin.setx( woodland.window_width() )
    franklin.setx(0)
    franklin.sety( woodland.window_height() )

    # Draw the line y = x in blue
    franklin.penup()
    franklin.goto(0,0)
    franklin.color('blue')
    franklin.pendown()
    franklin.goto(1, 1)

    # Draw the logistic map
    franklin.penup()
    franklin.goto(0,0)
    franklin.pendown()
    franklin.color('purple')

    # Draw the polynomial map, for the time being, the logistic map
    turtle_x_range = linspace(0, 1, 100)
    turtle_y_range = logistic_map(r, turtle_x_range)

    for i in range( len( turtle_x_range ) ):
        franklin.goto( turtle_x_range[i], turtle_y_range[i] )

    # Begin iteration of the map from our seed value
    franklin.penup()
    x_current = initial_val
    franklin.goto(x_current, 0)
    franklin.color('red')
    franklin.pendown()
    # i think it would be cool to see the cobweb being drawn
    franklin.speed(5)

    for i in range(200):
        x_new = logistic_map( r, x_current )
        franklin.goto( x_current, x_new )
        franklin.goto( x_new, x_new )
        x_current = x_new


    # to keep the  window from closing immediately
    master.mainloop()

