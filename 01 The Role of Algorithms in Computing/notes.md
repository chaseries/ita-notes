# The Role of Algorithms in Computing

## 1.1 Algorithms

Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input, and produces some value, or set of values, as output. An algorithm is thus the sequence of computational steps that transforms an input into an output.

Here is how we formally define the *sorting problem*:

**Input**: A sequence of *n* numbers ⟨a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>⟩.

**Output**: A permutation (reordering) ⟨a′<sub>1</sub>, a′<sub>2</sub>, ..., a′<sub>n</sub>⟩ of the input sequence such that a′<sub>1</sub> ≤ a′<sub>2</sub> ≤ ... ≤ a′<sub>n</sub>.

For example, given ⟨31, 41, 59, 26, 41, 58⟩, a sorting algorithm returns as output the sequence ⟨26, 31, 41, 41, 58, 59⟩. Such an input sequence is called an *instance* of the sorting problem. An algorithm is said to be *correct* if, for every input instance, it halts with the
correct output.

## Definitions:

*Instance*: the input sequence given to a particular algorithm

*Correct*: the quality of an algorithm such that for any given valid input it halts with the correct output.

