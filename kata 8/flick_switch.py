def flick_switch(lst):
    bool = True
    arr = []
    for c in lst:
        bool = not bool if c == "flick" else bool
        arr.append(bool)
        
    return arr