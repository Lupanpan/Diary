def create_diary():
    try:
        with open("Diary.txt", "x") as f:
            f.write("=== My Personal Diary ===\n")
        print("Diary created!")
    except FileExistsError:
        print("Diary already exists!")
