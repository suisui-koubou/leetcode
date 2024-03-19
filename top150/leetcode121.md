# 121. Best Time to Buy and Sell Stock

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = -inf
        min_price = inf
        for p in prices:
            if p > min_price:
                ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return 0 if ans == -inf else ans 
```
