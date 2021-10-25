import random
print("1부터 100사이의 숫자를 맞추시오.")
dap = random.randint(1,100)

i=0
while i<10:
    num=int(input("숫자를 입력하세요 :"))
    i+=1
    if num < dap:
        print("낮음!")
    elif num > dap :
        print("높음!")
    else:
        break

if dap == num:
    print("축하합니다. 시도 횟수 = %d" %i)
else:
    print("맞추지 못하셨군요. 답은 %d입니다." %dap)
