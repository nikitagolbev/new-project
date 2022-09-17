znak = ''
while znak != '-' and znak != '+':
  znak = input('Введите знак(+ или -): ')
  if znak != '+' and znak != '-':
    print('Ошибка ввода!!!')
    continue
  num1 = int(input('Введите первое число: '))
  num2 = int(input('Введите второе число: '))
  if znak == '+':
    calc = num1 + num2
    print(num1, '+', num2, '=' , calc)
  elif znak == '-':
    calc = num1 - num2
    print(num1, '-', num2, '=', calc)