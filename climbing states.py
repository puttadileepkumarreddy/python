def sta(n):
    if(n<=1):
        return n
    return sta(n-1)+sta(n-2)
def countways(s):
    return sta(s+1)
s=int(input("n="))
print("number of ways:",)
print(countways(s))
    
