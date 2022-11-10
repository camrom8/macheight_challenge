from string import Template


def pairs_finder(addends_list: list, target: int) -> list:
    """This function finds pairs of integers from a list that sum to a given value
    Args:
        addends_list: the values to pair
        target: the result for the sum pairs
    Returns:
        A list of tuples with pairs of integers
    """

    # create a sort list by using tims sort algorithm O(log n)
    addends_list_sorted = sorted(addends_list)
    addends = []
    add_pair = addends.append
    # loop thorough ordered list and find pairs
    for n in addends_list_sorted:
        # find out if a pair number exists for n in list and
        # since list is ordered, the last number must be greater than pair.
        # if it is not, then is possible to discard it, and move to the previous one
        pair = target - n
        while  len(addends_list_sorted) > 1 and addends_list_sorted[-1] > pair:
            addends_list_sorted.pop()
        else:
            if pair == addends_list_sorted[-1] and pair != n: # avoid adding the same number
                add_pair((n, pair))
                addends_list_sorted.pop()
    return addends


if __name__ == '__main__':
    input_list = [1, 9, 5, 0, 20, -4, 12, 16, 7, 12]
    target = 12
    pairs = pairs_finder(input_list, target)
    template_output = Template('\t $index), $pair1, $pair2')
    print(f'the possible pairs for {target} from the list: {str(input_list)} are:')
    # [print("\t",f'{index, pair[0], "and", pair[1]) for index, pair in enumerate(pairs, start=1)]
    [print(template_output.substitute(index=index, pair1=pair[0], pair2=pair[1]))
     for index, pair in enumerate(pairs, start=1)]