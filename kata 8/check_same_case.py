def same_case(a, b): 
    if not a.isalpha() or not b.isalpha():
        return -1
    whatA = a.islower()
    whatB = b.islower()
    if whatA == whatB:
        return 1
    else:
        return 0
