def find_err(input):
    input_len = len(input)
    stack = []
    result = [' '] * input_len
    for i, char in enumerate(input):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result[i] = '?'
    while stack:
        i = stack.pop()
        result[i] = 'x'
    return ''.join(result)

test_strings = "bge)))))))))"
print(test_strings)
print(find_err(test_strings))
print()

