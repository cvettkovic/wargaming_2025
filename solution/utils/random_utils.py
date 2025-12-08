import random
import constants


def get_random_number(min_inclusive=constants.MIN_RANDOM_NUMBER,
                      max_inclusive=constants.MAX_RANDOM_NUMBER):
    return random.randint(min_inclusive, max_inclusive)


def change_non_first_element_to_random(tuple_):
    tuple_length = len(tuple_)
    last_index_in_tuple = tuple_length - 1
    index_to_change = get_random_number(min_inclusive=1,
                                        max_inclusive=last_index_in_tuple)

    values = []
    for i in range(0, tuple_length):
        if i == index_to_change:
            values.append(get_random_number())
        else:
            values.append(tuple_[i])
    
    return tuple(values)

