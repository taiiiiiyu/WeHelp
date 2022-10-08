import urllib.request as req
with open("movie.txt",mode="w",encoding="utf-8") as file:
    good=[]
    nor=[]
    bad=[]
    def getData(url):
       
        request=req.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")
        import bs4
        root=bs4.BeautifulSoup(data,"html.parser")
        titles=root.find_all("div",class_="title")
        
    
        
        for title in titles:
            if title.a != None and "Re:" not in title.a.string:
                tit=title.a.string
                if "[好雷]" in tit :
                    good.append(title.a.string)
                if "[普雷]" in tit :
                    nor.append(title.a.string)
                if "[負雷]" in tit :
                    bad.append(title.a.string)
         
       
        
        nextlink=root.find("a",string="‹ 上頁")
        return nextlink["href"]
    pageURL="https://www.ptt.cc/bbs/movie/index.html"
    count=0
    while count<10:
        pageURL="https://www.ptt.cc/"+getData(pageURL)
        count+=1
    dataBase=good+nor+bad
    print(dataBase)
    for i in dataBase:
        file.write(i+"\n")