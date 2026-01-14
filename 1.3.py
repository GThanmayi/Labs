class CountIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

# Using the custom iterator
print("Iterator values:")
for num in CountIterator(5):
    print(num)


def count_generator(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

# Using the generator
print("\nGenerator values:")
for num in count_generator(5):
    print(num)

