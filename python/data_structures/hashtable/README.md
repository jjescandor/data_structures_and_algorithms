# Hashtables
Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.

## Challenge
Implement a Hashtable Class with the following methods:
1. set
1. get
1. contains
1. keys
1. hash

## Approach & Efficiency
1. set 
    - time: O(1)
    - space: O(1)
1. get
    - time: O(n)
    - space: O(1)
1. contains
    - time: O(n)
    - space: O(2)
1. keys
    - time: O(n^2)
    - space: O(n)
1. hash
    - time: O(n)
    - space: O(1)

## API
1. set
    - Arguments: key, value
    - Returns: nothing
    - This method should hash the key, and set the key and value pair in the table, - handling collisions as needed.
    - Should a given key already exist, replace its value from the value argument given to this method.
1. get
    - Arguments: key
    - Returns: Value associated with that key in the table
1. contains
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already.
1. keys
    - Returns: Collection of keys
1. hash
    - Arguments: key
    - Returns: Index in the collection for that key