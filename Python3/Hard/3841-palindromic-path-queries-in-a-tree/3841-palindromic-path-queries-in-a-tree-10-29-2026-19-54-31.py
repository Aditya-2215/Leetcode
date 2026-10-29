class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for node in order:
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                depth[neighbor] = depth[node] + 1
                order.append(neighbor)

        subtree_size = [1] * n
        heavy_child = [-1] * n

        for node in reversed(order[1:]):
            subtree_size[parent[node]] += subtree_size[node]
            parent_node = parent[node]

            if (
                heavy_child[parent_node] == -1
                or subtree_size[node] > subtree_size[heavy_child[parent_node]]
            ):
                heavy_child[parent_node] = node

        head = [0] * n
        position = [0] * n
        current_position = 0
        chain_stack = [(0, 0)]

        while chain_stack:
            node, chain_head = chain_stack.pop()

            while node != -1:
                head[node] = chain_head
                position[node] = current_position
                current_position += 1

                for neighbor in graph[node]:
                    if neighbor != parent[node] and neighbor != heavy_child[node]:
                        chain_stack.append((neighbor, neighbor))

                node = heavy_child[node]

        tree_size = 1
        while tree_size < n:
            tree_size <<= 1

        segment_tree = [0] * (2 * tree_size)

        for node in range(n):
            segment_tree[tree_size + position[node]] = 1 << (ord(s[node]) - ord("a"))

        for index in range(tree_size - 1, 0, -1):
            segment_tree[index] = (
                segment_tree[index * 2] ^ segment_tree[index * 2 + 1]
            )

        def update(index, value):
            tree_index = tree_size + index
            segment_tree[tree_index] = value
            tree_index >>= 1

            while tree_index:
                segment_tree[tree_index] = (
                    segment_tree[tree_index * 2]
                    ^ segment_tree[tree_index * 2 + 1]
                )
                tree_index >>= 1

        def range_query(left, right):
            left += tree_size
            right += tree_size
            result = 0

            while left <= right:
                if left & 1:
                    result ^= segment_tree[left]
                    left += 1

                if not (right & 1):
                    result ^= segment_tree[right]
                    right -= 1

                left >>= 1
                right >>= 1

            return result

        def path_query(first_node, second_node):
            result = 0

            while head[first_node] != head[second_node]:
                if depth[head[first_node]] < depth[head[second_node]]:
                    first_node, second_node = second_node, first_node

                result ^= range_query(
                    position[head[first_node]],
                    position[first_node]
                )
                first_node = parent[head[first_node]]

            left_position = position[first_node]
            right_position = position[second_node]

            if left_position > right_position:
                left_position, right_position = right_position, left_position

            return result ^ range_query(left_position, right_position)

        answers = []

        for query in queries:
            query_tokens = query.split()

            if query_tokens[0] == "update":
                node = int(query_tokens[1])
                character = query_tokens[2]
                update(position[node], 1 << (ord(character) - ord("a")))
            else:
                first_node = int(query_tokens[1])
                second_node = int(query_tokens[2])
                path_mask = path_query(first_node, second_node)
                answers.append(
                    path_mask == 0 or (path_mask & (path_mask - 1)) == 0
                )

        return answers