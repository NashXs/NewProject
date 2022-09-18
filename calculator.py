while True:
  X = input('\nВыберите операцию: ')
  if X == 'S':
    print('Выход из программы')
    break
  elif X == '+' or X == '-' or X == '*' or X == '/':
    A = int(input('Введите первое число: '))
    B = int(input('Введите второе число: '))
    if X == '+':
      C = A + B
    elif X == '-':
      C = A - B
    elif X == '*':
      C = A * B
    else:
      C = A / B
    print(A, X, B, '=', C)
  else:
    print('Ошибка: такой операции не существует. Попробуйте ещё раз.')