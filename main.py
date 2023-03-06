import minesweeper as ms


def sapper():
    ms.create_board()
    ms.print_board()
    while True:
        if not ms.STATUS:
            print("BOOOM! Przegrales!")
            ms.field += 10
            ms.print_board()
            break
        x = int(input("x: "))
        y = int(input("y: "))
        ms.reveal_fields(x, y)
        ms.print_board()


if __name__ == '__main__':
    sapper()
