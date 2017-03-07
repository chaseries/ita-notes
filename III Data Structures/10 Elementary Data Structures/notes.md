# 10 Elementary Data Structures

## 10.1 Stacks and queues

Stacks and queues are dynamic sets in which the element removed from the set by the DELETE option is prespecified. 

* In a *stack*, the element deleted from the set is the one most recently inserted (LIFO).
* In a *queue*, the element deleted is always the one that has been set for the longest time (FIFO).

### Stacks

We can implement a stack of at most *n* elements with an array *S*[1..*n*]. The following are fundamental operations on stacks:

* INSERT, often called PUSH, puts an element atop a stack
* DELETE, often called POP, removes an element from the top of the stack
* STACK-EMPTY, which queries whether or not a stack is empty

We also define the following terms for stacks:

* *Empty*, which designates a stack with 0 elements
* *Underflow*, the result of popping an empty stack
* *Overflow*, the result of adding the *n*+1<sup>th</sup> element to a stack *S*[1..*n*].

Here are pseudocode implementations of stack operations:

```
stackEmpty [] = True
stackEmpty _ = False

-- Ignoring overflow...
push x xs  = x :: xs

pop [] = error "Stack underflow"
pop (x:xs) = xs
```

### Queues

We define these operations for queues:

* INSERT, often called ENQUEUE
* DELETE, often called DEQUEUE, takes no argument

Like a line of customers waiting to check out, stacks are FIFO. We define these terms for a queue:

* *Head*, the first element waiting to be dequeued
* *Tail*, the position an element takes when it is enqueued, just as a customer takes her place at the back of a line

## 10.2 Linked lists

A *linked list* is a data structure in which the objects are arranged in a linear order.o

### Searching a linked list

### Inserting into a linked list

### Deleting from a linked list
