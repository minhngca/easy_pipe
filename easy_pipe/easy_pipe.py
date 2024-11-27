from functools import reduce

class Pipe:
    """
    A class representing a Pipe with Functional Programming style function chaining. 
    It also supports then, map, filter, reduce and match operations

    Attributes
    ----------
    __value : NoneType
        A private attribute, currently set to None. This attribute can be 
        assigned once during initialization or through static function x()
        of the Pipe class.
    """

    __value: None

    def __init__(self, input):
        self.__value = input
    
    @staticmethod
    def x(input):
        """
        A static method that initialize a Pipe object with value assigned

        Parameters
        ----------
        input : Any
            The input to be assigned to the __value property of the Pipe object

        Returns
        -------
        Pipe
            The Pipe object with private attribute `__value` assigned to `input`
        """
        return Pipe(input)
        
    @property
    def out(self):
        """
            Returns the value of the private attribute `__value`
        """
        return self.__value

    def then(self, func, *args):
        """
            Apply the function to internal attribute `__value` 

        Args:
            func (function): function to apply
            *args: extra arguments to supply when applying `func` function

        Returns:
            Pipe: a Pipe object with value as the output after applying the `func` function
        """
        return Pipe(func(self.__value, *args))

    def map(self, func, *args):
        """
            Apply the function `func` to all elements in the internal `__value` (iterable)

        Args:
            func (function): function to apply
            *args: extra arguments to supply when applying `func` function

        Returns:
            Pipe: a Pipe object with value as the output after applying the `func` function to all items of `__value`
        """
        return Pipe(map(func, self.__value, *args))

    def filter(self, func, *args):
        """
            Apply the filter operation to all elements in the internal `__value` (iterable)
            Keep only items that satisfy the `func` condition (return True)

        Args:
            func (function): function to filter (should return bool)
            *args: extra arguments to supply when applying `func` function

        Returns:
            Pipe: a Pipe object with value as the output after filter with the `func` function 
        """
        return Pipe(filter(func, self.__value, *args))

    def reduce(self, func, *args):
        """
            Apply the reduce operation to all elements in the internal `__value` (iterable)

        Args:
            func (function): function to reduce 
            *args: extra arguments to supply when applying `func` function

        Returns:
            Pipe: a Pipe object with value as the output after reduce with the `func` function 
        """
        return Pipe(reduce(func, self.__value, *args))

    def match(self, case_function_dict:dict, else_function=None, *args):
        """
            Apply the match operation to all elements in the internal `__value` (iterable)

        Args:
            case_function_dict (dict): the case and value (or function to apply)
            *args: extra arguments to supply when applying function

        Returns:
            Pipe: a Pipe object with value as the output after apply function with case matching internal `__value`
        """
        output = {case:value(case, *args) if callable(value) else value 
                  for case, value in case_function_dict.items()
                  if case == self.__value
                 }
        
        if len(output.items()) > 0:
            return Pipe(output[self.__value])
        elif else_function:
            # The "else" case, when there's no match
            return Pipe(else_function(self.__value))
        
        
    def __call__(self, func, *args):
        """ Make the object callable, e.g. pipe_1(func) is equivilant to pipe_1.then(func) """
        return self.then(func, *args)

    def __str__(self):
        """ Convert internal attribute `__value` to String """
        return str(self.__value)
    
