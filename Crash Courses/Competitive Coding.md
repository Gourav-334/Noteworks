# $\fbox{COMPETITIVE CODING}$





## **Topic - 1: Arrays**

### <u>Introduction</u>

- **<u>Array</u>:** Elements of same type stored contagiously in memory.
- *Traditional arrays* can not dynamically resize, unlike *vectors*.


### <u>Patterns</u>

- **<u>Traversal</u>:** Basic iteration (forward, backward, conditional).
- **<u>Prefix sum</u>:** Precomputing cumulative sum for array's pattern.
- **<u>Kadane's algorithm</u>:** Maximum subarray sum (`count = max(arr[i], count+arr[i])`).
- **<u>Frequency counting</u>:** Track occurrence counts.
- **<u>Two-pass processing</u>:** Scanning array twice for results.
- **<u>In-place modification</u>:** Modifying array without extra memory.


### <u>Thinking Skills</u>

- Boundary awareness
- Index visualization
- Complexity awareness


### <u>Problem (#238)</u>

#### Description:

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`. The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer. You must write an algorithm that runs in `O(n)` time and without using the division operation.

#### Examples:

>**Input:** `nums = [1,2,3,4]`
>**Output:** `[24,12,8,6]`

>**Input:** `nums = [-1,1,0,-3,3]`
>**Output:** `[0,0,9,0,0]`

#### Constraints:

- `2 <= nums.length <= 105`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

#### Code template:

```cpp
class Solution {
	public:
	    vector<int> productExceptSelf(vector<int>& nums) {
		    /* Code starts here... */
	}
};
```
