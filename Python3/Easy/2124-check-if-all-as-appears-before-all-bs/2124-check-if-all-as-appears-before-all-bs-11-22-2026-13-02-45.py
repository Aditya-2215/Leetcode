class Solution:
    def checkString(self, s: str) -> bool:
        string={}
        for i , ch in enumerate(s):
            if ch=='a':
                string['a']=i
            elif ch=='b' and 'b' not in string:
                string['b']=i
        if 'a' in string and 'b' in string:
            return string['a']<string['b']
        return True