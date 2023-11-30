# 9. Palindrome Number


# O(n)
def isPalindrome(num):
    if( (-2**31) <= num <= (2**31)-1):
        my_string = str(num)
        reversedStr = my_string[::-1]
        return my_string == reversedStr
    else:
        return "Enter a smaller number"
result1 = isPalindrome(11211)
# print(result1)


# O(log n): We don't have to convert or check entire number, just create a half of the original number by removing digits from the or num one by one, and compare both the halves

def isPalindrome2(num):
    # if the num if -ve it is not a palindrome as -121 palindrome is 121-, also, if number ends with 0, its not, as nums that begin with 0 aren't supported
    if num < 0 or (num != 0 and num %10 == 0):
        return False
    
    half = 0
    # as long as half is less than the num, we have not made it exactly half, so we run a loop
    while num > half:
        # first we multiply half to 10 so that we can add last  digit of num to ones place too. If we num % 10 we get the one's digit
        half = (half * 10) + (num % 10)
        # now remove that one digit from num
        num = num // 10 #floor divison will remove the decimal point digits if any
    # now, if digits we even number (112211), we will have num == half, if they were odd (12321) then half > num and we will have to reduce one digit from half
    return num == half or num == (half // 10)

result2 = isPalindrome2(1234321)
print(result2)