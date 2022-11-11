def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    odd=[]
    for i in data:
        if i%2!=0:
            odd.append(i)
        
    max_odd=odd[0]
    for i in odd:
        if i>max_odd:
            max_odd=i
    return max_odd
print(find_max_odd([1, 8, 3, 8, 5]))