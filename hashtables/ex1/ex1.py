"""
Algo:
1. Initialize an empty hash table
2. For each index in the array:
    - Calculate the complement by subtracting the current list element from the given number (limit)
    - Look up the complement in the hash table
        - If it exists, a pair that sums up to the given number has been found
    - Insert the current index of the array into the hash table after you perform the step above
    
Runtime Complexity: the execution count
* Time Complexity: Big O is O(n) - if n is a length of the array, n(linar)
* Space Complexity: O(m) - where m is the number of the unique weights in array
"""

# Find 2 items:
# Sum of 2 weights(num_arr) == limit(pair_sum)
def get_indices_of_item_weights(weights: list, length: int, limit: int) -> list:
    length = len(weights)
    # Initialize an empty hash table with python dictionary
    hashTable = dict()
    
    if length <= 1:
        return None
    
    # Traverse arr only once. For each weight in arr, compute its complement limit - weight and check wether that complement is hashed so far
    for i in range(length):
        weight = weights[i]
        # If found the complement in the map, return a pair that consists of weight's and limit - weight's indices
        if weight in hashTable:
            value = hashTable[weight]
            return [i, value]
        # If not, hash the weight while using:
        # weight = hash key
        # array index = hash value
        # Even if the same weight is found more than once, it doesn't matter because at the time of the lookup, we only need one item with that weight
        diff = limit - weight
        hashTable[diff] = i
    # if such a pair doesn't exist, return an empty array
    return None

# Driver code
print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))

"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""
