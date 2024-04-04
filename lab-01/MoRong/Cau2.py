import re
def tinh_tong_chuoi(chuoi):
    cac_so = re.findall(r'-?\d+', chuoi)
    tong_duong = 0
    tong_am = 0
    for so in cac_so:
        so = int(so)
        if so > 0:
            tong_duong += so
        elif so < 0:
            tong_am += so
    return tong_duong, tong_am
chuoi = "-100#^sdfkj8902w3ir021@swf-20"
tong_duong, tong_am = tinh_tong_chuoi(chuoi)
print("Giá trị dương:", tong_duong)
print("Giá trị âm:", tong_am)