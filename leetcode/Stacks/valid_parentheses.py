class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ["[", "{", "("]:
                stack.append(c)
                continue
            
            if len(stack) == 0:
                return False

            gc = stack.pop()

            if (c == ')' and gc == '(') or (c == '}' and gc == '{') or (c == ']' and gc == '['):
                continue
            
            return False
        if len(stack) != 0:
            return False
        return True


if __name__ == "__main__":
    s = Solution()

    data = []
    data = [ ["()", True], ["()[]{}", True], ["(]", False]]
    for i in data:
        res = s.isValid(i[0])
        if res == i[1]:
            print("Correct!\n")
        else:
            print("Error\n")

