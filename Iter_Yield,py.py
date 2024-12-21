list1 = [6, 8, 4]
iterable = iter(list1)

try:
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
except StopIteration:
    print("Reached the end of the list!")

def infinite_number():
    n = 1
    while True:
        yield n
        n += 1

numbers = infinite_number()
print(next(numbers))
print(next(numbers))
