scores = [
['Justin', 89, 90, 100],
['Tom', 92, 87, 100],
['Jane', 90, 90, 100],
['Philip', 89, 95, 100]
]
def calculate(scores):
    student_score=[(name, (a + b + c)/3) for name ,a,b,c in scores ]
    max_average = max(student_score, key=lambda x: x[1])
    print(student_score)
    return max_average



maxstudent=calculate(scores)
print(f"成績最高的是{maxstudent[0]} 平均成績{maxstudent[1]}")