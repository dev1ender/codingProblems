
def climbStairs( n: int) -> int:
    n_1 = 1
    n_2 = 2
    if n ==2:
        return 2
    if n==1:
        return 1 
    for i in range(3,n):
        print(i)
        ways = n_2+n_1 
        n_1 = n_2
        n_2 = ways
    return n_2 

print(climbStairs(3))
