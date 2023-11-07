num=int(input('請輸入一個數:'))
list=[]
for li in range(2,num+1):
    list.append(li)

for n in range(2,num+1):
    for i in range(2,n):
        if n%i==0:
            if n in [a for a in list]:
                list.remove(n)

           
print(list)
    









                

                    
        






    


    
    

    
    


