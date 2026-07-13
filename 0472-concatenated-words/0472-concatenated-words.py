class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.root = TrieNode()
        for word in words:
            if not word:
                continue
            ptr = self.root
            for ch in word:
                if ch not in ptr.child:
                    ptr.child[ch] = TrieNode()
                ptr = ptr.child[ch]
            ptr.word = True
        res = []
        for word in words:
            self.dp = {}
            if word and self.solve(word, 0, 0):
                res.append(word)
        return res
    def solve(self, word, index, wc):
        if index == len(word):
            return wc >= 2
        if index in self.dp:
            return self.dp[index]
        node = self.root
        for i in range(index, len(word)):
            ch = word[i]
            if ch not in node.child:
                break
            node = node.child[ch]
            if node.word:
                if self.solve(word, i + 1, wc + 1):
                    self.dp[index] = True
                    return True
        self.dp[index] = False
        return False