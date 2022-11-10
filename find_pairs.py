def pairs_finder(addends_list: list, target: int) -> list:
    """This function finds pairs of integers from a list that sum to a given value
    Args:
        addends_list: the values to pair
        target: the result for the sum pairs
    Returns:
        A list of tuples with pairs of integers
    """

    # sort list by using tims sort algorithm O(log n)
    addends_list.sort()
    addends = []
    add_pair = addends.append
    # loop thorough ordered list and find pairs
    for n in addends_list:
        pair = target - n
        # find out if pair for n exists in list and
        # since list is ordered, the last element must be greater than pair.
        # if it is not, then is possible to discard it
        while  len(addends_list) > 1 and addends_list[-1] > pair:
            addends_list.pop()
        else:
            if pair == addends_list[-1]:
                if pair != n:
                    add_pair((n, pair))
                    addends_list.pop()
    return addends


if __name__ == '__main__':
    input_list = [1, 9, 5, 0, 20, -4, 12, 16, 7, 12]
    target = 12
    pairs = pairs_finder(input_list.copy(), target)
    print(f'the possible pairs for {target} from the list: {str(input_list)} are:\n{pairs}')