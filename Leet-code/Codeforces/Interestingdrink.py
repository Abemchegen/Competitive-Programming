n= int(input())
shops = list(map(int, input().split()))
shops.sort()
day = int(input())
 
def bs(q):
 
    low = 0
    high = len(shops) - 1
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if shops[mid] <= q :
            low = mid + 1
 
        else:
            high = mid - 1
    
    return high + 1
 
for i in range(day):
 
    q = int(input())
    print(bs(q))