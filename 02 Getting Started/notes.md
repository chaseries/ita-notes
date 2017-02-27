# 2 Getting Started

## 2.1 Insertion sort

Our first algorithm solves the *sorting problem* introduced in Chapter 1:

**Input**: A series of numbers ⟨a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>⟩.

**Output**: A permutation (reordering) ⟨a′<sub>1</sub>, a′<sub>2</sub>, ..., a′<sub>n</sub>⟩ of the input sequence such that a′<sub>1</sub> ≤ a′<sub>2</sub> ≤ ... ≤ a′<sub>n</sub>.

The numbers that we wish to sort are the *keys*.

```
0 INSERTION-SORT(A):
1   for j = 2 to A.length:
2     key = A[j]
3     // Insert A[j] into the sorted sequence A[1..j - 1]
4     i = j - 1
5     while i > 0 and A[i] > key:
6       A[i + 1] = A[i]
7       i = i - 1
8     A[i + 1] = key
```

We use loop invariants to help us understand why an algorithm is correct. We
must show three things about a loop invariant:

* Initialization: It is true prior to the first iteration of the loop
* Maintenance: If it is true before an iteration of the loop, it remains true before the next iteration
* Termination: When the loop terminates, the invariant gives us a useful property that helps show the algorithm is correct.

### Definitions

*Keys*: In the *sorting problem*, *keys* are the numbers of an array by which we sort.
*Loop invariants*: 

## 2.2 Analyzing Algorithms

*Analyzing* an algorithm has come to mean predicting the resources that the algorithm requires. Occasionally, resources such as memory, communication bandwidth, or computer hardware are of primary concern. Usually, though, it is time.
