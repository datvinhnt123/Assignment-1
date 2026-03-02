e="sitting here in a boring room sitting here in a boring room"
def words_counting(n):
    s=e.split()
    sum = 0
    q=input("What is the word you are looking for? :")
    for i in range(len(s)):
        if s[i]==q:
            sum+=1
    print("There are",sum,q,"in the text")
words_counting(e)

