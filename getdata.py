import subprocess
import urllib.request
#khai báo biến
i = 1
listchamp = []
listlink = []
listname = []
dicfix = {"\\xe1\\xbb\\xaf": "ữ", "\\xe1\\xbb\\x91": "ố", "\\xe1\\xbb\\x87": "ệ", "\\xc3\\xa2": "â", "\\xc4\\x90": "đ", "\\xc3\\xaa": "ê", "\\xe1\\xbb\\x81": "ề", "&#039;": "'", "\\xe1\\xbb\\x99": "ộ", "\\xc3\\xb4ng": "ô"}
#get image
for i in range(1, 108):
    try:
        if i <= 108:
            champ = f"https://lienquan.garena.vn/tuong-chi-tiet/{i}"
            listchamp.append(champ)
            result = subprocess.check_output(f'curl {champ}')
            tamthoi = str(result)
            bientam = tamthoi[tamthoi.find("tabs-content-skin ") + 31: tamthoi.find("tabs-content-skin ") + 92]
            #get name champ
            for name_champ in range(tamthoi.find("heroes-page"), tamthoi.find("heroes-page") + 100):
            print(tamthoi[tamthoi.find("heroes-page"): tamthoi.find("heroes-page") + 100])
            #get img champ
            urllib.request.urlretrieve(f"https://lienquan.garena.vn{str(bientam)}", f"{i}.jpg")
    except:
