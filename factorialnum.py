def factorial(n: int) -> int:
    pass
    ans=1
    if n==0:
        return 1
    else:
        for i in range (1,n+1):
            ans=ans*i    
    return ans
