# PHYS220/MATH220/CPSC220 CW 10

**Author(s):** **Enea Dodi & Jack Savage**

## Specification

In this assignment, we will start thinking about how to solve "ordinary differential equations" numerically. These are simply equations that involve at least one derivative in the equation. We will use the intuition of the "forward difference" and "central difference" equations explored in the last classwork to develop increasingly accurate methods for numerically solving such an equation.

Consider a first-order ordinary differential equation (ODE) $$u'(t) = f[t, u(t)]$$ For concrete examples, consider $u'(t) = 2 u(t)$, or $u'(t) = 2t^2u(t)$. Such an equation states that the function $f[t, u(t)]$ is the slope of $u(t)$ at the domain point $t$; to calculate this slope, one generally needs to know both the range value $u(t)$ as well as the domain point $t$. The usual task of solving such a differential equation is to start from an "initial condition" $u(t_0) = u_0$ and reconstruct what the entire function $u(t)$ must be for $t>t_0$. There are analytical methods for cleverly reconstructing such a solution (e.g., solving $u'(t) = 2u(t)$ yields $u(t) = u_0 \exp(2 t)$, which you can verify by computing its derivative and plugging it back into the original equation), but we are interesting here in how to numerically obtain the solution without using analytical methods.

To construct a solution, we first define a discrete mesh of domain points $(t_0, t_1, t_2, ..., t_N)$ with uniform spacing $\Delta t = t_{k+1} - t_k$. Starting from the initial condition $u(t_0) = u_0$, we then iteratively construct a sequence of matching range points $(u_0, u_1, u_2, ..., u_N)$, where $u_k = u(t_k)$, by using the slopes $u'(t_k)$ at each domain point. This procedure is tricky for two reasons: (1) computing the slopes $u'(t_k)$ generally requires knowledge of the function $u(t_k)$ that one is trying to reconstruct, leading to a chicken-and-egg problem; (2) the first-derivative $u'(t_k)$ can only produce a linear approximations to $u(t)$ around the point $t_k$, so will only approximate $u(t)$ if $\Delta t$ is sufficiently small. To be more explicit about this latter reason, consider the Taylor expansion of $u(t)$ around a particular point $t_k$: $$u(t_k + s) = u(t_k) + u'(t_k)s + u''(t_k)s^2/2 + u'''(t_k)s^3/3! + ...$$ Generally one will need to know all higher-order derivatives of $u(t)$ at $t=t_k$ to reconstruct the function at the point $t_k + s$. However, if $s=\Delta t$ is small, then one can approximate $(\Delta t)^2 \approx 0$, yielding $u(t_k + \Delta t) = u(t_k) + u'(t_k)\Delta t$. Thus, if one knows the slope $u'(t_k) = f[t_k, u(t_k)]$, then one obtains $u_{k+1} = u_k + \Delta t\, f[t_k, u_k]$, which allows one to obtain the next range point $u_{k+1}$ given only knowledge of the current range point $u_k$. We say this method (called "Euler's method") for obtaining $u_{k+1}$ from $u_k$ is accurate to "1st-order in $\Delta t$", since the error of this approximation scales as $(\Delta t)^2$. Observe that Euler's method corresponds to rearranging the "forward difference" definition of the derivative.

This first-order method for obtaining the approximate sequence $(u_0, u_1, u_2, ..., u_N)$ of solution range points is not the only method. For example, consider the "Leapfrog Method" as an alternative. With this method, one starts from the point $t_k$, then looks both forward one point and backward one point. The Taylor expansion for each yields $u(t_k + \Delta t) = u_{k+1} = u_k + u'(t_k)\Delta t + u''(t_k)(\Delta t)^2/2 + O(\Delta t)^3$ and $u(t_k - \Delta t) = u_{k-1} = u_k - u'(t_k)\Delta t + u''(t_k)(\Delta t)^2/2 + O(\Delta t)^3$, where $O(\Delta t)^3$ means terms of order $(\Delta t)^3$. Note that the second-order terms have the same sign, while the first-order terms have opposite sign. This means that if we take the difference of these two expansions, we get the relation: $$u_{k+1} - u_{k-1} = 2u'(t_k)\Delta t + O(\Delta t)^3$$
That is, the second-order terms cancel entirely, leaving an expression that relates the next range point $u_{k+1}$ to the preceding range point (two steps back) $u_{k-1}$ and the current slope (one step back) $u'(t_k)$, with an error that scales as $(\Delta t)^3$ (making the method accurate to "second-order in $\Delta t$"). Since this method cancels out the second-order error terms, it will produce a more accurate approximation to the solution than Euler's method for finite mesh spacings $\Delta t$. Observe that the Leapfrog Method corresponds to rearranging the "central difference" definition of the derivative.

The goal of this assignment is to understand what these solution methods are doing graphically, as well as several more methods outlined below. To do this, for each of the following iterative solution methods, discuss together on the white board to understand how they work. Draw an arbitrary function $u(t)$ to start. Outline a (reasonably coarse) mesh of domain points $(t_0, t_1, t_2, ...)$ and find the initial value $u_0 = u(t_0)$ on the graph. Explain to each other graphically what each method is doing to construct the sequence of range points $(u_0, u_1, u_2, ...)$. When you have reached a good understanding graphically on the board, try to explain in words what the method is doing. With your group, write a notebook ```ode_methods.ipynb``` that summarizes your conclusions in words and details what each method is doing. (No need to draw graphs in the notebook, but use equations where needed.) Note that there is no coding in this assignment yet, so focus on making a clear and readable report of the methods in your notebook. We will implement the algorithms that you derive into code next week. 

1. Euler's Method (accurate to 1st-order):
   
   $u_{k+1} = u_k + \Delta t\, f[t_k, u_k]$
1. Leapfrog (Midpoint) Method (accurate to 2nd-order):
   
   $u_{k+1} = u_{k-1} + 2\Delta t\, f[t_k, u_k]$
   
   (How do you compute $u_1$?)
1. Heun's (Trapezoid) Method (accurate to 2nd-order):
   
   $\tilde{u}_{k+1} = u_k + \Delta t\, f[t_k, u_k]$, 
   
   $u_{k+1} = u_k + (\Delta t/2)(f[t_k, u_k] + f[t_{k+1}, \tilde{u}_{k+1}])$  
   
   (Note the two steps - what is each doing?)
1. 2nd-order Runge-Kutta Method (accurate to 2nd-order):
   
   $u_{k+1} = u_k + K_2$, 
   
   $K_1 = \Delta t\, f[t_k, u_k]$, 
   
   $K_2 = \Delta t\, f[t_k + \Delta t/2, u_k + K_1/2]$  
   
   (How does this differ from Heun's method?)
1. 4th-order Runge-Kutta Method (accurate to 4th-order):
   
   $u_{k+1} = u_k + (K_1 + 2K_2 + 2K_3 + K_4)/6$, 
   
   $K_1 = \Delta t\,f[t_k,u_k]$, 
   
   $K_2 = \Delta t\, f[t_k + \Delta t/2, u_k + K_1/2]$, 
   
   $K_3 = \Delta t\, f[t_k + \Delta t/2, u_k + K_2/2]$, 
   
   $K_4 = \Delta t\,f[t_k + \Delta t, u_k + K_3]$  
   
   (Note that final increment is a weighted average of four different increments - what is each doing? Why do you suppose the middle increments are more heavily weighted?)

In practice, the 4th-order Runge-Kutta method is the most popular method for solving ODEs numerically, since it nicely balances the accuracy per time step with the total number of required computations. It is usually more efficient to simply decrease the time step size using 4th-order Runge-Kutta rather than find methods of higher-order accuracy. More sophisticated approaches also dynamically resize the mesh into non-uniform spacings, but we will not explore that in this class.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have. You can use the GitHub web interface to edit this file directly for now.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Enea Dodi & Jack Savage**
