from typing import List

# initial solution
def canPlaceFlowersInitial(flowerbed: List[int], n: int) -> bool:
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

# improve code style
def canPlaceFlowersInitialBetterStyle(flowerbed: List[int], n: int) -> bool:
    # > do not have to insert
    if n == 0:
        return True
    
    # > flowerbed has only 1 element
    if len(flowerbed) == 1:
        # >> element is 0
        if flowerbed[0] == 0:
            return n <= 1
        # >> else case :: element is 1
        return n == 0
    
    # > else case :: flowerbed has 2 or more elements

    # >> check first position
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1

    # >> check middle elements except first and last
    for i in range(1, len(flowerbed) - 1):
        # only when the left and right of a 0 are also 0 can we plant
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            # print('3 consecutive flowers at {}: {}, {}, {}'.format(i, flowerbed[i-1], flowerbed[i], flowerbed[i+1]))
            # print('flower inserted at index {}'.format(i))
            flowerbed[i] = 1
            n -= 1
            # can immediately return if no more flower to plant
            if n <= 0:
                return True

    
    # >> check the last element
    if flowerbed[-2] == 0 and flowerbed[-1] == 0:
        flowerbed[-1] = 1
        n -= 1

    return n <= 0
    
testFlowerbed = [1,0,0,0,0,1]
n = 2
output = canPlaceFlowersInitialBetterStyle(testFlowerbed, n)
print('######## output: ', output)

    