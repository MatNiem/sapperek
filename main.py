import minesweeper as ms


def sapper():
    ms.create_board()
    ms.print_board()
    while True:
        check = True
        for x in ms.field:
            for y in x:
                if y < 9:
                    check = False
        if check:
            print("Wygrales!")
            ms.print_board()
            break
        if not ms.STATUS:
            print("BOOOM! Przegrales!")
            ms.field += 10
            ms.print_board()
            break
        x = int(input("x: "))
        y = int(input("y: "))
        ms.reveal_fields(y, x)
        ms.print_board()


if __name__ == '__main__':
    sapper()
