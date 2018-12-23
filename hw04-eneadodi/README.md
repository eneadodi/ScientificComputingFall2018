[![Build Status](https://travis-ci.com/chapman-phys220-2018f/CHANGEME.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/CHANGEME)

# PHYS220/MATH220/CPSC220 HW 4

**Author:** **Enea Dodi**

## Specification

1. Complete the classwork, in collaboration with your group (using Slack as needed). 
1. Create a python module ```convergent_sums.py```. In this module you will address the following general problem for several specific cases:
        - Compute an "infinite" sum like: $$\sum_{k=1}^\infty f_k \equiv \lim_{N\to\infty} \sum_{k=1}^N f_k$$
        - *Note:* It is impossible to actually add an infinite number of terms in practice. Instead, we must rely on the fact that the sum is *convergent* to compute an approximate value. That is, the terms that contribute to the sum should steadily get smaller as $k$ increases, so $f_k > f_{k+1}$. To guarantee convergence, the ratio of successive terms must limit to a value smaller than 1: $\lim_{k \to infty} |f_{k+1} / f_{k}| < 1$. 
        - To exploit this fact about a convergent summation, we specify a *tolerance* (small value) such that when the next term of the sum $f_{k+1}$ is below this tolerance, we truncate the sum and treat the uncomputed remainder $\sum_{j=k+1}^\infty f_k$ as a negligible remainder (error). To be more precise, the tolerance is a positive number $t$ such that if $|f_{k+1} / [\sum_{j = 1}^{k} f_j]| < t$ then the summation may be truncated at the index $k$. This ensures that the relative value of the next term $f_{k+1}$ compared to the partial summation through $k$ is sufficiently small to neglect.
1. Create a function `sum_1(tol=1e-5)` that returns the value of the following sum, up to the tolerance specified by the default keyword parameter `tol`. Stop the summation when the next term of the sum would be smaller than this tolerance. To what value does the summation converge for small tolerances? How many terms do you need before you get 5 digits of precision for the convergent result? $$4\sum_{k=1}^\infty \frac{(-1)^{k+1}}{2k - 1}$$
1. Create a function `sum_2(tol=1e-5)` that returns the value of the following sum, up to the tolerance specified by the default keyword parameter `tol`. Stop the summation when the next term of the sum would be smaller than this tolerance. To what value does the summation converge for small tolerances? How many terms do you need before you get 5 digits of precision for the convergent result? $$\frac{6}{\sqrt{3}}\sum_{k=1}^\infty \frac{(-1)^{k+1}}{3^k(2k + 1)}$$
1. Create a function `sum_3(tol=1e-5)` that returns the value of the following sum, up to the tolerance specified by the default keyword parameter `tol`. Stop the summation when the next term of the sum would be smaller than this tolerance. To what value does the summation converge for small tolerances? How many terms do you need before you get 5 digits of precision for the convergent result? $$4\sum_{k=1}^\infty \left[ \frac{4(-1)^{k+1}}{5^{2k+1}(2k + 1)} - \frac{(-1)^{k+1}}{239^{2k+1}(2k + 1)} \right]$$
1. Create a test module ```test_convergent_sums.py```. Using the test functions from previous classworks as a guide, write you own test functions for each of the three sum functions above. Make sure the test functions pass correctly with ```nosetests3```.  (Hint: Since the results of the sums are floating point numbers, you should not use the ```==``` test, but should instead use tests that are robust to numerical rounding errors. These include inequalities, or approximate equalities like the one described in https://www.python.org/dev/peps/pep-0485/ and implemented as of python 3.5 in the ```math``` module.)
1. Create a Jupyter notebook ```Convergent_Sums.ipynb```. Import your python module and present your results in a clear and readable way. Be sure to comment on your conclusions about what the sums must converge to and why.

**Notebook:** To cleanly present your work, your Jupyter notebook should imports your python module and demonstrate its key functionality by calling the appropriate functions in separate cells within the notebook. The notebook should be formatted professionally using Markdown headings, including your name and a brief description of each result within structured sections. Check that exporting the notebook to html produces nice results that you would feel happy sharing with a colleague. We will be trading work with other team mates next week.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**It was soooooooo hard for me to understand what you were asking for this assignment. I got help from Gwyneth Casey who demostrated her code for me and explained the structure on how she made it possible.**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Enea Dodi**
