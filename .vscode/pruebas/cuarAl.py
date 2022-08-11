'''
    target=6
    list = [3,2,4]
           v 
        [3,2,4]
         0 1 2

    for i in 3 
        for j in range (i + 1, 3)
        i = 1
        j = 2
        if list[j] == target - list[i]
        if 4 == 6 - 2   
            return [i, j]
'''



def twoSum(list,target):
    for i in range(len(list)):
        for j in range ( i + 1, len(list)):
            print(j)
            print(i)
            print(':',list[j])
            if list[j] == target - list[i]: 
                return [i,j]


nums = [3,2,4]
target = 6
print(twoSum(nums,target))
