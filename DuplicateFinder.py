def find_duplicate(numbers):
    seen=set()
    duplicates=set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
            
        else:
            seen.add(num)
            
    return list(duplicates)


print(find_duplicate([1,2,3,4,5,6,9,4,2,6,8]))            