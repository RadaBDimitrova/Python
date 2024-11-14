IN = "in"
OUT = "out"
SEP = ", "
INVALID_INPUT = "Invalid input arguments, expected "
INVALID_OUTPUT = "Invalid output value, expected "

def type_check(io):
    """Check types of input and output values for the function."""
    def expected_decorator(*types):
        def decorator(func):
            def inner(*args, **kwargs):
                if io == IN:
                    unexpected_types = set(filter(lambda x: not isinstance(x, types), args + tuple(kwargs.values())))
                    if unexpected_types:
                        print(INVALID_INPUT + SEP.join([str(s) for s in types]) + "!")
                
                actual_result = func(*args, **kwargs)

                if io == OUT:
                    if not isinstance(actual_result, types):
                        print(INVALID_OUTPUT + SEP.join([str(s) for s in types]) + "!")
                return actual_result
            return inner
        return decorator
    return expected_decorator
