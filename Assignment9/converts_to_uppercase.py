def convert_to_uppercase(text,output):
    result = []
    with open(text,'r',encoding="utf-8") as f:
        for i in f:
            for j in i:
                q= j.upper()
                result.append(q)
    with open(output,'w',encoding="utf-8") as a:
        a.writelines(result)
convert_to_uppercase("paragraph.txt","output.txt")
