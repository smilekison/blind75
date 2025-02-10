class Solution:
    def isValid(s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        mapV = {")":"(" , "}":"{" , "]":"["}
        stackV = []

        for c in s:
            if c in mapV:
                if stackV and stackV[-1] == mapV[c]:
                    stackV.pop()
                else:
                    return False
            else:
                stackV.append(c)
        
        return True if not stackV else False


    print(isValid("([]()"))