class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s# makes it easier to decode
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j]) # tells us how many character we are reading after j inorder to get every char
            result.append(s[j+ 1: j+ 1 + length])
            i = j + 1 + length # beginging of the next string

        return result