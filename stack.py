def isStackFull():
    global SIZE,stack,top
    if (top >=SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE,stack,top
    if(isStackFull()):
        print("스택이 꽉찼습니다.")
        return
    top += 1
    stack[top]=data

SIZE =5
stack = ["coffee","green tea","honye water","coke",None]
top = 3

print(stack)
push("fanta")
print(stack)
push("getoray")