def complex_function(data):
    result = []

    for i in range(len(data)):
        if data[i] > 0:
            for j in range(len(data)):
                if data[j] % 2 == 0:
                    for k in range(len(data)):
                        if data[k] < 10:
                            for l in range(len(data)):
                                if data[l] > 5:
                                    result.append((data[i], data[j], data[k], data[l]))
                                else:
                                    result.append((data[i], data[j], data[k], -1))
                        else:
                            result.append((data[i], data[j], -1, -1))
                else:
                    for m in range(len(data)):
                        if data[m] < 0:
                            result.append((data[i], -1, -1, -1))
                        else:
                            for n in range(len(data)):
                                if data[n] == 0:
                                    result.append((-1, -1, -1, -1))
                                else:
                                    result.append((data[i], data[j], data[m], data[n]))
        else:
            for p in range(len(data)):
                if data[p] > 20:
                    result.append((data[i], -2, -2, -2))
                else:
                    for q in range(len(data)):
                        if data[q] == 1:
                            result.append((-3, -3, -3, -3))
                        else:
                            for r in range(len(data)):
                                result.append((data[i], data[p], data[q], data[r]))

    return result


# Example usage
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = complex_function(data_list)
print(output)
print("")