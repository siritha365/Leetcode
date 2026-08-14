class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1 
        vowel = 0
        consonant = 0
        for ch in freq: 
            if ch in vowels:
                if freq[ch] > vowel:
                    vowel = freq[ch]
            else:
                if freq[ch] > consonant:
                        consonant = freq[ch]

        return vowel + consonant
                    
