with open('grades.csv', 'r', encoding='utf-8') as f:
    best_student = ""
    best_avg = 0
    subject_sums = [0, 0, 0, 0, 0]
    student_count = 0
    student_averages = []
    for line in f:
        parts = line.strip().split(",")
        name = parts[0] + " " + parts[1]
        grades = list(map(int, parts[2:]))
        avg = sum(grades) / len(grades)
        student_averages.append((name, avg))
        if avg > best_avg:
            best_avg = avg
            best_student = name
        for i in range(5):
            subject_sums[i] += grades[i]
        student_count += 1
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write("СЕРЕДНІ БАЛИ СТУДЕНТІВ:\n")
    for name, avg in student_averages:
        f.write(f"{name}: {round(avg, 1)}\n")
    f.write(f"\nКРАЩИЙ СТУДЕНТ: {best_student} ({round(best_avg, 1)})\n")
    f.write("\nСЕРЕДНІ БАЛИ З ПРЕДМЕТІВ:\n")
    for i in range(5):
        subject_avg = subject_sums[i] / student_count
        f.write(f"Предмет {i + 1}: {round(subject_avg, 1)}\n")