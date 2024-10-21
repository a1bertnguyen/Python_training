if __name__ == '__main__':
    n = int(input("Nhập số lượng học sinh: "))
    students = []

    for _ in range(n):
        name = input("Nhập tên học sinh: ")
        score = float(input("Nhập điểm số của học sinh: "))
        students.append([name, score])

    print("\nDanh sách học sinh:")
    for student in students:
        print(f"Tên: {student[0]}, Điểm: {student[1]}")
