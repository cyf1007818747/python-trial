# frequency bucket solution
# passed all leetcode tests
def frequencySort(s: str) -> str:
    max_frequency = 0
    frequency_map = {}
    for c in s:
        frequency_map[c] = frequency_map.get(c, 0) + 1 # *
        max_frequency = max(max_frequency, frequency_map[c])
    
    # * all [] share the same memory thus wrong
    # frequency_array = [[]] * (max_frequency + 1) 
    
    frequency_array = [[] for _ in range(max_frequency + 1)] # *

    # print("---- frequency_map: ", frequency_map)
    
    for c, f in frequency_map.items(): # *
        frequency_array[f].append(c)

    # print("---- frequency_array: ", frequency_array)

    final_str = ""

    for i in range(max_frequency, -1, -1): # *
        for c in frequency_array[i]:
            final_str += c * i

    return final_str

testStr = "acacac"
output = frequencySort(testStr)
print("#### output: ", output)


    
    
