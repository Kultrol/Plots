import numpy as np 
import matplotlib.pyplot as plt 

lambda_parameter = 0.5 #Controls Width
a = 0 #Center Point

x = np.linspace(-10,10,1000)
y = np.sqrt(lambda_parameter / np.pi) * np.exp(-lambda_parameter * (x-a)**2)

plt.plot(x,y)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Gaussian')

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.show()



