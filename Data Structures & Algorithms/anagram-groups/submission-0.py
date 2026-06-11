from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashcheck=defaultdict(list)
        for word in strs:
            freq=[0]*26
            for letter in word:
                freq[ord(letter)-ord('a')] +=1
            freq=tuple(freq)
            hashcheck[freq].append(word)
        return list(hashcheck.values())