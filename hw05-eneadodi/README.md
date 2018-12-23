[![Build Status](https://travis-ci.com/chapman-phys220-2018f/CHANGEME.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/CHANGEME)

# PHYS220/MATH220/CPSC220 HW 5

**Author:** **CHANGEME**

## Specification

1. Complete the classwork, in collaboration with your group (using Slack as needed).
1. In this homework, you will **refactor** your HW 4 to use classes. Be sure you have completed HW 4 correctly before continuing.
1. Recall that in HW 4 you addressed the following general problem for several specific cases:
        - Compute an "infinite" sum like: $$\sum_{k=1}^\infty f_k \equiv \lim_{N\to\infty} \sum_{k=1}^N f_k$$
        - *Note:* It is impossible to actually add an infinite number of terms in practice. Instead, we must rely on the fact that the sum is *convergent* to compute an approximate value. That is, the terms that contribute to the sum should steadily get smaller as $k$ increases, so $f_k > f_{k+1}$. To guarantee convergence, the ratio of successive terms must limit to a value smaller than 1: $\lim_{k \to infty} |f_{k+1} / f_{k}| < 1$. 
        - To exploit this fact about a convergent summation, we specify a *tolerance* (small value) such that when the next term of the sum $f_{k+1}$ is below this tolerance, we truncate the sum and treat the uncomputed remainder $\sum_{j=k+1}^\infty f_k$ as a negligible remainder (error). To be more precise, the tolerance is a positive number $t$ such that if $|f_{k+1} / [\sum_{j = 1}^{k} f_j]| < t$ then the summation may be truncated at the index $k$. This ensures that the relative value of the next term $f_{k+1}$ compared to the partial summation through $k$ is sufficiently small to neglect.
1. In a module ```convergent_sums.py``` create a new class ```ConvergentSum``` that specifies an infinite sum $ \sum_{k=1}^\infty f_k$. This class should have an attribute ```.term``` that will store a function that specifies each $k$-dependent term $f_k$ of the sum. This class should have an attribute ```.tolerance``` that stores the tolerance to which the sum will be evaluated. This class should have an attribute ```.value``` that stores either ```None``` or the computed value of the sum to the specified tolerance. The sum should have a method ```.evaluate(self)``` that computes the value of the sum up to the specified tolerance and stores it in the attribute ```.value```. Finally, the class should use the magic method ```.__call__(self)``` to either return the stored computed value, or execute ```.evaluate()``` before returning the computed value. In the constructor for your class, ```.__init__(self, f)``` specify the function ```f(k)``` for the $k$-dependent term $f_k$.
1. Create a Jupyter notebook ```Convergent_Sums.ipynb```. Import your python module and demonstrate that you can create instances of this class for each of the sums considered in HW 4. Show that each of those sums evaluate to the same results shown before in HW 4. Be sure to comment clearly about the value of this alternative approach to computing the sums.

**Notebook:** To cleanly present your work, your Jupyter notebook should imports your python module and demonstrate its key functionality by calling the appropriate functions in separate cells within the notebook. The notebook should be formatted professionally using Markdown headings, including your name and a brief description of each result within structured sections. Check that exporting the notebook to html produces nice results that you would feel happy sharing with a colleague. We will be trading work with other team mates next week.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
