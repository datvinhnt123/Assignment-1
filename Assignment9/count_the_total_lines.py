def count_lines(file):
    count = 0
    #ở đây em dùng encoding để nhận diện cả tiếng việt lẫn tiếng anh nhé thầy:>
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() != "":
                count = count + 1
    return count


result = count_lines("paragraph.txt")
print(result)