print("Observing the frequency of collisions in a random walk as elements diffuse over time.")
import matplotlib.pyplot as plt
print("> Required libraries imported")
print("> Remove collisions at instance 1: TRUE")
msg = ''
IN = input("[INPUT] Remove all collisions at instance '1' to prevent  massive scales in the plot? Y/N: ").lower()
if IN == 'y':
    rem1 = True
    print('> All collisions at instance 1 will be ignored')
elif IN == 'n':
    rem1 = False
    print("> All collisions will be considered for plotting")
else:
    print("> Response not recognised. Resorting to default setting...")
    print('> All collisions at instance 1 will be ignored')
    rem1 = True
# remove all collisions at instance 1
# >90% of collisions occur at time 1, which makes the rest of the histogram unreadable due to the skewed scale

with open('logs.txt' , 'r') as file: # pull logs file
    logstxt = file.read()
log_lines = logstxt.split('\n') # splitting logs to individual lines
data = []
for str in log_lines:
    try:
        data.append(str.split(' ')[10]) # aquiring appropriate data from each line
    except:
        pass
if rem1 == True: # removing all instances of collision at 1
    data = [num for num in data if num != '1']
    print("[O] All instances of collisions at time instance 1 have been removed")
    msg = '[All collisions at instance 1 have been removed]'
print("> Data extracted from logs.txt file")
print(f"> Total data points: {len(data)}")  
plt.figure()
plt.hist(data , 50)
plt.xlabel("Time Instance of Collision")
plt.ylabel("Number of Collisions")
plt.title(f"Frequency of collisions in a random walk as elements diffuse over time.\n{msg}")
print("> Data plotted")
    