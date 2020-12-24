def bin_search(list, item):
    low = -1
    high = len(list)
    while(abs(high - low) >1):
        mid = (high + low) // 2
        guess = list[mid]
        if(guess >= item):
            high = mid
        else:
            low = mid
    return high

L = [1,3,5,7,9]
print(bin_search(L, 10))
print(bin_search(L, 3))