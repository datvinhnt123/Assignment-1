import re
s="#ABC292"
def hex_color(code: str) -> bool:
    spec=re.findall(r'#([A-Fa-f0-9]{6})', code)
    print(bool(spec))
hex_color(s)