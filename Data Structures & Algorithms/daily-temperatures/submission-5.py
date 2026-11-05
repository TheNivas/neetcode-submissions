class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        n = len(temps)
        res = [0] * n
        stack = []

        # for i in range(n):
        #     while stack and temps[i] > temps[stack[-1]]: 
        #         ind = stack.pop()
        #         res[ind] = i - ind 
        #     stack.append(i)
        for index, temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                _, prevIndex = stack.pop()
                res[prevIndex] = index - prevIndex

            stack.append((temp, index))

            
        return res
