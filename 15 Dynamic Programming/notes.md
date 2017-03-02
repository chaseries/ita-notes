# Dynamic Programming

Dynamic programming, like the divide-and-conquer method, solves problems by combining solutions to subproblems. Dynamic programming applies when subproblems overlap (when subproblems share subproblems).

We typically apply dynamic programming to *optimization problems*. Each solution has a value, and we wish to find a solution with the optimal (minimum or maximum) value.

When developing a dynamic programming algorithm, we follow a sequence of four steps:

1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a bottom-up fashion
4. Construct an optimal solution from computed information

Steps 1-3 form the basis of a dynamic programming solution to a problem. If we need only the value of an optimal solution, and not the solution itself, then we can omit step 4.

## 15.1 Rod cutting

The *rod-cutting problem* is the following: Given a rod of length *n* inches and a table of prices *p*<sub>*i*</sub> for *i* = 1, 2, ..., *n*, determine the maximum revenue *r*<sub>*n*</sub> obtainable by cutting up the rod and selling the pieces. Note that if the price *p*<sub>*n*</sub> for a rod of length *n* is large enough, an optimal solution may require no cutting at all.


