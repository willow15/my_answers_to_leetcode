class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        count = len(bits)
        index = 0
        while index < count:
            if bits[index] == 0:  # must be 1-bit
                index += 1
                if index == count:
                    return True
            else:  # must be 2-bit
                index += 2
                if index == count:
                    return False


if __name__ == '__main__':
    bits = [1, 1, 1, 0]
    solution = Solution()
    print solution.isOneBitCharacter(bits)
