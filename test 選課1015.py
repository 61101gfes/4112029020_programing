def addcourse():
    while True:
        print('輸入課程:')
        name=input('class name or "c" to cancel:')
        if name=='c':
            print('結束')
            break
        else:
            id=input('class id:')
            teacher=input('class teacher:')
            courses.append({'name':name,'id':id,'teacher':teacher,'coursestudent':[]})
            for i in range(len(courses)):
                print(i+1,courses[i])
                print(courses[i]['name'],courses[i]['id'],courses[i]['teacher'])

courses=[]


def addstudent():
    while True:
        print('開始加入學生:')
        name=input('student name or "c" to cancel:')
        if name=='c':
            print('結束')
            break
        else:
            id=input('student id:')
            
            students.append({'name':name,'id':id,'schdule':[]})
            for i in range(len(students)):
                print(f"{i+1},學生資訊:{students[i]}")
                print(f"加入學生資訊:{students[i]['name']},學號:{students[i]['id']}")

students=[]

def choicecourse():
    while True:
        print('開始選課:')
        check1=input('student id 或按c取消')
        if check1=='c':
            print('取消')
            break
        else:
            check2=input('請輸入想修課程代碼class id:')
            for i in range(len(students)):
                for a in range(len(courses)):
                    if check1==students[i]['id'] and check2==courses[a]['id']:
                        students[i]['schdule'].append(courses[a]['name'])
                        courses[a]['coursestudent'].append(students[i]['name'])
                        print( f"該名學生課表:{students[i]['schdule']}")
                        print( f"該課程所有學生:{courses[a]['coursestudent']}")


def classstudent():
    while True:
        a=input('輸入class id查詢修這門課的學生')
        if a=='c':
            print('結束')
            break
        else:
            for i in range(len(courses)):
                if a==courses[i]['id']:
                    print(f"下列為所有修這門課的學生{courses[i]['coursestudent']}\n")

def studentlist():
    while True:
        b=input('輸入student id查詢這名學生所選課程')
        if b=='c':
            print('結束')
            break
        else:    
            for i in range(len(students)):
                if b==students[i]['id']:
                    print(f"此學生:{students[i]['name']}\n所有修的課程為:{students[i]['schdule']}\n")
print('請先建立課程')
addcourse()
print('請先輸入學生資料')
addstudent()
choicecourse()
classstudent()
studentlist()