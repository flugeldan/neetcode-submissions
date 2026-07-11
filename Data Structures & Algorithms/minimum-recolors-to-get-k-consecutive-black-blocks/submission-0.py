class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b, w = 0, 0
        l = 0
        mini = float('inf')
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                w += 1 
            else:
                b += 1
            if i - l + 1 == k:
                mini = min(mini, w)
                if blocks[l] == 'W':
                    w -= 1 
                else:
                    b -= 1 
                l += 1 
        return mini
