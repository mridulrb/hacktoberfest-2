#maximum sum of continous subarray

arr = [-2,-5,2,4,7,-1,9,12,-4]

s=0
maxx=arr[0]
for i in arr:
    maxx = maxx + i
    if s < maxx :
        maxx = s
    if s < 0 :
        maxx = 0

print(maxx)

