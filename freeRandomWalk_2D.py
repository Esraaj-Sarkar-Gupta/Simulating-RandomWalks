print("> Simulating a free random walk in a 2D plane")
import numpy as np
import time as t
import matplotlib.pyplot as plt

x = 0
y = 0
X = [0]
Y = [0] # initial positions

n = 1000 # number of moves

def walk(i , x , y , a): # a is the amplitude of the step, generally unity
    theta = 2*(np.pi) * np.random.rand() 
    x = x + a*np.sin(theta)
    y = y + a*np.cos(theta) # generate a random angle and advance by an amplitude 'a' 
    
    X.append(x)
    Y.append(y) # appending coordinates to list of coordinates
    
    return x , y

print("> Imports completed, functions and variables defined.")

s_time = t.time()

for i in range(1 , n+1):
    x , y = walk(i , x , y , 1)
    # print(f"- Position {i}: (" ,  x  , ' , ' ,  y , ')') # print position [logging]
    
e_time = t.time()   
print(f"> Random walk simulation completed for 1 point(s) for {n} moves in time = {e_time - s_time:.5f}")

plt.figure(figsize = (50,50))
plt.scatter(X , Y , s = 30) # plotting plot lines
plt.plot(X , Y , linewidth = 0.4 , color = 'purple') # plotting plot lines
plt.scatter(0 , 0 , color = 'red')
plt.xlabel = 'X Space'
plt.ylabel = 'Y Space'
plt.title(f"Path traveled by partical after {n} moves")
print("> Plotted scatter points")
print("> End")



    
    

