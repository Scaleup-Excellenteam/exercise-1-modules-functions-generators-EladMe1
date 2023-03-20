def interleave(*params):
    max_len = max(len(param) for param in params)
    interleaved = []
    # Loop over the range of max_len and the input parameters to interleave the elements
    for i in range(max_len):
        for param in params:
            # Check if the parameter has an element at the current index i
            if i < len(param):
                interleaved.append(param[i])

    return interleaved


print((interleave('abc', [1, 2, 3], ('!', '@', '#'))))