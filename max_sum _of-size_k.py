arr=[2,1,5,3,6,8,9]
k=9
max_length=0
ws,we=0,0
sum=0
while we<len(arr):
    sum+=arr[we]
    if sum==k:
        max_length=max(max_length,we-ws+1)
    if sum>k:
        sum=0
        ws+=1
    we+=1
print(max_length)           