

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length; 
        int i = 1, j = 1;
        for (j = 0; j < n; j++){
            if (nums[i-1] != nums[j]){
                nums[i] = nums[j]; 
                i++;
            }
        } 
        return i;
    }
}
```