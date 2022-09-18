while True:
    while True:
        operations = input("\nВыберите операцию: ")
        if operations in "+":
            break
        elif operations in '-':
            break
        elif operations in '*':
            break
        elif operations in '/':
            break
        else:
            print("Ошибка: такой операции не существует. Попробуйте ещё раз.")

    quantity = int(input('\nСколько чисел в операции? '))
    print('\nВведите число № 1: ', end='')
    numb = int(input(''))
    result = numb
    symbol = str(numb)
    answer = ''

    for step in range(1, quantity):
        print('\nВведите число №', str(step + 1) + ': ', end='')
        numb = int(input(''))

        if operations == '+':
            result += numb
        elif operations == '-':
            result -= numb
        elif operations == '*':
            result *= numb
        else:
            result /= numb

        symbol += ' ' + operations + ' ' + str(numb)

    print('\n', symbol + ' =', result)

    continuation = int(input('\nПродолжаем? 1 - Да, 2 - Нет : '))
    if continuation == 2:
        print('Выход')
        break

#test git
