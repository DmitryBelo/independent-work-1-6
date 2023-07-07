def fib():
    fib1 = fib2 = 1
    popravka = 0
    
    n =  int(input('Введите уровень игрока: '))
    if 7 > n > 1:
        popravka = 1
    n = n - 2
    
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2 + popravka
print('Убитых монстров 1-го уровня: ', fib())