def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    even=[]
    for i in data:
        if i%2==0:
            even.append(i)
        
    min_even=even[0]
    for i in even:
        if i<min_even:
            min_even=i
    return min_even
print(find_min_even([1, 8, 2, 8, 5]))

