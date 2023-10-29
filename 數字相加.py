no1={'a':1 , 'b':5  ,'c':10  , 'd':1, 'e':56, 'g':10}
no2={'a':1 , 'c':5  ,'g':10  }
new={}
for n1 in no1:
    if n1 in no2:
        total=no1[n1]+no2[n1]
        new[n1]={total}
print(new)

#for n2 in no2:
        #if n1 in n2:
            
            #total=no1[n1]+no2[n2]
            #new[n1[0]]={total}
#print(new)

    
    
            