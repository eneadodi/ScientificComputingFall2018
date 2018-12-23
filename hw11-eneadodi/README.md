
# PHYS220/MATH220/CPSC220 HW 11

**Author:** **CHANGEME**

## Specification

1. Complete the classwork, in collaboration with your group (using Slack as needed).

1. In this homework, we will explore the exciting new development in python of [```numba```](http://numba.pydata.org/), which is a just-in-time (JIT) compiler optimized for python's ```numpy``` library. In short, ```numba``` interprets python code and converts it into machine code using the low-level virtual machine (LLVM) before executing it. This means that code which is run repeatedly (such as vectorized code) will receive a dramatic speedup over raw python code since it is compiled. 

* Write a notebook ```juliasets.ipynb``` that includes the following bit of code.

```python
import numpy as np
#import numba as nb  #uncomment for numba
import matplotlib.pyplot as plt
%matplotlib inline

def julia(c):
    @np.vectorize  #comment for numba
    #@nb.vectorize #uncomment for numba
    def j(z):
        for n in range(100):
            z = z**2 + c
            if abs(z) > 2:
                return n
        return 0
    return j

j = julia(0.345 + 0.45j)

#@nb.jit  #uncomment for numba
def cplane(min=-1.5, max=1.5, points=10000):
    r = np.linspace(-1.5, 1.5, 10000)
    x, y = np.meshgrid(r,r)
    z = x + y * 1j
    return z

%time z = cplane()
%time jset = j(z)

plt.figure(1, (20,15))
plt.imshow(jset, cmap=plt.cm.bone)
plt.xticks([])
plt.yticks([])
plt.title("Julia Set : c = 0.345 + 0.45j")
plt.show()
```

As written, this will use ```numpy``` in a vectorized way as we have been using in class so far. Run the code and note how long the timed portions take. Then uncomment the ```@nb``` lines to enable ```numba```. Rerun the code and compare the results of the timings. (The ```@nb``` lines are called "decorators" and modify the subsequent function definitions to add functionality, in this case just-in-time compilation via ```numba```.) Discuss the difference in your notebook - did `numba` help speed up the code? Explain why.

1. Copy your CW11 into this repository and modify your implementations to use ```numba``` with the ```@nb.jit``` decorator. Are you able to speed up the run time of your integration methods? Comment on the gain in efficiency, and speculate why they may or may not be a speedup.

1. Check the syllabus for Supplementary links to YouTube videos about `numba`, if you have further interest in learning how it works. If you wish to learn more about Julia sets, like the one plotted above, see http://acko.net/blog/how-to-fold-a-julia-fractal/

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
