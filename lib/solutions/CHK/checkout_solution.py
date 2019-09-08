

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    countOfAs, countOfBs, countOfCs, countOfDs = [0, 0, 0, 0]
    totalAmountToPay = 0
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

        if countOfAs:
            itemWithOutOffer1 = 0
            if countOfAs >= 5:
                itemWithOffer1 = int(countOfAs / 5)
                itemWithOutOffer1 = countOfAs % 5
            if itemWithOutOffer1:
                 countOfAs = itemWithOutOffer1
            itemWithOffer = int(countOfAs / 3) if countOfAs >= 3 else 0
            itemWithOutOffer = countOfAs % 3
            totalAmountToPay = totalAmountToPay + itemWithOffer1 * 200 + itemWithOffer * 130 + itemWithOutOffer * 50
        if countOfBs:
            itemWithOffer = int(countOfBs / 2) if countOfBs >= 2 else 0
            itemWithOutOffer = countOfBs % 2
            totalAmountToPay = totalAmountToPay + itemWithOffer * 45 + itemWithOutOffer * 30
        if countOfCs:
            totalAmountToPay = totalAmountToPay + countOfCs * 20
        if countOfDs:
            totalAmountToPay = totalAmountToPay + countOfDs * 15

    return totalAmountToPay if totalAmountToPay else 0


