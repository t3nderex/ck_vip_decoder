import re


def read_ck_vip(path):
    return open(path,'rt').read()


def str_to_integer(str):
    return list(map(int, str))


def is_ck_encoded_url_format(str):
    if str[0] == 263 and str[1] ==275:
        return True
    else:
        return False

    
def decode(list):
    list = [i-=159 for i in list]
    return list


if __name__ =="__main__":
    ck_vip = ""                     # 파일 경로
    script = read_ck_vip(ck_vip)

    p = re.compile(r'(2\d\d)+')     # "2xx" 의 정규식 -> url 형식을 찾아내기 위함
    malware_str_li = p.findall(script)
    malware_int_li= str_to_integer(malware_ascii_li)

    is_ck_vip = is_ck_encoded_url_format(malware_int_li)

    if is_ck_vip:
        decode_data = decode(malware_int_li)

    print(f"최종 유포 URL:{docde_data}")
