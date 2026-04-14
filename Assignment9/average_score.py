def input_name_score(file):
    with open(file,'r', encoding="utf-8") as f:
        score=[]
        for line in f:
            for i in line.split(","):
                try:
                    score.append(float(i))
                except:
                    continue

    total=sum(score)/len(score)
    return total


print(input_name_score("test_score.txt"))

