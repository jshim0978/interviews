class Solution:
    def isValid(self, s: str) -> bool:
        leftCurve = '('
        rightCurve = ')'
        leftBrace = '{'
        rightBrace = '}'
        leftBracket = '['
        rightBracket = ']'

        arr = []
        for i in s:
            if i == leftCurve or i == leftBrace or i == leftBracket:
                arr.append(i)
            else:
                if len(arr) == 0:
                    return False
                if i == rightCurve and arr[-1] == leftCurve:
                    arr.pop()
                elif i == rightBrace and arr[-1] == leftBrace:
                    arr.pop()
                elif i == rightBracket and arr[-1] == leftBracket:
                    arr.pop()
                else:
                    return False
        if len(arr) == 0:
            return True
        else:
            return False