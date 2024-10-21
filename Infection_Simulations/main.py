import numpy as np
import time as tm
import os as os
import matplotlib as mpl
import matplotlib.pyplot as plt


try:
    os.makedirs('./Logs')
except:
    pass

T = tm.localtime()
filename = f"Logs/Logs_{T[7]}_{T[3]}-{T[4]}-{T[5]}.txt" # Set log file name

def log_display(text):
    with open(filename , 'a') as log_file:
        log_file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}\n")
    print(f"{T[3]}:{T[4]}:{T[5]} > {text}")
def log(text):
    with open(filename , 'a') as log_file:
        log_file.write(f"\n{T[7]} - {T[3]}:{T[4]}:{T[5]} > {text}\n")
        
# Random walk paramters

number_of_steps = int(input("Number of steps: "))
input_vector = input("Number of safe / number of infected (n , m): ")
safe = int(input_vector.split(',')[0])
infected = int(input_vector.split(',')[1])

total_elements = safe + infected
object_radius = 0.5

# Random walk elements

class Element():
    def __init__(self, X, Y, status):
        self.X = X
        self.Y = Y
        self.infected = status

elements = []

for i in range(safe):
    X, Y = np.random.randint(-100, 100) , np.random.randint(-100, 100)
    elements.append(Element(X, Y, False)) # 0 denotes non-infected element

for i in range(infected):
    X, Y = np.random.randint(-100, 100) , np.random.randint(-100, 100)
    elements.append(Element(X, Y, True)) # 1 denotes infected element
    
def plot(element_list, instance):
    plt.figure(figsize = (10, 10))
    plt.title(f"System at instant {instance}")
    
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    
    plt.xlabel("X")
    plt.ylabel("Y")
    
    for obj in element_list:
        x = obj.X
        y = obj.Y
        
        infected = obj.infected
        
        if infected:
            color = 'red'
        else:
            color = 'blue'
        
        plt.scatter(x, y, color = color)
    plt.show()
  
def update(element_list):
    for obj in element_list:
        theta = np.random.uniform(0, 2 * np.pi)
        r = 1
        
        obj.X = obj.X + np.cos(r * theta)
        obj.Y = obj.Y + np.sin(r * theta)

def collision(element_list):
    collisions = 0
    
    for obj_primary in element_list:
        for obj_secondary in element_list:
            if obj_primary == obj_secondary:
                continue
            
            delta_x = obj_primary.X - obj_secondary.X
            delta_y = obj_primary.Y - obj_secondary.Y
            
            delta_d = np.sqrt((obj_primary.X - obj_secondary.X)**2 + (obj_primary.Y - obj_secondary.Y)**2)
            
            collision_radius = 2 * object_radius
            
            if delta_d <= collision_radius:
                log_display(f"Collision between {obj_primary} and {obj_secondary} because {delta_x} x and {delta_y} y")
                collisions += 1
                if obj_primary.infected:
                    obj_secondary.infected = True
                elif obj_secondary.infected:
                    obj_primary.infected = True
                else:
                    pass # Neither element was infected
                    
    return collisions            
        
# Main instance loop    
for t in range(number_of_steps):
    plot(elements, t)
    
    collisions = collision(elements)
    log_display(f"There were {collisions} non-unique collisions resgistered at instance {t}.")
     
    update(elements)
            
        
        
    

        
    
    
    