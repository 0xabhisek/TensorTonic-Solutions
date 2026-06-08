from math import factorial, perm, comb

def perms_and_combs(n, r):
    """
    Returns: [permutations, combinations, factorial] as a list.
    """
    return [math.perm(n,r), math.comb(n,r),math.factorial(n)]