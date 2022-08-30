class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        len(x.__str__())
        for i in range(len(x.__str__()) // 2):
            if x.__str__()[i] != x.__str__()[len(x.__str__()) - i - 1]:
                return False
        return True
