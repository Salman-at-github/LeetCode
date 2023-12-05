# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def CheckParenthesis(string):
    pairs = {
        "(":")",
        "{":"}",
        "[":"]"
    }
    stack = [] #use append and pop for LIFO (Last open bracket must close First)
    for char in string:
        # first we check if char is openening bracket, for that we check pairs, if it does, we push it into a stack
        if char in pairs: #it is an opening bracket
            stack.append(char)
        #its a closing bracket, first check if stack has any opening bracket, if not, then no pair exists, also check if char != closing br of opening br i.e pairs[stack.pop()], if their true, return false
        elif len(stack) == 0 or char != pairs[stack.pop()]:
            return False
    # if loop completes, none of the rules were violated, final stack must be empty for it to be right ordered
    return len(stack) == 0


res = CheckParenthesis("{{()[}]}")
print(res)
