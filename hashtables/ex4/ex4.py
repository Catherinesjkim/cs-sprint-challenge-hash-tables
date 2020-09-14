"""
# Positive and Negative

For an input list of integers, we wish to know which positive numbers
have corresponding negative numbers in the list.

Example input:

```python
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
```

Input can be in any order.

Example return value:

```python
[ 1, 3, 4 ]
```

Because 1, 3, and 4 are the positive numbers that have corresponding
negative numbers in the list.

Return value can be in any order.

Solve this problem with a hash table.

Limits:
* The input list can contain approximately 5,000,000 elements.
"""
# Traverse the given array, increase the count at absolute value of hash table
# If count becomes 2, store its absolute value in another vector
# And finally sort the vector
# If the size of the vector is 0, print "0"
# else for each term in vector, print first its negative value and the positive value
def has_negatives(numbers):
    storage, result = set(), []
    
    # for each element of array
    for n in numbers:
        # Try to find the negative value of numbers[i] from i + 1 to numbers
        diff = 0 - n
        # If absolute values are equal to positive numbers,
        if diff in storage:
            # Print the positive number with negative value in the array
            result.append(abs(diff))
        else:
            storage.add(n)
            
    return result

# Driver code
if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
