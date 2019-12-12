#keep a minHeap with size of K2
#repeatly to get the sum
def rearrange_string(str):
    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char,0)+1