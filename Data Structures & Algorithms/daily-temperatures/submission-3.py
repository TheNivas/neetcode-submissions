class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        n = len(temps)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temps[i] > stack[-1][0]: 
                _, ind = stack.pop()
                res[ind] = i - ind 
            stack.append((temps[i], i))
            
        return res
