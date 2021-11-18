print('Enter Enter numbers separated by a space')
numbers = input('>>>')

numbers = [int(i) for i in numbers.split(' ')]
print(numbers)