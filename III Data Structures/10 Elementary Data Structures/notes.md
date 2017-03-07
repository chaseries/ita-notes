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

A queue *Q* may have an attribute *Q.head* which indexes its head and an attribute *Q.tail* which points to its tail. When *Q.head* == *Q.tail*, the queue is empty. When *Q.head* == *Q.tail* + 1, the queue is full, and if we attempt to enqueue an element, then the queue overflows.

## 10.2 Linked lists

A *linked list* is a data structure in which the objects are arranged in a linear order. Unlike an array, however, in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object.

Linked lists support all the dynamic set operations listed in the introduction (INSERT, DELETE, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR).

A *doubly linked list* is an object with an attribute *key* and two other pointer attributes, *next* and *prev*. The object may also contain other satellite data. Given an element *x* in a doubly linked list *L*, *x.next* points to its successor in the linked list, and *x.prev* points to its predecessor. If *x.prev* == NIL, the element *x* has no predecessor and is therefore the first element, or *head*, of the list. If *x.next* == NIL, the element *x* has no successor and is therefore the last element, or *tail*, of the list. If *L.head* == NIL, the list is empty. (I have never heard the last element of a list being referred to as the tail; *tail* usually refers to the last *n-1* elements of the list. That is, everything in the list but the head.—Ed.)

A list may have one of several forms. It may be either singly linked or doubly linked, it may be sorted or not, and it may be circular or not. 

* *Singly-linked list* a linked list whose keys *x*<sub>i</sub> only feature an *x.next* attribute.
* *Doubly-linked list* a linked list whose keys *x*<sub>i</sub> feature both *x.next* and *x.prev* attributes
* *Sorted list* a list whose linear order corresponds to the linear order of the keys within the list
* *Circular list* a list whose *prev* pointer of the head of the list points to the tail, and whose *next* pointer of the tail of the list points to the head.

### Searching a linked list

The procedure LIST-SEARCH(*L*, *k*) finds the first element with key *k* in a list *L* by a simple linear (Θ(*n*)) search, returning a pointer to this element. If no object *k* appears in the list, then the procedure returns NIL.

### Inserting into a linked list

Given an element *x* whose *key* attribute is already set, the LIST-INSERT procedure "splices" *x* onto the front of the linked list according to the following procedure:

LIST-INSERT(*L*, *x*)
1  *x.next* = *L.head*
2  **if** *L.head* ≠ NIL
3    *L.head.prev* = *x*
4  *L.head* = *x*
5  *x.prev* = NIL

The running time of LIST-INSERT on a list of *n* elements is *O*(1).

### Deleting from a linked list

LIST-DELETE operates in the obvious way, and runs in *O*(1) time for deleting from the head, else Ө(n) time.

LIST-DELETE(*L*, *x*)
2  **if** *x.prev* ≠ NIL
3    *x.prev.next* = *x.next*
4  **else** *L.head* = *x.next*
5  **if** *x.next* ≠ NIL
6    *x.next.prev* = *x.prev*

### Sentinels

A *sentinel* is a dummy object that allows us to simplify boundary conditions. For example, suppose we provide with list *L* an object *L.nil* that represents NIL but has all the other attributes of the other objects in the list. Whenever we have a reference to NIL in the code, we replace it by a reference to the sentinel *L.nil*.

This change turns a regular doubly-linked list into a *circular, doubly-linked list with a sentinel*. The sentinel *L.nil* lies between the head and the tail of the list, so that the attribute *L.nil.next* points to the head of the list, and the attribute *L.nil.prev* points to the tail of the list.

## 10.3 Implementing pointers and objects

How do we implement pointers and objects in languages that do not provide them? We synthesize objects and pointers from arrays and array indices.

### A multiple-array representation of objects

We can represent a collection of objects that have the same attributes by using an array for each attribute. For instance, we can represent a linked list using three arrays:

```
        1  2  3  4  5  6  7  8
next  |  |03| /|  |02|  |05|  |
key   |  |04|01|  |16|  |09|  |
prev  |  |05|02|  |07|  | /|  |
```

### A single-array representation of objects

The words in a computer memory are typically addressed by integers from 0 to *M* - 1, where *M* is a suitably large integer. In many programming languages, an object occupies and contiguous set of locations in the computer memory. A pointer is simply the address of the first memory location of the object, and we can address other memory locations within the object by adding an offset to the pointer.

### Definitions

*Linked list*:
*Doubly-linked list*:

TABLING THE REST OF THIS CHAPTER BECAUSE IT'S NOT VERY USEFUL TO ME
