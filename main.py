import subprocess
import urllib.request
import re
#khai báo biến
i = 1
listchamp = []
listlink = []
listname = []
dicfix = {"\\xe1\\xbb\\xaf": "ữ", "\\xe1\\xbb\\x91": "ố", "\\xe1\\xbb\\x87": "ệ", "\\xc3\\xa2": "â", "\\xc4\\x90": "đ", "\\xc3\\xaa": "ê", "\\xe1\\xbb\\x81": "ề", "&#039;": "'", "\\xe1\\xbb\\x99": "ộ", "\\xc3\\xb4": "ô"}
#get image
champ = f"https://lienquan.garena.vn/tuong-chi-tiet/1"
listchamp.append(champ)
result = subprocess.check_output(f'curl https://lienquan.garena.vn/tuong-chi-tiet/1')
tamthoi = str(result)
bientam = tamthoi[tamthoi.find("tabs-content-skin ") + 31: tamthoi.find("tabs-content-skin ") + 92]
#get name
result1 = subprocess.check_output(f'curl https://lienquan.garena.vn/tuong')
tam = str(result1)
try:
    for numcham in range(1, 107):
        dataname = tam[tam.find(f"champion-{numcham}") + 100: tam.find(f"champion-{numcham}") + 190]
        clean_name = dataname[dataname.find('">') :dataname.find(",")]
        num_less = 0
        final_name = clean_name[2:None]
        listname.append(final_name)
except:
    pass
listkey = ["\\xc3\\xa2", "\\xc4\\x90", "\\xc3\\xaa", "\\xc3\\xb4", "\\xe1\\xbb\\x91", "\\xe1\\xbb\\xaf", "\\xe1\\xbb\\x87", "\\xe1\\xbb\\x81", "\\xe1\\xbb\\x99", "&#039;"]
var1 = str()
var2 = str()

for i in listname:
    num_list = listname.index(i)
    while str(i.isalpha()) == "False":
        for bien in listkey:
            if i.find(str(bien)) == 1:
                name_1 = dicfix.get(bien)
                var1 = i.replace(bien, name_1)
                listname[num_list] = var1
print(listname)
