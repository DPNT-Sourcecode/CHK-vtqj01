

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
        'G': {'BasicPrice': 20},
        'H': {'SpecialOffer': 80, 'NormalOffer': 45, 'BasicPrice': 10},
        'I': {'BasicPrice': 35},
        'J': {'BasicPrice': 60},
        'K': {'NormalOffer': 150, 'BasicPrice': 80},
        'L': {'BasicPrice': 90},
        'M': {'BasicPrice': 15},
        'N': {'BasicPrice': 40},
        'O': {'BasicPrice': 10},
        'P': {'NormalOffer': 200, 'BasicPrice': 50},
        'Q': {'NormalOffer': 80, 'BasicPrice': 30},
        'R': {'BasicPrice': 50},
        'S': {'BasicPrice': 30},
        'T': {'BasicPrice': 20},
        'U': {'BasicPrice': 40},
        'V': {'SpecialOffer': 130, 'NormalOffer': 90, 'BasicPrice': 50},
        'W': {'BasicPrice': 20},
        'X': {'BasicPrice': 90},
        'Y': {'BasicPrice': 10},
        'Z': {'BasicPrice': 50},
    }
    if skus:
        countMap = {}
        for char in skus:
            if char in priceMap.keys():
                if countMap.get(char):
                    countMap[char] = countMap[char] + 1
                else:
                    countMap[char] = 1
            else:
                return -1

        for key in countMap.keys():
            if key == 'A':
                countOfAs = countMap[key]
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
                itemWithOutOffer = countOfFs % 3
                # countOfFs = countOfFs - itemWithOffer
                totalAmountToPay = totalAmountToPay + itemWithOffer * 2 * priceMap.get('F').get('BasicPrice') + itemWithOutOffer * priceMap.get('F').get('BasicPrice')

    return totalAmountToPay if totalAmountToPay else 0


