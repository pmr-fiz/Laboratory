def rev(s): 
    if len(s) == 1:
        return s
    else:
        return s[-1] + rev(s[:-1])
    
def pobuk(s):
    return list(s)