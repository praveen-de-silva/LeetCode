class Solution(object):
    # Method 01:
    def vowelStrings(self, words, queries):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = []

        for l, r in queries:
            countVowStr = 0
            for word in words[l:r+1]:
                if word[0] in vowels and word[-1] in vowels:
                    countVowStr += 1
            res.append(countVowStr)
        
        return res

    # Method 02: <LEGEND>

    def vowelStrings(self, words, queries):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0] * (len(words) + 1)
        res = []

        for i, word in enumerate(words):
            prefix[i+1] = prefix[i] + (1 if word[0] in vowels and word[-1] in vowels else 0)

        for l, r in queries:
            res.append(prefix[r+1] - prefix[l])

        return res
