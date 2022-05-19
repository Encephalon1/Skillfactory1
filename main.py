def greet():
    print('Приветствую в игре крестики-нолики!')
    print('Вводить 2 координаты x и y, от 0 до 2,')
    print('где х - это номер строки,')
    print('а y - номер столбца.')


greet()

field = [[' ']*3 for i in range(3)]


def show():
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i, row in enumerate(field):
        row1 = f"{i} | {' | '.join(row)} |"
        print(row1)
        print('---------------')


show()


def ask():
    while True:
        coords = input('  Ваш ход: ').split()
        x, y = coords
        if not x.isdigit() or not y.isdigit():
            print('Нужно ввести 2 числа!')
            continue
        if len(coords) != 2:
            print('Введите 2 числа!')
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Координаты за пределами диапазона!')
            continue
        if field[x][y] != ' ':
            print('Клетка занята!')
            continue

        return x, y


def win():
    vict = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
            ((0, 1), (1, 1), (2, 1)), ((0, 0), (1, 0), (2, 0)), ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for cord in vict:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != ' ':
            print(f'Выиграл {field[a[0]][a[1]]}')
            return True
    return False


num = 0
while True:
    num += 1
    if num % 2 == 1:
        print('Ходит Х')
    else:
        print('Ходит 0')
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'
    show()
    if win():
        break
    if num == 9:
        print('Ничья!')
        break
