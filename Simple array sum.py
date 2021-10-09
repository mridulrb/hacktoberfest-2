a=[]
n=int(input("Enter the length of array"))
sum=0
for i in range(n):
  x=int(input("enter a numeric value"))
  a.append(x)
for i in range(n):
  sum+=a[i]
print("Sum of elements of array is",sum)

  
