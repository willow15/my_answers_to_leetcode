class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] > 0:
                    changes[5] -= 1
                    changes[10] += 1
                else:
                    return False
            else:
                if changes[5] > 0:
                    if changes[10] > 0:
                        changes[5] -= 1
                        changes[10] -= 1
                        changes[20] += 1
                    elif changes[5] >= 3:
                        changes[5] -= 3
                        changes[20] += 1
                    else:
                        return False
                else:
                    return False
        return True


if __name__ == '__main__':
    bills = [5, 5, 10, 10, 20]
    solution = Solution()
    print solution.lemonadeChange(bills)
