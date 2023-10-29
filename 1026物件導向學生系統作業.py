class students:
    def __init__(self,name):
        self.name=name
        self.grade={}

class gradebook:
    def __init__(self):
        self.student_list=[]
    def addstudent(self,student):
        self.student_list.append(student)
        
    def addscore(self,name,subject,score):
        for s in self.student_list:
            if name== s.name:
                s.grade[subject]=score
                return
        raise ValueError(f"找不到名為{name}的學生")
    def list(self,name):
        search=input('請輸入你想要尋找學生:')
        for s in self.student_list:
            if search in s.name:
                print(f"學生{s.name}的成績單:{s.grade}")
            else:
                print('找不到')
    def average(self,subject):
        sum=0            
        count=0
        for s in self.student_list:
            for key,value in s.grade.items():
                if subject in key:
                    sum+=value
                    count+=1
                    
        print(f"科目{key}的平均成績為:{sum/count}分")
    def studentavg(self,name):
        sum=0 
        count=0     
        for a in self.student_list:
            if name in a.name:
                for key,value in a.grade.items():
                    sum+=value
                    count+=1
                    a=sum/count
        print(f"學生{name}成績平均為:{a}")
                        
                    

                
                    

            

gb=gradebook()

while True:
    print('現在進行加入學生成績')
    name=input('請輸入學生姓名 或list查看某學生 或end結束:')
    if name =='end':
        
        print('結束')
        break
    elif name in [i.name for i in gb.student_list]:
        subject=input('subject:')
        score=float(input('the subjects grade:'))
        gb.addscore(name,subject,score)
    elif name=='list':
        gb.list(name)    
    else:
        student=students(name)
        gb.addstudent(student)
        g=[s.name for s in gb.student_list]
        print(f"學生{g}")
        print('加入成功')
        subject=input('subject name:')
        score=float(input('the subjects grade:'))
        gb.addscore(name,subject,score)
while True:
    print('現在進行計算學生成績平均')
    name=input('請輸入學生姓名 或list查看某學生 或end結束:')
    if name =='end': 
        print('結束')
        break
    else:
        gb.studentavg(name)
    



while True:
    print('現在進行計算科目平均成績')
    
    subject=input('請輸入想要計算平均的科目:')
    if subject=='end':
            print('結束')
            break
    else:
            gb.average (subject)   
      




        






