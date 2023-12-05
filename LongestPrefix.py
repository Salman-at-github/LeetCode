# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

def getPre(arr):
    if len(arr) == 0:
        return ""
    base = arr[0]
    for i in range(len(base)):
        for word in arr[1:]:
            # if i reaches len(word), it means it has crossed the base len limit, because len is always +1 of index, so we break the loop
            if i == len(word) or base[i] != word[i]:
                # this will return "" if first letter does not match because in string indexing, the last element is always excluded, so word[0:0] = "", but if either of the conditions is true, we get the string
                return base[0:i]
    return base  # Move this line outside of the outer loop

strs = ["ab", "ad", "af"]
res = getPre(strs)
print(res)
