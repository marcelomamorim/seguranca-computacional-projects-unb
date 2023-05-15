# I'm going to plot a nice graph
from utils import *
import matplotlib.pyplot as plt
import numpy as np

# grab the cyphertext
file = "./app/parte_2/txts/ritaLee_ptbr.txt"
filetimetable = open(file,"r")
lines=filetimetable.readlines()
filetimetable.close()

# let's make it all one string
working=""
for line in lines:
    for char in line:
        asc=ord(char)
        if (64 < asc < 91) or ( 96 < asc < 123): # only letters; no spaces, punctuation, numbers etc
            char=char.upper() # make it all upper case
            working+=char # add it to the string
print("workinkg:\n\n", working)

# shift  the cyphertext against itself.
# count up number of matches between
# cyphertext and shifted cyphertext
offsets=[]
data=[]

# this is for labelling the peaks
threshold=0

# let's only do a small number of shifts, more text, longer keys tested.
# you might want to fiddle with the top value in the range
for offset in range(1,int(len(working)/50)):
    matches=0
    for j in range(len(working)-offset):
        if working[j]==working[j+offset]:
            matches+=1
    threshold+=matches
    data.append(matches)
    offsets.append(offset)
    
# this sets a threshold above which a point is labelled
print(f'threshold: {threshold}')
print(f'offset: {offset}')
threshold=int(1.2*threshold/offset)

# lets prep the data for plotting
x=np.array(offsets)
y=np.array(data)
plt.plot(x,y)

# let's label any high points
for i in range(len(offsets)):
    if data[i]>threshold:
        plt.text(offsets[i],data[i],str(i+1))
        
# How frequent are x-axis gridlines?
stepsize=int(offset/10)
plt.xticks(np.arange(0, offset, step=stepsize))
# label axes and title
plt.xlabel('Offsets')
plt.ylabel('Matches')
plt.title(f'{file}\nLook for peaks that are multiples of some key length')
plt.grid(visible=None, which='major', color='#666666', linestyle='-')
# show the graph
plt.show()