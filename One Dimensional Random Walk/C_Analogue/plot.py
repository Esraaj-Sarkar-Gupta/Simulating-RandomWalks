print("> Plotting results from file results.txt")
import matplotlib.pyplot as plt
import os as os


with open('results.txt' , 'r') as result_file: # Obtain result.txt data
    text = result_file.read()

selections = text.split(':') # Split the text into time stamps and their respective coordinates
selections.remove('')
time_instances = []
positions =  []
if 2%len(selections) != 0:
    print("> [Error]: Severe error - results.txt is erronious") 
for _ in range(int(len(selections) / 2)):
    #positions.append([])
    pass

for i in range(int(len(selections))): # Sort coordinates and time stamps into respective lists
    if i == 0 or i%2 == 0:
        time_instances.append(selections[i])
    elif i%2 == 1:
        positions.append(selections[i])  
    else:
        print("> Fatal Error") # How is this supposed to be possible anyway?
        pass

print("> result.txt data sorted")

try:
    os.makedirs('Frames')
    print("> Result frames directory made")
except:
    print("> Result frames directory already exists")
        
for t in range(len(time_instances)):
    time = time_instances[t]
    coordinatesY = positions[t]
    Y_str = coordinatesY.split(',')
    Y = [int(e) for e in Y_str if e]
    
    X = [n for n in range(len(Y))]

    plt.figure()
    plt.grid(True)
    #plt.plot(X, [0 for _ in range(len(X))])
    plt.title(f"Time instance {t}")
    plt.scatter(X , Y , color = 'green')

    plt.savefig(f'Frames/frame_{t}')
    plt.show()
    

     

