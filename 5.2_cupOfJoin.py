def join(*lists, sep='-'):
    result = [str(item) for lst in lists for item in lst]
    print(list(sep.join(result)))




join([1, 2], [8], [9, 5, 6])