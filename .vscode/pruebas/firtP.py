'''
    tacocats -> True
    racercar -> True
    abcd -> False

       v
    tacocats
       ^
           v
    racercar
    ^

       v
    abcd
    ^

      v
    abc
    ^
     

      ^  
    aaa
    v

       v 
    aaaa
    ^
if is polindrome return true

time:
    N + (polidrome check)
     2N
'''

###--###

'''
         01234567
string = racercar
            i
             j
i = 0|1|2|3 
j = 8 - 1 = 7|6|5|4

while 

break because i=3 and j = 4 and condition say i <= j 

isPolidrome([i:j])
isPolidrome([e:r])

         0123
string = abcd
         i
            j

i = 1
j = 3

while

isPolidrome(abc)
    reverseString = cba
    return cba = abc

isPolidrome(bcd)
    reverseString = dcb
    return dcb == bcd

    aca

'''

#Polindromo




def isPolindrome(string):
    reversedString = string[::-1]
    return reversedString == string 

def isPalindromeWithCharRemoved(string):
    if not string:
        return True
        #If the len of string is <= 2 bb cd 
    if len(string) <= 2:
        return True 
    i = 0
    j = len(string)-1

    while i <= j and string[i] == string[j]:
        i += 1
        j -= 1 
    # i == j or mimatched chars
    if i == j and len(string) % 2 ==1:
        return True
    if i > j and len(string) % 2 == 0:
        return True
    if isPolindrome(string[i:j]): # Remove char j
        return True 
    if isPolindrome(string[i+1:j+1]):# Remove char i
        return True
    return False



print(isPalindromeWithCharRemoved('abcd'))





    