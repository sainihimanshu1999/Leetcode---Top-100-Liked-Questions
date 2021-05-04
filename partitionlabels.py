def partitionlabels(self,s):
    counter = {c:i for i,c in enumerate(s)}
    left,right =0,0
    op = []

    for i,letter in enumerate(s):
        right = max[right,counter[letter]]

        if i == right:
            op +=[right-left+1]
            left = i+1

    return op