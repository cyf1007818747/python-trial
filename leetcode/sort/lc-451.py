# frequency bucket solution
# passed all leetcode tests
def frequencySort_bucket(s: str) -> str:
    max_frequency = 0
    frequency_map = {}
    for c in s:
        frequency_map[c] = frequency_map.get(c, 0) + 1 # *
        max_frequency = max(max_frequency, frequency_map[c])
    
    # * all [] share the same memory thus wrong
    # frequency_bucket = [[]] * (max_frequency + 1) 
    
    frequency_bucket = [[] for _ in range(max_frequency + 1)] # *

    # print("---- frequency_map: ", frequency_map)
    
    for c, f in frequency_map.items(): # *
        frequency_bucket[f].append(c)

    # print("---- frequency_bucket: ", frequency_bucket)

    final_str = ""

    for i in range(max_frequency, -1, -1): # *
        for c in frequency_bucket[i]:
            final_str += c * i

    return final_str

# frequency sort approach
def frequencySort_sort(s: str) -> str:
    frequency_map = {}
    for c in s:
        frequency_map[c] = frequency_map.get(c, 0) + 1
    
    frequency_array = []
    for c, f in frequency_map.items():
        frequency_array.append([c, f])

    frequency_array.sort(key=lambda arr: arr[1], reverse=True) # *
    
    output_str = ""

    for arr in frequency_array:
        output_str += arr[0] * arr[1]

    return output_str


testStr = "acacac"
output = frequencySort_sort(testStr)
print("#### output: ", output)


    
    
