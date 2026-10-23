elete_all()

    student.insert("뽀로로", 5, 90)
    student.insert("크롱", 4, 95)

    student.show_all()

    # 조회 조건 추가
    for row in student.select_by_score(92):
        print(row)

    student.update_score("뽀로로", 100)
    student.show_all()

    student.delete("크롱")
    student.show_all()