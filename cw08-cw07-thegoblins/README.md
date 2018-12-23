[![Build Status](https://travis-ci.com/chapman-phys220-2018f/cw08-cw07-thegoblins.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/cw08-cw07-thegoblins)

# PHYS220/MATH220/CPSC220 CW 8

**Author(s):** **CHANGEME**

## Specification

1. Recall the [Numpy/Pandas Slides](http://slides.com/profdressel/numpy-and-pandas-overview/) that introduce the `numpy` and `pandas` libraries and how to use them.
1. With your partner, go through and complete the notebook `plotting-examples.ipynb`. This notebook will demonstrate the implementation of useful functions, and how to plot them using `matplotlib`, `pandas`, and `seaborn`.
1. Implement the following problem using `numpy` arrays in the module ```sinesum.py```:

  **Approximating a function by a sum of sines**

  *Idea:* Any function can be approximated arbitrarily well by a sum of sines. (This is known as a Fourier series expansion of the original function.) Consider the following piecewise function defined in the interval $t\in[-T/2,T/2]$:
  $$f(t) = \begin{cases}
             1, & 0 < t < T/2 \\
             0, & t = 0 \\
             -1, & -T/2 < t < 0
           \end{cases}$$
  It can be shown that the following sum converges to $f(t)$ as $n\to\infty$:
  $$S_n(t) = \frac{4}{\pi}\sum_{k=1}^n \frac{1}{2k-1} \sin\left(\frac{2(2k-1)\pi t}{T}\right)$$
  We wish to show numerical evidence for this convergence.

  (a) Create a function `s(t,n)` that computes the sum $S_n(t)$ defined above.

  (b) Create a function `f(t)` that computes the function $f(t)$ defined above.
  
  (c) Write two test functions in `test_sinesum.py` that verify your implementations. Make sure they pass in Travis.
  
  (d) In a well-formatted notebook `sinesum_plots.ipynb`, import your code, discuss the approximation being made, write out the supporting equations as $\LaTeX$ in the notebook, and plot the approximations for different numbers of terms using `matplotlib`. Take special care to make the plots pretty and clear, and explain what they show in text. For specificity, compute and show plots for the cases $n = 1, 3, 5, 10, 30, 100$ and $t = \alpha T$, with $T = 2\pi$ and $\alpha = 0.01, 0.25, 0.49$. Use the computed plots to comment on how the quality of the approximation of $f$ by $S_n$ depends on $\alpha$ and $n$.
  - As a challenge exercise for homework (not graded) try implementing a few of the more interesting exercises from the following `matplotlib` tutorial for practice : https://www.labri.fr/perso/nrougier/teaching/matplotlib/

Pro-tip: using git to manage conflicts on Jupyter notebooks is a pain. I recommend delegating one person from your group to edit the notebook, to avoid merge conflicts.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have. You can use the GitHub web interface to edit this file directly for now.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAMES**



