# Cobweb_Diagrammer
A simple cobweb diagram generator for the logistic map

A cobweb diagram is a simple way of visualising the qualitative behaviour of a 1 dimensional map. This app focuses on the logistic map,
a discrete way of modeling the growth of a population. This map is notable in that though it is simple mathematically it has some interesting
behaviour: as the growth parameter r is varied from 3 to 3.555  the map experiences a period doubling cascade (meaning it goes from holding stable at one value,
to oscillating between 2, 4, 8...) as r is increased passed 3.56 the map displays chaotic behaviour with occasional periodic windows.

INPUTS
The logistic map has the form x_{n+1} = r*x_n*(1-x_n)

Growth Parameter: Specifies the value of r used for the iteration. A double bewteen 0 and 4.

Number of Iterations: Specifies how long we want to simulate the cobweb plot for. For small values of r convergence will be quick and obvious,
but for values of r between 3 and 4 it is nice to view the system over a longer period of time. Takes an integer value

Initial Value: Specifies the value of x_0. Takes a double value between 0 and 1



