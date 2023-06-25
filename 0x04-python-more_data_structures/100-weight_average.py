#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculates the weighted average of a list of integer tuples.

    Args:
        my_list (list): List of integer tuples in the format (<score>, <weight>).

    Returns:
        float: Weighted average of the scores.
    """
    if len(my_list) == 0:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    weighted_average = total_score / total_weight
    return weighted_average
