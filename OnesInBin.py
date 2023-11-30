#                                              Find number of 1 bits in a binary number

# # O(n)
# count = 0
# def DetectOnesBin(binaryNum):
#     global count
#     mystring = str(binaryNum)
#     for num in mystring:
#         if(num == '1'):
#             count+=1
#     return count        
# n = input()
# result = DetectOnesBin(n)
# print(result)

# Better way O(log n)

def GetOnes(n):
    counter = 0
    # run the loop until the binary num becomes 0
    while n!= 0:
        # we shift the binary number to right evertime, decreassing the binary number by 1 digit, since its a binary number n%2 will give us the last number, if its 10, then 0 gets added to counter, if its 1, it gets added to counter. THis is how counter value increases as binary number can only have 0 and 1
        counter += (n % 2)
        # this means n = n>>1 (shifting to right by 1 dig eg 1000>>1 becomes 100)
        n >>= 1
    return counter
result = GetOnes(0b110011)
print(result)
# number must be binary! therefore it must begin with 0b , eg, 11001100 will be 0b11001100