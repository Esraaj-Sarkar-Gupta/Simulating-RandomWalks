print("Simulating 2D random walks for several particals.")
print("> Collisions: DETECT ONLY (Resolution = 1e-2)")

import numpy as np
import time as t
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
print("- Imported 4 libraries")

T = 1001 - 1 # number of moves
N = 100 # number of independent particals (entities)

Ex = [] # lists that will hold the list of coordinates of points for every instance of time
Why = []
print("- Defined arrays")
    

for j in range(1 , N + 1): # create the required list variables
    X_j = [0]
    Y_j = [0]
    Ex.append(X_j)  
    Why.append(Y_j)  # place the lists in a list 

def walk(n , tao , a): # a is the amplitude of the step, generally unity
    theta = np.random.rand() * 2*np.pi
    Ex[n - 1].append(Ex[n-1][tao - 1] + np.cos(theta))
    Why[n - 1].append(Why[n-1][tao - 1] + np.sin(theta))
 
print("- Defined random walk function")

res = 1e-2 # collision resolution (gives particals some area )
collide_count = 0 # variable to count the number of collisions
logs = [] # list to temporarily hold all the collision data 
logfile = f"LOGS_T={T}_N={N}_collisionRES={res}.txt"
def collision(x , y , tao , c):
    for i in range(len(x)): #for every element, we interate through each element in Ex and Why
        current_x = x[i][tao]
        current_y = y[i][tao]
        for j in range(i + 1, len(x)):
            #print('[Debug] Counter: ' , i , ":" ,  j , ' @ ' , tao)
            other_x = x[j][tao]
            other_y = y[j][tao] 
            if abs(current_x - other_x) < res and abs(current_y - other_y) < res:  # Adjust tolerance as needed 1e-4
                print(f"[!] Collision detected between particles {i + 1} and {j + 1} at instant {tao}")
                logs.append(f"[!] Collision detected between particles {i + 1} and {j + 1} at instant {tao} \n" ,)
                c += 1 # adding to the collision counter
    return c
print("- Defined collision function")
   
cmap = plt.cm.get_cmap("viridis") # import colourmap
scalar_field = [m for m in range(1 , T + 1)] # scalar field values that will be mapped to colours using the colourmap. For loops builds the scalar field 
norm = Normalize(vmin=min(scalar_field), vmax=max(scalar_field)) # normalise colourmap
print("- Defined mapping colour maps ") 

print("> Required functions defined and imports completed") # standard logs
print("> Total number of independent elements: {N}")
print("> Number of moves (iterations) to be carried out: {T}")
s_time = t.time() #  log real time required to run simulation
# where the magic happens: 
for tao in range(1 , T):  # tao 0 already exists with all elements at the origin
    if tao % 100 == 0: # resolution of loading bar
        print(f">On iteration {tao}/{T}") # loading bar
    for n in range(1 , N + 1):
        walk(n  , tao , 1) # compute walk for every time instance
    if tao > 1:
        collide_count = collision(Ex , Why , tao - 1 , collide_count) # watch for collisions at every time instance

e_time = t.time()

print(f"> Finished mapping fields  and computing collisions in {e_time - s_time:.5f} seconds. ({(e_time - s_time) / 3600:.4f} hours)")
print(f"> Collision resolution set to {res}")  
print(f"> Total number collisions detected is {collide_count}")     
 
plt.figure(figsize = (100 , 100)) # large figure to facilitate a greater resolution
plt.scatter(0 , 0 , color = 'red' , s = 40) # origin
plt.title(f"Random walk map for {N} independent elements at time {T} with {collide_count} total collisions at resolution {res}")
plt.xlabel("X Space")
plt.ylabel("Y Space")
for i in range(0  , len(Ex)):
    plt.plot(Ex[i] , Why[i] , linewidth =  2) # connecting lines for each partical
    plt.scatter(Ex[i] , Why[i] , c = scalar_field , cmap = cmap , norm = norm , s = 40) # mapped points for every partical 
plt.show()
print("> Finished plotting random walk map")
with open(logfile , 'w') as logfile:
    for msg in logs:
        logfile.write(msg)
print("> Printed collisions logs in logfile")
print("> End script")
         

         
    


