

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    countOfAs, countOfBs, countOfCs, countOfDs = 0
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
            return
    countDict = {'A': countOfAs, 'B': countOfBs, 'C': countOfCs, 'D': countOfDs}



