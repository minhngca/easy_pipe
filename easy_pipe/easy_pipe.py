from functools import reduce

class Pipe:
    input: None

    def __init__(self, input):
        self.input = input
    
    @staticmethod
    def x(input):
        return Pipe(input)
        
    def then(self, func, *args):
        return Pipe(func(self.input, *args))

    def map(self, func, *args):
        return Pipe(map(func, self.input, *args))

    def filter(self, func, *args):
        return Pipe(filter(func, self.input, *args))

    def reduce(self, func, *args):
        return Pipe(reduce(func, self.input, *args))

    def __call__(self, func, *args):
        return self.then(func, *args)

    def __str__(self):
        return str(self.input)
    
    @property
    def out(self):
        return self.input
