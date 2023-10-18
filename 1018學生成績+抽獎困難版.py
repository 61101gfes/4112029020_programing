import re
import itertools
import random

def calculate_average(scores_a,scores_b): 
    return (scores_a+scores_b)/2
avg_scores = {}
# 請依據提示完成程式碼，勿修改變數名稱
def main():
    student_scores = {} # 此為儲存學生姓名與成績的字典
    student_count = 0  # 初始化學生人數為 0

    while True: # (40%)
       # 使用迴圈設定條件使程式能執行或停止
       # 使用 re模組檢查，學生姓名只能包含字母，成績必須為數字
        student_name = input("輸入學生姓名（輸入end則結束輸入成績）： ")
        if student_name=='end':
            print('結束')
            break
        elif not re.match("^[A-Za-z]+$", student_name):
            print("學生姓名只能包含字母，请重新输入。")
            continue
        else:
            subject_a=input('請輸入a卷的成績')
            subject_b=input('請輸入b卷的成績')
            if not subject_a.isdigit() or not subject_b.isdigit():
                print("成绩必须是数字，请重新输入。")
                continue
            
            else:
                c=calculate_average(int(subject_a),int(subject_b))
                student_scores[student_name]={'score_a':subject_a,'score_b':subject_b,'average':c}
                avg_scores[student_name]={'average_grade':c}
                student_count += 1
    print("學生成績單：")
    for student, scores in student_scores.items():
        print(f"學生姓名: {student}, a卷成绩: {scores['score_a']}, b卷成绩: {scores['score_b']}, 平均成绩: {scores['average']}")
        print(avg_scores)#{'a': {'average_grade': 50.5}, 's': {'average_grade': 50.0}}

    print(f"全班共有 {student_count} 位學生")
    ranked_students = sorted(avg_scores.items(), key=lambda x: x[1]['average_grade'], reverse=True)        
    print("學生成績排名：")
    for i, (student, scores) in enumerate(ranked_students, start=1):
        print(f"第{i}名 {student} 平均成绩: {scores['average_grade']}")
    top_six_students = ranked_students[:6]
    if len(top_six_students) >= 3:
        winners = random.sample(top_six_students, 3) # random為隨機抽取三位
        print("\n中獎學生：")
        for i, (student, scores) in enumerate(winners, start=1):
          print(f"第{i}名中獎人 {student} 平均成绩: {scores['average_grade']}")
      
    return student_scores
if __name__ == "__main__":
    main()