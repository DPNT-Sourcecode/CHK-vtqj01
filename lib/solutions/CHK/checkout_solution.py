

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    countOfAs, countOfBs, countOfCs, countOfDs = [0, 0, 0, 0]
    if skus:
        for char in skus:
            if char == 'A':
                countOfAs = countOfAs + 1
            elif char == 'B':
                countOfBs = countOfBs + 1
            elif char == 'C':
                countOfCs = countOfCs + 1
            elif char == 'D':
                countOfDs = countOfDs + 1
            else:
                return -1
        itemCount = {'A': countOfAs, 'B': countOfBs, 'C': countOfCs, 'D': countOfDs}
        totalAmountToPay = 0
        if countOfAs:
            itemWithOffer = countOfAs / 3
            itemWithOutOffer = countOfAs % 3
            totalAmountToPay = itemWithOffer * 130 + itemWithOutOffer * 50
        if countOfBs:
            itemWithOffer = countOfBs / 2
            itemWithOutOffer = countOfBs % 2
            totalAmountToPay = itemWithOffer * 45 + itemWithOutOffer * 30
        if countOfCs:
            totalAmountToPay = countOfCs * 20
        if countOfDs:
            totalAmountToPay = countOfDs * 15

        return totalAmountToPay

    return -1



