class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(str1)}${str1}" for str1 in strs])

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            dollar = s.find("$", i)
            strL = int(s[i:dollar])
            i = dollar + 1
            str1 = s[i: i+strL]
            decoded.append(str1)
            i  = i + strL
        
        return decoded
