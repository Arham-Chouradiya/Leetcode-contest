class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        stack = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            stack.append(nums[i])
            while len(stack)>= 2 and stack[-1]<=stack[-2]:
                stack[-2]+=stack[-1]
                stack.pop()
        return max(stack)