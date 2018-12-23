# PHYS220/MATH220/CPSC220 HW 12

**Author:** **CHANGEME**

## Specification

1. Complete CW12 with your teammate(s) and copy its completed module ```sombrero.py``` into this homework.
   
1. For $F = 0.4$, create a high-resolution scatterplot of $(x(t),y(t))$ for the specific points $t = (\phi + n)2\pi$ for $\phi = 0$ and $n = 0,1,\ldots,1000$. Label your horizontal axis $x$ and your vertical axis $x'$. Plot your axes on a fixed scale $x\in[-1.5,1.5]$ and $y\in[-1.1,1.1]$.  Export the plot directly to a file ```frame00.png```. The following example code fragment may help to figure out how to export `png` files rather than display plots directly in a notebook.
  ```python
  import matplotlib
  matplotlib.use('Agg')              # This tells matplotlib to write to png files
  import matplotlib.pyplot as plt
    
  plt.plot(YOURPLOTCODEHERE)         # Use matplotlib as you would normally to create a figure
  plt.savefig('frame00.png')         # Save the figure to filename "frame00.png"
  ```
      
1. Create another scatterplot like the previous one, but using $\phi = 0.01$, saving the file in ```frame01.png```. Repeat this process of creating and exporting scatter plots to image files by incrementing $\phi$ by $0.01$ each time, until you reach $\phi = 0.99$ and ```frame99.png```.
         
1. Create an animated gif out of the previous 100 frames, using the ```convert``` commandline tool by running the command
  ```bash
  convert -delay 50 -loop 0 frame*.png poincare.gif
  ``` 
in a terminal, in the same directory as all the `png` images you created. This will combine all the frames into a gif named `poincare.gif`. You can also try to optimize the size of the gif with the command
  ```bash
  convert poincare.gif -fuzz 30% -layers Optimize poincare-optimized.gif
  ```
The `fuzz` option tries to ignore colors that are close, which avoids preserving unnecessary `png` compression artifacts.
            
Finally, to cleanly present your work, create a Jupyter notebook ```hw12-poincare.ipynb``` that loads your animated gif and explains what sort of motion you observe from the dynamics as time evolves.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
