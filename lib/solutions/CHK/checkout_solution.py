# Dictionary with all the price mapping of items
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
        'K': {'NormalOffer': 120, 'BasicPrice': 70},
        'L': {'BasicPrice': 90},
        'M': {'BasicPrice': 15},
        'N': {'BasicPrice': 40},
        'O': {'BasicPrice': 10},
        'P': {'NormalOffer': 200, 'BasicPrice': 50},
        'Q': {'NormalOffer': 80, 'BasicPrice': 30},
        'R': {'BasicPrice': 50},
        'S': {'BasicPrice': 20},
        'T': {'BasicPrice': 20},
        'U': {'BasicPrice': 40},
        'V': {'SpecialOffer': 130, 'NormalOffer': 90, 'BasicPrice': 50},
        'W': {'BasicPrice': 20},
        'X': {'BasicPrice': 17},
        'Y': {'BasicPrice': 20},
        'Z': {'BasicPrice': 21},
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    totalAmountToPay = 0
    if skus:
        countMap = {}

        # create map of items count
        for char in skus:
            if char in priceMap.keys():
                if countMap.get(char):
                    countMap[char] = countMap[char] + 1
                else:
                    countMap[char] = 1
            else:
                return -1

        # apply special offer logic
        for key in countMap.keys():
            if key == 'E':
                count = countMap[key]
                itemWithOfferE = int(count / 2)
                if countMap.get('B'):
                    countMap['B'] = countMap['B'] - itemWithOfferE

            if key == 'N':
                count = countMap[key]
                itemWithOfferE = int(count / 3)
                if countMap.get('M'):
                    countMap['M'] = countMap['M'] - itemWithOfferE

            if key == 'R':
                count = countMap[key]
                itemWithOfferE = int(count / 3)
                if countMap.get('Q'):
                    countMap['Q'] = countMap['Q'] - itemWithOfferE

        # apply normal offer logic and calculate total amount of items.
        groupSpecialLogicCount = 0
        for key in countMap.keys():
            count = countMap[key]
            basicPrice = priceMap[key]['BasicPrice']
            normalOfferPrice = priceMap[key].get('NormalOffer')
            specialOfferPrice = priceMap[key].get('SpecialOffer')
            if key in ['A', 'B', 'F', 'H', 'K', 'P', 'Q', 'U', 'V']:
                if key == 'A':
                    flagForSpecialOffer = False
                    itemWithOutSpecialOffer = 0
                    itemWithSpecialOfferOffer = 0
                    if count >= 5:
                        itemWithSpecialOfferOffer = int(count / 5)
                        itemWithOutSpecialOffer = count % 5
                        flagForSpecialOffer = True
                    if flagForSpecialOffer:
                         count = itemWithOutSpecialOffer
                    itemWithOffer = int(count / 3)
                    itemWithOutOffer = count % 3
                    totalAmountToPay = totalAmountToPay + itemWithSpecialOfferOffer * specialOfferPrice + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key in ['B', 'K'] and count > 0:
                    itemWithOffer = int(count / 2)
                    itemWithOutOffer = count % 2
                    totalAmountToPay = totalAmountToPay + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key == 'F':
                    itemWithOffer = int(count / 3)
                    itemWithOutOffer = count % 3
                    totalAmountToPay = totalAmountToPay + itemWithOffer * 2 * basicPrice + itemWithOutOffer * basicPrice
                if key == 'U':
                    itemWithOffer = int(count / 4)
                    itemWithOutOffer = count % 4
                    totalAmountToPay = totalAmountToPay + itemWithOffer * 3 * basicPrice + itemWithOutOffer * basicPrice
                if key == 'P':
                    itemWithOffer = int(count / 5)
                    itemWithOutOffer = count % 5
                    totalAmountToPay = totalAmountToPay + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key == 'Q':
                    itemWithOffer = int(count / 3)
                    itemWithOutOffer = count % 3
                    totalAmountToPay = totalAmountToPay + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key == 'H':
                    flagForSpecialOffer = False
                    itemWithOutSpecialOffer = 0
                    itemWithSpecialOfferOffer = 0
                    if count >= 10:
                        itemWithSpecialOfferOffer = int(count / 10)
                        itemWithOutSpecialOffer = count % 10
                        flagForSpecialOffer = True
                    if flagForSpecialOffer:
                         count = itemWithOutSpecialOffer
                    itemWithOffer = int(count / 5) if count >= 5 else 0
                    itemWithOutOffer = count % 5
                    totalAmountToPay = totalAmountToPay + itemWithSpecialOfferOffer * specialOfferPrice + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key == 'V':
                    flagForSpecialOffer = False
                    itemWithOutSpecialOffer = 0
                    itemWithSpecialOfferOffer = 0
                    if count >= 3:
                        itemWithSpecialOfferOffer = int(count / 3)
                        itemWithOutSpecialOffer = count % 3
                        flagForSpecialOffer = True
                    if flagForSpecialOffer:
                        count = itemWithOutSpecialOffer
                    itemWithOffer = int(count / 2) if count >= 2 else 0
                    itemWithOutOffer = count % 2
                    totalAmountToPay = totalAmountToPay + itemWithSpecialOfferOffer * specialOfferPrice + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
            else:
                if countMap[key] > 0:
                    if key in ['S', 'T', 'X', 'Y', 'Z']:
                        groupSpecialLogicCount = groupSpecialLogicCount + count
                    else:
                        totalAmountToPay = totalAmountToPay + countMap[key] * basicPrice

        itemWithOffer = int(groupSpecialLogicCount / 3)
        itemWithOutOffer = groupSpecialLogicCount % 3
        avgPrice = 0
        if itemWithOutOffer == 2:
            if countMap.get('X'):
                if countMap.get('X') == 2:
                    avgPrice = priceMap['X']['BasicPrice']
                else:
                    price1 = priceMap['X']['BasicPrice']
                    if any(countMap.get('S'), countMap.get('T'), countMap.get('Y')):
                        price2 = priceMap['S']['BasicPrice']
                    avgPrice = (price1 + price2) / 2
            elif any(countMap.get('S'), countMap.get('T'), countMap.get('Y')):
                if (
                        (countMap.get('S') and countMap.get('T')) or
                        (countMap.get('S') and countMap.get('Y')) or
                        (countMap.get('T') and countMap.get('Y'))
                ):
                    avgPrice = priceMap['S']['BasicPrice']
                else:
                    price1 = priceMap['S']['BasicPrice']
                    price2 = priceMap['Z']['BasicPrice']
                    avgPrice = (price1 + price2) / 2
            else:
                avgPrice = priceMap['Z']['BasicPrice']

        elif itemWithOutOffer == 1:
             avgPrice = countMap.get('X') or countMap.get('S') or countMap.get('T') or countMap.get('Y') or countMap.get('Z')

        totalAmountToPay = totalAmountToPay = totalAmountToPay + itemWithOffer * 45 + itemWithOutOffer * avgPrice

    return totalAmountToPay if totalAmountToPay else 0






