n=int(input())
c=0
for i in range(n):
  Petya, Vasya, Tonya= map(int, (input().split()))
  if Petya + Vasya + Tonya>=2:
    c+=1
print(c)