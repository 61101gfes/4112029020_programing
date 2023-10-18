import itertools
import random
def addstudent():
  while True:
    name=input('輸入學生姓名 c取消:')
    if name== 'c':
      print('結束')
      break
    else:
      subject_a=int(input('請輸入該學生a考卷成績:'))
      if subject_a>100:
        print('wrong grade')
        continue
      subject_b=int(input('請輸入該學生b考卷成績:'))
      if subject_b>100:
        print('wrong grade')
        continue
      average=(subject_a+subject_b)/2
      students.append({'name':name,'grade':[subject_a,subject_b],'average':average})
      for i in range(len(students)):
        print(f" 該學生{students[i]['name']}成績:{students[i]['grade']}")
      for s in students:
        if name ==s['name']:
          print(s['average'])
    
students=[]
addstudent()
sortstudent=sorted(students, key=lambda x: x['average'], reverse=True )
for student in sortstudent:
        print(f"學生：{student['name']} 平均成績：{student['average']}")
top5=sortstudent[:5]
for i in range(len(top5)):
  print(f"成績排名{i+1}學生{top5[i]['name']}平均{top5[i]['average']}")
pick=random.sample(top5,3)
for a in pick:
  print(f"隨機挑選出三名{a['name']}")
pick3=iter(pick)
for p in pick3:
  print(f"iter後{p}")
