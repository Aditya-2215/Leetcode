class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.child:
                    node.child[ch] = TrieNode()
                node = node.child[ch]
            node.word = word
            #DRIVER CODE
        rows = len(board)
        cols = len(board[0])
        res = []

        def solve(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            ch = board[r][c]
            if ch == "#" or ch not in node.child:
                return
            node = node.child[ch]
            if node.word:
                res.append(node.word)
                node.word = None
            board[r][c] = "#"

            solve(r + 1, c, node)
            solve(r - 1, c, node)
            solve(r, c + 1, node)
            solve(r, c - 1, node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                solve(r, c, root)

        return res