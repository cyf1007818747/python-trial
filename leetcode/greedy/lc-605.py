from typing import List

# original solution
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    # do not have to insert any
    if n == 0:
        return True
    
    # only one element in flowerbed
    #   element is 0: n <= 1 => true else false
    #   element is 1: n == 0 => true else false
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            return True if n <= 1 else False
        return True if n == 0 else False

    flowerbedfilled = flowerbed.copy()

    # check first position
    if flowerbedfilled[0] == 0 and flowerbedfilled[1] == 0:
        flowerbedfilled[0] = 1
        n -= 1

    idx = 1
    while idx < len(flowerbed) - 1 and n > 0:
        # cannot plant if already planted
        if flowerbedfilled[idx] == 1:
            idx += 1
            continue
        
        # @assert: flowerbedfilled[idx] == 0
        if flowerbedfilled[idx - 1] == 1 or flowerbedfilled[idx + 1] == 1:
            idx += 1
            continue

        # @assert: flowerbedfilled[idx - 1] == 0  
        # @assert: flowerbedfilled[idx] == 0
        # @assert: flowerbedfilled[idx + 1] == 0
        flowerbedfilled[idx] = 1
        n -= 1
        idx += 2

        # early return if no more flower to plant
        if n <= 0:
            return True
    
    # deal with last potision
    if flowerbedfilled[-2] == 0 and flowerbedfilled[-1] == 0:
        flowerbedfilled[-1] = 1
        n -= 1

    return True if n <= 0 else False