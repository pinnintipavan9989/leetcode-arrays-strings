def twoSum(numbers, target):
    p1,p2 =0,len(numbers)-1

    while p1<p2:
        sum = numbers[p1]+numbers[p2]

        if sum == target:
            return[p1+1, p2+1]
        elif sum > target:
            p2 -=1
        else:
            p1 +=1          