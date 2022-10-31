class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        # if len(A)!=len(B):
        #     return -1

        A.sort()
        B.sort()

        for i in range(N):
            if A[i]==B[i]:
                continue
            else:
                return False

        return True
