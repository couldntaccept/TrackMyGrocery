from bottle import route, get, post, error, request, static_file
import re
from datetime import date
import easyocr
global reader
reader = easyocr.Reader(['en'])



@route("/img/<picture:path>")
def serve_pictures(picture):
    return static_file(picture, root="static/img/")



@route("/hello")
def hello():
    return "hello,world"



@route("/profile/<uid>")
def get_profile_pic(uid):
    return static_file("{}.jpeg".format(uid), root="static/profile/")



@post("/profile/update")
def update_profile_pic():
    media = request.files.get("media")
    uid = request.forms.get("uid")
    media.save("static/profile/{}.jpeg".format(uid), overwrite=True)

    # print(media.filename)
    # print(uid)
    return "1"



@post("/item/update")
def update_item_pic():
    media = request.files.get("media")
    item_id = request.forms.get("item_id")
    print("item id, ", item_id)
    media.save("static/item/{}.jpeg".format(item_id), overwrite=True)

    # result = reader.readtext("static/item/{}.jpeg".format(item_id))
    # print(result)
    return "hello world"



@post("/ocr")
def ocr():
    media = request.files.get("media")
    print(dict(request.files))
    print(dict(request.forms))
    print(dict(request.params))
    
    print("------------------------")
    # return "2021-12-12"
    name = media.filename
    media.save("static/ocr/{}".format(name), overwrite=True)
    return extrace_date("static/ocr/{}".format(name))
    



def extrace_date(path:str):
    result = reader.readtext(path)
    if not result:
        return None
    str_ls = [i[1] for i in result]
    s = "".join(str_ls)
    date_str = _process_date(s)
    return date_str


