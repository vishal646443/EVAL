s=eval(input("enter input"))
print(s)
prime=[]
composite=[]
length=len(s)
for i in range(length):
    for j in range(2,length):
        if s[i]%j==0:
          composite.append(s[i])
          break
    else:
        prime.append(s[i])

print("prime=",prime)
print("composite=",composite)
