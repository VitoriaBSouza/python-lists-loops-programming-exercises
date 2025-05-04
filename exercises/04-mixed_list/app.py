mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below
def count(arr):
    for i in arr:
        print(type(i))

print(count(mix))