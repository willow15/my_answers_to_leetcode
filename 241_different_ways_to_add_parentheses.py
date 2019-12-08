class Solution(object):
    def splitNumbersAndOperators(self, input):
        """
        :type input: str
        :rtype: List[int, str]
        """
        result = list()
        input_count = len(input)
        operators = ['+', '-', '*']
        j = 0
        for i in xrange(input_count):
            if input[i] in operators:
                result.append(int(input[j:i]))
                result.append(input[i])
                j = i + 1
        result.append(int(input[j:]))
        return result

    def diffWaysToCompute2(self, input):
        """
        :type input: List[int, str]
        :rtype: List[int]
        """
        input_count = len(input)
        if input_count == 1:
            return input
        elif input_count == 3:
            if input[1] == '+':
                return [input[0] + input[2]]
            elif input[1] == '-':
                return [input[0] - input[2]]
            elif input[1] == '*':
                return [input[0] * input[2]]

        result = list()
        for i in xrange(1, input_count, 2):
            operator = input[i]
            left_results = self.diffWaysToCompute2(input[:i])
            right_results = self.diffWaysToCompute2(input[i + 1:])
            for left_result in left_results:
                for right_result in right_results:
                    if operator == '+':
                        result.append(left_result + right_result)
                    elif operator == '-':
                        result.append(left_result - right_result)
                    elif operator == '*':
                        result.append(left_result * right_result)
        return result

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        numbers_and_operators = self.splitNumbersAndOperators(input)
        return self.diffWaysToCompute2(numbers_and_operators)


if __name__ == '__main__':
    input = '2*3-4*5'
    solution = Solution()
    print solution.diffWaysToCompute(input)
