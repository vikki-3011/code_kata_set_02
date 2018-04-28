a=int(raw_input())
b="no"
for i in range (a+1):
    r=2**i
    if(r==a):
      b="yes"
print(b)
