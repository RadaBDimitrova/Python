from functools import reduce

NI = "Ni!"

def append_currrency(func):
    def format(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str) and result != NI:
            return f"{result}лв"
        return result
    return format


@append_currrency
def function_that_says_ni(*args, **kwargs):
    keywords = set(["храст", "shrub", "bush"])

    important_args = list(filter(lambda arg: isinstance(arg, dict) and arg.get("name", "").lower() in keywords, args))
    important_kwargs = list(filter(lambda key_value: isinstance(key_value[1],dict) and key_value[1].get("name","").lower() in keywords, kwargs.items()))

    bushes = important_args + [key_value[1] for key_value in important_kwargs]

    total_cost = round(sum(map(lambda bush: bush.get('cost', 0), bushes)), 2)

    unique_characters = set()
    for key_value in important_kwargs:
        unique_characters.update(key_value[0])
    if int(total_cost) == 0:
        return NI
    elif total_cost <= 42.00 and total_cost >= 0.00 and len(unique_characters) % int(total_cost) == 0:
        return f"{total_cost:.2f}"
    return NI
