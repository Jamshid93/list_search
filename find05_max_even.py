def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    even=[]
    for i in data:
        if i%2==0:
            even.append(i)
        
    max_even=even[0]
    for i in even:
        if i>max_even:
            max_even=i
    return max_even
print(find_max_even([7, 6, 3, 4, 9]))
