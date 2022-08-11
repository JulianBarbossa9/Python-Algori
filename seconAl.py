'''

balance("()") -> "()"
balance(")(") -> ""
balance("(((((") -> ""
balance("(()()(") -> "()()"

balance("(())())") -> "(()())" or "(())()"
balance("a(b)c") -> "a(b)c" or "a(bc)"


###---###
  )(a))(
  string = ' )(a))('
  weights = { 
    ( => 1
    ) => -1
}

    removeUnccessaryChar( ')(a))(', weights)
    weight_sum = 0|1-1=0|1
    partial_result = ['(','a',')','(']
     
     for char in string:
        char = )|(|a|)|)|(
             v
        )(a))(

    procecedString=[(a)(]
    reversedString = [()a(]
     weights = {
        ) => 1,
        ( => -1
    }
    removeUnncessaryChar(string = '()a(', weights)
     weight_sum = 0
    partial_result = ['','','']
    for char in string:
        char=(|)|a|(|
        v
        ()a('

    partial_result = ['(',')','a','(']
    partial_result.reverse(['(','a',)','('])

}
'''
def removeUnncessaryChar(string,weights):
    weight_sum = 0
    partial_result = []
    for char in string:
        if char not in weights:
            partial_result.append(char)
            continue
        if weight_sum + weights[char] < 0:
            continue
        weight_sum += weights[char]
        partial_result.append(char)
        continue
        raise Exception ('Error')
    return partial_result

#Remove a parenthesis or character
def balanceParentheses(string):
    if not string:
        return ""
    #Helper functions
    weights = { "(":1, ")":-1}
    partial_result=removeUnncessaryChar(string, weights)
    
    '''
    partial_result = []
    weightSum = 0
    for char in string:
        if char not in weights:
            partial_result.append(char)
        if char == "(":
            weightSum += 1
            partial_result.append(char)
            continue
        if char == ")":
            if weightSum <= 0:
                continue
            weightSum -= 1
            partial_result.append(char)
            continue
        raise Exception('Error')
    '''

    procecedString = "".join(partial_result)
    reverseString = procecedString[::-1]
    weights = {")":1,"(":-1}
    # do helper function
    partial_result=removeUnncessaryChar(reverseString, weights)
    partial_result.reverse()
    return "".join(partial_result)


   # if char == "(":
        #     if weight_sum + weights[char] < 0:
        #         continue
        #     weight_sum += weights[char]
        #     partial_result.append(char)
        #     continue 
        # if char == ")":
        #     if weight_sum <= 0:
        #         continue
        #     weight_sum += weights[char]
        #     partial_result.append(char)
        #     continue