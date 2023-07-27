class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            newWord = word.split(separator)
            for new in newWord:
                if len(new):
                    res.append(new)
        return res