
我比较笨想不到。

- 数组是连续的
- 只需要**往前看第x个(最多x个重复)**，
  - 如果 `nums[i-x] == nums[j]` 就意味着可以构成 `x+1`个`nums[i-x]` 
  - 不满足题目要求


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

