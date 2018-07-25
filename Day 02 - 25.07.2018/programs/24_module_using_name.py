if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

"""
$ python module_using_name.py
This program is being run by itself

$ python
>>> import module_using_name
I am being imported from another module
>>>
"""