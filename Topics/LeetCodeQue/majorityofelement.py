# Intuition
# <!  we used Idea of Boyer–Moore Algorithm. Pair up different elements and cancel them. -->

# Approach
""" 1. define the ele= None, count to 0
2. loop through the nums, if count is 0 then assign the ele to num
3. if num is equal to ele then increase the count by 1 else decrease the count by 1
4. return the ele  
"""

# Complexity
# - Time complexity:
# <!-- O(n)-->

# - Space complexity:
# <!-- o(1) -->

# Code
# ```python []
class Solution(object):
    def majorityElement(self, nums):
        ele = None
        count = 0
        for num in nums:
            if count == 0:
                ele = num
            
            if num == ele:
                count+=1
            else:
                count-=1

        return ele


nums = [3,2,3,4 ,7,7]
obj1 = Solution()
print(obj1.majorityElement(nums))
