from random import randint
import numpy as np


height = 0
width = 0

mines_locations = []
field = []
STATUS = True


def get_number(a, b, text: str) -> int:
    while True:
        number = int(input(text))
        if a <= number <= b:
            break
        else:
            print("Podaj liczbę z zakresu")

    return number


def lay_mines(height, width):
    mines_amount = get_number(10, (height - 1) * (width - 1), "Podaj liczbę min: ")
    result = []
    for i in range(mines_amount):
        while True:
            x = randint(0, height - 1)
            y = randint(0, width - 1)
            cords = (x, y)
            if cords not in result:
                result.append(cords)
                break

    return result


def number_of_neighboring_mines(x: int, y: int) -> int:
    number_of_mines = 0
    for (x_cord, y_cord) in mines_locations:
        if abs(x - x_cord) <= 1 and abs(y - y_cord) <= 1:
            number_of_mines += 1
        if abs(x - x_cord) == 0 and abs(y - y_cord) == 0:
            return 9

    return number_of_mines


def create_board():
    global height, width
    height = get_number(8, 30, "Podaj wysokość: ")
    width = get_number(8, 24, "Podaj szerokość: ")
    global mines_locations
    mines_locations = lay_mines(height, width)
    global field
    field = np.zeros((height, width))
    for x in range(height):
        for y in range(width):
            field[x][y] = number_of_neighboring_mines(x, y)

    return field


def reveal_fields(x, y):
    if 0 <= x <= height - 1 and 0 <= y <= width - 1:
        if field[x][y] == 9:
            global STATUS
            STATUS = False
        if field[x][y] <= 9:
            if field[x][y] == 0:
                field[x][y] += 10
                reveal_fields(x - 1, y - 1)
                reveal_fields(x - 1, y)
                reveal_fields(x - 1, y + 1)
                reveal_fields(x, y - 1)
                reveal_fields(x, y + 1)
                reveal_fields(x + 1, y - 1)
                reveal_fields(x + 1, y)
                reveal_fields(x + 1, y + 1)
            else:
                field[x][y] += 10

# 🟦🟦💣💣💣🟥🟥🟥
# 1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣


def print_board():
    text = "y\\x 0 1 2 3 4  5 6 7 8 9\n"
    i = 0
    for x in field:
        text += str(i) + "  "
        i += 1
        for y in x:
            if y < 10:
                text += "🟥"
            elif y == 10 or y == 20:
                text += "🟦"
            elif y == 11 or y == 21:
                text += "1️⃣"
            elif y == 12 or y == 22:
                text += "2️⃣"
            elif y == 13 or y == 23:
                text += "3️⃣"
            elif y == 14 or y == 24:
                text += "4️⃣"
            elif y == 15 or y == 25:
                text += "5️⃣"
            elif y == 16 or y == 26:
                text += "6️⃣"
            elif y == 17 or y == 27:
                text += "7️⃣"
            elif y == 18 or y == 28:
                text += "8️⃣"
            elif y == 19 or y == 29:
                text += "💣"
        text += "\n"
    print(text)


if __name__ == '__main__':

    print(create_board())
    print(number_of_neighboring_mines(0, 0))
    print_board()
    while True:
        if not STATUS:
            print("BOOOM! Przegrales!")
            field += 10
            print_board()
            break
        x1 = int(input("x: "))
        y1 = int(input("y: "))
        reveal_fields(x1, y1)
        print_board()
