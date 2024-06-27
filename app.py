
def myfunc(num1, **kwargs:'Dictionary, unknown amount'):
    """This function does all kindsa stuff
    """
    if num1 == 1:
        return "it's a 1!!!"
    return kwargs
def myfunc2(num1, **kwargs):
    if num1 == 1:
        return "it's a 1!!!"
    return kwargs





dict1 = {'one':1, 'two':2, 'three':3}
print(myfunc(1, one=1, two=2, three=3))

