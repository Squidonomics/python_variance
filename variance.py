def variance(data):
    n = len(data)
    mean = sum(data)/n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations)/n
    return variance

print(variance([5, 3, 9, 10, 2, 8, 6, 7, 1]))
