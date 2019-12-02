#every time move the shorter, then the bigger pair can only appear in that place
def find_max_water(building_heights):
    left,right = 0,len(building_heights)-1
    water_max =0
    while right>left:
        short = min(building_heights[left],building_heights[right])
        water_max = max(short*(right-left+1),water_max)
        if building_heights[left]<=building_heights[right]:
            left+=1
        else:
            right-=1
    return water_max
