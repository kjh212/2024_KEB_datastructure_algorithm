alpha =["a","b","c","d","e"]

def LinearList(katok):
    length1=len(katok)
    while True:
        input_number = int(input(f'몇번째에 넣을지 적으시오(최대{length1}까지) : '))
        if input_number <=length1 and input_number >=1:
            katok.append(None)
            input_st = input('무엇을 넣은건지 적으시오 : ')
            for i in range(1,length1+3-input_number):
                if i < length1+2-input_number:
                    katok[length1+1-i]=katok[length1-i]
                elif i == length1+2-input_number:
                    katok[length1+1-i]=input_st
                else:
                    pass
            break
        else:
            print('다시 적으시오.')
            pass

LinearList(alpha)
print(alpha)

