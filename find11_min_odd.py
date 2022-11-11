def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    odd=[]
    for i in data:
        if i%2!=0:
            odd.append(i)
        
    min_odd=odd[0]
    for i in odd:
        if i<min_odd:
            min_odd=i
    return min_odd
print(find_min_odd([7, 8, 4, 3, 5]))

