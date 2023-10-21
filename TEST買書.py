inventory={}
buy={}
def book():
  inventory['a']={'remain':5,'price':100,'id':1}
  inventory['b']={'remain':10,'price':500,'id':2}
  inventory['c']={'remain':15,'price':120,'id':3}
  inventory['d']={'remain':20,'price':500,'id':4}
  inventory['e']={'remain':25,'price':1200,'id':5}
  inventory['f']={'remain':30,'price':1000,'id':6}
def addbook():
    while True:
        name=input('name:')
        if name =='end':
            print('結束')
            break
        elif name in inventory:
            quantity=int(input('quantity:'))
            inventory[name]['remain']+=quantity
            
            print(inventory)
        else:
            remain=int(input('quantity:'))
            price=int(input('price:'))
            id = input('id:')
            inventory[name]={'remain':remain , 'price':price ,'id':id}
            print(inventory)  

def purchase():
  buy.clear()
  while True:
    found=False
    name=input('name or id')
    if name =='end':
      break
    else:
      
      for key,value in inventory.items():
        if name==str(value['id']) or name==key:
          quantity=int(input('how many'))
          if quantity>value['remain']:
            print('不夠')
            continue
          else:
            found=True
            buy[key]={'name':key, 'price':value['price'], 'quantity':quantity}
            value['remain']-=quantity
            print(buy)
    if not found:
        print('找不到')
           

def total():
  sum=0
  for key,value in buy.items():
    money=value['price']*value['quantity']
    sum+=money
  print(sum)
  return sum
  

book()
addbook()
purchase()
total()  

print(inventory)
