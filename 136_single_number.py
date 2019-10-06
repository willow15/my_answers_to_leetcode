# Approach 1: list operation
# Approach 2: hash table
# Approach 3: 2*(a+b+c) - (a+a+b+b+c) = c
# Approach 4: a^b^a = a^a^b = 0^b = b (a^0=a, a^a=0)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appear_once = []
        for num in nums:
            if num in appear_once:
                appear_once.remove(num)
            else:
                appear_once.append(num)

        return appear_once[0]


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    print solution.singleNumber(nums)
