class course:
    def __init__(self,name,id,time,teacher):
        self.name=name
        self.id=id
        self.time=time
        self.teacher=teacher
        self.students=[]

    def add_student(self,student):
      self.students.append(student)

    def remove_student(self,student):
      self.students.remove(student)

    def list_student(self):
      for student in self.students:
        print(f"修課學生:{student.name},學號:{student.id}")
    
   
    
def add_course():
      while True:
        x=input('請輸入要加入課程name or id:')
        if x=='c':
          print('結束123')
          break
        else:
          for i in range(len(courses)):
            if x==courses[i].name or x==str(courses[i].id):
              print(f"加入課程:{courses[i].name}  課程代碼:{courses[i].id}  課程時間:{courses[i].time}  老師:{courses[i].teacher}")
              print(courses[i].name) 
              schdule.append(courses[i].name)
              print(f"目前課程{schdule}") 
              
def remove():
    while True:
        r=input('請輸入要刪除課程name or id:')
        if r=='c':
          print('結束123')
          break
        else:
          for i in range(len(courses)):
            if r==courses[i].name or r==str(courses[i].id):              
             print(f"即將刪除課程:{courses[i].name}  課程代碼:{courses[i].id}  課程時間:{courses[i].time}  老師:{courses[i].teacher}")
             schdule.remove(courses[i].name)
             print(f"目前課程{schdule}")
             
schdule=[]        
courses=[]    
def view():
  for i in range(len(courses)):
    print(f"{i+1},{courses[i].name},{courses[i].id},{courses[i].time},{courses[i].teacher}")        

class student:
    def __init__(self,name,id):
      self.name=name
      self.id=id
      self.courses=[]
    def list_courses(self):
        for course in self.courses:
            print(f"課程名稱{course.name},課程代碼 {course.id}")
    def add_course(self, course):
        self.courses.append(course)
def enroll():
  while True:
    cancel=input('輸入c結束或輸入任何地方繼續')
    if cancel=='c':
      print('結束')
      break
    else:
        student_id=input('student id:')
        course_id=input('course id:')
        coursefound=None
        studentfound=None
        for course in courses:
          if course_id==str(course.id):
            coursefound=course
            break
        for student in students:
          if student_id==str(student.id):
            studentfound=student
            break
        if coursefound is not None and studentfound is not None:
          studentfound.add_course(coursefound)  

def list_student_courses():
    while True:
        student_id =input('請輸入學生學號 (輸入"c"結束): ')
        if student_id == 'c':
            print('結束')
            break

        student_found = None
        for student in students:
            if student_id == str(student.id):
                student_found = student
                break

        if student_found is not None:
            print(f"{student_found.name} 選的課程:")
            student_found.list_courses()
        else:
            print("無效的學號")

# 列出某一課程有哪些學生選
def list_course_students():
    course_code = input('請輸入課程代碼: ')

    course_found = None
    for course in courses:
        if course_code == str(course.id):
            course_found = course
            break

    if course_found is not None:
        print(f"{course_found.name} 課程的學生:")
        course_found.list_student()
    else:
        print("無效的課程代碼")                  


students=[]    
def watch():
  for a in range(len(students)):
      print({a+1},{students[a].name},{students[a].id})









while True:
  n=input('課程name:')
  if n=='c':
    print('結束')
    break
  i=int(input('課程id:'))
  if i>10000:
    i=int(input('id只能輸入4碼,請再輸入一次'))
  t=input('上課時間time:')
  tc=input('授課老師teacher:')
  courses.append(course(n,i,t,tc))
  view()

while True:
  sn=input('student name:')
  if sn=='c':
    print('結束')
    break
  sid=int(input('student id:'))
  if sid>10000000000:
    sid=int(input('學號不得超過十碼'))
  elif sid<1000000000:
    sid=int(input('學號需要十碼'))
  sn=sn.title()
  students.append(student(sn,sid))
  watch()

while True:
    print("選擇操作:")
    print("1. 學生選課")
    print("2. 列出學生所選課程")
    print("3. 列出課程的學生清單")
    choice = input("請輸入選項 (1/2/3或輸入 'c' 結束): ")

    if choice == '1':
        enroll()
    elif choice == '2':
        list_student_courses()
    elif choice == '3':
        list_course_students()
    elif choice == 'c':
        print("結束")
        break
    else:
        print("無效的選項")