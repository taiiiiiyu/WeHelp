import csv
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src)as response:
    data=json.load(response)
clist=data["result"]["results"]
with open("week3\week3data.csv",mode="w",newline="",encoding="utf-8") as file:
    for information in clist:
        stitle=information["stitle"]#景點
        longitude=information["longitude"]#經度
        latitude=information["latitude"]#緯度
        address=information["address"]
        xpostDate=information["xpostDate"]
        img=information["file"]
        district=address[4:8]#區
        year=xpostDate[:4]#年分
        img0=img.split("https")
        imgSite="https"+img0[1]#圖檔網址
        dataBase=[]
        if int(year)>=2015:#(2015(含)之後)
            dataBase.append([stitle,district,longitude,latitude,imgSite])
        write=csv.writer(file)
        write.writerows(dataBase)
    
            
            

