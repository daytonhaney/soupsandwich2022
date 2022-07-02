__name__: = __JasonPreneveau__



def bin_search(list,item):

    low = 0
    high = len(list) -1
    
    while low <= high:
        mid = (low + high ) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            return mid - 1
        else:
                high = mid -1
        



