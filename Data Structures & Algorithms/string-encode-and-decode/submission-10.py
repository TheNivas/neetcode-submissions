class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += f"{len(string)}${string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            dollar_pos = s.find("$", i)
            str_len = int(s[i:dollar_pos])
            i = dollar_pos + 1
            str_val = s[i : i + str_len]
            decoded.append(str_val)
            i += str_len
        return decoded
