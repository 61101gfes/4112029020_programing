class students:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.schdule=[]
class courses(students): 
    def __init__(self,name,id):
        super().__init__(name,id)  
        self.list=[]     
studentlist=[]
allcourses=[courses('國文','1')  ,courses('英文','2')  ,courses('體育','3'),  courses('通識','4'),courses('音樂','5')]

while True:
    name=input('正在加入學生...\n請輸入學生姓名:')
    if name=='end':
        break
    elif name in [s.name for s in studentlist]:
        print('重複')
        continue
    else:
        id=str(input('請輸入學生代碼:'))
        student=students(name,id)
        studentlist.append(student)

while True:
    print('開始選課程...')
    nameid=input('請輸入你的學生姓名或代碼:')
    check=0
    if nameid=='end':
        check+=1
        break
    else:
        for s in studentlist:
            if nameid in s.name or nameid in s.id:
                people=s
                check+=1
                print(f"你好{s.name}")
        if check==0:
            print('找不到學生')
            continue    
        
    nid=input('請輸入課程名稱或代碼:')
    for a in allcourses:
        if nid in a.name or nid in a.id:
            print(f"學生{people.name}加入{a.name}")
            a.list.append(people.name)
            people.schdule.append(a.name)

while True:
    print('開始尋找這堂課的修課名單')
    nameid =input('請輸入你要查找課程名稱代碼:')
    if nameid=='end':
        break
    else:
        for a in allcourses:
            if nameid in a.name or nameid in a.id:
                print(f"這堂課{a.name}的學生有{len(a.list)}人:")
                print(a.list)

    


