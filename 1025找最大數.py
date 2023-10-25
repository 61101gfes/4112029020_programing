num={'a': 5, 'b': 1, 'c': 3, 'd': 4, 'e': 2}
ranked=sorted(num.items() ,key=lambda x :x[1],reverse=True)
top3=ranked[:3]
print(top3[0][0],top3[1][0],top3[2][0])