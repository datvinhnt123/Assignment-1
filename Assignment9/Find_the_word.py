def find_the_word(word, file):
    result = []
    with open(file, "r", encoding="utf-8") as f:
        line_numbers=1
        for line in f:
            if word in line:
                result.append(line_numbers)
            line_numbers+=1
    return result

print(find_the_word("mk", "paragraph.txt"))