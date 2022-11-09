def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    m=data[0]
    for i in data:
        if i>m:
            m=i
    return m
print(find_max([1,2,3,4,5]))
    