from typing import List

"""
[ 2, 3, 5, 1, 1 ]
[ 2, 3, 5, 5, 1, 1, 1 ]

"""

def brickSort(arr: List[int]):
    maxNum = {"highest_index":0, "lowest_index":0, "value":arr[0]}
    minNum = {"highest_index":0, "lowest_index":0, "value":arr[0]}
    num_of_bricks_added = 0

    pivot = 0

    for index in range(len(arr)):
        value = arr[index]

        if value == maxNum["value"]: 
            if index > maxNum["highest_index"]:
                maxNum["highest_index"] = index
        if value == minNum["value"]: 
            if index > minNum["highest_index"]:
                minNum["highest_index"] = index

        if value > maxNum["value"]:
            maxNum["value"] = value
            maxNum["highest_index"] = maxNum["lowest_index"] = index 
        if value < minNum["value"]:
            minNum["value"] = value
            minNum["highest_index"] = minNum["lowest_index"] = index 

    hh = abs(minNum["highest_index"] - maxNum["highest_index"])
    ll = abs(minNum["lowest_index"] - maxNum["lowest_index"])

    if ll <= hh:
        is_decreasing = True
        pivot = maxNum["highest_index"]
        temp = pivot
        count = -1 

        for index in range(pivot+1, len(arr)):
            if count == 0:
                break
            count = arr[temp] - arr[index] - 1
            if count < 0:
                count = 0
            num_of_bricks_added += count
            arr[index] += count
            temp = index

        temp = len(arr)-1
        for index in range(len(arr)-2, -1, -1):
            count = arr[temp] + 1 - arr[index]  
            if count <= 0:
                count = 0
            num_of_bricks_added += count
            arr[index] += count
            temp = index
    else:
        
        pivot = maxNum["lowest_index"]
        temp = pivot
        count = -1 
        for index in range(pivot-1, -1, -1):
            if count == 0:
                break
            count = arr[temp] - arr[index] - 1
            if count < 0:
                count = 0
            num_of_bricks_added += count
            arr[index] += count
            temp = index

        temp = 0
        for index in range(1, len(arr)):
            count = arr[temp] + 1 - arr[index]  
            if count <= 0:
                count = 0
            num_of_bricks_added += count
            arr[index] += count
            temp = index

    print(f"num_of_bricks_added is {num_of_bricks_added}")

    return arr

print(brickSort([5, 1, 1, 5, 1, 1, 1]))
