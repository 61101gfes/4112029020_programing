import random
ans=random.sample(range(1,10),4)
print(ans)
c=0
while c<5:
    c+=1
    print(f"還剩{5-c}次")
    guess=input('請輸入數字:')
    a=0
    b=0
    for i in range(4):
        if guess[i]==str(ans[i]):
            a+=1
        else:
            if guess[i] in str(ans):
                b+=1
    if a==4:
        print('答對了')
        break
    else:
        print(f"目前{a}A{b}B")
if a==4:
    print(f"一共猜了{c}次才對")
else:
    print(f"一共猜了{c}次")
    


    
    

    
    


