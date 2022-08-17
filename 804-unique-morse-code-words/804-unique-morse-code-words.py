class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        wordset = set()
        
        for word in words:
            temp = ""
            for letter in word:
                temp += (morse[ord(letter)-ord('a')])
            wordset.add(temp)
            
        return len(wordset)