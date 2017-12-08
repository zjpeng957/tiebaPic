import requests
from bs4 import BeautifulSoup
import os
preStr = "http://tieba.baidu.com"

if __name__ == "__main__":
    link = preStr+"/p/5457147302"
    page = requests.get(link).text
    x = 0
    os.makedirs("pic")
    soup = BeautifulSoup(page,'html.parser')

    while True:
        img_list = soup.find_all("img","BDE_Image")
        i = 0
        for img in img_list:
            html = requests.get(img.get("src"))
            img_name = str(x)+"-"+str(i)+".png"
            with open("pic/"+img_name,"wb") as file:
                file.write(html.content)
                file.flush()
            i = i+1
            file.close()
        x = x+1

        nextP = soup.find("a",text="下一页")
        if nextP is None:
            break
        page = requests.get(preStr + nextP.get("href")).text
        soup = BeautifulSoup(page, 'html.parser')
