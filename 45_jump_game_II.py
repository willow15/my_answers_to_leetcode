class Solution(object):
    # def jump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     end_index = len(nums) - 1
    #     if end_index > 0:
    #         count = [None] * end_index
    #         cur_index = end_index - 1
    #         while cur_index >= 0:
    #             farthest_index = cur_index + nums[cur_index]
    #             if farthest_index == cur_index:
    #                 pass
    #             elif farthest_index < end_index:
    #                 count_set = filter(lambda x: x is not None, count[cur_index + 1: farthest_index + 1])
    #                 if count_set:
    #                     minimum_count = min(count_set)
    #                     count[cur_index] = minimum_count + 1
    #                 else:
    #                     count[cur_index] = None
    #             else:
    #                 count[cur_index] = 1
    #             cur_index -= 1
    #         return count[0]
    #     else:
    #         return 0

    def jump(self, nums):
        destination = len(nums) - 1
        if destination <= 0:
            return 0

        count = 1
        begin_index = 1
        end_index = nums[0]
        while end_index < destination:
            count += 1
            max_jump = 0
            for i in xrange(begin_index, end_index + 1):
                cur_jump = i + nums[i]
                if max_jump < cur_jump:
                    max_jump = cur_jump
            if max_jump >= destination:
                break
            begin_index = end_index + 1
            end_index = max_jump
        return count


if __name__ == '__main__':
    # nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    nums = [2, 1]
    solution = Solution()
    print solution.jump(nums)
