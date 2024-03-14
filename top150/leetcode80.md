
我比较笨想不到。

- 假设有一个长度为2的**滑窗**
- 只有两种情况，就是 `x|y` 和 `x|x`
  - 想清楚以后，只有第一种情况可以写入。


```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length; 
        if (n <= 2){
            return n; 
        }
        int i = 2, j = 2; 
        for (; j < n; j++){
            if (nums[i-2] != nums[j]){
                nums[i] = nums[j]; 
                i++; 
            }
        }
        return i; 
    }
}
```

