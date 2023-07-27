class Solution:
    def maxScore(self, n: List[int], x: int) -> int:
        even = n[0] - (x if n[0]%2 else 0)
        odd = n[0] - (x if n[0]%2==0 else 0)
        
        for i in range(1, len(n)):
            if n[i]%2:
                odd = n[i] + max(odd, even-x)
            else:
                even = n[i] + max(even, odd-x)

        return max(odd, even)