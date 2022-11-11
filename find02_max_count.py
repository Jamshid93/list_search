def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    m=data[0]
    for i in data:
        if i>m:
            m=i
    return data.count(m)
print(find_max_count([1,2,3,4,5,8,9,9,9]))
