# Vector Math
## Base Equation
$$E = \frac{kd}{r^2}$$
Foo the sake of the simulation **K is equal to 1**

## Known Variables
<div style='text-align: center'>X and Y of point for calculation<div>
<br>
<div style='text-align: center'>X, Y, and charge (q) of particle<div>

## Calculating Forces with one particle
$$dx = x_{point} -  x_{charge}$$
$$dy = y_{point} - x_{charge}$$
### The pythagorem theorum is then used to get the the distance between the point and charge (r)
$$r = \sqrt{dx^2 + dy^2}$$
### Now the formula for finding the vectors is as follows
$$U = \frac{dx \times q}{r^2}$$ 
$$V = \frac{dy \times q}{r^2}$$

## Normalization
Within this calculation comes a problem, **exponential** increase in value. The graphs currently being used are able to display this exponential function, I dont want this, instead I want the *colors to display intesity*. While the *arrows soley display direction* while all remaining the *same size*. While simply not squaring $r$ works when calculation for a single point, it results in summation errors when calculating for multiple. In order to acheive this I will need to use some form of **logorithmic normilization**.

### Logorithmic Normilzation - Idea 1
