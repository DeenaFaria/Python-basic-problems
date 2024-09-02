def maxNumber(numbers):
    max=numbers[0]
    for num in numbers:
        if num>max:
            max=num
            
    return max

print(maxNumber([1,4,8,3,9,1,2]))        