

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    countOfAs, countOfBs, countOfCs, countOfDs = 0
    if skus:
        for char in skus:
            if skus == 'A':
                countOfAs = countOfAs + 1
            elif skus == 'B':
                countOfBs = countOfBs + 1
            elif skus == 'C':
                countOfCs = countOfCs + 1
            elif skus == 'D':
                countOfDs = countOfDs + 1
            else:
                return -1
        itemCount = {'A': countOfAs, 'B': countOfBs, 'C': countOfCs, 'D': countOfDs}
        totalAmountToPay = 0
        for item in itemCount.keys():
            if item == 'A':
                if itemCount[itemCount] >

    return -1





