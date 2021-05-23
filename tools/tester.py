class K:

    def __init__(self):
        self.k = [0, 1]

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self

for a in K():
    print(a)