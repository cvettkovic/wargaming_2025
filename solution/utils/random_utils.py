import random
import utils.constants as constants


def get_random_number(min_inclusive=constants.MIN_RANDOM_NUMBER,
                      max_inclusive=constants.MAX_RANDOM_NUMBER):
    """
    Return a random integer from the range provided.
    
    :param min_inclusive: Inclusive lower range bound 
    (default: MIN_RANDOM_NUMBER from utils.constants).
    :param max_inclusive: Inclusive upper range bound 
    (default: MAX_RANDOM_NUMBER from utils.constants).
    """
    return random.randint(min_inclusive, max_inclusive)


def change_random_integer_and_move_first_element(tuple_):
    """
    Return tuple that has random non-first element set to a random allowed 
    value, and move first element to the end.
    
    :param tuple_: Tuple with the original data.
    """
    tuple_length = len(tuple_)
    last_index_in_tuple = tuple_length - 1
    # Find randomly which element to change (except first one)
    index_to_change = get_random_number(min_inclusive=1,
                                        max_inclusive=last_index_in_tuple)
    
    # Change index element to random number and add first element from tuple
    values = list(tuple_[1:])
    values[index_to_change - 1] = get_random_number()
    values.append(tuple_[0])
    
    return tuple(values)

