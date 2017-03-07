# Hash Tables

Many applications require a dynamic set that supports only the dictionary operations INSERT, SEARCH, and DELETE. For example, a compiler that translates a programming language maintains a symbol table, in which the keys of the elements are arbitrary character strings corresponding to identifiers in the language.

Although searching for an element in a hash table can take as long as searching for an element in a linked list—Ө(*n*) time in the worst case—in practice, hashing performs extremely well.

When the number of keys actually stored is small relative to the total number of possible keys, hash tables become an efective alternative to directly addressing an array, since a hash table typically uses an array of size proportional to the number of keys actually stored.

Instead of using the key as an array index directly, the array index is *computed* from the key. The main ideas focus on "chaining" as a way to handle "collisions," in which more than one key maps to the same array index. Later we see "open addressing," which is another way to deal with collisions.

The bottom line is that hashing is an extremely effective and practical technique. **Important**: Basic hashing techniques only require *O*(1) time on the average. "Perfect hashing" can support searching in O(1) *worst-case* time, when the set of keys being stored is static.

## 11.1 Direct-address tables

*Direct addressing* is a simple technique that works well when the universe *U* of keys is reasonably small. Suppose that an application needs a dynamic set in which each element has a key drawn from the universe *U* = {0, 1, ..., *m*-1}, where *m* is not too large. We assume that no two elements share a key.

### Definitions

*Direct addressing*:
