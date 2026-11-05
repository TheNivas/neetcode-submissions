class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(pair):
            time = (target -p) /s
            while stack and time >= stack[-1]:
                # a prev car reaches target before or at the same time
                # Thus they form a fleet, and move by slow speed
                # pop the faster car
                stack.pop()
            stack.append(time)
        return len(stack)