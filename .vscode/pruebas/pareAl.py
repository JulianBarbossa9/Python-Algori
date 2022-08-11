def removeUnnessaryChar(string, weights):
    weights_sum = 0
    partial_result = []
    for char in string:
        if char not in weights:
            partial_result.append(char)
            continue
        if weights_sum + weights[char] < 0:
            continue
        weights_sum += weights[char]
        partial_result.append(char)
        continue
    return partial_result
    


def isValid(string):
    if not string:
        return ""
    weights = {"(":1,")":-1,"{":1,"}":-1, "[":1, "]":-1}
    #Helper function
    partial_result = removeUnnessaryChar(string, weights)
    proccesed_result = "".join(partial_result)
    reverse_result = proccesed_result[::-1]
    weights = {"(":-1,")":1,"{":-1,"}":1, "[":-1, "]":1}
    partial_result = removeUnnessaryChar(reverse_result, weights)
    partial_result.reverse()
    return "".join(partial_result)

print(isValid('(()()('))


