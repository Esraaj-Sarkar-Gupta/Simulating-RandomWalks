The python files used in the project have been rewritten in C to allow faster, more efficient compuation. The C script writes its data into a file results.txt.

results.txt is then read by plot.py which interprets the data and plots the system for each time instance (a feature unavailable in the original python scripts). plot.py stores its plots in the directory Frames. 

videomaker.py reads ./Frames to make a .mp4 video of the system changing through time. 