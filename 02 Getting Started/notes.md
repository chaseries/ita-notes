# 2 Getting Started

## 2.1 Insertion sort

Our first algorithm solves the *sorting problem* introduced in Chapter 1:

**Input**: A series of numbers ⟨a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>⟩.

**Output**: A permutation (reordering) ⟨a′<sub>1</sub>, a′<sub>2</sub>, ..., a′<sub>n</sub>⟩ of the input sequence such that a′<sub>1</sub> ≤ a′<sub>2</sub> ≤ ... ≤ a′<sub>n</sub>.

The numbers that we wish to sort are the *keys*.

```
0 insertion_sort(A):
1   for j = 2 to A.length:
2     key = A[j]
3     // Insert A[j] into the sorted sequence A[1..j - 1]
4     i = j - 1
5     while i > 0 and A[i] > key:
6       A[i + 1] = A[i]
7       i = i - 1
8     A[i + 1] = key
```


### Definitions

*Keys*: In the *sorting problem*, *keys* are the numbers of an array by which we sort.
*Loop invariants*: 
