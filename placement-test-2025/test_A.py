# Вводится число N - число посылок в контест от студентов.
# Далее вводится N строк: Фамилия студента, номер задачи и вердикт Яндекс контеста через пробел.
# Задача считается сданной, если получила вердикт "OK".
# Студент мог сдавать задачу несколько раз: если хотя бы одна попытка получила вердикт "ОК", задача считается сданной.
# Формат вывода
# Информация о каждом студенте: фамилия, количество отправленных посылок, количество сданных задач.
# Студенты должны быть отсортированы в алфавитном порядке.
# exam_data = [{"last_name":"Taylor","task_id":0,"result":"ERR"},{"last_name":"Williams","task_id":1,"result":"OK"},{"last_name":"Taylor","task_id":3,"result":"ERR"},{"last_name":"Davis","task_id":0,"result":"ERR"},{"last_name":"Davis","task_id":2,"result":"ERR"},{"last_name":"Garcia","task_id":0,"result":"ERR"},{"last_name":"Jones","task_id":3,"result":"ERR"},{"last_name":"Taylor","task_id":0,"result":"ERR"},{"last_name":"Taylor","task_id":1,"result":"ERR"},{"last_name":"Garcia","task_id":2,"result":"ERR"},{"last_name":"Brown","task_id":2,"result":"OK"},{"last_name":"Anderson","task_id":4,"result":"OK"},{"last_name":"Jones","task_id":3,"result":"ERR"},{"last_name":"Miller","task_id":1,"result":"ERR"},{"last_name":"Smith","task_id":2,"result":"ERR"},{"last_name":"Davis","task_id":2,"result":"OK"},{"last_name":"Williams","task_id":3,"result":"OK"},{"last_name":"Williams","task_id":4,"result":"ERR"},{"last_name":"Brown","task_id":4,"result":"OK"},{"last_name":"Davis","task_id":0,"result":"ERR"},{"last_name":"Williams","task_id":3,"result":"ERR"},{"last_name":"Brown","task_id":0,"result":"ERR"},{"last_name":"Johnson","task_id":4,"result":"OK"},{"last_name":"Davis","task_id":0,"result":"ERR"},{"last_name":"Brown","task_id":0,"result":"ERR"},{"last_name":"Davis","task_id":3,"result":"OK"},{"last_name":"Smith","task_id":4,"result":"ERR"},{"last_name":"Jones","task_id":2,"result":"ERR"},{"last_name":"Taylor","task_id":0,"result":"OK"},{"last_name":"Garcia","task_id":3,"result":"ERR"},{"last_name":"Garcia","task_id":3,"result":"ERR"},{"last_name":"Davis","task_id":4,"result":"OK"},{"last_name":"Brown","task_id":1,"result":"ERR"},{"last_name":"Johnson","task_id":3,"result":"ERR"},{"last_name":"Garcia","task_id":4,"result":"OK"},{"last_name":"Davis","task_id":1,"result":"ERR"},{"last_name":"Anderson","task_id":3,"result":"ERR"},{"last_name":"Miller","task_id":0,"result":"ERR"},{"last_name":"Taylor","task_id":0,"result":"ERR"},{"last_name":"Brown","task_id":0,"result":"ERR"},{"last_name":"Johnson","task_id":0,"result":"ERR"},{"last_name":"Taylor","task_id":2,"result":"OK"},{"last_name":"Davis","task_id":2,"result":"ERR"},{"last_name":"Brown","task_id":3,"result":"ERR"},{"last_name":"Anderson","task_id":0,"result":"ERR"},{"last_name":"Miller","task_id":2,"result":"ERR"},{"last_name":"Taylor","task_id":3,"result":"ERR"},{"last_name":"Brown","task_id":3,"result":"ERR"},{"last_name":"Jones","task_id":1,"result":"ERR"},{"last_name":"Williams","task_id":1,"result":"ERR"},{"last_name":"Brown","task_id":1,"result":"ERR"},{"last_name":"Jones","task_id":3,"result":"ERR"},{"last_name":"Garcia","task_id":4,"result":"ERR"},{"last_name":"Garcia","task_id":1,"result":"ERR"},{"last_name":"Taylor","task_id":2,"result":"ERR"},{"last_name":"Johnson","task_id":2,"result":"ERR"},{"last_name":"Garcia","task_id":2,"result":"ERR"},{"last_name":"Jones","task_id":1,"result":"ERR"},{"last_name":"Brown","task_id":3,"result":"ERR"},{"last_name":"Garcia","task_id":2,"result":"OK"},{"last_name":"Garcia","task_id":2,"result":"ERR"},{"last_name":"Taylor","task_id":4,"result":"ERR"},{"last_name":"Smith","task_id":1,"result":"ERR"},{"last_name":"Anderson","task_id":0,"result":"OK"},{"last_name":"Anderson","task_id":1,"result":"ERR"},{"last_name":"Johnson","task_id":1,"result":"OK"},{"last_name":"Smith","task_id":4,"result":"ERR"},{"last_name":"Johnson","task_id":4,"result":"ERR"},{"last_name":"Johnson","task_id":0,"result":"ERR"},{"last_name":"Williams","task_id":3,"result":"ERR"},{"last_name":"Taylor","task_id":2,"result":"ERR"},{"last_name":"Miller","task_id":2,"result":"ERR"},{"last_name":"Miller","task_id":4,"result":"ERR"},{"last_name":"Taylor","task_id":2,"result":"ERR"},{"last_name":"Miller","task_id":1,"result":"OK"},{"last_name":"Garcia","task_id":1,"result":"ERR"},{"last_name":"Brown","task_id":2,"result":"ERR"},{"last_name":"Smith","task_id":2,"result":"ERR"},{"last_name":"Miller","task_id":3,"result":"ERR"},{"last_name":"Anderson","task_id":2,"result":"ERR"},{"last_name":"Brown","task_id":1,"result":"ERR"},{"last_name":"Garcia","task_id":4,"result":"ERR"},{"last_name":"Taylor","task_id":4,"result":"ERR"},{"last_name":"Garcia","task_id":4,"result":"ERR"},{"last_name":"Johnson","task_id":4,"result":"ERR"},{"last_name":"Jones","task_id":4,"result":"ERR"},{"last_name":"Miller","task_id":2,"result":"ERR"},{"last_name":"Anderson","task_id":0,"result":"ERR"},{"last_name":"Taylor","task_id":3,"result":"ERR"},{"last_name":"Anderson","task_id":1,"result":"ERR"},{"last_name":"Davis","task_id":3,"result":"ERR"},{"last_name":"Miller","task_id":4,"result":"ERR"},{"last_name":"Jones","task_id":3,"result":"ERR"},{"last_name":"Garcia","task_id":0,"result":"ERR"},{"last_name":"Johnson","task_id":4,"result":"ERR"},{"last_name":"Smith","task_id":4,"result":"OK"},{"last_name":"Miller","task_id":0,"result":"ERR"},{"last_name":"Taylor","task_id":1,"result":"ERR"},{"last_name":"Taylor","task_id":3,"result":"ERR"},{"last_name":"Anderson","task_id":1,"result":"ERR"}]
# conn = sqlite3.connect("./placement-test-2025/my.db")
# cur.execute("""
# SELECT
#     last_name,
#     COUNT(*) AS total_attempts,
#     SUM(CASE WHEN result = 'OK' THEN 1 ELSE 0 END) AS ok_count
# FROM exam_results
# GROUP BY last_name
# ORDER BY last_name ASC;
# """)
import sqlite3

connection = sqlite3.connect(":memory:")
cur = connection.cursor()
cur.execute("CREATE TABLE exam_results (last_name TEXT, task_id INTEGER, result TEXT)")

n = int(input())
exam_data = []
for i in range(0, n):
	last_name, task_id, result = map(str, input().split())
	cur.execute("INSERT INTO exam_results (last_name, task_id, result) VALUES (?, ?, ?)", (last_name, task_id, result))
connection.commit()

cur.execute("""
SELECT
    last_name,
    COUNT(*) AS total_attempts,
    COUNT(DISTINCT CASE WHEN result = 'OK' THEN task_id END) AS ok_count
FROM exam_results
GROUP BY last_name
ORDER BY last_name ASC;
""")
rows = cur.fetchall()
for row in rows:
    print(*row)
