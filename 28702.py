for i in range(3, 0, -1):
    a = input()
    if a not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(a)+i
if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)