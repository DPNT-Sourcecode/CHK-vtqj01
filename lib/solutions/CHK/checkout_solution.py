
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

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    totalAmountToPay = 0
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
            if key == 'E':
                count = countMap[key]
                itemWithOfferE = int(count / 2) if count >= 2 else 0
                if countMap.get('B'):
                    countMap['B'] = countMap['B'] - itemWithOfferE

            if key == 'N':
                count = countMap[key]
                itemWithOfferE = int(count / 3) if count >= 3 else 0
                if countMap.get('M'):
                    countMap['M'] = countMap['M'] - itemWithOfferE

            if key == 'R':
                count = countMap[key]
                itemWithOfferE = int(count / 3) if count >= 3 else 0
                if countMap.get('Q'):
                    countMap['Q'] = countMap['Q'] - itemWithOfferE

        for key in countMap.keys():
            count = countMap[key]
            basicPrice = priceMap[key]['BasicPrice']
            normalOfferPrice = priceMap[key].get('NormalOffer')
            specialOfferPrice = priceMap[key].get('SpecialOffer')
            if key in ['A', 'B', 'F', 'H', 'K', 'P', 'Q', 'V']:
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
                    itemWithOffer = int(count / 3) if count >= 3 else 0
                    itemWithOutOffer = count % 3
                    totalAmountToPay = totalAmountToPay + itemWithSpecialOfferOffer * specialOfferPrice + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key in ['B', 'K'] and count > 0:
                    itemWithOffer = int(count / 2) if count >= 2 else 0
                    itemWithOutOffer = count % 2
                    totalAmountToPay = totalAmountToPay + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key == 'F':
                    itemWithOffer = int(count / 3) if count >= 3 else 0
                    itemWithOutOffer = count % 3
                    totalAmountToPay = totalAmountToPay + itemWithOffer * 2 * basicPrice + itemWithOutOffer * basicPrice
                if key == 'P':
                    itemWithOffer = int(count / 5) if count >= 5 else 0
                    itemWithOutOffer = count % 5
                    totalAmountToPay = totalAmountToPay + itemWithOffer * normalOfferPrice + itemWithOutOffer * basicPrice
                if key == 'Q':
                    itemWithOffer = int(count / 3) if count >= 3 else 0
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
                    if count >= 5:
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
                    totalAmountToPay = totalAmountToPay + countMap[key] * basicPrice

    return totalAmountToPay if totalAmountToPay else 0



