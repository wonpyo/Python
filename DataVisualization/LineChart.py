# A line chart can be created using the Matplotlib plot() function. 
# While we can just plot a line, we are not limited to that. 
# We can explicitly define the grid, the x and y axis scale and labels, title and display options.

from pylab import *

t = arange(0.0, 2.0, 0.01)
s = sin(2.5*pi*t)
plot(t, s)

xlabel('time (s)')
ylabel('voltage (mV)')
title('Sine Wave')
grid(True)
show()