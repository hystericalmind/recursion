print()
print(
print()
def test(txt: 'Fruits', *positions, made='Egipt', **total_weight):
    print(txt, *positions, made, total_weight)

test('apple',20, 400, 800, made='India', apple='pallet', lemon='box', banana='counter', a=20, b=20, c=20)

print()
print()
print()
print('--------------------------------------------------------------------------------------------------------')
print()
print()
print()
print('                            Вычисляем факториал любого числа                             ')
print()

def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)
n = int(input('Enter number : '))

factorial(n)
print(factorial(n))