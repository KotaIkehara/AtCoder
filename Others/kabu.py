import sys


def main():
    # read file
    f = open(sys.argv[1], "r")
    for line in f.readlines():
        prices = list(map(int, line.split()))
    f.close()

    currentMax = 0
    maxSoFar = 0
    for i in range(1, len(prices)):
        prevCurrentMax = currentMax
        currentMax = max(0, currentMax + prices[i] - prices[i - 1])
        prevMaxSoFar = maxSoFar
        maxSoFar = max(currentMax, maxSoFar)

        if prevCurrentMax == 0:
            buyPrice = prices[i - 1]
        if maxSoFar != prevMaxSoFar:
            sellPrice = prices[i]

    print("buy", buyPrice, ", sell", sellPrice)
    return 0


main()
