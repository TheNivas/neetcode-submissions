class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        print(res)
        return res
        

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i : i+length])
            i += length
            print(res)
        return res