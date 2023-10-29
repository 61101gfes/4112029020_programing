import re

a=input('請輸入字母')
if re.match(r"[A-Za-z]",a)==None:
    print('輸入須為字母')

cal={}
for i in a:
    if i not in cal:
        cal[i]=1
    
    else:
        cal[i]+=1
    



print(cal)

        
