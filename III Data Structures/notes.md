# III Data Structures

## Introduction

Sets are as fundamental to computer science as they are to mathematics. Whereas mathematical sets are unchanging, the sets manipulated by algorithms can grow, shrink, or otherwise change over time.

We call such sets *dynamic*.

The best wy to implement a dynamic set depends upon the operations that must be supported.

## Elements of a dynamic set

In a typical implementation of a dynamic set, each element is represented by an object whose attributes can be examined and manipulated if we have a pointer to the object.

Some kinds of dynamic sets assume that one of the object's attributes is an identifying *key*. Objects may also contain *satellite data*, which are carrie daround in other object attributes but are otherwise unused by the set implementation.

### Operations on dynamic sets

Operations on dynamic sets can be grouped into two categories: *queries*, which simply return information about the set, and *modifying operations*, which change the set.

Below is a typical list of operations; any specific application will require only a few of these to be implemented.

SEARCH(*S*, *k*)
  A query that, given a set *S* and key value *k*, returns a pointer to an element in *S* such that *x.key == k*, or NIL if no such element belongs to *S*.

INSERT(*S*, *x*)
  A modifying operation that augments the set *S* with the element pointer to by *x*. We usually assume that any attributes in element *x* needed by the set implementation have halready been initialized.

DELETE(*S*, *x*)
  A modifying operation that, given a pointer *x* to an element in the set *S*, removes *x* from *S*. 

MINIMUM(*S*)
  A query on the totally-ordered set *S* that returns a pointer to the element of *S* with the smallest key.

MAXIMUM(*S*)
  A query on the totally-ordered set *S* that returns a pointer to the element *S* with the largest key. 

SUCCESSOR(*S*, *x*)
  A query that, given an element *x* whose key is from a totally-ordered set *S*, returns a pointer to the next-larger element in *S*, or NIL if *x* is the maximum element.

PREDECESSOR(*S*, *x*)
  A query that, given an element *x* whose key is from a totally-ordered set *S*, returns a pointer to the next-smaller element in *S*, or NIL if *x* is the minimum element.

(Damn!)

### Definitions:

*Dynamic set*: A set which can grow, shrink, or otherwise change over time.
*Dictionary* A dynamic set which supports the ability to insert elements into, delete elements from, and test membership in a set.
*Key*: An attribute of an object that identifies it; if all keys are different, we can think of the dynamic set as being a set of key values.
*Satellite data*: Data which are carried around in other object attributes but are otherwise unused by the set implementation.
