# 189. Rotate Array

## 额外内存

```java
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length; 
        k = k % n; 
        if (k == 0) return; 
        int[] newNums = new int[n];
        int j = n - k; 
        for (int i = 0; i < n; i++){
            newNums[i] = nums[j]; 
            j = (j + 1) % n; 
        }
        for (int i = 0; i < n; i++){
            nums[i] = newNums[i]; 
        }
        return;  
    }
}
```

## 数组翻转

基于以下观察, 当我们将数组的元素向右移动 $k$ 次后，
- 尾部 $k\bmod n$ 个元素会移动至数组头部，
- 其余元素向后移动 $k\bmod n$ 个位置。

