## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions: 

Hashing is the process of using an algo to map data of any size to a fixed length. This is called a hash value. Hashing is used to create high performance, direct access data structures where large amount of data is to be stored and accessed quickly. Hash values are computed with hash functions. 

The hash() function returns the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).


2. Collision resolution: 

Two keys mapping to the same location in the hash table is called "Collision"

Collisions can be reduced with a selection of a good hash function

But it's not possible to avoid collisions altogether
    - Unless we find a perfect hash function
    - Which is hard to do

Few Collision Resolution ideas
    - Separate chaining
    - Some open addressing techniques
        - Linear Probing
        - Quadratic Probing


3. Performance of basic hash table operations: Since there's always the initial (constant) cost of hashing, the cost of hash table operations with a good hash function is, on average, O(1 + a). If we can ensure that the load factor a never exceeds some fixed value a^max, then all operations will be O(1 + a^max) = O(1) 


4. Load factor: It's a measure of how full the hash table is allowed to get before its capacity is automatically increase. 


5. Automatic resizing: When the number of entries in the hash table exceeds the product of the load factor and the current capacity, the hash table is rehashed (that is, internal data structures are rebuilt) so that the hash table has approximately twice the number of buckets.


6. Various use cases for hash tables:

Typical questions that rely on hash tables contain phrases like:

- Search for elements within a large data set
- Find duplicate elements in a data set
- Quickly store and retrieve elements from a large data sets

Useful for real apps with millions of data points (names, emails, database rowse, etc.) The difference between writing a series of nested loops and using hash tables can be the difference between your program running for seconds and running for days.


We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.