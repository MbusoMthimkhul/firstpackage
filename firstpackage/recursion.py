def sum_array(array):

    '''Return sum of all items in array

    Args:
        array (list): list with numerical values to sum

    return:
        int: sum of the terms in the list

    Examples:
        >>> sum_array([1,2,3,4,5,6])
        21
        >>> sum_array([1,2,3,4,5])
        15
        '''
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''Return n!

    Args:
        n (int): number to calculate it factorial

    Returns:
        int: factorial of n

    Examples:
        >>> factorial(1)
        1
        >>> factorial(4)
        24
        >>> factorial(3)
        6
    '''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def reverse(word):
    '''Return word in reverse
    Args:
        word (list): list to the sorted

    Returns:
        list: reverse sorted list

    Examples:
        >>> reverse('mbuso')
        'busom'
        >>> reverse('man')
        'nam'
        >>> reverse('female')
        'elamef'
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
