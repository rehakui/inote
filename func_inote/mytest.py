def dec(function):
    print('dec')
    return function


@dec
def say_hello():
    print('hello')


say_hello()