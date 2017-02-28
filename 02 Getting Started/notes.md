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

*Loop invariants*: Some portion of an input set which remains correct throughout the running of the algorithm. In the case of insertion sort on array A, it is the trivially-sorted 1-element subarray A[0] against which each loop iteration is compared. The result of each iteration i is the sorted subarray A[0:i + 1].

### Exercises

**2.1-1**

Not doing this.

**2.1-2**

Answered in `insertion_sort_dec.py`.

**2.1-3**

Not doing this.

**2.1-4**

Not doing this.

## 2.2 Analyzing Algorithms

*Analyzing* an algorithm has come to mean predicting the resources that the algorithm requires. Occasionally, resources such as memory, communication bandwidth, or computer hardware are of primary concern. Usually, though, it is time as a function of input size.

The best notion for *input size* depends on the problem; sometimes it is the number of items in the input (e.g., discrete Fourier transforms), other times it is the number of bits (e.g., multiplying two integers).

The *running time* of an algorithm on a particular input is the number of primitive
operations or “steps” executed. For simplicity, we assume a constant amount of time is required to execute each line of our code. One line may take a different amount of time than another line, but we shall assume that each execution of the *i*th line takes time c<sub>i</sub>, where c<sub>i</sub> is a constant.

### Worst-case and average-case analysis

We will generally focus on worst-case and average-case analysis and disregard the best case, because:

* The worst-case running time of an algorithm gives us an upper bound on the running time for any input. It is a guarantee the algorithm will never take any longer.
* For some algorithms, worst-case occurs fairly often
* The average case is often roughly as bad as the worst case.

### Order of growth

In general, it isn't constant factors, but only the *rate of growth* or *order of growth* that interests us.

### Definitions

*Analysis*: Predicting the resources an algorithm requires.
*Input size*: A notion representing the heft of the problem a given algorithm must solve. *Input size* may most appropriately refer to different things, like the number of elements in a sortable array, or the number of bits involved in integer multiplication.
