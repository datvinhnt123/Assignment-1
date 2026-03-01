import re
o="Today is January 16, 2025. The temperature is 11 degrees Celsius."

def sum(s: str):
    p=0
    e=re.findall(r'[0-9]+', s)
    for i in e:
        p+=int(i)
    print(p)
sum(o)