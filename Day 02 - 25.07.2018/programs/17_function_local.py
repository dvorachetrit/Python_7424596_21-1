x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


"""
$ python function_local.py
x is 50
Changed local x to 2
x is still 50
"""