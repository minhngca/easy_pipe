# easy_pipe
Easy function chaining like piping in R (|>).


## Installation
`pip install git+https://github.com/minhngca/easy_pipe.git`

## How to use
- Import the easy_pipe library
- First, we need to supply the input using `Pipe.x()` or `Pipe(input=...)`
- Then, use `.then(function_name, extra_arguments)` to apply the function to the input
- We can use `.then()` as many times as we want
- Finally, to get the output value, we use `.out` 

Example code:
```
from easy_pipe import Pipe

# define some functions to apply
double_fn = lambda x: x*2
double_fn(100) # should be 200

add_fn = lambda x, y: x+y
add_fn(10, 20) # should be 30

Pipe(10).then(double_fn).then(square_fn).out 
# should be 10*2 -> square() = 400
```


## Functional programming operations
easy-pipe supports Functional programming style operations such as `map`, `filter` and `reduce`

#### Map
```

numbers = [1, 2, 3, 4, 5]
Pipe.x(numbers).map(square_fn).then(list).out
# output: [1, 4, 9, 16, 25]
```

#### Filter
```
numbers = [1, 2, 3, 4, 5]
(Pipe.x(numbers)
 .map(square_fn)
 .filter(lambda x: x % 2 == 0) # filter and keep even numbers
 .then(list)
 .out 
)
# output: # [4, 16]

```

#### Reduce
```
numbers = [1, 2, 3, 4, 5]
(Pipe.x(numbers)
 .reduce(add_fn)   
 .out 
)
# output: 15 (1+2+3+4+5)
```

### Match
```
# Pipe match with values
number = 100
(Pipe
 .x(number % 2)
 .match(
    {0: "The number is even",
     1: "The number is odd"
    })
 .out
)
# Output: 'The number is even'
```

Match with functions 
```
number = 101
(Pipe
 .x(number)
 .then(lambda x: x%2)
 .match(
    {0: lambda x: f"{x} is even",
     1: lambda x: f"{x} is odd"
    })
 .out
)

# output: '1 is odd'
```