# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

class Solution:
# @param A : integer
# @return a list of integer
    def isprime(self, a):
        if a <= 1:
            return 0
        if a == 2:
            return 1
        for i in range(2,int(a**0.5)+1):
            if(i<=a and a%i==0):
                return 0
        return 1

    def primesum(self, A):
        for i in range(2,A):
            if self.isprime(i)==1 and self.isprime(A-i)==1:
                return (i,A-i)