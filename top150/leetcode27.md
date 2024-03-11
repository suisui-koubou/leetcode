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

由于最终的输出数组小于或者等于输入数组，可以直接往数组写(写的指针追不上扫描的指针，不会出现覆盖的情况)。

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length; 
        int l = 0, r = 0; 
        for (r = 0; r < n; r++){
            if (nums[r] != val){
                nums[l++] = nums[r]; 
            }
        }
        return l; 
    }
}
```

## 双指针优化

换了元素以后有可能会相同，先不要`l++`，等确认了 `nums[l] != val` 再 `l++`。

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length; 
        int l = 0, r = n-1;  // 警惕 n = 1 的情况
        while (l <= r){
            if (nums[l] == val){
                nums[l] = nums[r]; 
                r--; 
            }else{
                l++; 
            }
        }

        return l; 
    }
}
```