fruit= {'1': 'Apple', '2': 'Orange', '3': 'Pineapple', '4': 'watermelon'}
list1=[]
for key,value in fruit.items():
    if len(value)<6:
        list1.append(key)
for i in list1:
    del fruit[i]





print(f"被刪除後{fruit}")       