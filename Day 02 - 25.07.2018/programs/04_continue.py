while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    # Do other kinds of processing here...


"""
python continue.py
Enter something : "a"
Too small
Enter something : "test"
Input is of sufficient length
Enter something : "quit"
"""