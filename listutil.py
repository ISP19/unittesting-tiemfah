def unique(lst):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        lst: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    """
    if not isinstance(lst, list):
        raise TypeError("this function only take list")
    new_lst = []
    for stuff in lst:
        if stuff not in new_lst:
            new_lst.append(stuff)
    return new_lst

def average(lst):
    """Return an average of item in list 

    Arguments:
        lst: list object
    Returns:
        float of average

    Exmaples:
    >>> average([1, 1])
    1.0
    >>> average([])
    Traceback (most recent call last):
      ...
    ValueError
    >>> average([0])
    0.0
    """
    if not lst:
        raise ValueError
    if not isinstance(lst, list):
        raise TypeError
    else:
        return sum(lst)/len(lst)

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)