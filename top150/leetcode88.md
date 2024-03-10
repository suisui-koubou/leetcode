# 88. Merge Sorted Array


## Solution 1 
```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = 0; i < n; i++){
            nums1[m + i] = nums2[i]; 
        }   
        Arrays.sort(nums1); 
    }
}
```

## Solution 2
```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] sorted = new int[m + n]; 
        int k = 0; 
        int i = 0, j = 0; 
        for (; i < m && j < n; ){
            if (nums1[i] < nums2[j]){
                sorted[k++] = nums1[i++]; 
            }else{
                sorted[k++] = nums2[j++]; 
            }
        }
        for (; i < m; i++){
            sorted[k++] = nums1[i]; 
        }
        for (; j < n; j++){
            sorted[k++] = nums2[j]; 
        }
        for (i = 0; i < k; i++){
            nums1[i] = sorted[i]; 
        }
    }
}
```

## Solution 3 

思考一下 `nums1` 的 `i` 和 `k` 指针会不会相遇。

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1; 
        int k = m + n - 1; 
        while (i >= 0 && j >= 0){
            if (nums1[i] > nums2[j]){
                nums1[k--] = nums1[i--]; 
            }else{
                nums1[k--] = nums2[j--]; 
            }
        }
        while (i >= 0){
            nums1[k--] = nums1[i]; 
            i--; 
        }
        while (j >= 0){
            nums1[k--] = nums2[j]; 
            j--; 
        }
    }
}
```