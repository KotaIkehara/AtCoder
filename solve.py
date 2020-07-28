import sys


def checkSquare(self, n):
    seen = []
    for i in range(n):
        if self[i] in seen:
            return False
        else:
            seen.append(self[i])
    return True


def main():
    square = []  # input square
    n = 0  # num of row

    # read file
    f = open(sys.argv[1], "r")
    for line in f.readlines():
        square.append(line.rstrip("\n").split())
        n += 1
    f.close()

    # check square
    for i in range(n):
        if (not checkSquare(square[i], n)) or (
            not checkSquare([row[i] for row in square], n)
        ):
            print("invalid")
            return 0
    print("valid")
    return 0


main()
