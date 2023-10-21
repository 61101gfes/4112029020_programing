books=[]
def book():
    books.append({'name':'english','id':'1111','price':100,'remain':10,'buyer':[]})
    books.append({'name':'music','id':'2222','price':1200,'remain':20,'buyer':[]})
    books.append({'name':'pe','id':'1234','price':150,'remain':23,'buyer':[]})
    books.append({'name':'chinese','id':'3333','price':200,'remain':50,'buyer':[]})
customs=[]
def custom():
    customs.append({'name':'a','id':'1','car':[]})
    customs.append({'name':'b','id':'2','car':[]})
    customs.append({'name':'c','id':'3','car':[]})

def buy():
    while True:
        name=input('請輸入你的姓名或代碼:')
        custom_found=0
        book_found=0
        want=0
        
        if name =='end':
            print('結束')
            custom_found=1
            book_found=1
            break
        else:
            nameid=input('book name or id:')
            for i in range(len(customs)):
                for k in range(len(books)):
                    if name == customs[i]['name'] or name == customs[i]['id']:
                        custom_found+=1
                        
                        if nameid==books[k]['name'] or nameid==books[k]['id']:
                            num=int(input('購買數量:'))
                            want=books[k]['name']
                            
                            if want in [c['書名'] for c in customs[i]['car']]:
                                book_found+=1
                                for c in customs[i]['car']:
                                    c['數量']+=num
                                    books[k]['remain']-=num
                                    print(customs[i]['car'])

                                
                            else:
                                if num>books[k]['remain']:
                                    book_found+=1
                                    print('庫存不足')
                                    continue
                                else:
                                    customs[i]['car'].append({'書名':books[k]['name'], '數量':num, '價格':books[k]['price']})
                                    books[k]['buyer'].append({customs[i]['name']})
                                    books[k]['remain']-=num
                                    
                                    book_found+=1
                                    print(customs[i]['car'])
            if book_found==0:
                print('找不到書')
            if custom_found==0:
                print('錯誤顧客資料')
            

           

                
            
            
                
                    
                    
book()
custom()
buy()

