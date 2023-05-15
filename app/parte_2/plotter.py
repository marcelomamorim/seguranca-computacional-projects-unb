#https://www.murky.org/blog/2020-8/vigkeylength

import matplotlib.pyplot as plt
import numpy as np

def plotter(offsets, data, threshold=100):

    offset=len(offsets)

    # this sets a threshold above which a point is labelled
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
    plt.title(f'Look for peaks that are multiples of some key length')
    plt.grid(visible=None, which='major', color='#666666', linestyle='-')
    # show the graph
    plt.show()

if __name__ == "__main__":
    print("This is a module, not a program. Please import it.")     
    # This is a module, not a program. Please import it.
    #test:
    plotter([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    
    
    