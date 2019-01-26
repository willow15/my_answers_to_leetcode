class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        station_number = len(gas)
        for i in xrange(len(gas)):
            if gas[i] < cost[i]:
                continue
            remainder = gas[i] - cost[i]
            next_station = i + 1
            if next_station == station_number:
                next_station = 0
            while next_station != i:
                remainder = remainder + gas[next_station]
                if remainder < cost[next_station]:
                    break
                remainder = remainder - cost[next_station]
                next_station = next_station + 1
                if next_station == station_number:
                    next_station = 0
            if next_station == i:
                return i
        return -1


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution()
    print solution.canCompleteCircuit(gas, cost)
