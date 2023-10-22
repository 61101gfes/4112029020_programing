inventory={}
import itertools
def book():
    inventory['國文']={'author':'古人','date':'1000'}
    inventory['英文']={'author':'mr','date':'200'}
def addbook():
    while True:
        print('請新增書籍至書庫')
        name=input('請輸入書籍名稱:')
        if name=='end':
            print('結束')
            break
        elif name in inventory:
            print('已經存在')
            continue
        else:
            author=input('請輸入作者:')
            date=input('請輸入出版日期:')
            inventory[name]={'author':author,'date':date}
            print(inventory)

def search():
    while True:
        found=False
        name=input('請輸入書籍名稱或作者尋找書籍資訊:')
        if name=='end':
            print('結束')
            found=True
            break
        else:
            for key,value in inventory.items():
                
                if name == key or name ==value['author']:
                    found=True
                    print(inventory[key])
                    print(f"書名:{key} 作者:{value['author']} 出版日期:{value['date']}")
            if found==False:
                print('找不到此書')        
           
def group_by(criteria):
    sorted_inventory = sorted(inventory.items(), key=lambda x: x[1][criteria])
    for key, group in itertools.groupby(sorted_inventory, key=lambda x: x[1][criteria]):
        print(f'分組條件: {criteria} = {key}')
        for item in group:
            print(item[0], item[1])
book()
addbook()
search()
group_by('author')
