def basic_probability(p_a, p_b, p_a_and_b):
    """
    Returns: [p_union, p_a_complement, p_b_complement, p_a_and_not_b] as a list.
    """
    r = lambda x: round(x,4)
    p_union = r(p_a + p_b - p_a_and_b)

    p_a_complement = r(1 - p_a)
    p_b_complement = r(1 - p_b)

    p_a_and_not_b = r(p_a - p_a_and_b)

    return [p_union, p_a_complement, p_b_complement, p_a_and_not_b]