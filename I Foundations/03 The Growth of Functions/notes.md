# 3 Growth of Functions

The order of growth of the *running time* of an algorithm gives a simple characterization of the algorithm's efficiency and also allows us to compare the relative performance of alternative algorithms.

When we look at input sizes large enough to make only the order of growth of the running time relevant, we are studying the *asymptotic* efficiency of algorithms. That is, we are concerned with how the running time of an algorithm increases with the size of the input in the limit, as the size of the input increases without bound.

## 3.1 Asymptotic notation

The notations we use to describe the asymptotic running time of an algorithm are defined in terms of functions whose domains are the set of natural numbers ℕ.

### Asymptotic notation, functions, and running times

The expression Θ(*g*(*n*)) is the set of functions: 

{ *f*(*n*) | ∃ *c*<sub>1</sub>, *c*<sub>2</sub>, *n*<sub>0</sub> ∈ ℕ, ∀ *n* ≥ *n*<sub>0</sub>, 0 ≤ *c*<sub>1</sub> *g*(*n*) ≤ *f*(*n*) ≤ *c*<sub>2</sub>*g*(*n*) }.


