

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
        if countOfAs:
            itemWithOffer = countOfAs / 3
            itemWithOutOffer = countOfAs % 3
            totalAmountToPay = itemWithOffer * 130 + itemWithOutOffer * 50
        if countOfBs:
            itemWithOffer = countOfBs / 3
            itemWithOutOffer = countOfBs % 3
            totalAmountToPay = itemWithOffer * 130 + itemWithOutOffer * 50
        if countOfCs:
            itemWithOffer = countOfCs / 3
            itemWithOutOffer = countOfCs % 3
            totalAmountToPay = itemWithOffer * 130 + itemWithOutOffer * 50
        if countOfDs:
            itemWithOffer = countOfDs / 3
            itemWithOutOffer = countOfDs % 3
            totalAmountToPay = itemWithOffer * 130 + itemWithOutOffer * 50

        return totalAmountToPay

    return -1







