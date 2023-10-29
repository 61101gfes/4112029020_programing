class custom:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.car={}
    

books=[{'name':'a','price':100},{'name':'b','price':120},
       {'name':'c','price':230},{'name':'d','price':620},{'name':'e','price':200},{'name':'f','price':600},{'name':'g','price':120}]
    
list=[]
while True:
    name=input('name:')
    if name =='end':
        break
    elif name in [a.name for a in list]:
        print('重複加入')
        continue
    
    else:
        id =input('id:')
        new=custom(name,id)
        list.append(new)
        for a in list:
            print(a.name)

while True:
    name=input('custom name:')
    if name=='end':
        break
    else:
        buy=input('book name or id:')
        for i in range(len(books)):
            for a in list:
                if name ==a.name and buy ==books[i]['name']:
                    print(books[i])
                    a.car[books[i]['name']]=books[i]['price']
                    print(a.car)

while True:
    name=input('custom name to pay:')
    if name=='end':
        break
    else:
        sum=0
        for a in list:
            if name in a.name:
                for key ,value in a.car.items():
                    an=a.name
                    ac=a.car
                    sum+=value
        ac['total']=sum
        print(f"顧客{an}需付:{ac['total']}元")

    


