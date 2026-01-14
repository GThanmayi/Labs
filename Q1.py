class Count:
    def __init__(self,limit):
        self.limit=limit
        self.current=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<=self.limit:
            val=self.current
            self.current+=1
            return val

        else:
            raise StopIteration

obj=Count(int(input()))
for num in obj:
    print(num)