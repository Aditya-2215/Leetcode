class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        # (finish_time, weight, server_index)
        busy = []

        ans = []
        time = 0

        for i, task in enumerate(tasks):

            # Current time cannot be earlier than task arrival
            time = max(time, i)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # If no server is available, jump to next completion
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            # Assign the next queued task
            weight, idx = heapq.heappop(free)
            ans.append(idx)

            # Update server's availability
            heapq.heappush(busy, (time + task, weight, idx))

        return ans