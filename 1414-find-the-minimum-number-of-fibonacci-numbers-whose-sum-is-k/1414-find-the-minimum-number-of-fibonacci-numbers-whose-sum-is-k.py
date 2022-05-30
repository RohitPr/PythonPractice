class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        n1, n2 = 1, 1
        fib= [n1]
        
        while n2 <= k:
            fib.append(n2)
            n1, n2 = n2, n1 + n2
        
        count = 0 
        for i in fib[::-1]:
            
            if k >= i:
                k = k - i
                count+=1

            if k==0:
                return count