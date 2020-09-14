"""
# Positive and Negative

For an input list of integers, we wish to know which positive numbers
have corresponding negative numbers in the list.

Example input:

```python
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
```

Input can be in any order.

Example output/return value:

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

def has_negatives(numbers):
    # Traverse the given array, increase the count at absolute value of hash table
    storage, result = set(), []
    
    # for each element of array
    for n in numbers:
        # find the negative value of numbers[n] 
        diff = 0 - n
        # if absolute values are equal to positive numbers
        if diff in storage:
            # store its absolute value in another vector
            result.append(abs(diff))
        # else for each term in vector, print first its negative value and the positive value
        else:
            # add the positive number with negative value in the array
            storage.add(n)
    return result

# Driver code
if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
