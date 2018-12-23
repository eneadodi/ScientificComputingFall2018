
# PHYS220/MATH220/CPSC220 HW 10

**Author:** **CHANGEME**

## Specification

1. Complete the classwork, in collaboration with your group (using Slack as needed).
1. Go through the Sympy Tutorial Notebook in this repository carefully. Make sure you understand how things work.
1. Recall the Taylor expansion of a function $f$ a small displacement $y$ away from a point $a$: $$f(a + y) = \sum_{n=0}^\infty \frac{y^n}{n!}\left[\frac{d^n}{dy^n}f(a+y)\right]_{y=0}\\ = f(a) + f'(a)y + f''(a)\frac{y^2}{2} + \cdots$$ This formula states that an analytic function $f$ can be approximated by a polynomial series in the region around a domain point $a$, with the polynomial weights determined only by the derivatives of $f$ at the single point $a$. The purpose of this assignment is to show how this expansion really works in practice. By shifting the domain point to $x = a + y$, we can rewrite the formula as: $$f(x) = \sum_{n=0}^\infty \frac{(x-a)^n}{n!}\left[\frac{d^n}{dx^n}f(x)\right]_{x=a}\\ = f(a) + f'(a)(x-a) + f''(a)\frac{(x-a)^2}{2} + \cdots$$ This formulation makes it more clear that the function $f$ at any point $x$ in the domain may be approximated entirely by the function derivatives at a single point $a$ and the small displacements $(x-a)$ away from that point $a$.
1. In a notebook ```taylor.ipynb``` explain the above formula using ($\LaTeX$) equations and your own words.
1. In a separate module ```taylor_approx.py``` define a function ```derivatives(f, x, a, n)``` that does the following. The parameter `f` should be a `sympy` expression for the function you wish to approximate. The parameter `x` should be the `sympy` variable that composes the expression `f`. The parameter `a` should be a float that indicates the single point in the domain of `f` that you wish to "Taylor-expand around" later: you will compute the first `n` derivatives of `f` at this point `a`. The parameter `n` should be a positive integer that indicates how many derivatives to compute. Implement this function so it returns one `numpy` array `fderivs` of length `n+1` containing the numerical values (as floats) `[f(a), f'(a), f''(a), ...]` up to and including the `n`th derivative of `f` evaluated at `a`. (Hint: use `sympy` to compute these values easily) Then define a function ```taylor(xnum, a, dfs)``` that does the following: The parameter `xnum` should be a numpy array of points representing the domain of the function `f`. The parameter `a` should be the same float used in the `derivatives` function to represent the point that you are "Taylor-expanding around". The parameter `dfs` should be an array of derivatives of `f` at `a` exactly as output by the function ```derivatives``` that you just defined. The function `taylor` should return an array of points of the same length as `xnum` that represents the range of an approximation to `f` consisting of the sum of the first `n+1` terms of its Taylor expansion. This should use the above formula for the Taylor expansion, using vectorized multiplications to handle the arrays `xnum` for the domain points, and using the specific derivative values that you computed. (Hint: you will need to subtract constant arrays of replicated values `a`; these can be created easily using the `np.ones_like(xnum)` function.) Done properly, the output of `taylor` for large `n` should closely approximate the output of the exact function using `sp.lambdify(x, f)(xnum)`.
1. Write test functions in a test module ```test_taylor_approx.py``` that verify your implementation is correct.
1. In your notebook, import `taylor_approx.py` and demonstrate how the Taylor expansion really works by plotting it. That is, define a domain array `xnum` of $1000$ points between $[-5,5]$. Define range arrays using `taylor` for the following interesting functions: (1) $f(x) = \sin(x)$, (2) $f(x) = \tanh(x)$, and (3) $f(x) = x^2/10 + \sin(2x)/2$. For each of these functions, plot the function and the Taylor approximations of the function for $n=0,1,2,3,4,5$ around the points `a=-3,0,2`. (Make a separate plot showing approximations for each point `a` you expand around, for each function. Draw a dot on the graph on the point `a` in each case to make it clear which point you are considering. Label your plots accordingly to make it clear what you are showing.)
1. Discuss your observations in your notebook. When is the Taylor expansion a good approximation? When does it have difficulty?

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAME**
