class customs:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.car={}
member=[]
books={}
books['1']={'name':'a','price':150,'remain':10}
books['2']={'name':'b','price':450,'remain':1}
books['3']={'name':'c','price':200,'remain':20}
books['4']={'name':'d','price':120,'remain':100}
books['5']={'name':'e','price':1050,'remain':1000}

while True:
    name=input('請輸入會員名稱:')
    if name=='end':
        break
    elif name in [a.name for a in member]:
        print('重複加入')
    else:
        id=input('請輸入會員號碼:')
        member.append(customs(name,id))

while True:
    name=input('請輸入會員名稱:')
    if name=='end':
        break
    else:
        found=0
        for m in member:
            if name in m.name:
                found+=1
                people=m
        if found==0:
            print('找不到該會員')
            continue
        id=input('請輸入書籍代碼:')
        found2=0
        for key,value in books.items():
            if id in key:
                found2+=1
                bookname=key
                bookprice=value['price']
                bookremain=value['remain']
        if found2==0:
            print('找不到該書籍')
            continue
        num=int(input('請輸入購買數量:'))
        if num>bookremain:
            print('庫存不足')
            continue
        else:
            people.car[bookname]={'price':bookprice,'num':num}
            bookremain-+num

while True:
    name=input('請輸入會員名稱:')
    if name=='end':
        break
    else:
        found=0
        for m in member:
            if name in m.name:
                found+=1
                people=m
        if found==0:
            print('找不到該會員')
            continue
        sum=0
        for key,value in people.car.items():
            total=value['price']*value['num']
            sum+=total
        print(f"顧客{people.name}一共消費{sum}")






                

                    
        






    


    
    

    
    


