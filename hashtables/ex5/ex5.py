"""
# File Finder

Given a list of full paths to files, and a list of filenames to query,
report all the full paths that match that filename.

Example input:

```python
paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]

queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
```

Example return value:

```
[ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
```

because that's where the `foo.txt` and `ls` files are. 

The file `"nosuchfile.txt"` is ignored because it's not in the `paths`.

Return list can be in any order.

Limits:

* Up to approximately 1,000,000 paths.
* Up to approximately 1,000,000 queries.

"""

def finder(files, queries):
    storage, result = {}, []
    
    for f in files:
        # get the path to the file
        file_name = f.split("/")[-1]
        if file_name in storage:
            # add or append the file path
            storage[file_name].append(f)
            # else, leave the file path where it is
        else:
            storage[file_name] = [f]
    
    # for each item in queries,
    for q in queries:
        # if that item is in the bucket/slot,
        if q in storage:
            # then at that item to the result
            result += storage[q]
    
    return result


if __name__ == "__main__":
    # Input
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

# Expected Output: ['/bin/foo', '/usr/bin/baz']
