print("> Simulating random walks for multiple independent variables in one dimension.")
import numpy as np
import matplotlib.pyplot as plt
import time as t
print("> Completed imports")
NOE = 1000 #number of elements to be simulated
NOI = 100000 #number of iterations (moves)
print(f"> Number of independent elements: {NOE}")
print(f"> NUmber of iterations: {NOI}")
#X Axis: Element
#Y Axis: Position
ElementsX =[]
for num in range(1,NOE - 1):
    ElementsX.append(num)
Pos = []
for _ in ElementsX:
    Pos.append(0)
print("> Defined elements")    
plt.scatter(ElementsX , Pos) #plotting initial positions
plt.xlabel("Element")
plt.ylabel("Position")
plt.title("Elements at starting position.")
plt.grid()

def walk(i):
    for element in ElementsX:
        move = np.random.randint(1,3);
        if move == 1:
            Pos[element-1] = Pos[element-1] - 1
        elif move == 2:
            Pos[element-1] = Pos[element-1] + 1
        #end function 
 
s_time = t.time()
for i in range(0,NOI):
    walk(i)
    if i%100 == 0:
        print(f"- On iteration number {i}")
e_time = t.time()
print(f"> Finished computing {NOI} random walks for {NOE} independent elements in time = {e_time - s_time:.3f} seconds.")
    
plt.scatter(ElementsX , Pos , color='green') #plotting results of randomwalk
plt.xlabel("Element")
plt.ylabel("Position")
plt.title(f"Elements after iteration {i+1}.")
plt.grid() 
print('> Scatter plotted')

nbins = int(NOE/10)   
plt.figure()
plt.hist(Pos, nbins, color='red')
plt.title(f"Distribution for {NOE} independent elements with {nbins} bins.")
print("> Histogram plotted")

sum = 0
for m in Pos:
    sum = sum + m
print(f"> Mean position = {sum/NOE}.")
print('> End')
