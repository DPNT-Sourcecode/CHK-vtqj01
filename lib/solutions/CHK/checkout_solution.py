

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    countOfAs, countOfBs, countOfCs, countOfDs, countOfEs, countOfFs = [0, 0, 0, 0, 0, 0]
    totalAmountToPay = 0
    priceMap = {
        'A': {'SpecialOffer': 200, 'NormalOffer': 130, 'BasicPrice': 50},
        'B': {'NormalOffer': 45, 'BasicPrice': 30},
        'C': {'BasicPrice': 20},
        'D': {'BasicPrice': 15},
        'E': {'BasicPrice': 40},
        'F': {'BasicPrice': 10},
    }
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
            elif char == 'E':
                countOfEs = countOfEs + 1
            elif char == 'F':
                countOfFs = countOfFs + 1
            else:
                return -1

        if countOfAs:
            flagForSpecialOffer = False
            itemWithOutSpecialOffer = 0
            itemWithSpecialOfferOffer = 0
            if countOfAs >= 5:
                itemWithSpecialOfferOffer = int(countOfAs / 5)
                itemWithOutSpecialOffer = countOfAs % 5
                flagForSpecialOffer = True
            if flagForSpecialOffer:
                 countOfAs = itemWithOutSpecialOffer
            itemWithOffer = int(countOfAs / 3) if countOfAs >= 3 else 0
            itemWithOutOffer = countOfAs % 3
            totalAmountToPay = totalAmountToPay + itemWithSpecialOfferOffer * priceMap.get('A').get('SpecialOffer') + \
                               itemWithOffer * priceMap.get('A').get('NormalOffer') + itemWithOutOffer * priceMap.get('A').get('BasicPrice')
        if countOfCs:
            totalAmountToPay = totalAmountToPay + countOfCs * priceMap.get('C').get('BasicPrice')
        if countOfDs:
            totalAmountToPay = totalAmountToPay + countOfDs * priceMap.get('D').get('BasicPrice')
        if countOfEs:
            itemWithOfferE = int(countOfEs / 2) if countOfEs >= 2 else 0
            totalAmountToPay = totalAmountToPay + countOfEs * priceMap.get('E').get('BasicPrice')
            countOfBs = countOfBs - itemWithOfferE
        if countOfBs > 0:
            itemWithOffer = int(countOfBs / 2) if countOfBs >= 2 else 0
            itemWithOutOffer = countOfBs % 2
            totalAmountToPay = totalAmountToPay + itemWithOffer * priceMap.get('B').get('NormalOffer') + itemWithOutOffer * priceMap.get('B').get('BasicPrice')
        if countOfFs:
            itemWithOffer = int(countOfFs / 3) if countOfFs >= 3 else 0
            itemWithOutOffer = countOfBs % 3
            countOfFs = countOfFs - itemWithOffer
            totalAmountToPay = totalAmountToPay + countOfFs * priceMap.get('F').get('BasicPrice')

    return totalAmountToPay if totalAmountToPay else 0



