def min_number(source, target):
    target_len = len(target)
    source_len = len(source)
    j = 0 
    count = 0   
    while j < target_len:
        i = 0
        match = False
        while i < source_len:
            if j < target_len and source[i] == target[j]:
                j += 1
                match = True
            i += 1
        if not match:
            return -1
        count += 1
    return count

source = "xyz"
target = "xzyxz"
print(min_number(source, target))
