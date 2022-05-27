class numbers:

    def __iter__(self):

        self.x=1

        return self

    def __next__(self):

        y=self.x

        self.x+=1

        return y

a=numbers()

b=iter(a)

print(next(b))

print(next(b))

print(next(b))

print(next(b))

print(next(b))
