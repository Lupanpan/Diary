def create_diary():
    try:
        with open("Diary.txt", "x") as f:
            f.write("=== My Personal Diary ===\n")
        print("Diary created!")
    except FileExistsError:
        print("Diary already exists!")

def add_entry():
    entry = input("Write your diary entry: ")
    with open("Diary.txt", "a") as f:
        f.write(entry + "\n")
    print("Entry added!")

