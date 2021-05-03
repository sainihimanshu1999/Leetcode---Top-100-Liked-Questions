def decode(self,s):
    stack,currString,currNum = [],'',0

    for i in s:
        if i == '[':
            stack.append(currString)
            stack.append(currNum)
            currString = ''
            currNum = 0

        elif i ==']':
            num = stack.pop()
            prevString = stack.pop()
            currString = prevString + num*currString

        elif i.isdigit():
            currNum = currNum*10 + int(i)

        else:
            currString += i
    return currString