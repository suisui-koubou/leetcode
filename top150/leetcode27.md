# 27. Remove Element


## 瞎写

我这个写法太挫了。

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int p; 
        for (p = nums.length - 1;  p >= 0 && nums[p] == val ; p--){ }
        if (p < 0) return 0;  
        int end = p; 
        for (int i = 0; i < end; i++){
            if (nums[i] == val){
                nums[i] = nums[p--];
                while (nums[p] == val) p--; 
            }
            if (i == p) break; 
        }
        return p+1; 
    }
}
```

## 双指针


## 双指针优化

