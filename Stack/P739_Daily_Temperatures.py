#Brute Force Solution
#TLE Problem

# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         stack = []
#         n = len(temperatures)
#         for i in range(n-1):
#             found_days = False
#             for j in range(i+1,n):
#                 if temperatures[i] < temperatures[j]:
#                     stack.append(j-i)
#                     found_days = True
#                     break
#             if found_days == False:
#                 stack.append(0)
#         stack.append(0)
#         return stack

#Trying new approach
#still not enough but enough to pass the test cases

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        
        return answer