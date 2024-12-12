
from scipy.stats import beta
from scipy.stats import arcsine
import matplotlib.pyplot as plt
import numpy as np
  
x = np.linspace(0, 1.0, 200)
  
# Varying positional arguments
y1 = beta.pdf(x, 4, 8)
y2 = beta.pdf(x, 5, 6)
y3 = beta.pdf(x, 6, 5)
plt.xlabel('x')
plt.ylabel('p(x)')

plt.plot(x, y1, '*', label='Daring', c='red')
plt.plot(x, y2, '*', label='Default',c = 'green')
plt.plot (x, y3, '*', label='Slow', c='blue')
plt.legend(loc="upper left")
plt.show()