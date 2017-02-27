# The Role of Algorithms in Computing

TODO: Flesh out problems

## 1.1 Algorithms

Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input, and produces some value, or set of values, as output. An algorithm is thus the sequence of computational steps that transforms an input into an output.

Here is how we formally define the *sorting problem*:

**Input**: A sequence of *n* numbers ⟨a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>⟩.

**Output**: A permutation (reordering) ⟨a′<sub>1</sub>, a′<sub>2</sub>, ..., a′<sub>n</sub>⟩ of the input sequence such that a′<sub>1</sub> ≤ a′<sub>2</sub> ≤ ... ≤ a′<sub>n</sub>.

For example, given ⟨31, 41, 59, 26, 41, 58⟩, a sorting algorithm returns as output the sequence ⟨26, 31, 41, 41, 58, 59⟩. Such an input sequence is called an *instance* of the sorting problem. An algorithm is said to be *correct* if, for every input instance, it halts with the
correct output.

### What kinds of problems are solved by algorithms?

* Graph problems.
* Longest common subsequence of two strings (exponential, solvable via dynamic programming).
* Ordering libraries of parts so that each part appears before any part that uses it (n! possible solutions).
* Convex hull


### Definitions:

*Instance*: the input sequence given to a particular algorithm

*Correct*: the quality of an algorithm such that for any given valid input it halts with the correct output.

### Exercises

Honestly, these are a bit silly.

## 1.2 Algorithms as a technology

Of course, computers may be fast, but they are not infinitely fast. And memory may be inexpensive, but it is not free. Computing time is therefore a bounded resource, and so is space in memory. You should use these resources wisely, and algorithms that are efficient in terms of time or space will help you do so.

### Exercises

**1.2-2**

Assume or inputs of size *n*, insertion sort runs in 8*n*<sup>2</sup> steps, while merge sort runs in 64*n* lg *n* steps. For which values of n does insertion sort beat merge sort?

**1.2-3**

