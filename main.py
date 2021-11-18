def num(numbers):
	numbers = [int(i) for i in numbers.split(' ')]
	return numbers


print('Enter numbers separated by a space')
n = input('>>>')

print(num(n))
