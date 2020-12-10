from test_pcc import get_formatted_name

print('Enter "q" at any time to quit.')
while True:
    first = str(input('\nPlease enter first name: '))
    if first == 'q':
        break
    last = str(input('Please provide last name: '))
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
