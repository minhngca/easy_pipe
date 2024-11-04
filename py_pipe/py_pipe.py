class Pipe:
    input: None

    def __init__(self, input):
        self.input = input

    def then(self, func, *args):
        return Pipe(func(self.input, *args))

    def __call__(self, func, *args):
        return self.then(func, *args)

    def __str__(self):
        return str(self.input)
    
    @property
    def out(self):
        return self.input
