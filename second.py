dicfix = {"\\xe1\\xbb\\xaf": "ữ", "\\xe1\\xbb\\x91": "ố", "\\xe1\\xbb\\x87": "ệ", "\\xc3\\xa2": "â", "\\xc4\\x90": "đ", "\\xc3\\xaa": "ê", "\\xe1\\xbb\\x81": "ề", "&#039;": "'", "\\xe1\\xbb\\x99": "ộ", "\\xc3\\xb4ng": "ô"}

print(dicfix.get("\\xe1\\xbb\\xaf"))

import re

a = ["a", "w", "g", "h"]
a[a.index("w")] = "j"
print(a)

b = " Hoang nguyen van\\sss aas\\ass"

x = b.replace("\\sss", "hhhhhh")
print(x)
