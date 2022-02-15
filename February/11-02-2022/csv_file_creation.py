import csv

header = ['name', 'english', 'math', 'chemistry']
data = [
    ['Hari', 70, 80, 60],
    ['Alisha', 30, 40, 60]
]
with open('student_result.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
