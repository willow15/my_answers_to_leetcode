class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for hour_num in xrange(0, num + 1):
            minute_num = num - hour_num
            sub_hours = self.read_time(hour_num, 0, [8, 4, 2, 1])
            sub_minutes = self.read_time(minute_num, 0, [32, 16, 8, 4, 2, 1])
            for sub_hour in sub_hours:
                if sub_hour > 11:
                    continue
                for sub_minute in sub_minutes:
                    if sub_minute > 59:
                        continue
                    if sub_minute < 10:
                        result.append(str(sub_hour) + ':0' + str(sub_minute))
                    else:
                        result.append(str(sub_hour) + ':' + str(sub_minute))
        return result

    def read_time(self, time_num, start_index, candidates):
        sub_times = []
        if time_num == 0:
            return [0]
        elif time_num < 0:
            return []
        else:
            for i in xrange(start_index, len(candidates)):
                sub_results = self.read_time(time_num - 1, i + 1, candidates)
                for sub_result in sub_results:
                    sub_times.append(candidates[i] + sub_result)
        return sub_times


if __name__ == '__main__':
    num = 2
    solution = Solution()
    result = solution.readBinaryWatch(num)
    print len(result)
    print result
