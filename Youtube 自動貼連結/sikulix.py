import random

python_note_link = 'http://bit.ly/2L0XiHM'
c1 = unicode("內容很扎實 希望能提供更多教學影片", "utf8")
c2 = unicode("感謝你的認真教學 我會持續關注", "utf8")
c3 = unicode("謝謝唷 教得很棒 讓我能力提升很多", "utf8")
c4 = unicode("有你真好 讓我能學到更多東西", "utf8")
c5 = unicode("感謝大大提供的教學", "utf8")
c6 = unicode("讚讚讚 又學到一招", "utf8")
c7 = unicode("只有一個字 讚", "utf8")
c8 = unicode("如果可以的話 希望你能提供更多相關的影片", "utf8")
c9 = unicode("太棒了 學到很多唷", "utf8")
c10 = unicode("感謝大大的認真教學耶", "utf8")
c11 = unicode("網路上有很多教學 我覺得你講的很棒", "utf8")

e1 =unicode('Great, I hope to see more instructional videos.', "utf8")
e2 =unicode('Thank you for your instructional videos.', "utf8")
e3 = unicode('The content is very careful, I will continue to pay attention', "utf8")
e4 = unicode('I hope to see the follow-up teaching.', "utf8")
e5 = unicode('Teaching taught me a lot, I also changed jobs.', "utf8")
e6 =unicode('Learning python really makes me find a good job, thank you very much for your teaching.', "utf8")
e7 = unicode('This python course has made me grow a lot.', "utf8")
e8 = unicode('Thank you very much, the teacher said step by step.', "utf8")
e9 =unicode('Does the teacher have any other teaching', "utf8")
e10 =unicode('I also want to learn more about the Python program. Is there a recommended movie', "utf8")
e11 =unicode('You actually made this quite easy to understand for the beginners. In other words, a beginner could easily understand it.', "utf8")
e12 =unicode('Finally a video that is not confusing!', "utf8")
e13 =unicode('I generally use Sublime Text for coding, but to be honest, I quite liked the built in editor. And I\'m a petty bastard when it comes to editors.﻿', "utf8")
e14 =unicode('thanks for this tutorial  it helped me a lot﻿', "utf8")
e15 =unicode('It is really helpful to understand.﻿', "utf8")
e16 =unicode('Very helpful tutorial, thanks for sharing your knowledge.﻿', "utf8")
e17 =unicode('Thanks your videos Helped me﻿', "utf8")


ch = unicode("學習筆記本", "utf8")

re = Region(18,71,883,581)
def past_link(con,link):
    if re.exists("1544865376864.png",3):
        change_url(link)
    else:
        wait("1540904057809.png",60) #等待留言圖片
        wait(3)
        click("1540904057809.png")
        paste(con)
        wait(1)
        type(Key.ENTER)
        paste('python'+' requests '+python_note_link)
        click("1540989566290.png") #留言
        wait(1)

def change_url(link):
    click("1541206320143.png") # http//:
    paste(link)
    wait(1)
    type(Key.ENTER)
    wait(1)
region = Region(1350,681,16,87)

# 頁面往下
def page_down():
    for d in range(15):
        region.click("1541206334777.png")
    
url =[ 
        
]
list = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
eng = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17]

for time in range(len(url)):
    change_url(url[time]) # 切換連結
    page_down() # 頁面往下
    a = random.randrange(0, 17)#亂數選取留言內容
    ## if list index out of range 則略過
    try:
        link=url[time+1]
    except:
        pass
    past_link(eng[a],link) # 將內容貼上

# sikuli 1.1.3
# https://sikulix-2014.readthedocs.io/en/latest/basicinfo.html
# Java
# https://www.java.com/zh_TW/








    

    
