def isStackEmpty():
    global SIZE,stack,top
    if (top == -1):
        return True
    else:
        return False
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
stack = [None for _ in range(SIZE)]
top = -1

print("스택이 비었는지 여부 ==>",isStackEmpty())