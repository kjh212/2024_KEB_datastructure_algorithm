stack = ["커피","녹차","꿀물",None,None]
top = 2

print("----스택상태----")
for i in range (len(stack)-1,-1,-1):
    print(stack[i])
print("--------------")

while top >= 0 :
    data = stack[top]
    stack[top]=None
    top -= 1
    print("pop -->",data)

print("----스택상태----")
for i in range(len(stack)-1,-1,-1):
    print(stack[i])