mon_ls = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")
year_ls = ('2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029')
short_year_ls = ('21', '22', '23', '24', '25', '26')
def _process_date(string : str) -> str :
    date_res = [0, 0, 0]
    string = string.upper()
    print(string)
    for mon in mon_ls:
        if mon in string:
            date_res[1] = mon_ls.index(mon) + 1
            nums = re.split(r'[\D]+', string)
            nums = [i for i in nums if i]
            print(nums)
            if (len(nums) < 1 ) :
                break
            elif (len(nums) == 1) :
                if len(nums[0]) <= 2:
                    date_res[2] = int(nums[0])
                else:
                    year = int(nums[0])
                    if year < 2019 or year > 2030:
                        date_res[2] = int(str(year)[0:2])
                    else:
                        date_res[0] = year
            else :
                year = int(nums[0])
                if year < 2019 or year > 2030:
                    date_res[2] = year // 100
                else:
                    date_res[0] = year
            break
    
    if date_res[1] == 0:
        for yr in year_ls:
            datess = re.findall(yr + r'[-./]\d{1,2}[-./]\d{1,2}', string)
            if not datess:
                datess = re.findall(r'\d{1,2}[-./]\d{1,2}[-./]' + yr, string)
                if not datess:
                    datess = re.findall(r'\d{1,2}[-./]\d{1,2}[-./]' + yr[2:], string)
                    if datess:
                        print(datess)
                        res = re.split(r'[\D]', datess[0])
                        print(res)
                        date_res[0] = int(res[2]) + 2000
                        date_res[1] = int(res[1])
                        date_res[2] = int(res[0])
                else:
                    print(datess)
                    res = re.split(r'[\D]', datess[0])
                    print(res)
                    date_res[0] = int(res[2])
                    date_res[1] = int(res[1])
                    date_res[2] = int(res[0])
            else:
                print(datess)
                res = re.split(r'[\D]', datess[0])
                
                print(res)
                date_res[0] = int(res[0])
                date_res[1] = int(res[1])
                date_res[2] = int(res[2])

    if (date_res[0] == 0 or date_res[0] > 2030 or date_res[0] < 2010):
        date_res[0] = int(date.today().strftime("%Y"))
    if (date_res[1] == 0 or date_res[1] > 12):
        date_res[1] = int(date.today().strftime("%m"))
    if (date_res[2] == 0 or date_res[2] > 31):
        date_res[2] = int(date.today().strftime("%d"))


    return "-".join(str(i) for i in date_res)
    


    date_res = [0, 0, 0]
    for mon in mon_ls:
        if mon in string:
            date_res[1] = mon_ls.index(mon) + 1
            tmp = string.split(mon)
            ldis, rdis = 0, 0
            while(tmp[0] and not tmp[0][-1].isnumeric()):
                tmp[0] = tmp[0][0:-1]
                ldis += 1
            while(tmp[1] and not tmp[1][0].isnumeric()):
                tmp[1] = tmp[1][1:]
                rdis += 1
            day, year = 0, 0
            if tmp[0] and ldis <= rdis :
                if ldis > 4 :
                    break
                else :
                    llen ,lcur = -len(tmp[0]), 0
                    while(lcur > llen and tmp[0][lcur-1].isnumeric()):
                        lcur -=1
                    print(lcur)
                    tmp[0]=tmp[0][lcur:]
                    day = int(tmp[0])
                    if (day < 31) :
                        date_res[2] = day
                        rlen, rcur = len(tmp[1]), 0
                        while(rcur < rlen and rcur < 4 and tmp[1][rcur].isnumeric()):
                            rcur += 1
                        year = int(tmp[1][0:rcur])
                        if (year < 30):
                            year += 2000
                        date_res[0] = year
                    elif (day > 2000) :
                        year = day
                        day = 0
                        date_res[0] = year
                        rlen, rcur = len(tmp[1]), 0
                        while(rcur < rlen and rcur < 2 and tmp[1][rcur].isnumeric()):
                            rcur += 1
                        day = int(tmp[1][0:rcur])
                        if (day < 31):
                            date_res[2] = day
                    break
            elif tmp[0] :
                llen ,lcur = -len(tmp[0]), 0
                while(lcur >= llen and tmp[0][lcur-1].isnumeric()):
                    lcur -=1
                tmp[0]=tmp[0][lcur:]
                year = int(tmp[1][0:lcur])
                rlen, rcur = len(tmp[1]), 0
                while(rcur < rlen and rcur < 2 and tmp[1][rcur].isnumeric()):
                    rcur += 1
                day = int(tmp[1][0:rcur])
                if (day < 31):
                    date_res[2] = day
                break
            
            else: # MON/DD/YY(YY)
                rcur = 0
                rlen, rcur = len(tmp[1]), 0
                while(rcur < rlen and rcur < 2 and tmp[1][rcur].isnumeric()):
                    rcur += 1
                day = int(tmp[1][0:rcur])
                if (day < 31):
                    date_res[2] = day
                tmp[1] = tmp[rcur:]
                rlen, rcur = len(tmp[1]), 0
                while(rcur < rlen and not tmp[1][rcur].isnumeric()):
                    rcur += 1
                if (rcur < rlen):
                    tmp[1] = tmp[1][rcur:]
                    rlen, rcur = len(tmp[1]), 0
                    while(rcur < rlen and  tmp[1][rcur].isnumeric()):
                        rcur += 1
                    year =  int(tmp[1][0:rcur])
                    if (year < 30):
                        year += 2000
                        date_res[0] = year
                    elif (year > 2000 and year < 2030):
                        date_res[0] = year
                    else :
                        year = year // 100
                        year += 2000
                        date_res[0] =  year
                else:
                    year = int(date.today().strftime("%Y"))
                    date_res[0] = year
                break

    if (date_res[1] == 0): ## when abbr is not appear 
        NotImplemented
    if (date_res[0] < 2019 or date_res[0] > 2022):
        date_res[0] = int(date.today().strftime("%Y"))
    if (date_res[1] == 0):
        date_res[1] = int(date.today().strftime("%m"))
    if (date_res[2] == 0):
        date_res[2] = int(date.today().strftime("%d"))
    
    
    return "-".join(str(i) for i in date_res)
