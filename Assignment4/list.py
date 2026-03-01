import re

s="ABC292"
def is_valid_course_code(code: str) -> bool:
    pattern = re.findall(r'^[A-F]{3}[0-9]{3}$',code)
    print(bool(pattern))
is_valid_course_code(s)