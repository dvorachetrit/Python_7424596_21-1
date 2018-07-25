s = 'quit'
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')


"""
python break.py
Enter something : "test"
('Length of the string is', 4)
Enter something : "quit"
Done
"""