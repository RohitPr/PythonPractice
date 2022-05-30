class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        for a in range(1, n + 1):
            if a % 5 == 0 and a % 3 == 0:
                res.append('FizzBuzz')
            elif a % 3 == 0:
                res.append("Fizz")
            elif a % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(a))
        
        return res