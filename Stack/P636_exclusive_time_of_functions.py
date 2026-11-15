class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        final = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(":")
            function_id = int(function_id)
            timestamp = int(timestamp)

            if action == "start":
                if stack:
                    final[stack[-1]] += timestamp - prev_time
                stack.append(function_id)
                prev_time = timestamp

            else:
                final[stack[-1]] += timestamp - prev_time + 1
                stack.pop()
                prev_time = timestamp + 1

        return final