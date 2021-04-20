'''
Stack solution
'''

def paran(self,s):
    stack = []

    for i in s:
        if i in '{([':
            stack.append(i)
        
        else:
            if not stack:
                return False
            x = stack.pop()

            if x =='(':
                if i != ')':
                    return False
            
            elif x =='{':
                if i != '}':
                    return False

            elif x == '[':
                if i != ']':
                    return False
    if stack:
        return False
    return True



'''
Dictionary solution
'''


def paran(self,s):
    dic = { ')':'(', '}':'{' , ']':'['}

    stack = []

    for i in s:
        if i in dic.values():
            stack.append(i)
        elif i in dic.keys():
            if not stack or dic[i] != stack.pop():
                return False
        else:
            return False
    return stack == []