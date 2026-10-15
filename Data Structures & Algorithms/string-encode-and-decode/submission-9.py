class Solution:

    def encode(self, strs: list[str]) -> str:
        s = ""
        for strr in strs:
            s += f"{len(strr)}#{strr}"
        return s

    def decode(self, s: str) -> list[str]:
        rex = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            word = s[i: j]
            print(word)
            rex.append(word)
            i = j
        return rex
        