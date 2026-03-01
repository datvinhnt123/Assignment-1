import re

s = "today is +84231123121 then u are nuggets 0347012911"

def phone_privacy(num: str):
    pattern = re.compile(r'\+84[0-9]{9}|[0-9]{10}')
    return re.sub(pattern, "REDACTED", num)

print(phone_privacy(s))



